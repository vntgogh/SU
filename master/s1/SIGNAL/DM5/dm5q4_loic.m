% Définir l'ordre du filtre
Omega_s = 0.3*pi;
Omega_p = 0.2*pi;
ordre = ceil((1.8*pi)/(Omega_s - Omega_p));
if (mod(ordre, 2) == 0)
    ordre = ordre + 1; % Mettre l'ordre impair pour avoir un filtre type I
end
M = ordre;

% Calcul de la fréquence de coupure
Omega_c = (Omega_p + Omega_s) / 2;

% INDICES CAUSAUX : n de 0 à M-1
n = 0:M-1;

% Calcul des coefficients h[n] avec retard (M-1)/2
h = (sin(Omega_c * (n - (M-1)/2))) ./ (pi * (n - (M-1)/2));

% Gérer le cas n = (M-1)/2 (limite sin(x)/x quand x->0)
idx_center = find(n == (M-1)/2);
h(idx_center) = Omega_c/pi;

% Vecteur de fréquences
f = 0:0.0001:3;  % Normalisé entre 0 et 1 (Nyquist)
w = pi * f;     % w entre 0 et pi
z = exp(1j * w);

% Calcul de H(z) avec indices CAUSAUX
h_z = zeros(size(w));
for k = 0:M-1
    h_z = h_z + h(k+1) * z.^(-k);
end

% Tracer le module (en dB)
figure;
subplot(2, 1, 1);
plot(w/pi, 20*log10(abs(h_z)/max(abs(h_z))), 'b', 'LineWidth', 1.5);
title('Module de la réponse en fréquence H(e^{j\omega})');
xlabel('\omega/\pi');
ylabel('Gain (dB)');
grid on;
hold on;
line([Omega_p/pi Omega_p/pi], ylim, 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1);
line([Omega_s/pi Omega_s/pi], ylim, 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1);
legend('|H(e^{j\omega})|', '\omega_p', '\omega_s');
hold off;

% Tracer la phase (dépliée)
subplot(2, 1, 2);
plot(w/pi, unwrap(angle(h_z)), 'r', 'LineWidth', 1.5);
title('Phase de la réponse en fréquence H(e^{j\omega})');
xlabel('\omega/\pi');
ylabel('Phase (radians)');
grid on;
hold on;
line([Omega_p/pi Omega_p/pi], ylim, 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1);
line([Omega_s/pi Omega_s/pi], ylim, 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1);
hold off;
