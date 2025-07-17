import socket, sys, argparse

args_list = []
def init_program():
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--domin', help="which domain to test")
    parse.add_argument('-p', '--port', help="specify which port you want to scan")
    parse.add_argument('-c', '--comun', action="store_true", help="tests all the most common ports")
    parse.add_argument('-f', '--first', action='store_true', help="test wing first 1000 doors")
    argv = parse.parse_args()

    if argv.domin:
        args_list.append(argv.domin)
    

print(args_list)   
    



init_program()

