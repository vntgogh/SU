t = 0:0.1:10;

w = exp(-t);
x = t .* exp(-t);
y = exp(-t) + t .* exp(-t);

figure;
hold on;
plot(t, w, 'Color', [0, 1, 0], 'DisplayName', 'w(t) = e^{-t}'); %vert
plot(t, x, 'Color', [1, 0, 1], 'DisplayName', 'x(t) = t * e^{-t}'); %magenta
plot(t, y, 'Color', [0, 1, 1]', 'DisplayName','y(t) = e^{-t} + t * e^{-t}'); %cyan
hold off;
    
xlabel('t');
ylabel('w(t), x(t), y(t)');
title('');
legend show;
