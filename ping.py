import platform
import os
from datetime import datetime


def ping(host, count=1, wait=-1, _print=False, log=False):

    # set number of packets
    count_param = '-c {} '.format(count) if platform.system().lower() != 'windows' else '-n {} '.format(count)

    # set waiting time
    wait_param = '' if wait == -1 else '-W {} '.format(wait)

    # making the command
    command = 'ping {}{}{}'.format(count_param, wait_param, host)
    if _print:
        print('> ' + command + '\n...')
    ping_result = os.popen(command).read()
    if log:
        log_ping(command, ping_result)
    return ping_result


def log_ping(command, ping_result):
    try:
        with open("results/result_ping.txt", "a") as file:
            file.write('@ {}'.upper().format(datetime.now()))
            file.write('\n> {}'.upper().format(command))
            file.write('\n{}'.format(ping_result.replace('\n\n', '\n')))
            file.write('---------------------------------------------------------------------------------------\n')
    except FileNotFoundError:
        print('PLEASE CREATE \"/results/result_ping.txt\" AND TRY AGAIN.')


if __name__ == '__main__':
    ping(host=input('HOST : '), count=int(input('COUNT: ')), wait=-1, _print=True, log=True)
