""" This module uses a basic binary sort algorithm to maintain a sorted list WHILE inserting an item rather than inserting then
sorting the list. May improve speed for long lists with involved comparisons (expensive operations)."""

# lists must be sorted

import bisect
import random
import timeit
from collections import Counter

def person_before_bob(people_list, person_name):
    #find the name of the person who comes before Bob in a sorted list of names, Capitalized name come first
    people_list = sorted(people_list)
    print(people_list)
    left_of_Bob = bisect.bisect_left(people_list, person_name)
    try:
        if left_of_Bob != len(people_list) and people_list[left_of_Bob] == person_name:
            return people_list[left_of_Bob -1]
    except ValueError:
        # no one comes before BOB!
        return None

def how_many_kids_failed(grades_list, number_grade):
    grades = sorted(grades_list)
    failure_fulcrum = bisect.bisect_left(grades, number_grade)
    return len(grades_list[:failure_fulcrum])

def how_many_kids_passed(grades_list, number_grade):
    grades = sorted(grades_list)
    success_fulcrum = bisect.bisect_right(grades, number_grade)
    return len(grades_list[success_fulcrum:])

""" Time trials using bisect and simple add then sort"""
# see 27.5 timeit lib for detes

def time_wrapper(f, *args, **kwargs):
    # wraps function that takes args into one that doesn't, necessary for timeit
    def time_wrapped():
        return f(*args, **kwargs)
    return time_wrapped

def insert_number_bisect(num_list, number_of_numbers_to_insert):
    # inserts numbers into list while keeping it sorted
    num_list = sorted(num_list)
    for num in range(number_of_numbers_to_insert):
        num = random.randint(1, 100)
        bisect.insort(num_list, num)
    return num_list

def add_number(num_list, number_of_numbers_to_insert):
    # no insertion just add and sort
    num_list = sorted(num_list)
    for num in range(number_of_numbers_to_insert):
        num = random.randint(1, 100)
        num_list.append(num)
    x = sorted(num_list)
    return x

def value_items(discounts, breakpoints=[10, 25, 50, 80], deals=['meh', 'good deal', 'great deal', 'Steal!']):
    # might be used to see how great a sale at a store is depending on the percent of items that are a Steal
    discounts = sorted(discounts)
    deal_qualities = []
    for discount in discounts:
        index = bisect.bisect(breakpoints, discount)
        deal_qualities.append(deals[index-1])
    return deal_qualities

def hows_the_sale(discounts):
    deals = value_items(discounts)
    x = len(set(deals))
    #print(x)
    if x == 1:
        return x
    else:
        quality_count = Counter(deals)
        return max(deals, key=quality_count.get)            
        



if __name__ == "__main__":

    grades = [12, 88, 93, 22, 67, 50, 76, 94, 83, 72, 66, 55, 92, 63, 53, 32, 100, 98, 64, 62, 75, 93, 55, 49, 73]
    big_list = [random.randint(1, 100) for num in range(5000)]
    sale_percents = [50, 62, 10, 15, 15, 15, 80, 10, 60, 20, 45, 60, 75]
    people_list = ['Timmy', 'Judy', 'Alice', 'Bob', 'Karen', 'Steve', 'Hula']

   

    print(person_before_bob(['alice', 'steve', 'bob', 'timmy', 'Hank', 'George' ], 'bob'))
    print(person_before_bob([2, 7, 23, 4232, 5], 5))

    
    print("{} many kids are failing this class".format(how_many_kids_failed(grades, 60)))
    print("{} are actually passing".format(how_many_kids_passed(grades, 60)))

   
    
    print(value_items(sale_percents))
    print("Based on the above tags the sale is {}!".format(hows_the_sale(sale_percents)))
    # Timeit shows it's faster to just add and sort rather than insert, so bisect better suited for lambda functions
    # perhaps, where items are inserted in a stream ?

    wrap_x = time_wrapper(add_number, grades, 500)
    wrap_bisect = time_wrapper(insert_number_bisect, grades, 500)
    time_x = timeit.timeit(wrap_x, number=1000)
    time_bisect = timeit.timeit(wrap_bisect, number=1000)

    
    big_wrap_bisect = time_wrapper(insert_number_bisect, big_list, 500)
    big_add_wrap = time_wrapper(add_number, big_list, 500)
    time_big_bisect = timeit.timeit(big_wrap_bisect, number=1000)
    time_big_add = timeit.timeit(big_add_wrap, number=1000)

    print("Time of execution for {} with 25 items:  {}".format(insert_number_bisect, time_bisect))
    print("Time of execution for {} with 25 items:  {}".format(add_number, time_x))
    
    print("Time of execution for {} with 5000 items:  {}".format(insert_number_bisect, time_big_bisect))
    print("Time of execution for {} with 5000 items:  {}".format(add_number, time_big_add))
    
     