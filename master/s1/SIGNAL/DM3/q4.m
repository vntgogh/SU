% Define the range for theta
theta = [0, pi/4, pi/2]; % Three different theta values

% Define the complex variable s
s = 1j; % s is the complex variable

% Initialize figure
figure;
hold on; % Hold on to plot multiple curves

% Loop through each theta value to calculate and plot H(s)
for i = 1:length(theta)
    H = 1 ./ (s + 1j * theta(i)); % Calculate H(s)
    plot(real(H), imag(H), 'DisplayName', sprintf('\\theta = %.2f', theta(i))); % Plot the curve
end

% Customize the plot
title('Curves for H(s) with varying \\theta');
xlabel('Real Part');
ylabel('Imaginary Part');
legend show; % Show legend
grid on; % Add grid
hold off; % Release the hold
