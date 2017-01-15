#import os,re,socket,sys

# Echo server program
import socket, sys

def main():
   HOST = None               # Symbolic name meaning all available interfaces
   PORT = 30008              # Arbitrary non-privileged port
   s = None
   # Returns a list of addresses associated with the current machine
   for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                                 socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
      # get the data for each connection
      af, socktype, proto, canonname, sa = res
      # listen on PORT variable above for every connection
      s = socket.socket(af, socktype, proto)
      s.bind(sa)
      s.listen(1)

   # wait until someone bites. eg someone tries to access your website
   conn, addr = s.accept()
   print('Connected by', addr)

   #simple
   my_website = "HTTP/1.1 200 Found\r\nContent-Length: 3\r\nConnection:\r\n Close\r\n\r\nHi!"

   # advanced
   # my_content = "<html><body>Hello this is my <strong>website</strong></body></html>"
   # my_website = "HTTP/1.1 200 Found\r\nContent-Type: text/html\r\nContent-Length: "+ str(len(my_content))+"\r\nConnection:\r\n Close\r\n\r\n" + my_content

   while True:
      data = conn.recv(1024)
      print(data)
      if not data: break
      conn.send(bytes(my_website,'utf-8'))
   conn.close()

if __name__ == '__main__':
   main()