import time

def countdown(my_time):

    while my_time >= 0:
    
        mins, secs = divmod(my_time, 60)
        timer = '{:02d}:{:02}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        my_time -= 1
    print('Houston has lift off!!')
    
my_time = int(input("Enter a time in seconds: "))

countdown(int(my_time))