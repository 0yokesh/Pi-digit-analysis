%Analysis of number density in Pi digits

%Created by Yokesh
%Email: yzs0074@auburn.edu

clear;clc;
close all;

%Import the Pi data text file
%Read the entire .txt file as a string
%Beware you should have enough to memory to handle, when to try >1e9 digits
data = fileread("pi_dec_1m.txt");
data = data(3:end); %To elminiate 3. at the start

tracker = zeros(10,1); %Tracker counts #digit
n = length(data);

for i = 1:n

    %Rips the string and converts into a double data type
    %Then it is converted to int data type using 'floor'
    cc = floor(str2double(data(i)));  %I know, but this is the faster way in Matlab
    tracker(cc+1) = tracker(cc+1) + 1; %Update the tracker
end

percent = zeros(10,1); %Percent calculates percentage of occurence of each #digit
for i = 1:10
    percent(i) = tracker(i)/n*100;
end

%Plot
figure(1);
plot(0:9, percent, 'k*');
title("Pi digits - analysis");
xlabel("#digits");
% axis([-1 10 9.9 10.2]); (optional)
ylabel("Percentage");
