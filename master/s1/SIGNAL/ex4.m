% Define the time vector
t = 0:0.1:10;

% Define the functions
w = exp(-t);
x = t .* exp(-t);
y = exp(-t) + t .* exp(-t);

% Create the plot
figure;
plot(t, w, 'r', 'DisplayName', 'w(t) = e^{-t}');
hold on;
plot(t, x, 'g', 'DisplayName', 'x(t) = t * e^{-t}');
plot(t, y, 'b', 'DisplayName', 'y(t) = e^{-t} + t * e^{-t}');
hold off;
    
% Add labels and legend
xlabel('t');
ylabel('w(t), x(t), y(t)');
title('');
legend show;
grid on;
