from socket import socket, gaierror, getservbyport, AF_INET, SOCK_STREAM, setdefaulttimeout
from tqdm import tqdm
from datetime import datetime


def detect_port_services(ip, range_start, range_end):
    port_services = {}
    port_detecting_progress = tqdm(range(range_start, range_end + 1))
    try:
        for port in port_detecting_progress:
            port_detecting_progress.set_description('checking port {}'.upper().format(port))

            setdefaulttimeout(2)
            s = socket(AF_INET, SOCK_STREAM)
            result = s.connect_ex((ip, port))

            # trying to get more information about port service
            try:
                message = b'WhoAreYou'
                s.send(message)
                banner = s.recv(100)
                s.close()
            except IOError:
                banner = b''

            if result == 0:
                service_name = getservbyport(port)
                port_services.update({port: (service_name, banner.replace(b'\r\n', b'').decode('utf-8'))})

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
            [file.write('\n {}:\t{} {}'
                        .format(port,
                                port_services[port][0].upper(),
                                '' if not port_services[port][1] else '\n\t\t({})\n'
                                .format(port_services[port][1]))
                        ) for port in port_services.keys()]
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
