import time 
def recur_countdown_timer(n):
    if n == 0:
        print(n)
        print("Time Over!")
    else:
        print(n)
        time.sleep(1)
        n -= 1
        recur_countdown_timer(n)

def iter_countdown_timer(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print(n)
    print("Time Over!")
    