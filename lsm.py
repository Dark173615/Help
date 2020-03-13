#Help
import tkinter as tk

m = tk.Tk()
m.title("Help")

img = tk.PhotoImage(file='help.png')
label1 = tk.Label(m, image=img)
label1.pack()


label = tk.Label(m, text = "\nEnter address: ", font = 20)
label.pack()
text = tk.Text(m, height = 2, width = 50)
text.pack()

button = tk.Button(m, text="Next", width = 25, command = m.destroy)
button.pack()

m.mainloop()
