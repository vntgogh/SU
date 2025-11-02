Wp = 0.2 * pi;
Ws = 0.3 * pi; 
M = 19; 

m1 = -(M-1)/2;
m2 = (M-1)/2;
n = m1:m2; 

Wc = (Wp + Ws) / 2; 
h = (sin((Wc * n))) ./ (Wc * n); 

h(n == 0) = 1; 


% Gérer le cas n = (M-1)/2
idx_center = find(n == (M-1)/2);
h(idx_center) = Wc/pi;

figure;
stem(n, h);
title('Coefficients du filtre h[n]');
xlabel('n');
ylabel('h[n]');
grid on;


% Calculer H(e^jw) avec indices causaux
w = linspace(0, pi, 512);
H = h * exp(-1j * n' * w);

% Calculer le module et la phase
Module = abs(H);
Phase = unwrap(angle(H));

% Tracer le module
figure;
subplot(2,1,1);
plot(w/pi, Module, 'b', 'LineWidth', 1.5);
title('Module de H(e^{j\omega})');
xlabel('\omega/\pi');
ylabel('|H(e^{j\omega})|');
grid on;

hold on;
line([Wp/pi Wp/pi], ylim, 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1);
line([Ws/pi Ws/pi], ylim, 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1);
legend('|H(e^{j\omega})|', '\omega_p', '\omega_s');
hold off;

% Tracer la phase
subplot(2,1,2);
plot(w/pi, Phase, 'r', 'LineWidth', 1.5);
title('Phase de H(e^{j\omega}) - Linéaire');
xlabel('\omega/\pi');
ylabel('Phase (radians)');
grid on;

hold on;
line([Wp/pi Wp/pi], ylim, 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1);
line([Ws/pi Ws/pi], ylim, 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1);
hold off;
