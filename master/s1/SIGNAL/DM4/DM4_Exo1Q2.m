% Configuration des pôles pour un filtre TC (Temps Continu)
% avec approximation de Butterworth - ordre 6

% Définition des angles des pôles (6 pôles répartis sur le cercle unité)
angles = [0, pi/3, 2*pi/3, pi, 4*pi/3, 5*pi/3];

% Calcul des positions des pôles sur le cercle unité
poles = 0.5 * (exp(1j * angles));

% Création de la figure
figure;
hold on;
grid on;
axis equal;

% Tracé du cercle unité pour référence
theta = linspace(0, 2*pi, 100);
plot(0.50 * cos(theta), 0.50 * sin(theta), 'k--', 'LineWidth', 0.5);

% Placement des pôles sur le plan S (marqueurs 'x' en rouge)
plot(real(poles), imag(poles), 'rx', 'MarkerSize', 10, 'LineWidth', 2);

% Configuration des axes et labels
xlabel('Partie Réelle (\sigma)');
ylabel('Partie Imaginaire (j\omega)');
title('Plan S - Pôles du filtre TC (Butterworth ordre 6)');
legend('Cercle unité', 'Pôles', 'Location', 'best');

% Ajout des axes x et y pour référence
xline(0, 'k-', 'Alpha', 0.3);
yline(0, 'k-', 'Alpha', 0.3);

% Affichage des coordonnées des pôles
fprintf('Coordonnées des pôles:\n');
for i = 1:length(poles)
    fprintf('Pôle %d: %.4f + j%.4f\n', i, real(poles(i)), imag(poles(i)));
end

hold off;