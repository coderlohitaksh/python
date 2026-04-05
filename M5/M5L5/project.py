import tkinter as tk
import random
import time
import os
from PIL import Image, ImageTk

TRACK_LENGTH = 700

class Car:
    def __init__(self, name, image, top_speed, accel, is_player=False):
        self.name = name
        self.image = image
        self.base_top_speed = top_speed
        self.base_accel = accel
        self.is_player = is_player
        self.reset()

    def reset(self):
        self.top_speed = self.base_top_speed
        self.accel = self.base_accel
        self.speed = 0
        self.position = 0
        self.nitro = 0
        self.luck = random.uniform(0.9, 1.1)

    def update(self, dt, weather_factor):
        if not self.is_player:
            if random.random() < 0.02:
                self.speed += random.uniform(0.5, 1.5)

        if not self.is_player and random.random() < 0.01:
            self.nitro = random.randint(10, 25)

        if random.random() < 0.01:
            if random.choice(["boost", "slow"]) == "boost":
                self.speed += random.uniform(2, 4)
            else:
                self.speed *= random.uniform(0.7, 0.9)

        boost = 6 if self.nitro > 0 else 0
        target_speed = (self.top_speed + boost) * self.luck

        self.speed += (target_speed - self.speed) * self.accel * dt * weather_factor

        if not self.is_player:
            self.speed += random.uniform(-0.5, 0.5)

        if self.speed < 0:
            self.speed = 0

        if self.speed > self.top_speed + 6:
            self.speed = self.top_speed + 6

        self.position += self.speed * dt * 60

        if self.nitro > 0:
            self.nitro -= 1

class RaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Racing Game")

        self.canvas = tk.Canvas(root, width=1000, height=500, bg="black")
        self.canvas.pack()

        self.load_sprites()

        self.cars = [
            Car("BMW M5", self.car_images[0], 13, 1.8),
            Car("Ferrari SF90", self.car_images[1], 15, 2.0),
            Car("Lamborghini Aventador", self.car_images[2], 14.5, 1.9),
            Car("Tesla Model S Plaid", self.car_images[3], 13.5, 2.2),
        ]

        self.car_objs = []
        self.labels = []
        self.flames = []

        self.running = False
        self.last_time = time.time()
        self.weather = "clear"

        self.player_choice = tk.StringVar(value=self.cars[0].name)

        self.setup_ui()
        self.draw_track()
        self.create_cars()

        self.root.bind("<space>", self.player_nitro)
        self.root.bind("<Up>", self.accelerate)
        self.root.bind("<Down>", self.brake)

    def load_sprites(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        files = [
            "BMW M5.png",
            "Ferrari SF90.png",
            "lamborghini Aventador.png",
            "Tesla Model S Plaid.png"
        ]

        self.car_images = []

        for file in files:
            path = os.path.join(base_dir, file)
            img = Image.open(path)
            img = img.resize((120, 60), Image.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            self.car_images.append(tk_img)

        self.root.images = self.car_images

    def setup_ui(self):
        frame = tk.Frame(self.root, bg="black")
        frame.pack()

        tk.Button(frame, text="START", command=self.start).grid(row=0, column=0)
        tk.Button(frame, text="RESET", command=self.reset).grid(row=0, column=1)
        tk.Button(frame, text="RAIN", command=self.toggle_weather).grid(row=0, column=2)

        tk.OptionMenu(frame, self.player_choice, *[c.name for c in self.cars]).grid(row=1, column=0)

        self.info = tk.Label(self.root, text="", fg="white", bg="black", font=("Arial", 14))
        self.info.pack()

    def draw_track(self):
        self.road_lines = []

        self.canvas.create_rectangle(0, 100, 1000, 400, fill="#333", outline="")

        for i in range(10):
            line = self.canvas.create_line(i * 120, 250, i * 120 + 60, 250, fill="white", width=4)
            self.road_lines.append(line)

        self.canvas.create_line(TRACK_LENGTH + 100, 100, TRACK_LENGTH + 100, 400, fill="yellow", width=4)

    def create_cars(self):
        y = 140
        for car in self.cars:
            obj = self.canvas.create_image(80, y, image=car.image)
            label = self.canvas.create_text(180, y, text=car.name, anchor="w", fill="white")
            flame = self.canvas.create_oval(0, 0, 0, 0, fill="", outline="")

            self.car_objs.append(obj)
            self.labels.append(label)
            self.flames.append(flame)
            y += 70

    def start(self):
        for car in self.cars:
            car.reset()
            car.is_player = (car.name == self.player_choice.get())

            if not car.is_player:
                car.top_speed *= random.uniform(0.88, 1.02)
                car.accel *= random.uniform(0.9, 1.05)

        self.running = False
        self.info.config(text="3")
        self.root.after(1000, lambda: self.info.config(text="2"))
        self.root.after(2000, lambda: self.info.config(text="1"))
        self.root.after(3000, self.begin_race)

    def begin_race(self):
        self.running = True
        self.last_time = time.time()
        self.loop()

    def reset(self):
        self.running = False

        for i, car in enumerate(self.cars):
            car.reset()
            self.canvas.coords(self.car_objs[i], 80, 140 + i * 70)
            self.canvas.coords(self.labels[i], 180, 140 + i * 70)
            self.canvas.coords(self.flames[i], 0, 0, 0, 0)

        self.info.config(text="")

    def toggle_weather(self):
        self.weather = "rain" if self.weather == "clear" else "clear"

    def player_nitro(self, event):
        for car in self.cars:
            if car.is_player:
                car.nitro = 25

    def accelerate(self, event):
        for car in self.cars:
            if car.is_player:
                car.speed += 2.5

    def brake(self, event):
        for car in self.cars:
            if car.is_player:
                car.speed -= 2
                if car.speed < 0:
                    car.speed = 0

    def scroll_road(self, speed):
        for line in self.road_lines:
            self.canvas.move(line, -speed, 0)
            x1, y1, x2, y2 = self.canvas.coords(line)
            if x2 < 0:
                self.canvas.move(line, 1000, 0)

    def animate_effects(self, index, car):
        obj = self.car_objs[index]
        flame = self.flames[index]

        if car.nitro > 0:
            x, y = self.canvas.coords(obj)
            size = random.randint(8, 16)
            offset = random.randint(20, 30)
            self.canvas.coords(flame, x - offset, y - size/2, x - offset + size, y + size/2)
            color = random.choice(["orange", "yellow", "red"])
            self.canvas.itemconfig(flame, fill=color, outline=color)
            self.canvas.move(obj, random.uniform(-2, 2), random.uniform(-1, 1))
        else:
            self.canvas.coords(flame, 0, 0, 0, 0)

    def update_leaderboard(self):
        positions = sorted(self.cars, key=lambda c: c.position, reverse=True)
        text = " | ".join([f"{c.name}: {int(c.position)}" for c in positions])
        self.info.config(text=f"{text}   | Weather: {self.weather}")

    def loop(self):
        if not self.running:
            return

        now = time.time()
        dt = now - self.last_time
        self.last_time = now

        weather_factor = 0.7 if self.weather == "rain" else 1.0

        for car in self.cars:
            if car.is_player:
                car.speed += 0.3

        max_dx = 0

        for i, car in enumerate(self.cars):
            car.update(dt, weather_factor)

            dx = car.speed * dt * 60
            max_dx = max(max_dx, dx)

            self.canvas.move(self.car_objs[i], dx, 0)
            self.canvas.move(self.labels[i], dx, 0)

            self.animate_effects(i, car)

            if car.position >= TRACK_LENGTH:
                self.finish(car)
                return

        self.scroll_road(max_dx)
        self.update_leaderboard()

        self.root.after(16, self.loop)

    def finish(self, car):
        self.running = False
        self.info.config(text=f"Winner: {car.name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RaceApp(root)
    root.mainloop() 