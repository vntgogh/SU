clc; clear; close all;

% Paramètres
wc = 0.5;

% Définition des pôles complexes
P2 = wc * exp(1j * 2*pi/3);
P3 = wc * exp(1j * pi);
P4 = wc * exp(1j * 4*pi/3);

% Vecteur de pulsations
w = logspace(-2, 1, 1000); % de 0.01 à 10 rad/s
s = 1j * w;

% Fonction de transfert H(s)
Hs = (wc^3) ./ ((s - P2) .* (s - P3) .* (s - P4));

% Calcul du gain (module) et de la phase
gain = abs(Hs);
phase = unwrap(angle(Hs) * 180/pi); % en degrés

% Tracé du Bode
figure;

subplot(2,1,1);
semilogx(w/pi, 20*log10(gain), 'LineWidth', 1.5);
grid on;
xlabel('\omega (rad/s)');
ylabel('Gain (dB)');
title('Diagramme de Bode - Gain');

subplot(2,1,2);
semilogx(w/pi, phase, 'LineWidth', 1.5);
grid on;
xlabel('\omega (rad/s)');
ylabel('Phase (°)');
title('Diagramme de Bode - Phase');
