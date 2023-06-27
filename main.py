# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from  threading import Timer

class RepeaterTimer(Timer):
    def run(self) -> None:
        while not self.finished.wait(self.interval):
            self.function(*self.args,**self.kwargs)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    i=1
    timer = RepeaterTimer(1,print_hi,args=[1])
    print_hi('PyCharm')
    timer.start()
    while True:
        pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
