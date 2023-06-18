import socket

def main():
    # Creamos un socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Definimos la dirección del servidor
    direccion_servidor = ('localhost', 8000)
    
    try:
        # Nos conectamos al servidor
        cliente_socket.connect(direccion_servidor)
        
        # Enviamos datos al servidor
        mensaje = '¡Hola desde el cliente!'
        cliente_socket.send(mensaje.encode())
        
        # Recibimos la respuesta del servidor
        respuesta = cliente_socket.recv(1024)
        print(f'Respuesta del servidor: {respuesta.decode()}')
        
    except ConnectionRefusedError:
        print('No se puede establecer conexión con el servidor.')
    
    # Cerramos la conexión
    cliente_socket.close()

if __name__ == '__main__':
    main()
