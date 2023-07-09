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
    value: int =0
    

    def __init__(self, bPedal=None) -> None:
        self.bpedal = bPedal
        if ENABLE_CONTROLS is True:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(bPedal, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(bPedal, GPIO.FALLING, self.pedal_counter)
        self.timer = RepeaterTimer(0.1, self.reset_counter)
        self.timer.start()

    def reset_counter(self):
        self.value= self.counter
        self.counter = 0

    def pedal_counter(self,pin):
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
    p2 = c_pedal(5)
    p3 = c_pedal(23)
    for i in range(100000):
        print(f'Counter1 {p.value}')
        print(f'Counter2 {p2.value}')
        print(f'Counter3 {p3.value}')

        time.sleep(0.5)
        pass

    p.__del__()
