import socket

def main():
    # Creamos un socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Asociamos el socket a un puerto específico
    direccion_servidor = ('localhost', 8000)
    servidor_socket.bind(direccion_servidor)
    
    # Escuchamos conexiones entrantes
    servidor_socket.listen(1)
    
    print('El servidor está listo para recibir conexiones...')
    
    while True:
        # Esperamos a que llegue una conexión
        print('Esperando una conexión...')
        conexion_cliente, direccion_cliente = servidor_socket.accept()
        print(f'Conexión establecida desde: {direccion_cliente}')
        
        # Recibimos los datos del cliente
        datos = conexion_cliente.recv(1024)
        print(f'Datos recibidos: {datos.decode()}')
        
        # Enviamos una respuesta al cliente
        respuesta = '¡Hola desde el servidor!'
        conexion_cliente.send(respuesta.encode())
        
        # Cerramos la conexión
        conexion_cliente.close()
        print('Conexión cerrada.')
    
if __name__ == '__main__':
    main()
