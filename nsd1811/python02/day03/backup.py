from time import strftime

def full_backup():


def incr_backup():


if __name__ == '__main__':
    if strftime('%a') == 'Mon':
        full_backup()
    else:
        incr_backup()
