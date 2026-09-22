np = py.importlib.import_module('numpy');
poles_py = np.roots(py.list({13.125, -26.625, 19.375, -4.875}));

% Convertir numpy.ndarray en liste Python
poles_list = py.list(poles_py);

% Convertir la liste Python en cellule MATLAB
poles_cell = cell(poles_list);

% Initialiser un tableau MATLAB
poles = zeros(1, numel(poles_cell));

% Remplir le tableau avec les valeurs converties
for k = 1:numel(poles_cell)
    poles(k) = double(poles_cell{k});
end

disp(poles)

% Tracé des pôles
figure;
plot(real(poles), imag(poles), 'rx', 'MarkerSize', 10, 'LineWidth', 2)
hold on

% Tracé du cercle unité
theta = linspace(0, 2*pi, 200);
plot(cos(theta), sin(theta), 'b--')  % Cercle unité

% Configuration du graphe
axis equal
grid on
xlabel('Partie réelle')
ylabel('Partie imaginaire')
title('Pôles du filtre dans le plan Z')
legend('Pôles', 'Cercle unité')
hold off