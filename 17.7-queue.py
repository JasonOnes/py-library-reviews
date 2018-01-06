"""queue - synchronized queue class - takes care of all the locking stuff for threading
by blocking competing threads and keeping things orderly within the queue. Three different
queue types for different order of operations. """
# queue.Queue => (FIFO)First In First Out
# queue.LifoQueue => Last In First Out
# queue.PriorityQueue => prioritized by lowest value first, priority designated during thread
#                        construction (priority_rate, data) or lowest first would be 
#                        sorted(list(entries))[0]
# (maxsize) => default is 0 in which case the queue size may be infinite otherwise size is limited 
#              to what is set e.g. queue.LifoQueue(23) can only contain up to 23 entries

import queue
import threading
from time import sleep 

"""simple demo functs"""
def simple_queue(some_list): #FIFO
    q = queue.Queue()
    for item in some_list:
        q.put(item)
    while not q.empty():
        print(q.get())

def last_in_last_out(some_list): #LIFO
    q = queue.LifoQueue()
    for item in some_list:
        q.put(item)
    while not q.empty():
        print(q.get())

def prioritize_family(some_list): # execute by priority use family for specificity
    # in the case of names, prioritized alphabetically
    #list_x = ['steve', 'julie', 'karen', 'dave']
    q = queue.PriorityQueue()
    for item in some_list:
        q.put(item)
    #     if item == 'steve':
    #         q.put(item, 3)
    #     elif item == 'julie':
    #         q.put(item, 1)
    #     elif item == 'karen':
    #         q.put(item, 2)
    #     elif item == 'dave':
    #         q.put(item, 0)
    while not q.empty():
        print(q.get())


"""demo with threads"""
# TODO go over this again
def nap_time(duration_in_secs, napper_name):
    print('Sleep well {}.'.format(napper_name))
    sleep(duration_in_secs)
    print('{} Up and ATOM!'.format(napper_name))

def make_a_queue_of_naps(family_size, nap_length):
    # people of the family need to nap but not all at once, first to sleep is the first to wake (FIFO)
    queue_of_naps = queue.Queue(family_size+1)
    family = ['MomAnna', 'MomBetty', 'Brother', 'Sister']
    for member in family:
        member_nap = threading.Thread(target=nap_time, args=[nap_length, member])
        queue_of_naps.put(member_nap)
        member_nap.start()
    print("there are {} naps scheduled".format(queue_of_naps.qsize()))
    print("the queue is empty: {}".format(queue_of_naps.empty()))
    print("the queue is full: {}".format(queue_of_naps.full()))
    print("How about now?")
    queue_of_naps.put(threading.Thread(target=nap_time, args=[5, 'Timmy']))
    print("the queue is full: {}".format(queue_of_naps.full()))

def make_lifo_queue_of_naps(family_size, nap_length):
    # in this family the kids don't sleep as long as the parents, last to sleep first to wake
    queue_of_naps = queue.LifoQueue(family_size)
    family = ['DadBob', 'DadSteve', 'Erica', 'Steve Jr.']
    for member in family:
        member_nap = threading.Thread(target=nap_time, args=[nap_length, member])
        queue_of_naps.put(member_nap)
        member_nap.start()
    try:
        queue_of_naps.put(threading.Thread(target=nap_time, args=[5, 'Timmy']))
    except Fullerror:
        print("the queue is full: {}".format(queue_of_naps.full()))
        

def prioritize_naps():
    # same family but priority given to the Steve's because the have a B-Ball game 
    queue_of_naps = queue.PriorityQueue() #not going to bother with maxsize
    family = ['DadBob', 'DadSteve', 'Erica', 'Steve Jr.']
    for member in family:
        if member == 'DadSteve':
            dad_steve_nap = threading.Thread(target=nap_time, args=[6, member])
            queue_of_naps.put(1, dad_steve_nap)
            # priority = 1
            # naptime = 6
        elif member == 'Steve Jr.':
            stevie_nap = threading.Thread(target=nap_time, args=[6, member])
            queue_of_naps.put(2, stevie_nap)
    
        elif member == 'DadBob':
            bob_nap = threading.Thread(target=nap_time, args=[10, member])
            queue_of_naps.put(3, bob_nap)
            
        elif member == 'Erica':
            erica_nap = threading.Thread(target=nap_time, args=[8, member])
            queue_of_naps.put(4, erica_nap)
            # priority = 4
            # naptime = 8
    while not queue_of_naps.empty():
        next_nap = queue_of_naps.get()
       


family = ['Momma Jo', 'Mommy Kathy', 'Timmy', 'Billy', 'Karen']
nums = [12, 33, 2, 43, 348]
places_in_race = [(2, 'steve'), (4, 'mike'), (1, 'joanie'), (3, 'billie')]
simple_queue(family)
print("+++++++++++++++++++++++++")
last_in_last_out(family)
print("-------------------------")
prioritize_family(family) # alphabetical
prioritize_family(nums) # asc order
prioritize_family(places_in_race) # by given priority
