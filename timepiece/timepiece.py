import tkinter as tk
import time
import nltk
print(nltk.__file__)

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("计时器")

        self.is_timing = False
        self.start_time = 0
        self.elapsed_time = 0

        self.label = tk.Label(root, text="00:00:00", font=("Verdana", 30))
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="开始", command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT, padx=30)

        self.reset_button = tk.Button(root, text="重置", command=self.reset_stopwatch)
        self.reset_button.pack(side=tk.RIGHT, padx=30)

        self.update_time()

    def start_stopwatch(self):
        if not self.is_timing:
            self.is_timing = True
            self.start_time = time.time() - self.elapsed_time
            self.start_button.config(text="停止")
            self.update_time()
        else:
            self.is_timing = False
            self.start_button.config(text="开始")

    def reset_stopwatch(self):
        self.is_timing = False
        self.start_button.config(text="开始")
        self.elapsed_time = 0
        self.update_time()

    def update_time(self):
        if self.is_timing:
            self.elapsed_time = time.time() - self.start_time
        minutes, seconds = divmod(int(self.elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)
        time_str = "{:0>2d}:{:0>2d}:{:0>2d}".format(hours, minutes, seconds)
        self.label.config(text=time_str)
        if self.is_timing:
            self.label.after(1000, self.update_time)


root = tk.Tk()
root.geometry("200x130")
app = StopwatchApp(root)
root.mainloop()
