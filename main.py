from ping import ping
from detect_active_hosts import detect_active_hosts
from detect_open_ports import detect_open_ports


if __name__ == '__main__':
    while True:
        print('------------------------- PING  PROGRAM -------------------------')
        try:
            option = int(input(
                'select an option:\n\t 1) ping and ip\n\t 2) ping and ip range and show active hosts\n\t 3) scan open '
                'ports of an active host\n\t-1) exit program\n'.upper()))

            if option == 1:
                try:
                    response = ping(host=input('HOST : '), count=int(input('COUNT: ')), wait=-1, _print=True, log=True)
                    print(response if response else 'no response'.upper())
                except ValueError:
                    print('value error!\nplease try again and enter a valid number for \"count\"'.upper())

            elif option == 2:
                try:
                    active_hosts = detect_active_hosts(
                        range_start=list(map(lambda x: int(x), input('START OF RANGE: ').strip().split('.'))),
                        range_end=list(map(lambda x: int(x), input('END  OF  RANGE: ').strip().split('.')))
                    )
                    print('\n{} active host(s):'.upper().format(len(active_hosts)))
                    [print('√ {}'.format(active_host)) for active_host in active_hosts]
                except ValueError:
                    print('value error!\nplease try again...'.upper())
                except IndexError:
                    print('index error!\nplease enter valid ip addresses'.upper())

            elif option == 3:
                try:
                    open_ports = detect_open_ports(
                        ip=input('TARGET IP ADDRESS: '),
                        range_start=int(input('START OF RANGE   : ')),
                        range_end=int(input('END  OF  RANGE   : ')),
                    )
                    print('\n{} open port(s):'.upper().format(len(open_ports)))
                    [print('√ {}'.format(open_port)) for open_port in open_ports]
                except ValueError:
                    print('value error!\nplease try again...'.upper())

            elif option == -1:
                print('end of program'.upper())
                break

            else:
                print('bad input! try again.'.upper())

        except ValueError:
            print('value error!\nplease enter a valid option'.upper())
        except KeyboardInterrupt:
            print('keyboard interrupt\nend of program'.upper())
            break
