"""Project for Event Management using Python"""
from datetime import datetime
import random
import re
print("Welcome to VIT Funfest - Event registration page\nPlease scroll further for more details!!\n\n")

"""Student Details"""
class student:
    
    def __init__(self):
        
        self.name=input("Enter your name: ")
        
        cntr=0
        while cntr==0:
            self.regno=input("Enter your registration number: ")
            if(len(self.regno)==9):
                cntr=1
            else:
                print('Regno is invalid!')
                
        counter=0
        while counter==0:
            self.no=input("Enter mobile number:")
            if re.match('[1-9][0-9]{9}',self.no):
                counter=1
            else:
                print('Phone Number is invalid!')

"""Function for viewing events in File-EventList"""
def file():
    
    print("Total events planned are as follows: ")

    foo = open("EventList.csv","r")
    x=foo.read()
    print(x)

"""Getting Registration"""
def registration():
    
    dict = {1:"1.Finding Nemo",2:"2.Lucky-7",3:"3.Dance-Off",4:"4.Karate Kid",5:"5.Bottoms up",6:"6.Beer Pong",7:"7.Shots and codes",8:"8.Dumb Sharades",9:"9.Devil's Garden",10:"10.Superbowl"}

    x=input("Please enter the event you want to choose to participate in: ")
    a=int(x)


    while((a>0)&(a<=10)):
        print(dict[a])
        print("You have successfully chosen the event!")
        break
    else:
        print("There is no event associated with the index you have provided! Please retry!!")

    rand = random.randrange(10000,99999)
    print("------------------------Prove you're not a robot! Enter the sequence %s below-----------------------------"%rand)

    flag=0
    while flag==0:
        user=int(input('Enter here:'))
        if (user==rand):
            flag=1
            
        else:
            print("The sequence is not correct")
            flag=0
    print("Thank you")

    
"""Calling the functions"""
file()
registration()


"""Class Object Instantiation"""
student_detail=student()
now=datetime.now()

print('Congratulations! You have successfully registered for the event\n at %s:%s on %s/%s/%s'%(now.hour,now.minute,now.day,now.month,now.year))
