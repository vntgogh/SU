package algorithms;

import characteristics.IFrontSensorResult;
import characteristics.IRadarResult;
import characteristics.Parameters;
import java.util.ArrayList;
import robotsimulator.Brain;

public class TeamBMainBot extends Brain {
    private enum State {
        MOVING, TURNING, FIRING, CHASING, REPOSITIONING
    }

    private enum Identity {
        ROCKY, MARIO, GEORGE
    }

    private class Position {
        public double x;
        public double y;

        Position(final double x, final double y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return x + "," + y;
        }

        @Override
        public boolean equals(Object object) {
            if (object instanceof Position pos) {
                return this.x == pos.x && this.y == pos.y;
            }
            return false;
        }
    }

    // ---PARAMETERS---//
    private static final double MOVEMENT_ANGLE_PRECISION = 0.02;
    private static final double FIRING_ANGLE_PRECISION = 0.5;
    private static final double TURN_ANGLE = Math.PI / 2.5;
    private static final double RESET_DELAY = 5;
    private static final double SPEED = Parameters.teamBMainBotSpeed;
    private static final double RADIUS = Parameters.teamBMainBotRadius;
    private static final double FRONTAL_DETECTION_RANGE = Parameters.teamBMainBotFrontalDetectionRange;

    // ---VARIABLES---//
    private Identity id;
    private State state;
    private double targetAngle;
    private boolean isMoving;
    private Position position;
    private Position enemyPosition;
    private Position lastPosition;
    private double minMovement;
    private double resetDelay;

    public TeamBMainBot() {
        super();
    }

    public final void activate() {
        setIdentity();
        state = State.MOVING;
        isMoving = false;
        minMovement = 0;
        resetDelay = RESET_DELAY;
    }

    public final void step() {
        // --- Mort ---
        if (getHealth() == 0) {
            sendLogMessage("I'm dead.");
            return;
        }

        double heading = getHeading();
        boolean willCollideAlly = false;
        boolean willCollideEnemy = false;
        boolean willCollideWreck = false;
        boolean enemyDetected = false;

        // --- Radar ---
        for (IRadarResult object : detectRadar()) {
            // --- Collision ---
            if (willCollide(heading, object, RADIUS)
                    && object.getObjectType() != IRadarResult.Types.BULLET) {
                if (object.getObjectType() == IRadarResult.Types.TeamMainBot
                        || object.getObjectType() == IRadarResult.Types.TeamSecondaryBot) {
                    willCollideAlly = true;
                } else if (object.getObjectType() == IRadarResult.Types.OpponentMainBot
                        || object.getObjectType() == IRadarResult.Types.OpponentSecondaryBot) {
                    enemyDetected = true;
                    willCollideEnemy = true;
                } else if (object.getObjectType() == IRadarResult.Types.Wreck) {
                    willCollideWreck = true;
                }
            }

            // --- Cible abattue ---
            if (!enemyDetected && object.getObjectType() == IRadarResult.Types.Wreck) {
                enemyPosition = null;
                broadcast("RESET");
            }

            // --- Partage position ennemie ---
            if (object.getObjectType() == IRadarResult.Types.OpponentMainBot
                    || object.getObjectType() == IRadarResult.Types.OpponentSecondaryBot) {
                double dist = object.getObjectDistance();
                double direction = object.getObjectDirection();
                enemyPosition = new Position(
                        position.x + dist * Math.cos(direction),
                        position.y + dist * Math.sin(direction));
                broadcast(enemyPosition.toString());
            }
        }

        // --- Ennemi déplacé ---
        if (enemyPosition != null && !enemyDetected) {
            enemyPosition = null;
        }

        // --- Réception messages ---
        ArrayList<String> messages = fetchAllMessages();
        for (String message : messages) {
            if (message.equals("RESET")) {
                enemyPosition = null;
            } else {
                String[] enemyPos = message.split(",");
                enemyPosition = new Position(Double.valueOf(enemyPos[0]), Double.valueOf(enemyPos[1]));
            }
        }

        // --- Détection mur ---
        if (detectFront().getObjectType() == IFrontSensorResult.Types.WALL) {
            willCollideAlly = true;
        }

        // --- Odométrie ---
        if (isMoving && !willCollideAlly && !willCollideEnemy) {
            lastPosition.x = position.x;
            lastPosition.y = position.y;
            position.x += SPEED * Math.cos(heading);
            position.y += SPEED * Math.sin(heading);
        } else {
            resetDelay--;
            if (resetDelay <= 0) {
                minMovement = 0;
                resetDelay = RESET_DELAY;
            }
        }
        isMoving = false;

        // --- Automate ---
        switch (state) {
            case MOVING:
                if (willCollideAlly || willCollideWreck) {
                    state = State.REPOSITIONING;
                    targetAngle = normalize(heading + TURN_ANGLE);
                    minMovement = RADIUS;
                } else if (enemyPosition != null) {
                    state = State.CHASING;
                } else {
                    actionMove();
                }
                break;
            case CHASING:
                if (willCollideAlly || willCollideWreck) {
                    state = State.REPOSITIONING;
                    targetAngle = normalize(heading + TURN_ANGLE);
                    minMovement = RADIUS;
                } else if (enemyPosition == null) {
                    state = State.MOVING;
                    break;
                } else {
                    double enemyAngle = getAngleToPosition(enemyPosition);
                    double enemyDistance = getDistance(enemyPosition);

                    if (enemyDistance > FRONTAL_DETECTION_RANGE) {
                        if (!isSameDirection(heading, enemyAngle, MOVEMENT_ANGLE_PRECISION)) {
                            state = State.REPOSITIONING;
                            targetAngle = enemyAngle;
                        } else {
                            actionMove();
                        }
                    } else {
                        state = State.FIRING;
                    }
                }
                break;
            case FIRING:
                if (enemyPosition != null) {
                    fire(getAngleToPosition(enemyPosition));
                    state = State.CHASING;
                } else {
                    state = State.MOVING;
                }
                break;
            case REPOSITIONING:
                if (!isSameDirection(heading, targetAngle, MOVEMENT_ANGLE_PRECISION)) {
                    if (normalize(targetAngle - heading) <= Math.PI) {
                        stepTurn(Parameters.Direction.RIGHT);
                    } else {
                        stepTurn(Parameters.Direction.LEFT);
                    }
                } else if (minMovement <= 0) {
                    state = State.MOVING;
                    minMovement = 0;
                } else {
                    actionMove();
                    if (minMovement > 0) {
                        minMovement -= SPEED;
                    }
                }
                break;

            default:
                break;
        }

        // --- Debug ---
        sendLogMessage(
                id.toString() + " | " +
                        "(" + (int) position.x + ", " + (int) position.y + ") | " +
                        "STATE: " + state
                        + (enemyPosition != null
                                ? " | ENEMY: (" + (int) enemyPosition.x + ", " + (int) enemyPosition.y + ")"
                                : ""));
    }

    private void setIdentity() {
        boolean allyNorth = false;
        boolean allySouth = false;

        for (IRadarResult o : detectRadar()) {
            if (o.getObjectType() == IRadarResult.Types.TeamMainBot) {
                if (isSameDirection(o.getObjectDirection(), Parameters.NORTH, MOVEMENT_ANGLE_PRECISION)) {
                    allyNorth = true;
                }
                if (isSameDirection(o.getObjectDirection(), Parameters.SOUTH, MOVEMENT_ANGLE_PRECISION)) {
                    allySouth = true;
                }
            }
        }

        if (allyNorth && allySouth) {
            id = Identity.MARIO; // Centre
            position = new Position(Parameters.teamBMainBot2InitX, Parameters.teamBMainBot2InitY);
            targetAngle = Parameters.teamBMainBot2InitHeading;
        } else if (!allyNorth) {
            id = Identity.ROCKY; // Haut
            position = new Position(Parameters.teamBMainBot1InitX, Parameters.teamBMainBot1InitY);
            targetAngle = Parameters.teamBMainBot1InitHeading;
        } else {
            id = Identity.GEORGE; // Bas
            position = new Position(Parameters.teamBMainBot3InitX, Parameters.teamBMainBot3InitY);
            targetAngle = Parameters.teamBMainBot3InitHeading;
        }

        lastPosition = new Position(position.x, position.y);
    }

    // --- FONCTIONS UTILITAIRES ---

    private boolean willCollide(double heading, IRadarResult object, double minDistance) {
        double diff = normalize(object.getObjectDirection() - heading);
        if (diff > Math.PI) {
            diff = 2 * Math.PI - diff;
        }

        // Angle de 90° (45°, 45° à gauche et droite)
        // Marge d'une distance d'un rayon du robot actuel
        if (diff < Math.PI / 2
                && object.getObjectDistance() < RADIUS + object.getObjectRadius() + minDistance) {
            return true;
        }

        return false;
    }

    private void actionMove() {
        isMoving = true;
        move();
    }

    private boolean isSameDirection(final double dir1, final double dir2, final double precision) {
        double diff = Math.abs(normalize(dir1) - normalize(dir2));
        double shortestDiff = Math.min(diff, 2 * Math.PI - diff);
        return shortestDiff < precision;
    }

    private double normalize(final double dir) {
        double res = dir % (2 * Math.PI);
        if (res < 0) {
            res += 2 * Math.PI;
        }
        return res;
    }

    private double getAngleToPosition(Position target) {
        return normalize(Math.atan2(target.y - position.y, target.x - position.x));
    }

    private double getDistance(Position target) {
        return Math
                .sqrt(Math.pow(target.x - position.x, 2) + Math.pow(target.y - position.y, 2));
    }
}
