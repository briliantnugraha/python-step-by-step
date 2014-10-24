import socket, os

server_address = ('localhost', 29000)

size = 32769

makeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
makeSocket.connect(server_address)
judul = raw_input()

titleSplit=judul.split()#membagi isi string yang berspasi menjadi array of string

if titleSplit[0]=='unggah':

    title = titleSplit[1]
    count = 2
    
    while True:
        if count==len(titleSplit):  break

        else:
            title += " " + titleSplit[count]
            count += 1
    print title

    makeSocket.send(title)
    
    try:        
        isi = os.path.abspath(title)
        print isi
        try:
            f = open(isi,'rb')

            #while True:
            #    fsend = f.read(size)
            #    if not fsend: break;
            #    makeSocket.sendall(fsend)
            for send in f:
                makeSocket.sendall(send)
            
            #print cekEnd
        except: fread.close()
        finally: fread.close()
        try:
            message = makeSocket.recv(size)
            if message: print message      
        except: makeSocket.close()
        
    except: makeSocket.close()
makeSocket.close()        
