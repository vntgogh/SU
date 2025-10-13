% Calcul de H sans la fonction bode()
f = 0.1:0.1:1000; % Fréquences de 0.1 à 1000 
s = 1j*2*pi*f;
H1 = (20 * s .* (s + 100)) ./ ((s + 2) .* (s + 10)); % Calcul de H(s)

gain1 = 20 * log10(abs(H1)); % Gain en dB
phase1 = angle(H1) * (180/pi); % Phase en degrés

% Calcul de H avec la fonction bode()
H = tf([20, 2000], [1, 12, 20]);
[~, ~, wout] = bode(H, 2 * pi * f);
gain2 = squeeze(gain1); 
phase2 = squeeze(phase1); 

figure;

% Superpositions des gains
subplot(2, 1, 1);
yyaxis left;
semilogx(f, gain1, 'Color', [1, 0, 1]);
ylabel('Gain (dB)');
title('Superpositions des gains');
hold on;

yyaxis right;
semilogx(f, gain2, '--r', 'Color', [0, 1, 1]');

xlabel('Fréquence');
legend('Gain sans bode()', 'Gain avec bode()');
hold off;

% Superpositions des phases
subplot(2, 1, 2);
yyaxis left;
semilogx(f, phase1, 'Color', [1, 0, 1]);
ylabel('Phase (degrés)');
title('Superpositions des phases');
hold on;

yyaxis right;
semilogx(f, phase2, '--r','Color', [0, 1, 1]');
xlabel('Fréquence');
legend('Phase sans bode()', 'Phase avec bode()');
hold off;