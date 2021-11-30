from socket import socket, gaierror, getservbyport
from tqdm import tqdm
from datetime import datetime


def detect_port_services(ip, range_start, range_end):
    port_services = {}
    port_detecting_progress = tqdm(range(range_start, range_end + 1))
    try:
        for port in port_detecting_progress:
            port_detecting_progress.set_description('checking port {}'.upper().format(port))
            s = socket()
            result = s.connect_ex((ip, port))
            if result == 0:
                service_name = getservbyport(port, 'tcp')
                port_services.update({port: service_name})
            s.close()
        log_port_services(ip, range_start, range_end, port_services)

    except KeyboardInterrupt:
        print("\ncanceled...".upper())
    except gaierror:
        print("\nHostname Could Not Be Resolved".upper())
    return port_services


def log_port_services(ip, range_start, range_end, port_services):
    try:
        with open("results/result_port_services.txt", "a") as file:
            file.write('@ {}'.upper().format(datetime.now()))
            file.write('\nhost {} open ports\' services from {} to {}:'.upper().format(ip, range_start, range_end))
            [file.write('\n {}:\t{}'.format(port, port_services[port])) for port in port_services.keys()]
            if not port_services.keys():
                file.write('\n× no open ports was founded!'.upper())
            file.write('\n----------------------------------------------------\n')
    except FileNotFoundError:
        print('PLEASE CREATE \"/results/result_detect_open_ports.txt\" AND TRY AGAIN.')


if __name__ == '__main__':
    detect_port_services(
        ip=input('TARGET IP ADDRESS: '),
        range_start=int(input('START OF RANGE   : ')),
        range_end=int(input('END  OF  RANGE   : ')),
    )
