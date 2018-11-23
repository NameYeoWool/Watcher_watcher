from pynput import mouse
from tkinter import *
from PIL import ImageGrab
import time

from seat_detect import Main2

root = Tk()
root.resizable(True, True)

start_point = ()
end_point = ()
take_shot = False


def point(event):
    print(event.char)
    if event.char=='s':
        global start_point
        start_point = mouse.Controller().position
        startLbl.config(text=mouse.Controller().position)
    if event.char == 'e':
        global end_point
        end_point = mouse.Controller().position
        endLbl.config(text=mouse.Controller().position)

def screenshot():
    if not take_shot:
        return
    imgGrab = ImageGrab.grab(bbox=(*start_point,*end_point))
    imgGrab.save("screen_shot.jpg")

    print("o")
    Main2.main()

    root.after(1000,screenshot)

def start():
    global take_shot
    take_shot = True
    processLbl.config(text="시작 -> press s")
    time.sleep(5)
    screenshot()

def stop():
    global take_shot
    take_shot = False
    processLbl.config(text="멈춤 -> press e")


canvas = Canvas(root)
canvas.pack(expand=True)
canvas.bind('<Key>', point)
canvas.focus_set()

lbl0 = Label(root, text="시작 좌표")
lbl0.pack()

startLbl = Label(root, text=start_point)
startLbl.pack()

lbl1 = Label(root, text="끝 좌표")
lbl1.pack()

endLbl = Label(root, text=" ")
endLbl.pack()

processLbl = Label(root, text="멈춤")
processLbl.pack()

start_btn = Button(root, text="START", width=15, command=start)
start_btn.pack()

end_btn = Button(root, text="END", width=15, command=stop)
end_btn.pack()

root.mainloop()
