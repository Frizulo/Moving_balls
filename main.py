'''
Auther: Frizulo <frizulo.0326@gmail.com>
Date: 2025.06.02

Description: 
Python Tkinter + threading → animated moving balls in a GUI window.  

features:
- Right-click to generate up to 10 balls with random attributes (color, speed, lifespan, direction) 
- Middle-click to clear all balls instantly   
- Balls move smoothly on the canvas and bounce off window edges 
- Remaining lifespan is displayed at the center of each ball 
- Balls automatically disappear when their lifespan ends   
- Real-time display of current ball count at the bottom-left corner of the window
'''
# main.py

from tkinter import Tk
from app import BallApp

if __name__ == "__main__":
    root = Tk()
    app = BallApp(root)
    root.mainloop()
