/*
lista(B,B,[B]).
lista(A,B,[A|R]):- 
    C is A+1,
    lista(C,B,R).


reinas(0,L,L):-
    noChoque(L).

reinas(N,L,R):-
    lista(1,4,A),
    menber(X,A),
    append(L,[X],Ln),
    noChoque(Ln),
    K is N-1,
    reinas(K,Ln,R).

noChoque([]).
noChoque([X|Xs]):-
    not(member(X,Xs)),
    noDiag(X,Xs,1).
    %noChoque(Xs).

noDiag(X,[],N).
noDiag(X,[Y|Ys],D):-
    A is abs(X-Y),
    A \= D,
    D1 is D+1,
    noDiag(X,Ys,D1).


caballoP(N,R):-caballo(N,[(1,1)],R).

caballo(N,L,L):-
    length(L,M),
    M is N*N.

caballo(N,[(X,Y)|L],R):-
    salto((X,Y),(U,W),N),
    not(menber((U,W),L)),
    caballo(N,[(U,W),(X,Y)|L],R).

salto((X,Y),(X1,Y1),N):- %Salta 2 arriba y una a la derecha
    X1 is X+1,
    Y1 is Y+2,
    X1=<N,%checa no salirse de los limites 
    Y1=<N.


salto((X,Y),(X1,Y1),N):-
    X1 is X+1,
    Y1 is Y-2,
    X1=<N,%checa no salirse de los limites 
    Y1>0.


salto((X,Y),(X1,Y1),N):-
    X1 is X-2,
    Y1 is Y-1,
    X1>0,
    Y1>0.

salto((X,Y),(X1,Y1),N):-
    X1 is X-2,
    Y1 is Y+1,
    X1>0,
    Y1=<N.

*/
% Predicado principal para resolver el problema de las N reinas
n_reinas(N, Solucion) :-
    % Generar una lista de números del 1 al N
    numlist(1, N, Filas),
    % Generar una permutación de las filas
    permutation(Filas, Solucion),
    % Verificar que la solución sea válida
    valida(Solucion).

% Predicado para verificar si una solución es válida
valida([]).
valida([X | Xs]) :-
    % Verificar si no hay conflicto con las reinas anteriores
    no_conflicto(X, Xs, 1),
    % Verificar las reinas en las filas siguientes
    valida(Xs).

% Predicado para verificar si no hay conflicto con las reinas anteriores
no_conflicto(_, [], _).
no_conflicto(X, [Y | Ys], D) :-
    % Verificar si hay conflicto en la misma columna o diagonal
    X =\= Y + D,
    X =\= Y - D,
    % Verificar con la siguiente diagonal
    D1 is D + 1,
    no_conflicto(X, Ys, D1).