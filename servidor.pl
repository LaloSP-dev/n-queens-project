%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%             Servidor
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

:- use_module(library(socket)).

:- consult(queens).

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
    % dispatch(AcceptFd). % Con esta linea se pueden atender muchas llamadas
    % Sin ella solo se atiende una llamada

process_client(Socket, Peer) :-
        write(' Recibi llamada de: '), write(Peer), nl,
        setup_call_cleanup(
            tcp_open_socket(Socket, StreamPair),
            doService(StreamPair),
            close(StreamPair)).

%%% Lo de las listas
doService(Stream):-
    % Manda Varias cadenas
    repeat,
       % Antes era member(X, [hola,esta,es,una,prueba,fin]),
       read(Stream,L),read(Stream,E),
       (reinasP(N,L), write(Stream, yes), put(Stream, 13), put(Stream, 10);
        not(member(E,L)),write(Stream, no), put(Stream, 13), put(Stream, 10)),
       flush_output(Stream),
    E==fin, % Aca terminas
    !,
    write(' Adios '), nl.

