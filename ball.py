# ball.py

import random
import threading
import time
import tkinter as tk

class Ball:
    MAX_RADIUS = 15
    MIN_RADIUS = 5
    MIN_LIFE = 2
    MAX_LIFE = 15
    MIN_SPEED = 1.0
    MAX_SPEED = 3.0

    # --- init ---
    def __init__(self, canvas: tk.Canvas, x: float, y: float) -> None:
        self.canvas = canvas
        self.radius = random.randint(self.MIN_RADIUS, self.MAX_RADIUS)
        self.life = random.uniform(self.MIN_LIFE, self.MAX_LIFE)
        self.speed = random.uniform(self.MIN_SPEED, self.MAX_SPEED)
        self.dx = random.choice([-1, 1]) * self.speed
        self.dy = random.choice([-1, 1]) * self.speed

        # Random color
        __colors = ['lightcoral', 'palegreen', 'lightsteelblue', 'moccasin', 'violet', 'pink', 'cyan', 'gold']
        color = random.choice(__colors)

        # Draw ball and life label
        self.id = canvas.create_oval(
            x - self.radius, y - self.radius,
            x + self.radius, y + self.radius,
            fill=color
        )
        self.text_id = canvas.create_text(x, y, text=str(int(self.life)), fill='black', font=("Arial", 8))

        self.start_time = time.time()
        self.running = True

        self.thread = threading.Thread(target=self.animate, daemon=True)
        self.thread.start()
    # --- init ---

    # --- animate ---
    def animate(self):
        while self.running and (time.time() - self.start_time) < self.life:
            self.canvas.after(0, self.move)
            time.sleep(0.02) # Frame delay
        self.canvas.after(0, self.remove)
    # --- animate ---

    # --- move ---
    def move(self):
        if not self.running:
            return

        x1, y1, x2, y2 = self.canvas.coords(self.id)
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Bounce off window edges
        if x1 + self.dx < 0 or x2 + self.dx > width:
            self.dx *= -1
        if y1 + self.dy < 0 or y2 + self.dy > height:
            self.dy *= -1

        # Update remaining life
        remaining = max(0, int(self.life - (time.time() - self.start_time)))
        self.canvas.itemconfig(self.text_id, text=str(remaining))

        # Move ball and label
        self.canvas.move(self.id, self.dx, self.dy)
        self.canvas.move(self.text_id, self.dx, self.dy)
    # --- move ---

    # --- remove ---
    def remove(self):
        self.running = False
        self.canvas.delete(self.id)
        self.canvas.delete(self.text_id)
    # --- remove ---