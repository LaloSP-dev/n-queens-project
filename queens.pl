
:- style_check(-singleton).

reinasP(N,L):-
    reinas(N,[],L).

reinas(N,L,L):-
    length(L,N),
    noChoque(L).

reinas(N,L,R):-
    lista(1,N,A),
    member(X,A),
    noChoque([X|L]),
    reinas(N,[X|L],R).

noChoque([]).
noChoque([X|Xs]):-
    not(member(X,Xs)), 
    noDiag(X,Xs,1),
    noChoque(Xs).

noDiag(X,[],N).
noDiag(X,[Y|Ys],D):-
    A is abs(X-Y),
    A \= D,
    D1 is D + 1,
    noDiag(X,Ys,D1).

%LISTA DE A a B
lista(A,A,[A]).
lista(A,B,[A|R]):- 
    A < B, C is A + 1, lista(C,B,R).

member(X,[X|Xs]).
member(X,[Y|Xs]):-
    member(X,Xs).



/*reinas(N,L,R):-
        lista(1,N,A),
        member(X,A), %append(L,[X],Ln),
        noChoque(Ln),
        K is N - 1,
        reinas(K,Ln,R).
*/
