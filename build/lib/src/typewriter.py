from time import sleep

def write(text,delay,en='\n'):
    for i in text:
        print(i,end='',flush=True)
        sleep(delay)
    print(end=en)


