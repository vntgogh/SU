Rs = 7;
As = 16;
omegap = 0.2 * pi;
omegas = 0.3 * pi;

wp = 2 * tan(omegap / 2);
ws = 2 * tan(omegas / 2);

N = ceil(log10((10^(As/10) - 1) / (10^(Rs/10) - 1)) / (2 * log10(ws/wp)));

wc = wp / ((10^(Rs/10) - 1)^(1/(2*N)));

poles = zeros(1, N);
for k = 1:N
    poles(k) = wc * exp(1j * pi * (2*k + N - 1) / (2*N));
end

den_a = real(poly(poles));  
num_a = wc^N;               
fs = 2;
[num, den] = bilinear(num_a, den_a, fs);

omega = linspace(0, pi, 1000);
Hz = zeros(size(omega));
for k = 1:length(omega)
    z = exp(1j * omega(k));
    Nz = 0;
    Dz = 0;
    for n = 0:length(num)-1
        Nz = Nz + num(n+1) * z^(-n);
    end
    for n = 0:length(den)-1
        Dz = Dz + den(n+1) * z^(-n);
    end
    Hz(k) = Nz / Dz;
end

% Ajuster le gain pour que le module à 0.2*pi soit -7 dB
[~, idx_07] = min(abs(omega - 0.2*pi));
gain_factor = 10^((-7 - 20*log10(abs(Hz(idx_07)))) / 20);
num = num * gain_factor;

% Recalcul après ajustement gain
for k = 1:length(omega)
    z = exp(1j * omega(k));
    Nz = 0;
    Dz = 0;
    for n = 0:length(num)-1
        Nz = Nz + num(n+1) * z^(-n);
    end
    for n = 0:length(den)-1
        Dz = Dz + den(n+1) * z^(-n);
    end
    Hz(k) = Nz / Dz;
end

mag_dB = 20 * log10(abs(Hz));
phase_deg = unwrap(angle(Hz)) * 180 / pi;

% Tracé
figure;
subplot(2,1,1);
plot(omega/pi, mag_dB, 'b', 'LineWidth', 1.5);
hold on;
grid on;
xlabel('\omega / \pi');
ylabel('Module (dB)');
title('Réponse en module du filtre');
plot([0.2 0.2], ylim, 'r--');
plot([0.3 0.3], ylim, 'k--');
yline(-7, 'r--', 'Rp=7 dB');
yline(-16, 'k--', 'As=16 dB');
hold off;

subplot(2,1,2);
plot(omega/pi, phase_deg, 'm', 'LineWidth', 1.5);
grid on;
xlabel('\omega / \pi');
ylabel('Phase (°)');
title('Réponse en phase du filtre');
