#May 20 12:32 Typing Speed Test Using time Module

import time
#this module helpful in games , performance mesurement, timers, real applications

def speed_test(sentence):
    print(sentence)
    start_time = time.time()
    typed = input("Enter the sentence to measure your speed: ")
    end_time = time.time()
    total_time = end_time - start_time
    if typed == sentence:
        print("correctly typed!")
    else:
        print("Type again!")
    print(f"Time taken: {total_time}")

while True:
    sentence = "Python is awesome!"
    print("1.Start Typing Test"
    "\n2.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        speed_test(sentence)
    elif choice == "2":
        print("Exiting. . .")
        break
    else:
        print("Error occured!")

        