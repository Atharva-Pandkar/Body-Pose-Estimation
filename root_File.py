import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
import argparse
import os
parser = argparse.ArgumentParser(description='Run keypoint detection')
parser.add_argument("--device", default="cpu", help="Device to inference on")
parser.add_argument("--image_file", default="single.jpeg", help="Input image")
parser.add_argument("--call", default="options", help="which function to call")
args = parser.parse_args()
Main_Window = tkinter.Tk()
Main_Window.geometry("900x400")
Main_Window.title("Pose Estimation")
Main_Window.configure(bg='antique white')
to = Frame(Main_Window)
to.config(bg="antique white")
lst=[0,0,0,0]
# Helper function

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list
def delete(obj):
    lst=all_children(Main_Window)
    for x in lst:
        x.destroy()

#/home/atharva/PycharmProjects/For_Paper/venv/demo.jpeg
#Second first final 0-0-1-et
def Perform_Image(top,address):
    delete(top)

    frame = Frame(Main_Window)
    frame.grid(row=0, column=0)
    frame.config(bg="antique white")
    if address=="":
        Label(text="Address not entered",background="antique white").grid(row=0,column=1)
        Button(text="Back",command=lambda :Image(frame),background="antique white",padx=30).grid(row=0,column=0)
    elif os.path.exists(address):
        Main_Window.destroy()
        os.system('python3 '+os.getcwd()+"/Files/Image/pose.cpython-38.pyc"+' --device cpu --image_file '+address+' --call option')
        options(frame,0)
    else:
        Label(text="Address Entered is incorrect", background="antique white").grid(row=0, column=1)
        Button(text="Back", command=lambda: Image(frame), background="antique white", padx=30).grid(row=0, column=0)
#Second First 0-0-1
def Image(top):
    delete(top)
    frame = Frame(Main_Window)
    address = StringVar()
    frame.grid(row=0, column=0)
    frame.config(bg="antique white")
    Label(frame,text="Enter Image address",pady=10,background="antique white").grid(row=1,column=0)
    Entry(frame,width=40,textvariable=address).grid(row=1, column=1,pady=10)
    Button(frame, text="Confirm", font="Times", width=30, command=lambda: Perform_Image(frame,str(address.get())),background="peach puff").grid(row=2, column=1, pady=10)


#Second Second Final 0-0-2-et
def Perform_Video(top,address):
    delete(top)

    frame = Frame(Main_Window)
    frame.grid(row=0, column=0)
    frame.config(bg="antique white")
    if address == "":
        Label(text="Address not entered", background="antique white").grid(row=0, column=1)
        Button(text="Back", command=lambda: video(frame), background="antique white", padx=30).grid(row=0, column=0)
    elif os.path.exists(address):
        Main_Window.destroy()
        os.system('python3 '+os.getcwd()+"/Files/Video/pose_video.cpython-38.pyc"+' --device gpu --video_file ' + address + ' --call option')
        #options(frame, 0)
    else:
        Label(text="Address Entered is incorrect", background="antique white").grid(row=0, column=1)
        Button(text="Back", command=lambda: video(frame), background="antique white", padx=30).grid(row=0, column=0)
#Second second 0-0-2
def video(top):
    delete(top)
    frame = Frame(Main_Window)
    address = StringVar()
    frame.grid(row=0, column=0)
    frame.config(bg="antique white")
    Label(frame, text="Enter Image address", pady=10, background="antique white").grid(row=1, column=0)
    Label(frame, text="Please Note Video takes a lot more time then photos . DO NOT CLOSE THIS APPLICATION", pady=10, background="antique white").grid(row=3, column=1)
    Entry(frame, width=40, textvariable=address).grid(row=1, column=1, pady=10)
    Button(frame, text="Confirm", font="Times", width=30, command=lambda: Perform_Video(frame, str(address.get())),
           background="peach puff").grid(row=2, column=1, pady=10)

# Second Third Final 0-0-3-et
def Perform_Live_Video(top, address):
    delete(top)

    frame = Frame(Main_Window)
    frame.grid(row=0, column=0)
    frame.config(bg="antique white")
    if address == "":
        Label(text="Address not entered", background="antique white").grid(row=0, column=1)
        Button(text="Back", command=lambda: video(frame), background="antique white", padx=30).grid(row=0, column=0)
    Main_Window.destroy()
    os.system('python3 '+os.getcwd()+"/Files/Live-Stream/pose_video.cpython-38.pyc"+' --device gpu --video_file_name ' + address + ' --call option')
    # options(frame, 0)

#Second Third 0-0-3
def Live_stream(top):
    delete(top)
    frame = Frame(Main_Window)
    name = StringVar()
    frame.grid(row=0, column=0)
    frame.config(bg="antique white")
    Label(frame, text="Enter Name for file ", pady=10, background="antique white").grid(row=1, column=0)
    Label(frame, text="Please Note Video takes a lot more time then photos . DO NOT CLOSE THIS APPLICATION", pady=10,
          background="antique white").grid(row=3, column=1)
    Entry(frame, width=40, textvariable=name).grid(row=1, column=1, pady=10)
    Button(frame, text="Confirm", font="Times", width=30, command=lambda: Perform_Live_Video(frame, str(name.get())),
           background="peach puff").grid(row=2, column=1, pady=10)
#Second Page 0-0
def options(top,confirm):
    delete(top)
    frame = Frame(Main_Window)
    frame.grid(row=0, column=0)
    frame.config(bg="antique white")
    Button(frame,text="Image Pose Estimation",font="Times",width=30, command=lambda: Image(frame),background="peach puff").grid(row=0, column=1,pady=10)
    Button(frame, text="Live Stream Pose Estimation", font="Times", width=30, command=lambda: Live_stream(frame),
           background="peach puff").grid(row=0, column=2, pady=10)
    Button(frame, text="Ready Video Pose Estimation", font="Times", width=30, command=lambda: video(frame),
           background="peach puff").grid(row=0, column=3, pady=10)
    if confirm ==1:
        Label(frame,text="Last Task performed Sucessfully ",pady=40).grid(row=2,column=2)
# First Page 0
def First_window(top):
    top.grid(row=0, column=0)
    lst[0] = 0
    Label(top, text="   Welcome to Pose estimation software ",font="Times 30 bold",fg="orange red",bg='antique white').grid(row=4, column=2)

    Button(top, text="Click to Enter",font="Times",width=30, command=lambda: options(top,0),background="peach puff").grid(row=5, column=2,pady=10)
First_window(to)
if args.call == 'option':
    frame = Frame(Main_Window)
    options(frame,1)

Main_Window.mainloop()
