import socket
# <<---- handle port host & callback Listenar And Start Server ---->>
def ServerListenerHandler(self, port, *args,Server):
    # find arg length 
    args_len = len(args)

    # <-- arg not given -->
    if args_len == 0: 
        server = Server(port)
    elif args_len == 1 and isinstance(args[0], str): #<-- only host given
        server = Server(port, host=args[0])
    elif args_len == 1 and callable(args[0]):#<-- only port given
        server = Server(port, listenerHandler=args[0])
    # <-- port and host both given -->
    elif args_len == 2 and isinstance(args[0], str) and callable(args[1]):
        server = Server(port, host=args[0], listenerHandler=args[1])
    
    # <-- run server -->
    server.start() 


# < -- handle host name -- >
def set_host__name(host):
    # print(socket.gethostbyname(socket.gethostname()))
    if host == "0.0.0.0" and host != "localhost" and host != "127.0.0.1":
        return socket.gethostbyname(socket.gethostname())
    return host

# < -- handle port check port running or not -- >
def check_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()