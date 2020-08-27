import tkinter as tk
from PIL import Image, ImageTk
import os
import cv2

script_dir = os.path.dirname(__file__)


class GUI(tk.Frame):
    def __init__(self, master, size=(1280, 720)):
        super().__init__(master=master)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.size = size
        self.display = tk.Canvas(self, bd=0, highlightthickness=0, bg="pink")
        self.display.grid(row=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.pack(fill=tk.BOTH, expand=1)
        self.cap = cv2.VideoCapture(0)
        self.loadUI()
        self.drawFrame()
        self.drawUI()
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        self.size = (event.width, event.height)
        self.drawUI()

    def loadUI(self):
        leftImg = Image.open(os.path.join(script_dir, "assets/leftController.png")).resize((250, 250))
        self.leftTk = ImageTk.PhotoImage(image=leftImg)
        rightImg = Image.open(os.path.join(script_dir, "assets/rightController.png")).resize((250, 250))
        self.rightTk = ImageTk.PhotoImage(image=rightImg)
        holdImg = Image.open(os.path.join(script_dir, "assets/hold.png")).resize((100, 100))
        self.holdTk = ImageTk.PhotoImage(image=holdImg)

        bt1Img = Image.open(os.path.join(script_dir, "assets/bt1.png")).resize((80, 80))
        self.bt1Tk = ImageTk.PhotoImage(image=bt1Img)
        bt2Img = Image.open(os.path.join(script_dir, "assets/bt2.png")).resize((80, 80))
        self.bt2Tk = ImageTk.PhotoImage(image=bt2Img)
        bt3Img = Image.open(os.path.join(script_dir, "assets/bt3.png")).resize((80, 80))
        self.bt3Tk = ImageTk.PhotoImage(image=bt3Img)
        bt4Img = Image.open(os.path.join(script_dir, "assets/bt4.png")).resize((80, 80))
        self.bt4Tk = ImageTk.PhotoImage(image=bt4Img)

    def drawUI(self):
        self.display.delete("GUI")
        self.display.create_image(10, self.size[1] - 10, anchor=tk.SW, image=self.leftTk, tags=["GUI"])
        self.display.create_image(self.size[0] - 10, self.size[1] - 10, anchor=tk.SE, image=self.rightTk, tags=["GUI"])

        self.display.create_image(86, self.size[1] - 84, anchor=tk.SW, image=self.holdTk, tags=["GUI", "HOLD"])
        self.display.create_image(self.size[0] - 84, self.size[1] - 84, anchor=tk.SE, image=self.holdTk, tags=["GUI", "HOLD"])

        self.display.create_image(0, 30, anchor=tk.NW, image=self.bt1Tk, tags=["GUI"])
        self.display.create_image(0, 120, anchor=tk.NW, image=self.bt2Tk, tags=["GUI"])
        self.display.create_image(0, 210, anchor=tk.NW, image=self.bt3Tk, tags=["GUI"])
        self.display.create_image(0, 300, anchor=tk.NW, image=self.bt4Tk, tags=["GUI"])

    def drawFrame(self):
        _, frame = self.cap.read()
        resizedFrame = cv2.resize(frame, (self.size))
        cv2image = cv2.cvtColor(resizedFrame, cv2.COLOR_BGR2RGBA)
        image = Image.fromarray(cv2image)
        self.imgtk = ImageTk.PhotoImage(image)
        self.display.delete("VID")
        self.display.create_image(0, 0, image=self.imgtk, anchor=tk.NW, tags="VID")
        self.drawUI()
        self.after(10, self.drawFrame)

root = tk.Tk()
root.geometry("1280x720")
app = GUI(root)
app.mainloop()
