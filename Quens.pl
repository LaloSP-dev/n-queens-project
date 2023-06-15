reinas(0,L,L):-
    noChoque(L).
reinas(N,L,R):-
    Lista(1,4,A),
    menber(X,A),
    append(L,[X],Ln),
    noChoque(Ln),
    K is N -1,
    reinas(K,Ln,R).

noChoque([]).
noChoque([X|Xs]):-
    not(member(X,Xs)),
    noDiag(X,Xs,1),
    %noChoque(Xs).

noDiag(X,[],N).
noDiag(X,[Y|Ys],D):-
    A is abs(X-Y),
    A \= D,


caballoP(N,R):-caballo(N,[(1,1)],R).

caballo(N,L,L):-
    length(L,M),
    M is N*N.

caballo(N,[(X,Y)|L],R):-
    salto((X,Y),(U,W),N),
    not(menber((U,W),L)),
    caballo(N,[(U,W),(X,Y)|L],R).

salto((X,Y),(X1,Y1),N):-    %Salta 2 arriba y una a la derecha
    X1 is X+1.

salto((X,Y),(X1,Y1),N):-
    X1 is X-2,
    Y1 is Y-1,
    X1>0,
    Y1>0.

salto((X,Y),(X1,Y2),N):-
    X1 is X-2,
    Y1 is Y+1,
    X1>0,
    Y1=<N.

salto((X,Y),(X1,Y1),N):-
    X1 is X+1,
    Y1 is Y+2,
    X1=<N,%checa no salirse de los limites 
    Y1=<N.


salto((X,Y),(X1,Y1),N):-
    X1 is X+1,
    Y1 is Y-2,
    X1=<N,%checa no salirse de los limites 
    Y1>0.
