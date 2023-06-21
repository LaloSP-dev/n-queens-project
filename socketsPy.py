
import socket
import sys
#import tablero as tb
""""
################################################################################################    
                                Lenguajes De Programacion 
                                    Proyecto Final

Integrantes del Equipo 10:

    Nombre: Guerrero Torres Jesus Cesar 
    Matricula: 2173048598

    Nombre: Sanchez Pascual Eduardo
    Matricula: 2173048730

    Nombre: Treviño De Jesus Jose Alfredo
    Matricula: 2173011028

Lenguajes de Programacion 
Grupo:CJ01
#################################################################################################
"""
host = 'localhost'
port = 50000
s = None

print('Crea Socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('No se pudo crear')
    sys.exit()

print('Trata obtener ip')
try:
    rip = socket.gethostbyname(host)
except socket.gaierror:
    print(f'No se encontro {host}')
    sys.exit()

print('Conectandose al sistema')
s.connect((rip,port))

def utilizar_valor_ingresado(n):
    e = n
    query = bytes(f'{e}.\nno.\n'.encode('ascii')) # dos lineas
    try:
        s.sendall(query)
    except socket.error:
        print('Error de coms')

    reply = s.recv(256)
    #print(reply)
    reply = reply.decode()
    while not '\n' in reply:
        res = s.recv(256)
        reply += res.decode()
    
    #print(reply)
    #print(f'Este el reply {reply}')

    fin = bytes('0.\nfin.\n'.encode('ascii')) # dos lineas
    s.sendall(fin)
    res = s.recv(256)
    s.close()
    
    return reply
