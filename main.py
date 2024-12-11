#1
import tkinter as tk
import pyshorteners
#pyshorteners helps to  short and expand urls using the most famous URL Shorteners availables


#44(command=shorten)
def shorten():
    shortener = pyshorteners.Shortener()  #shortens the website's address and adds a random combination of letters and numbers.
    short_url = shortener.tinyurl.short(longurlvalue.get())
    #short() function takes in the URL as an argument and shortens it. The short() function, tinyurl. short() , is one of the pyshorteners library's many APIs
    print(shorturlvalue.insert(0, short_url))
    

#3
root = tk.Tk()
root.title("URL Shortener")
root.geometry("300x180")
bg = tk.PhotoImage(file="pic/bg.png")

#33
canvas =tk.Canvas(root, width=300, height=180)
canvas.pack(fill="both", expand=True)

canvas.create_image(0,0,image=bg, anchor="nw")



#frame = tk.Frame(root, width=300, height=180, bg="white")
#frame.pack( fill="y")




#4
longurl= tk.Label(root, text="Enter Your Long URL")
longurlvalue = tk.Entry(root)

shortenbtn = tk.Button(root, text="Shorten URL", command=shorten, bg="light blue")

shorturl=tk.Label(root, text="Here Is Your Shortened URL!") 
shorturlvalue = tk.Entry(root)

#5

longurlvalue.pack()


shorturlvalue.pack()

canvas.create_text(125, 40, text = "Enter Your Long URL", fill="black", font=('Helvetica bold', 10))
canvas.create_window(125,60, window=longurlvalue)

canvas.create_text(125, 120, text = "Here Is Your Shortened URL!", fill="black", font=('Helvetica bold', 10))
canvas.create_window(125,140, window=shorturlvalue)

canvas.create_window(125, 90, window=shortenbtn)



#2
root.mainloop()