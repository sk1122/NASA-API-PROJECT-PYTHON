from tkinter import *
import requests, json
from tkinter import messagebox

def nasa():
    api_key = "o1wN6rg7pDTjDbr9EwMPQp1KBXLX77tbwFbnmgR6"

    while True:
        date = text_input.get()

        r = requests.get("https://api.nasa.gov/planetary/apod?api_key="+ api_key +"&date="+ date)

        x = r.json()
        g = x['copyright']
        z = x['explanation']
        if 'copyright' in x == True:
                      messagebox.showinfo(title = "Result", message = f'Writer:  {g} Explanation:  {z}')
        else: 
            messagebox.showinfo(title = "Result", message = f' Explanation: {z}')
        
if __name__ == "__main__":

    root = Tk()

    root.geometry("500x300")
    root.title("NASA")

    label1 = Label(root, text='Nasa APOD finder')
    label1.grid(row=0, column=0)

    label3 = Label(root, text='')
    label3.grid(row=1, column=0)


    label2 = Label(root, text='Date: ')
    label2.grid(row=2, column=0)

    text_input = Entry(root)
    text_input.grid(row=2, column = 1)

    button1 = Button(root, text="Submit", command=nasa)
    button1.grid(row=3, column=1)
