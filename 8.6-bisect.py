""" This module uses a basic binary sort algorithm to maintain a sorted list WHILE inserting an item rather than inserting then
sorting the list. May improve speed for long lists with involved comparisons (expensive operations)."""

# lists must be sorted

import bisect
import random
import timeit

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

def put_person_before_bob(people_list, person_name):
    #inserts new person into sorted list before bob
    #new_people_list = bisect.insort_left(people_list, person_name)
    print(bisect.insort_left(people_list, person_name))

def how_many_kids_failed(grades_list, number_grade):
    grades = sorted(grades_list)
    failure_fulcrum = bisect.bisect_left(grades, number_grade)
    return len(grades_list[:failure_fulcrum])

def how_many_kids_passed(grades_list, number_grade):
    grades = sorted(grades_list)
    success_fulcrum = bisect.bisect_right(grades, number_grade)
    return len(grades_list[success_fulcrum:])

""" Time trials using bisect and simple add then sort"""
def insert_number(num_list, number_of_numbers_to_insert):
    num_list = sorted(num_list)
    for num in range(number_of_numbers_to_insert):
        num = random.randint(1, 100)
        num_list.append(num)
    return sorted(num_list)



def insert_number_bisect(num_list, number_of_numbers_to_insert):
    # inserts numbers into list while keeping it sorted
    num_list = sorted(num_list)
    for num in range(number_of_numbers_to_insert):
        num = random.randint(1, 100)
        bisect.insort(num_list, num)
    return num_list

"""
def value_items(percent_off, breakpoints=[10, 25, 50, 80], deals=['meh', 'good deal', 'great deal', 'Steal!']):
    # might be used to see how great a sale at a store is depending on the percent of items that are a Steal
    index = bisect.bisect(breakpoints, percent_off)
    return deals[index]
"""
if __name__ == "__main__":

    people_list = ['Timmy', 'Judy', 'Alice', 'Bob', 'Karen', 'Steve', 'Hula']
    print(person_before_bob(['alice', 'steve', 'bob', 'timmy', 'Hank', 'George' ], 'bob'))
    print(person_before_bob([2, 7, 23, 4232, 5], 5))

    grades = [12, 88, 93, 22, 67, 50, 76, 94, 83, 72, 66, 55, 92, 63, 53, 32, 100, 98, 64, 62, 75, 93, 55, 49]
    print(how_many_kids_failed(grades, 60))
    print(how_many_kids_passed(grades, 60))

    print(":::::::::::::::::::")
    put_person_before_bob(people_list, 'Dave')
    # sale_percents = [50, 62, 10, 15, 15, 15, 80, 10, 60, 20, 45, 60, 75]
    # print([value_items(percent_off) for percent_off in sorted(sale_percents)])
    print(insert_number(grades, 12))

#TODO come back with timeit and function wrappers
    # timeit.timeit(insert_number(grades, 100), 1000)
    # timeit.timeit(insert_number_bisect(grades, 100), 1000)