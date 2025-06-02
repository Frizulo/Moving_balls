# app.py

import tkinter as tk
from ball import Ball

MAX_BALLS = 10

class BallApp:
    # --- init ---
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Moving Balls")
        self.root.geometry("300x200")

        self.canvas = tk.Canvas(root, width=300, height=200, bg='white')
        self.canvas.pack()

        # Status label (ball count) 
        self.status = tk.Label(root, text="number of balls: 0")
        self.status.place(x=0, y=180)

        # Bind mouse events
        self.canvas.bind("<Button-3>", self.add_ball)           # Right-click: Add ball
        self.canvas.bind("<Button-2>", self.clear_all_balls)    # Middle-click: Clear all

        self.balls = []
        self.cleanup_loop()
    # --- init ---

    # --- add_ball ---
    def add_ball(self, event):
        if len(self.balls) >= MAX_BALLS:
            return
        try:
            ball = Ball(self.canvas, event.x, event.y)
            self.balls.append(ball)
            self.status.config(text=f"number of balls: {len(self.balls)}")
        except Exception as e:
            print("Error creating ball:", e)

    def clear_all_balls(self, event=None):
        for ball in self.balls:
            ball.running = False
            ball.remove()
        self.balls.clear()
    # --- add_ball ---

    # --- cleanup_loop ---
    def cleanup_loop(self):
        # Remove inactive balls when running=False
        self.balls = [b for b in self.balls if b.running]
        self.status.config(text=f"number of balls: {len(self.balls)}")
        self.root.after(100, self.cleanup_loop) # Update interval: every 100 ms
    # --- cleanup_loop ---
