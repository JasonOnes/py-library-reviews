""" Sched module is a basic event schduler that defines the scheduler class that takes two arguments a time function and a 
delay function. 

sched.scheduler(timefunc, delayfunc)
where timefunc >>> number of time units (time.monotonic, defaults to time.time*)
delayfunc takes one compatible arg compatible with timefunc eg time.sleep. Will be called with 0 after task is completed to allow 
other thread to run *

Each instance regulates its own queue unless explicitly multithreaded.

* as of Python3.3 the timefunc and delayfunc paramaters are optional and can be used in multi-threaded environs
"""
import sched, time, datetime

# refer to 16.3-time

skedge = sched.scheduler(time.time, time.sleep)

def greeting_object(name):
    print(name)

def print_something_in_two_seconds(name):
    #name = str(name)
    print("Hello")
    print(time.time())
    skedge.enter(2, 1, greeting_object, argument=name) # enters an event into schedule (delay, priority, function, args, kwargs)
    # also .enterabs => schedule an event at specific time, priority used if multiple events scheduled at same time
    skedge.enterabs(time.time(), 2, greeting_object, argument="Y")
    # TODO better demonstrate priority, time.time() can't signify same time, run in order of call, hard code future time?
    skedge.enterabs(time.time(), 1, print, argument="Now")
    print(skedge.queue) # prints list of scheduled events as tuples 
    print(skedge.empty()) #checks event queue
    skedge.run()
    print(time.time())

if __name__ == "__main__":
    print(skedge.empty())# empty
    print_something_in_two_seconds("X") # not empty
    print(skedge.empty())# tasks run, empty again

