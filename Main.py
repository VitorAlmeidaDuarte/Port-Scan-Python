import socket, sys, argparse

def connect_port(target, *port):

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if client.connect_ex((target, port)) == 0:
            return 'da'
    
    except:
        return 'daaa'
    


def define_arguments():
    args_list = {}
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--domin', help="which domain to test")
    parse.add_argument('-p', '--port', help="specify which port you want to scan")
    parse.add_argument('-c', '--common', action="store_true", help="tests all the most common ports")
    parse.add_argument('-f', '--first', action='store_true', help="test wing first 10000 doors")
    argv = parse.parse_args()

    if argv.domin:
        args_list['domin'] = argv.domin
    if argv.port:
        args_list['port'] = argv.port
    if argv.common:
        args_list['common'] = argv.common
    if argv.first:
        args_list['first'] = argv.first

    return args_list
    
ports_common = [20,21,22,25,53,80,123,179,443,500,587,3389]

args_def = define_arguments()

'''if args_def['common'] == True:
    for p in ports_common:
        port = connect_port(args_def['domin'], ports_common)
        print(f'Aberta: {port}')'''


p = connect_port(args_def['domin'], args_def['port'])

print(p)

