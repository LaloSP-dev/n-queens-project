%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                           Servidor
%
%   Integrantes del Equipo 10:
%
%       Nombre: Guerrero Torres Jesus Cesar 
%       Matricula: 2173048598
%
%       Nombre: Sanchez Pascual Eduardo
%       Matricula: 2173048730
%
%       Nombre: Treviño De Jesus Jose Alfredo
%       Matricula: 2173011028
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

:- use_module(library(socket)).

%:- consult(metro).

servidor:-
    tcp_socket(Socket), 
    tcp_bind(Socket, 50000), 
    tcp_listen(Socket, 5), 
    tcp_open_socket(Socket, AcceptFd, _),
    dispatch(AcceptFd).

dispatch(AcceptFd):-
    tcp_accept(AcceptFd, Socket, Peer),
    process_client(Socket, Peer).
%     thread_create(process_client(Socket, Peer), _,
%                      [ detached(true)
%                      ]).
    %dispatch(AcceptFd). % Con esta linea se pueden atender muchas llamadas
    % Sin ella solo se atiende una llamada

process_client(Socket, Peer) :-
        write(' Recibi llamada de: '), write(Peer), nl,
        setup_call_cleanup(
            tcp_open_socket(Socket, StreamPair),
            doService(StreamPair),
            close(StreamPair)).

%%% Soluciones de N reinas
doService(Stream):-
    % Manda Varias cadenas
    repeat,
       % Antes era member(X, [hola,esta,es,una,prueba,fin]),
       read(Stream,L),read(Stream,E),
       (all_solutions(L,Lista), write(Stream, Lista), put(Stream, 13), put(Stream, 10);
         write(Stream, no), put(Stream, 13), put(Stream, 10)),
       flush_output(Stream),
    E==fin, % Aca terminas
    !,
    write(' Adios '), nl.


all_solutions(Numero, Listas):-
    findall(Lista, (reinasP(Numero, Lista)), Listas).
reinasP(N,L):-
    reinas(N,[],L).

reinas(N,L,L):-
    length(L,N),
    noChoque(L).

reinas(N,L,R):-
    lista(1,N,A),
    member(X,A),
    noChoque([X|L]),
    reinas(N, [X|L], R).

noChoque([]).
noChoque([X|Xs]):-
    not(member(X, Xs)),
    noDiag(X,Xs,1),
    noChoque(Xs).

noDiag(X,[],N).
noDiag(X, [Y|Ys], D):-
    A is abs(X-Y),
    A \= D,
    D1 is D+1,
    noDiag(X,Ys,D1).

lista(B,B,[B]).
lista(A,B,[A|R]):-
    A<B,
    C is A+1,
    lista(C,B,R).