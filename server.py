import socket

def serverFunction():
    # create server socket
    s = socket.socket()
    # get host name
    host = socket.gethostname()
    # initialize port
    port = 8888
    # bind socket to address (tuple containing host and port)
    s.bind((host, port))
    # accept two connections
    s.listen(2)
    # accept connects rsocket and address
    rsocket, address = s.accept()

    print('Server listening on: ' + str(host) + ' on port: ' + str(port))
    print("Connected by: " + str(address))
    print('Waiting for message ...')
    # reads and decodes data from rsocket socket
    data = rsocket.recv(1024).decode()
    # prints data
    print(str(data))
    print('Type /q to quit')
    print('Enter message to send...')
    while True: # loops while connection exists
        data = rsocket.recv(1024).decode() # reads and decodes data throughout loop
        if not data: # if no data, the loop breaks
            break
        print(str(data)) # prints data
        data = input('>') # asks for reply message to received messages
        rsocket.send(data.encode()) # encodes data and sends

        # didn't know how to make the loop condition
        # recv(1024)
        # didn't really know i needed the if not condition for a loop break
        # small cleaning up of code

    rsocket.close() # close socket


if __name__ == '__main__':
    serverFunction()