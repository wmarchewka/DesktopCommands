import socket
import time


class Connection(object):

    def __init__(self):
        self.my_socket = None

    def create(self):
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        try:
            self.my_socket.connect((host, port))
        except Exception as e:
            print('error: {}'.format(e))

    def send(self, data):
        rtn_data = "Error"
        try:
            dataout = bytes((data + '\r'), 'ascii')
            self.my_socket.sendall(dataout)
            while True:
                rtn_data = self.my_socket.recv(1024)
                if '\r' in rtn_data.decode():
                    break
        except Exception as e:
            print('error: {}'.format(e))
        return rtn_data

    def close(self):
        self.my_socket.close()
