%Analysis of number density in Pi digits

clear;clc;
close all;

%Import the Pi data text file
data = fileread("pi_dec_1k.txt");
data = data(3:end);

tracker = zeros(10,1);
n = length(data);

for i = 1:n
    cc = floor(str2double(data(i)));
    tracker(cc+1) = tracker(cc+1) + 1;
end

percent = zeros(10,1);
for i = 1:10
    percent(i) = tracker(i)/n*100;
end

%Plot
figure(1);
plot(0:9, percent, 'k*');
title("Pi digits - analysis");
xlabel("#digits");
% axis([-1 10 9.9 10.2]);
ylabel("Percentage");