#!/usr/bin/python3

import progress
from progress.bar import Bar
import colored 
from colored import fg,attr
import pyperclip
from pyperclip import copy
import time
from time import sleep
import banner
from banner import logo


yellow = fg("light_yellow")
red = fg("light_red")
green = fg("light_green")
reset = attr("reset")
cyan =fg("light_cyan")




def example():
    print("Please use " + red+'quit'+ reset +" or " + red + "'exit'" + reset +" to EXIT")
    

def validation():
    

    passwd = input(cyan+"Input Password to be validated>>"+reset)
    def bar_():
        with Bar( max=20) as bar:
            for i in range(len(list(passwd))):
                bar.next()
                sleep(0.01)
        bar.finish        

    def password_check(passwd): 
        SpecialSym =['$', '@', '#', '%'] 
        val = True
        if passwd in ["exit","quit"]:
            quit()
        if len(passwd) < 8: 
            print(red+'Length should be at least 8'+reset) 
            val = False
            
        if len(passwd) > 20: 
            print(red+'length should be not be greater than 20'+reset) 
            val = False
            
        if not any(char.isdigit() for char in passwd): 
            print(red +'Password should have at least one numeral'+reset) 
            val = False
            
        if not any(char.isupper() for char in passwd): 
            print(red +'Password should have at least one uppercase letter'+ reset) 
            val = False
            
        if not any(char.islower() for char in passwd): 
            print(red +'Password should have at least one lowercase letter'+reset) 
            val = False
            
        if not any(char in SpecialSym for char in passwd): 
            print(red + "Password should have at least one of the symbols '$@#'" + reset) 
            val = False
        if val : 
            print(green+"The Password is Strong!"+reset)
            pyperclip.copy(passwd)
            print(yellow+"Password Copied!"+reset) 
        if val == False :
            repeat()
        
    bar_()
    password_check(passwd)
     
def nothing():
    print()            

def repeat ():
    validation()

banner.logo()   
validation()

