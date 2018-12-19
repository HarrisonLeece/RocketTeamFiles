%Wave drag curve fit for Mach 1.4 to ~Mach 4
%James Hribal
function [fitresult, gof] = createFit1(x, y)
%CREATEFIT1(X,Y)
%  Create a fit.
%
%  Data for 'Cd vs Mach' fit:
%      X Input : x
%      Y Output: y
%  Output:
%      fitresult : a fit object representing the fit.
%      gof : structure with goodness-of fit info.
%
%  See also FIT, CFIT, SFIT.

%  Auto-generated by MATLAB on 17-Dec-2018 11:41:58


%% Fit: 'Cd vs Mach'.
clc
clear all
close all 

x = [1.5:.25:4.5];
y = [.55, .525, .4625, .4025, .3625, .3155, .2725, .2515, .2410, .2310, .2200, .2199, .2150]; 

[xData, yData] = prepareCurveData( x, y );

% Set up fittype and options.
ft = fittype( 'poly6' );
opts = fitoptions( 'Method', 'LinearLeastSquares' );
opts.Robust = 'Bisquare';

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, opts );

% Create a figure for the plots.
figure( 'Name', 'Cd vs Mach' );

% Plot fit with data.
subplot( 2, 1, 1 );
h = plot( fitresult, xData, yData );
legend( h, 'Data Points', 'Curve Fit', 'Location', 'NorthEast' );
% Label axes
xlabel 'Mach Number'
ylabel 'Drag Coefficient'
grid on

% Plot residuals.
subplot( 2, 1, 2 );
h = plot( fitresult, xData, yData, 'residuals' );
legend( h, 'Cd vs Mach - residuals', 'Zero Line', 'Location', 'NorthEast' );
% Label axes
xlabel x
ylabel y
grid on



