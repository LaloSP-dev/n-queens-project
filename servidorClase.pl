###################################
       Servidor
#######################################
:- use_module(library(socket)).

:-consult(queens).

servidor:-
    write('Empieza servidor'),nl,
    socket('AF_INET',Socket),
    socket_bind(Socket, 'AF_INET'(N, 50000))
    socket_listen(Socket, 5),
    socket_accept(Socket, ClienteIP, Stream),
    doService(ClienteIP, Stream),
    socket_close(Socket).

doService(ClienteIP, Stream):-
       write('Recibi llamada de : '), write(ClienteIP), nl,
       % manda varias cadenas
       repeat,
              % antes era member [x, [hola,esta,es,una,prueba,fin]].
              read(Stream,N),
              (reinasP(N,L), write(Stream, L), put(Stream, 13), put(Stream, 10);
               write(Stream, no), put(Stream, 13), put(Stream, 10)),
              flush_output(Stream),
       N==fin, % aca termina
       !,
       write('Adios'), nl,
       close(Stream).
       