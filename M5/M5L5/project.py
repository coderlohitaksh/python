import tkinter as tk
import random
import time

TRACK_LENGTH = 700


class Car:
    def __init__(self, name, image, top_speed, accel, is_player=False):
        self.name = name
        self.image = image
        self.top_speed = top_speed
        self.accel = accel
        self.is_player = is_player
        self.reset()

    def reset(self):
        self.speed = 0
        self.position = 0
        self.nitro = 0

    def update(self, weather_factor):
        boost = 2 if self.nitro > 0 else 0
        self.speed += (self.accel + boost + random.uniform(-0.2, 0.2)) * weather_factor
        self.speed = max(0, min(self.speed, self.top_speed + 3))
        self.position += self.speed

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
            Car("BMW M5", self.car_images[0], 13, 1.1),
            Car("Ferrari SF90", self.car_images[1], 15, 1.4),
            Car("Lamborghini Aventador", self.car_images[2], 14.5, 1.3),
            Car("Tesla Model S Plaid", self.car_images[3], 13.5, 1.7),
        ]

        self.car_objs = []
        self.labels = []

        self.running = False
        self.last_time = time.time()
        self.weather = "clear"

        self.player_choice = tk.StringVar(value=self.cars[0].name)

        self.setup_ui()
        self.draw_track()
        self.create_cars()

        self.root.bind("<space>", self.player_nitro)

    def load_sprites(self):
        self.sprite = tk.PhotoImage(file = "High_performance_sports_car_sprite_sheet.png")

        self.car_images = []

        frame_height = self.sprite.height() // 4
        frame_width = self.sprite.width()

        for i in range(4):
            img = tk.PhotoImage(width=frame_width, height=frame_height)

            img.tk.call(
                img, "copy", self.sprite,
                "-from", 0, i * frame_height, frame_width, (i + 1) * frame_height,
                "-to", 0, 0
            )

            self.car_images.append(img)

    def setup_ui(self):
        frame = tk.Frame(self.root, bg="black")
        frame.pack()

        tk.Button(frame, text="START", command=self.start).grid(row=0, column=0)
        tk.Button(frame, text="RESET", command=self.reset).grid(row=0, column=1)
        tk.Button(frame, text="RAIN", command=self.toggle_weather).grid(row=0, column=2)

        tk.OptionMenu(frame, self.player_choice, *[c.name for c in self.cars]).grid(row=1, column=0)

        self.info = tk.Label(self.root, text="", fg="white", bg="black")
        self.info.pack()

    def draw_track(self):
        self.road_lines = []

        self.canvas.create_rectangle(0, 100, 1000, 400, fill="#333", outline="")

        for i in range(10):
            line = self.canvas.create_line(
                i * 120, 250, i * 120 + 60, 250,
                fill="white", width=4
            )
            self.road_lines.append(line)

        self.canvas.create_line(TRACK_LENGTH + 100, 100, TRACK_LENGTH + 100, 400, fill="yellow", width=4)

    def create_cars(self):
        y = 140
        for car in self.cars:
            obj = self.canvas.create_image(80, y, image=car.image)
            label = self.canvas.create_text(180, y, text=car.name, anchor="w", fill="white")

            self.car_objs.append(obj)
            self.labels.append(label)
            y += 70

    def start(self):
        for car in self.cars:
            car.is_player = (car.name == self.player_choice.get())

        self.running = True
        self.last_time = time.time()
        self.loop()

    def reset(self):
        self.running = False

        for i, car in enumerate(self.cars):
            car.reset()
            self.canvas.coords(self.car_objs[i], 80, 140 + i * 70)
            self.canvas.coords(self.labels[i], 180, 140 + i * 70)

        self.info.config(text="")

    def toggle_weather(self):
        self.weather = "rain" if self.weather == "clear" else "clear"

    def player_nitro(self, event):
        for car in self.cars:
            if car.is_player:
                car.nitro = 20

    def scroll_road(self, speed):
        for line in self.road_lines:
            self.canvas.move(line, -speed, 0)
            x1, y1, x2, y2 = self.canvas.coords(line)

            if x2 < 0:
                self.canvas.move(line, 1000, 0)

    def animate_effects(self, obj, car):
        if car.nitro > 0:
            self.canvas.move(obj, random.uniform(-1, 1), random.uniform(-1, 1))

    def loop(self):
        if not self.running:
            return

        now = time.time()
        dt = now - self.last_time
        self.last_time = now

        weather_factor = 0.7 if self.weather == "rain" else 1.0

        for i, car in enumerate(self.cars):
            car.update(weather_factor)

            dx = car.speed * dt * 10

            self.canvas.move(self.car_objs[i], dx, 0)
            self.canvas.move(self.labels[i], dx, 0)

            self.animate_effects(self.car_objs[i], car)
            self.scroll_road(dx)

            if car.position >= TRACK_LENGTH:
                self.finish(car)
                return

        self.root.after(16, self.loop)

    def finish(self, car):
        self.running = False
        self.info.config(text=f"Winner: {car.name}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RaceApp(root)
    root.mainloop()