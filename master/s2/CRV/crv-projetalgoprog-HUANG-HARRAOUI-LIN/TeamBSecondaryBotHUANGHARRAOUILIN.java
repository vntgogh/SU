package algorithms;

import characteristics.IFrontSensorResult;
import characteristics.IRadarResult;
import characteristics.Parameters;
import java.util.Random;
import robotsimulator.Brain;

public class TeamBSecondaryBot extends Brain {
    private enum State {
        MOVING, TURNING
    }

    private enum Identity {
        ROCKY, MARIO
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
    }

    // ---PARAMETERS---//
    private static final double MOVEMENT_ANGLE_PRECISION = 0.02;
    private static final double TURN_ANGLE = Math.PI / 3;
    private static final double RESET_DELAY = 5;
    private static final double SPEED = Parameters.teamBSecondaryBotSpeed;
    private static final double RADIUS = Parameters.teamBSecondaryBotRadius;
    private static final Random RANDOM = new Random();

    // ---VARIABLES---//
    private Identity id;
    private State state;
    private double targetAngle;
    private boolean isMoving;
    private Position position;

    public TeamBSecondaryBot() {
        super();
    }

    public final void activate() {
        setIdentity();
        state = State.MOVING;
        isMoving = false;
    }

    public final void step() {
        // --- Mort ---
        if (getHealth() == 0) {
            sendLogMessage("I'm dead.");
            return;
        }

        double heading = getHeading();
        boolean willCollide = false;

        // --- Radar ---
        for (IRadarResult object : detectRadar()) {
            // --- Collision ---
            if (willCollide(heading, object, RADIUS)) {
                willCollide = true;
            }

            // --- Partage position ennemie ---
            if (object.getObjectType() == IRadarResult.Types.OpponentMainBot
                    || object.getObjectType() == IRadarResult.Types.OpponentSecondaryBot) {
                double dist = object.getObjectDistance();
                double direction = object.getObjectDirection();
                Position enemyPosition = new Position(
                        position.x + dist * Math.cos(direction),
                        position.y + dist * Math.sin(direction));
                broadcast(enemyPosition.toString());
            }
        }

        // --- Détection mur ---
        if (detectFront().getObjectType() == IFrontSensorResult.Types.WALL) {
            willCollide = true;
        }

        // --- Odométrie ---
        if (isMoving && !willCollide) {
            position.x += SPEED * Math.cos(heading);
            position.y += SPEED * Math.sin(heading);
        }
        isMoving = false;

        // --- Automate ---
        switch (state) {
            case MOVING:
                if (willCollide) {
                    state = State.TURNING;
                    targetAngle = normalize(heading + TURN_ANGLE * RANDOM.nextDouble(0, 1));
                } else {
                    actionMove();
                }
                break;
            case TURNING:
                if (!isSameDirection(heading, targetAngle)) {
                    if (normalize(targetAngle - heading) <= Math.PI) {
                        stepTurn(Parameters.Direction.RIGHT);
                    } else {
                        stepTurn(Parameters.Direction.LEFT);
                    }
                } else {
                    state = State.MOVING;
                }
                break;

            default:
                break;
        }

        // --- Debug ---
        sendLogMessage(
                id.toString() + " | " +
                        "(" + (int) position.x + ", " + (int) position.y + ") | " +
                        "STATE: " + state);
    }

    private void setIdentity() {
        boolean allyNorth = false;
        boolean allySouth = false;

        for (IRadarResult o : detectRadar()) {
            if (o.getObjectType() == IRadarResult.Types.TeamSecondaryBot) {
                if (isSameDirection(o.getObjectDirection(), Parameters.NORTH)) {
                    allyNorth = true;
                }
                if (isSameDirection(o.getObjectDirection(), Parameters.SOUTH)) {
                    allySouth = true;
                }
            }
        }

        if (!allyNorth) {
            id = Identity.ROCKY; // Haut
            position = new Position(Parameters.teamBSecondaryBot1InitX, Parameters.teamBSecondaryBot1InitY);
            targetAngle = Parameters.teamBSecondaryBot1InitHeading;
        } else {
            id = Identity.MARIO; // Bas
            position = new Position(Parameters.teamBSecondaryBot2InitX, Parameters.teamBSecondaryBot2InitY);
            targetAngle = Parameters.teamBSecondaryBot2InitHeading;
        }
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

    private boolean isSameDirection(final double dir1, final double dir2) {
        double diff = Math.abs(normalize(dir1) - normalize(dir2));
        double shortestDiff = Math.min(diff, 2 * Math.PI - diff);
        return shortestDiff < MOVEMENT_ANGLE_PRECISION;
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
