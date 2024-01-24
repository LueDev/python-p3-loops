#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while(counter > 0):
        print(counter)
        counter -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [num**2 for num in int_list]

def fizzbuzz():
    # code goes here!
    
    # List Comprehension fizzbuzz. Notice the "Else" can be reused rather than elif's 
    return [print("FizzBuzz") if i % 5 == 0 and i % 3 == 0 else print("Fizz") if i % 3 == 0 else print("Buzz") if i % 5 == 0 else print(str(i)) for i in range(1, 101)]
    
    # Normal Conditional : 
    # for i in range(1, 101):
    #     if i % 5 == 0 and i % 3 == 0:
    #         print("FizzBuzz")
    #     elif i % 3 == 0 :
    #         print("Fizz")
    #     elif i % 5 == 0 :
    #         print("Buzz")
    #     else: 
    #         print(i)

fizzbuzz()