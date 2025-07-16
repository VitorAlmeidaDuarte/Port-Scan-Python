import socket, sys, argparse


def argument():
    parse = argparse.ArgumentParser()
    parse.add_argument('-p', '--port', help="specify which port you want to scan")
    parse.add_argument('-hs', help="test")

    argv = parse.parse_args()
    print(argv.port)


argument()