#A simple implementation of Peer-to-Peer communication using sockets



import socket
import threading


def receiver(myip):
    while True:

        receiver_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        receiver_socket.bind((myip, 20001))

        bytes_received = receiver_socket.recvfrom(1024)
        message = bytes_received[0]

        print(message.decode())

def sender(peerip,username):
    while True:
        print(username,": ", end = "")
        msg = input()
        msg = username+":"+msg

        sender_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        sender_socket.sendto(str.encode(msg), (peerip,20001))


def main():
    myip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
    if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
    s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
    socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    port = 20001
    buffer = 1024

    username = input("Username:")
    peerip = input("Peer IP:")

    #Reciver Thread
    rec = threading.Thread(target=receiver, args=(myip,))
    rec.start()

    #Sender Thread
    send = threading.Thread(target=sender, args=(peerip,username,))
    send.start()
    rec.join()
    send.join()
    


if __name__ == '__main__':
    main()