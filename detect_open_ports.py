from socket import socket, gaierror
from tqdm import tqdm
from datetime import datetime


def detect_open_ports(ip, range_start, range_end):
    open_ports = []
    port_detecting_progress = tqdm(range(range_start, range_end + 1))
    try:
        for port in port_detecting_progress:
            port_detecting_progress.set_description('checking port {}'.upper().format(port))
            s = socket()
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        log_open_ports(ip, range_start, range_end, open_ports)

    except KeyboardInterrupt:
        print("\ncanceled...".upper())
    except gaierror:
        print("\nHostname Could Not Be Resolved".upper())
    return open_ports


def log_open_ports(ip, range_start, range_end, open_ports):
    try:
        with open("results/result_detect_open_ports.txt", "a") as file:
            file.write('@ {}'.upper().format(datetime.now()))
            file.write('\nhost {} open ports from {} to {}:'.upper().format(ip, range_start, range_end))
            [file.write('\n√ {}'.format(port)) for port in open_ports]
            if not open_ports:
                file.write('\n× no open ports was founded!'.upper())
            file.write('\n----------------------------------------------------\n')
    except FileNotFoundError:
        print('PLEASE CREATE \"/results/result_detect_open_ports.txt\" AND TRY AGAIN.')


if __name__ == '__main__':
    detect_open_ports(
        ip=input('TARGET IP ADDRESS: '),
        range_start=int(input('START OF RANGE   : ')),
        range_end=int(input('END  OF  RANGE   : ')),
    )
