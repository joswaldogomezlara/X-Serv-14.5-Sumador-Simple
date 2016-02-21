#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random

host = socket.gethostname()
port = 1235
primer_num = True

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind((host, port))

mySocket.listen(5)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'

        recibido = recvSocket.recv(2048)

        print recibido

        if primer_num:

            sumando1 = recibido.split(' ')[1][1:]

            if sumando1 == 'favicon.ico':
                continue
            elif sumando1 == '':
                continue

            print 'Recibido el número: ', sumando1

            print 'Answering back...'
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body>" +
                            "<p>Recibido el numero: " + str(sumando1) + "</p>"
                            "<p>Esperando el segundo numero a sumar...</p>" + 
                            "</body></html>" + "\r\n")
            recvSocket.close()

            primer_num = False

        else:

            sumando2 = recibido.split(' ')[1][1:]

            if sumando2 == 'favicon.ico':
                continue
            elif sumando2 == '':
                continue

            print 'Recibido el número: ', sumando2

            resultado = int(sumando1) + int(sumando2)

            print 'Answering back...'
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body>" +
                            "<p>" + 
                            str(sumando1) + 
                            "+" + 
                            str(sumando2) + 
                            "=" + 
                            str(resultado) +
                            "</p>" + 
                            "</body></html>" + "\r\n")
            recvSocket.close()

            primer_num = True



except KeyboardInterrupt:
    mySocket.close()
    print "\nClosing binded socket"
