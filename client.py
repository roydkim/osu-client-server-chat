import socket

def clientFunction():
    # create client socket
    c = socket.socket()
    # get host name
    host = socket.gethostname()
    # initialize port
    port = 8888
    # connect through host and port
    c.connect((host, port))

    print('Connected to: ' + str(host) + ' on port: ' + str(port))
    print('Type /q to quit')
    print('Enter message to send...')
    # create field to input a message
    message = input(">")
    # sends first encoded message from client
    c.send(message.encode())
    # loop that makes sure that client is running as long as user does not quit ('/q')
    while message != '/q':
        # The following code is taken from:
        # https://www.chegg.com/homework-help/questions-and-answers/using-python-3-write-simple-client-server-program-using-python-sockets-program-emulate-sim-q69849994
        c.send(message.encode()) # throughout loop, encodes and sends input message
        data = c.recv(1024).decode() # reads and decodes data received from server
        print(data) # prints that data
        message = input(">") # and asks for another input

        # really only took the c.recv(1024) part
        # some code that made the code cleaner/more efficient

    c.close() # closes socket


if __name__ == '__main__':
    clientFunction()