import socket,select

server_address=('localhost',29000)

size = 32769
cekSend = "Isi file sudah diterima"

makeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#membuat socket

makeSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#memaksa addr dan port untuk digunakan

makeSocket.bind(server_address);#mengaitkan socket ke port dan addressnya
makeSocket.listen(5)#listen koneksi dari klien

listSocket = [makeSocket]#membuat list client
c=1
while True:
    readable, writeable, exception = select.select(listSocket,[],[])
    for sock in readable:

        if sock == makeSocket:
            clientSocket, clientAddress = makeSocket.accept()
            listSocket.append(clientSocket)

        else:
            title = sock.recv(size)
            print "unggah " + title
            temp = 'dataset/' + title
            try:
                fwrite = open(temp,'wb')#wb = write binary

                #print "cekIn client ",c
                while True:
                    isiData = sock.recv(size)
                    if not isiData: break;
                    fwrite.write(isiData) #write isiData
                
                #print "cekOut clinet ",c
                sock.send(cekSend)
                c += 1
                fwrite.close() #menutup file
                
                
            except: fwrite.close()
            sock.close()
            listSocket.remove(sock)

print "cek out"
makeSocket.close()#menutup koneksi ke client
