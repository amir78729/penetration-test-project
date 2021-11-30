from ping import ping
from datetime import datetime
from tqdm import tqdm


def detect_active_hosts(range_start, range_end):
    active_hosts = []
    detecting_progress = tqdm(range(range_start[3], range_end[3] + 1))
    for i in detecting_progress:
        target_host = '{}.{}.{}.{}'.format(range_start[0], range_start[1], range_start[2], i)
        detecting_progress.set_description('PINGING {}'.format(target_host))
        response = ping(host=target_host, count=1, wait=0.5)
        if '1 packets transmitted, 1 packets received, 0.0% packet loss' in response:
            active_hosts.append(target_host)
    log_active_results(range_start, range_end, active_hosts)
    return active_hosts


def log_active_results(range_start, range_end, active_hosts):
    try:
        with open("results/result_detect_active_hosts.txt", "a") as file:
            file.write('@ {}'.upper().format(datetime.now()))
            file.write('\nactive hosts in range [{}.{}.{}.{} - {}.{}.{}.{}]:'.upper().format(
                range_start[0], range_start[1], range_start[2], range_start[3],
                range_end[0], range_end[1], range_end[2], range_end[3],
            ))
            [file.write('\n√ ' + host) for host in active_hosts]
            if not active_hosts:
                file.write('\n× no active host was founded!'.upper())
            file.write('\n----------------------------------------------------------\n')
    except FileNotFoundError:
        print('PLEASE CREATE \"/results/result_detect_active_hosts.txt\" AND TRY AGAIN.')


if __name__ == '__main__':
    detect_active_hosts(
        range_start=list(map(lambda x: int(x), input('START OF RANGE: ').strip().split('.'))),
        range_end=list(map(lambda x: int(x), input('END  OF  RANGE: ').strip().split('.')))
    )
