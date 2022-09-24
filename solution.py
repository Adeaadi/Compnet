# import socket module
from socket import *
# In order to terminate the program

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  addr = (server,port)
  header = 64
  format='utf-8'
  disconnect_message ="!disconnect"
  #Prepare a server socket


  #Fill in start
  serverSocket.bind(("", port))
  serverSocket.listen(1)
  print 'the web server is active and ready to receive on port:', port
  #Fill in end
    while True:
      #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serversocket.accept()#Fill in start -are you accepting connections?
    sentence = connectionSocket.recv().decode()
    capitalizedsentence = sentence.upper()
    connectionsocket.send(capitalizedsentence.encode())
    connectionsocket.close()
  #Fill in end

    #socket.connect(192.168.1.166, port)


  #print("[starting] server is starting...")
  #start()
    try:
      message = #Fill in start -a client is sending you a message

        def handle_client(conn, addr):
    pass
    print(f"[new connection] {addr} connected.")
    connected=true
      while connected:
        msg_length = conn.recv(header).decode(format)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(format)
        if msg == disconnect_message:
            connected=false
        print (f"[{addr}] {msg}")

      # #Fill in end
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "helloworld.html","r", "utf-8")#fill in start
               # #fill in end)
      #fill in end
      
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"\
      #Fill in start -This variable can store your headers you want to send for any valid or invalid request. 
      #Content-Type above is an example on how to send a header as bytes
      #Fill in end

      #Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok? 
      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      #Fill in start

      #Fill in end
               

      #Send the content of the requested file to the client
      for i in f: #for line in file
        #Fill in start - send your html file contents #Fill in end 
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      #Fill in start

      #Fill in end


      #Close client socket
      #Fill in start
     client.close()
      #Fill in end

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
