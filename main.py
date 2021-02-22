import socket

def doSearch(server, request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, 43))
    s.send((request + '\r\n').encode())

    info = s.recv(300)
    info = info.decode()
    info = info.split("\r\n")
    info = info[6].lstrip()
    s.close()

    return info[22:32]

def getDate():

    server = "whois.internic.net"
    request = input("Enter a .com domain: ")

    if "www." in request:
        request = request.replace("www.","")
    if "http://" in request:
        request = request.replace("http://","")

    print("Domain expiration date: " + doSearch(server, request))

getDate()
