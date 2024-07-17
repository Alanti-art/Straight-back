import cv2
import time
import win10toast
from tkinter import *
from PIL import Image, ImageTk

x=0
y=0
x_ref = 0
y_ref = 0


root = Tk()

def btn_click():
    cap = cv2.VideoCapture(0)
    cap.set(3, 500)
    cap.set(4, 500)
    ret, frame = cap.read()
    cv2.imwrite('.venv/imagines/photo(reference).png', frame)
    toast = win10toast.ToastNotifier()
    toast.show_toast('Straight Back', 'Программа запущена')
    cap.release()
    cap = cv2.VideoCapture(0)
    cap.set(3, 500)
    cap.set(4, 500)
    ret, frame = cap.read()
    img = cv2.imread('.venv/imagines/photo(reference).png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('faces.xml')
    results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=50)
    for (x, y, w, h) in results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
        x_ref=x
        y_ref=y
        print(x_ref,y_ref)
    cap.release()
    root.destroy()



root.title('Straight Back')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=600, width=600)
canvas.pack()
frame = Frame(root)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
title = Label(frame, text='Привет!\n\n Эта программа будет конролировать вашу осаку!\n Для начала примите правильное положнение\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', font=30)
title.pack()

our_image2 = Image.open(".venv/imagines/image.png")
our_image2 = ImageTk.PhotoImage(our_image2)
our_label2 = Label(image= our_image2)
our_label2.image = our_image2
our_label2.place(x=110,y=190)

btn = Button(frame, text='Поехали!', bg='gray', command=btn_click)
btn.pack()


root.mainloop()


while True:
    cap = cv2.VideoCapture(0)
    cap.set(3, 500)
    cap.set(4, 500)
    ret, frame = cap.read()
    cv2.imwrite('.venv/imagines/photo.png', frame)
    cap.release()
    img = cv2.imread('.venv/imagines/photo.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('faces.xml')
    results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=50)
    for (x, y, w, h) in results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
        print('x=',x,'y=',y)
    if (abs(x)-abs(x_ref)>10) or (abs(y)-abs(y_ref))>5:
        toast = win10toast.ToastNotifier()
        toast.show_toast('Straight Back', 'не будь креветкой')
    time.sleep(30)
