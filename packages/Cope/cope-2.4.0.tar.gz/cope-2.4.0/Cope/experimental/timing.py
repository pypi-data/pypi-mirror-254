from atexit import register as registerExit

timingData = {}
def timeFunc(func, accuracy=5):
    """ A function decorator that prints how long it takes for a function to run """
    def wrap(*params, **kwparams):
        global timingData

        t = process_time()

        returns = func(*params, **kwparams)

        t2 = process_time()

        elapsed_time = round(t2 - t, accuracy)
        name = func.__name__

        try:
            timingData[name] += (elapsed_time,)
        except KeyError:
            timingData[name] = (elapsed_time,)

        _printDebugCount()
        # print(name, ' ' * (10 - len(name)), 'took', elapsed_time if elapsed_time >= 0.00001 else 0.00000, '\ttime to run.')
        print(f'{name:<12} took {elapsed_time:.{accuracy}f} seconds to run.')
        #  ' ' * (15 - len(name)),
        return returns
    return wrap

def _printTimingData(accuracy=5):
    """ I realized *after* I wrote this that this is a essentially profiler. Oops. """
    global timingData
    if len(timingData):
        print()

        maxName = len(max(timingData.keys(), key=len))
        maxNum  = len(str(len(max(timingData.values(), key=lambda x: len(str(len(x)))))))
        for name, times in reversed(sorted(timingData.items(), key=lambda x: sum(x[1]))):
            print(f'{name:<{maxName}} was called {len(times):<{maxNum}} times taking {sum(times)/len(times):.{accuracy}f} seconds on average for a total of {sum(times):.{accuracy}f} seconds.')
registerExit(_printTimingData)

class getTime:
    """ A class to use with a with statement like so:
        with getTime('sleep'):
            time.sleep(10)
        It will then print how long the enclosed code took to run.
    """
    def __init__(self, name, accuracy=5):
        self.name = name
        self.accuracy = accuracy

    def __enter__(self):
        self.t = process_time()

    def __exit__(self, *args):
        # args is completely useless, not sure why it's there.
        t2 = process_time()
        elapsed_time = round(t2 - self.t, self.accuracy)
        print(self.name, ' ' * (15 - len(self.name)), 'took', f'{elapsed_time:.{self.accuracy}f}', '\ttime to run.')

def psleep(seconds, func, rtn=True):
    """ Process sleep: run func in a while loop for a specified amount of time """
    end = now()
    while now() < end:
        func()
