import socket,  argparse

def connect_port(target, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    if client.connect_ex((target, port)) == 0:
        return  print(f'open: {port}')



def define_arguments():
    args_list = {}
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--domin', help="which domain to test")
    parse.add_argument('-p', '--port', help="specify which port you want to scan")
    parse.add_argument('-c', '--common', action="store_true", help="tests all the most common ports")
    parse.add_argument('-f', '--first', action='store_true', help="test wing first 10000 doors")
    argv = parse.parse_args()


    args_list['domin'] = argv.domin
    args_list['port'] = argv.port
    args_list['common'] = argv.common
    args_list['first'] = argv.first

    return args_list
    
ports_common = [20,21,22,25,53,80,123,179,443,500,587,3389]

args_def = define_arguments()


if args_def['common'] == True:
    for p in ports_common:
        connect_port(args_def['domin'], p)


if args_def['first'] == True:
    for p in range(1, 10000):
        connect_port(args_def['domin'], p)

if args_def['port']:
    connect_port(args_def['domin'], int(args_def['port']))

if args_def['domin']:
    for p in range(1, 65536):
        connect_port(args_def['domin'], p)

