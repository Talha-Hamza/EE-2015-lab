% Define the transfer function
s = tf('s');
H = ((800*pi)/(s+(800*pi))) + ((s)/(s+(8000*pi))); % Transfer function of problem 15.29

% Plot the frequency response with x-axis in Hz
h = bodeplot(H);
grid on;

% Customize plot settings for frequency in Hz
opts = getoptions(h);
opts.FreqUnits = 'Hz';
setoptions(h, opts);
