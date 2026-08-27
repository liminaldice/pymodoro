# Rewritten to have a cleaner switch case prompt
# Needs to use venv python file to execute the playsound3 module
import sys
import time
from playsound3 import playsound

class Program():
    counter = 0
    counter_update = counter

    def __init__(self) -> None:
        self.prompt_timer()


    def prompt_timer(self) -> None:
        answer = input("\nStart timer? Y/n: ").lower()
        match answer:
            case 'y' | 'yes' | '':
                self.timer_start()
            case 'n' | 'no':
                print(f"\nTotal sessions: {self.counter}")
                print(f"\nTerminated.")
            case _:
                print("\nPlease enter a valid answer.")

    def prompt_rest(self) -> None:
        answer = input("\nStart rest? Y/n: ").lower()
        match answer:
            case 'y' | 'yes' | '':
                self.rest_start()
            case 'n' | 'no':
                print(f"\nTotal sessions: {self.counter}")
                print(f"\nTerminated.")
            case _:
                print("\nPlease enter a valid answer.")



    def timer_start(self) -> None:
        pomodoro:int = 1
        print("CTRL+C to STOP")
        try:
            print("\nPomodoro Started!")
            for x in range(pomodoro, 0, -1):
                seconds = x % 60
                minutes = int(x / 60) % 60
                sys.stdout.write("\r")

                sys.stdout.write(f"{minutes:02}:{seconds:02}")
                sys.stdout.flush()
                time.sleep(1)
            else:
                self.counter += 1
                self.notification_sound()
                self.prompt_rest()

        except KeyboardInterrupt:
            print(f"Total sessions: {self.counter}")
            print(f"\nTerminated.")

    def rest_start(self) -> None:
        rest_timer = 1
        print("\nRest Started!")
        for x in range(rest_timer, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            sys.stdout.write("\r")
            
            sys.stdout.write(f"{minutes:02}:{seconds:02}")
            sys.stdout.flush()
            time.sleep(1)
        else:
            self.notification_sound()
            print(f"\nSessions = {self.counter}")
            self.prompt_timer()
                
    def notification_sound(self) -> None:
        print("\nsound")

Program()
