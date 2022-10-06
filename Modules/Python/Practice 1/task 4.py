import time

def set_timer():

    hours = int(input('hours: '))
    minutes = int(input('minutes: '))
    seconds = int(input('seconds: '))

    total = seconds + minutes*60 + hours*3600

    for i in range(total, 0, -1):
        print(f'{i//3600}:{i//60%60}:{i%60}')
        time.sleep(1)

set_timer()
