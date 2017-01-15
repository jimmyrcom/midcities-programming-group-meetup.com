#import os,re,socket,sys

# Echo server program
import socket, sys

def main():
   HOST = None               # Symbolic name meaning all available interfaces
   PORT = 30008              # Arbitrary non-privileged port
   s = None
   for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                                 socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
       af, socktype, proto, canonname, sa = res
       try:
           s = socket.socket(af, socktype, proto)
           s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       except OSError as msg:
           s = None
           continue
       try:
           s.bind(sa)
           s.listen(1)
       except OSError as msg:
           s.close()
           s = None
           continue
       break
   if s is None:
       print('could not open socket')
       sys.exit(1)
   conn, addr = s.accept()
   print('Connected by', addr)

   my_website="HTTP/1.1 200 Found\r\nContent-Length: 3\r\nConnection:\r\n Close\r\n\r\nHi!"

   while True:
       data = conn.recv(1024)
       if not data: break
       conn.send(bytes(my_website,'utf-8'))
   conn.close()



#if __name__ == '__main__':
#    main()