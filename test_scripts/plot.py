x = [0 0.2 0.4 0.8 1.2 1.6 2.0];
y = [0 0.155 0.240 0.328 0.450 0.582 0.692];
p = polyfit(x, y, 1);
v = polyval(p, x);
figure(1)
plot(x,y,'x','MarkerEdgeColor','black')
hold on
plot(x, v)
hold off
grid on;
xlabel('Protein standard concentration (µg/µl)')