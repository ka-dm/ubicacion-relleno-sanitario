% Parametros
int: n; % tamaño de la region
int: m; % cantidad de ciudades
array[1..m,1..2] of float: ciudades;

% Variables 
var float: f;
var 0.0..n: x;
var 0.0..n: y;

% Restricciones
constraint forall (i in 1..m) (ciudades[i,1] != x /\ ciudades[i,2] != y);  

% Objetivo
array[int] of var float: dist = [abs(x - ciudades[i,1]) + abs(y - ciudades[i,2]) | i in 1..m];
constraint f = min(dist);
solve maximize f;
 
output ["este = ", show(x),"\n", "norte = ", show(x),"\n","distancia = ", show(f),"\n"];