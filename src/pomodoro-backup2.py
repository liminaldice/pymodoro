import sys
import time

"""
# Example user input
    user_input = input('yes/no: ')

    if user_input.lower() == 'yes':
        print('typed yes')
    elif user_input.lower() == 'no':
        print('typed no')
    else:
        print('type an answer please')

# Example timer

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("Time's up!")


"""

class MyClass():

    counter = 0

    def __init__(self) -> None:
        valid_input = ['y', 'yes']
        user_input = input('Start timer? Y/N: ')
        if user_input.lower() in valid_input:
            timer_started = self.timer_start()
        else:
            pass

    def timer_start(self) -> None:
        pomodoro = 5 #1500
        print("CTRL+C to STOP")
        try:
            print("\nPomodoro Started!")
            for x in range(pomodoro, 0, -1):
                seconds = x % 60
                minutes = int(x / 60) % 60
                hours = int(x / 3600)
                sys.stdout.write("\r")
                sys.stdout.write(f"{minutes:02}:{seconds:02}")
                sys.stdout.flush()
                time.sleep(1)

            else:
                self.counter += 1
                rest_started = self.rest_start()


        except KeyboardInterrupt:
            print(f"Total sessions: {self.counter}")
            print("\nTerminated.")

    def rest_start(self) -> None:
        rest_timer = 5 #300
        print("\nRest Started!")
        for x in range(rest_timer, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            sys.stdout.write("\r")
            sys.stdout.write(f"{minutes:02}:{seconds:02}")
            sys.stdout.flush()
            time.sleep(1)
        else:
            print(f"\nSessions = {self.counter}")
            valid_input = ['y', 'yes']
            user_input = input('Start NEW session? Y/N: ')
            if user_input.lower() in valid_input:
                timer_started = self.timer_start()
            else:
                print(f"Total sessions: {self.counter}")




MyClass()


