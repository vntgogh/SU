Wp = 0.2 * pi;
Ws = 0.3 * pi; 
M = 19; 

m1 = -(M-1)/2;
m2 = (M-1)/2;
n = m1:m2; 

Wc = (Wp + Ws) / 2; 
h = (sin((Wc * n))) ./ (Wc * n); 

h(n == 0) = 1; 

figure;
stem(n, h);
title('Coefficients du filtre h[n]');
xlabel('n');
ylabel('h[n]');
grid on;
