from tkinter import *

root = Tk()
root.title("Institute Configuration")

# Create labels
label1 = Label(root, text="Institute Name:")
label2 = Label(root, text="Address:")
label3 = Label(root, text="Phone Number:")
label4 = Label(root, text="Website:")

# Create entry boxes
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)

# Position labels and entry boxes
label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
label3.grid(row=2, column=0, padx=10, pady=10)
entry3.grid(row=2, column=1, padx=10, pady=10)
label4.grid(row=3, column=0, padx=10, pady=10)
entry4.grid(row=3, column=1, padx=10, pady=10)

# Create submit button
button = Button(root, text="Submit")
button.grid(row=4   , column=1, padx=10, pady=10)

root.mainloop()
    