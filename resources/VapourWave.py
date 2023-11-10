import tkinter as tk
import random
from PIL import ImageTk, Image


iteration = 0

root = tk.Tk()

def idoit():
    root.title('You are an idiot')
    windows = 11


    frame.destroy()
    label.destroy()

    for window in range(windows):
        window = window + 1
        globals()['window%s' % window] = tk.Toplevel()

    #for window in range(windows):
        #new = tk.Toplevel()

    def moveWidget():
        for window in range(windows):
            window = window + 1
            globals()['window%s' % window].geometry("260x190+" + str(random.randint(1, 1050)) + "+" + str(random.randint(1, 470)))
        root.geometry("260x190+" + str(random.randint(1, 1050)) + "+" + str(random.randint(1, 470)))
        root.after(300, moveWidget)

    def image():
        global iteration
        for canvis in range(windows):
            canvis = canvis + 1
            if iteration == 0:
                globals()['canvis%s' % canvis].create_image(1, 1, anchor='nw', image=white)
                realcanvis.create_image(1, 1, anchor='nw', image=white)
                iteration = 1
            else:
                globals()['canvis%s' % canvis].create_image(1, 1, anchor='nw', image=black)
                realcanvis.create_image(1, 1, anchor='nw', image=black)
                iteration = 0
        root.after(600, image)

    for canvis in range(windows):
        canvis = canvis + 1
        globals()['canvis%s' % canvis] = tk.Canvas(globals()['window%s' % canvis], width=400, height=300)
        globals()['canvis%s' % canvis].pack()
    realcanvis = tk.Canvas(root, width=400, height=300)
    realcanvis.pack()

    moveWidget()
    image()


def dumbQuestion():
    global frame
    global label
    global canvis

    def rannumy():
        num = random.randint(7, 9)
        num = num / 10
        return num

    def rannumx():
        num = random.randint(4, 9)
        num = num / 10
        return num

    def move():
        no.place(relheight=0.1, relwidth=0.1, relx=rannumx(), rely=rannumy())

    canvis = tk.Canvas(root, height=200, width=300)
    canvis.pack(fill='both', expand=True)

    frame = tk.Frame(root, bg='#F61E61')
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(frame, text='are you an idiot?', bg='#1E2F97')
    label.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.3, anchor="center")

    yes = tk.Button(root, text='Yes', bg='grey', command=idoit)
    yes.place(relheight=0.1, relwidth=0.1, relx=0.3, rely=0.9)

    no = tk.Button(root, text='No', bg='grey', command=move)
    no.place(relheight=0.1, relwidth=0.1, relx=0.6, rely=0.9)

def head():
    global headTab
    headTab = tk.Toplevel()
    headCanvis = tk.Canvas(headTab, height=200, width=300)
    headCanvis.pack()  # fill='both', expand=True

    headCanvis.create_image(1, 1, anchor='nw', image=vapourTab)

    headTab.geometry("290x160+" + str(500) + "+" + str(200))  # 1050, 470

vapourTab = ImageTk.PhotoImage(Image.open("VapourTab.jpg"))
black = ImageTk.PhotoImage(Image.open("blackIdiot.png"))
white = ImageTk.PhotoImage(Image.open("whiteIdiot.jpg"))

def movement():
    global x
    global y
    global moveAmount
    root.geometry("300x190+" + str(x) + "+" + str(y))  # 1050, 470
    x = x + 10
    y = y + 10
    moveAmount = moveAmount + 1
    if moveAmount < 32:
        root.after(200, movement)
    else:
        up()

def down():
    global y
    global downAmount
    root.geometry("300x190+" + str(x) + "+" + str(y))  # 1050, 470
    y = y + 10
    downAmount = downAmount + 1
    if downAmount < 10:
        root.after(100, down)
    else:
        up()

def up():
    global y
    global upAmount
    root.geometry("300x190+" + str(x) + "+" + str(y))  # 1050, 470
    y = y - 10
    upAmount = upAmount + 1
    if upAmount < 30:
        root.after(100, up)
    #else:
        #os.system('start https://www.youtube.com/watch?v=SoDM9wwYpFw')
        #time.sleep(5)
        #pyautogui.press('f')
def open():
    global openX
    global openY
    global openAmount
    headTab.geometry(str(openX) + 'x' + str(openY) + '+' + "500+200")  # 1050, 470
    openY = openY + 10
    openX = openX + 10
    openAmount = openAmount + 1
    if openAmount < 10:
        root.after(200, open)
    else:
        dumbQuestion()
        movement()


x = 200
y = 30
moveAmount = 0
openAmount = 0
downAmount = 0
upAmount = 0
openX = 210
openY = 70

head()
open()

tk.mainloop()
