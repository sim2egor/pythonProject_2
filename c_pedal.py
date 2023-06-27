from threading import Timer
import time

ENABLE_CONTROLS = False

if ENABLE_CONTROLS is True:
    import RPi.GPIO as GPIO


class RepeaterTimer(Timer):
    def run(self) -> None:
        while not self.finished.wait(self.interval):
            self.function()


class c_pedal:
    bpedal: int
    counter: int = 0
    

    def __init__(self, bPedal=None) -> None:
        self.bpedal = bPedal
        if ENABLE_CONTROLS is True:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(bPedal, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(bPedal, GPIO.FALLING, self.pedal_counter)
        self.timer = RepeaterTimer(1, self.reset_counter)
        self.timer.start()

    def reset_counter(self):
        self.counter = 0

    def pedal_counter(self):
        self.counter += 1
        pass

    def __del__(self):
        self.timer.cancel()
        self.timer.join()
        print("Timer die...")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    counter: int = 0
    bPedal = 19
    i = 0
    p = c_pedal(bPedal)
    p2 = c_pedal(22)
    p3 = c_pedal(44)
    for i in range(100000):
        p.pedal_counter()
        p2.pedal_counter()
        p3.pedal_counter()
        print(f'Counter {p.counter}')
        print(f'Counter {p2.counter}')
        print(f'Counter {p3.counter}')

        time.sleep(0.5)
        pass

    p.__del__()
