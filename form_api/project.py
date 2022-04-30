from tkinter import * 
root = Tk()

# width & height for the Tkinter box
root.geometry("500x300")

# Define function
def getVal():
    print("Your form is accepted")

# Heading
Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)

# Field Names
name = Label(root, text="Name").grid(row=1, column=2)
phone = Label(root, text="Phone").grid(row=2, column=2)
email = Label(root, text="Email").grid(row=3, column=2)
payment_mode = Label(root, text="Payment Mode").grid(row=4, column=2)

# Variable for storing data
nameValue = StringVar
phoneValue = StringVar
emailValue = StringVar
payment_mode_value = StringVar
checkValue = IntVar

# Input Fields
nameEntry = Entry(root, textvariable = nameValue).grid(row=1, column=3)
phoneEntry = Entry(root, textvariable = phoneValue).grid(row=2, column=3)
emailEntry = Entry(root, textvariable = emailValue).grid(row=3, column=3)
payment_mode_entry = Entry(root, textvariable = payment_mode_value).grid(row=4, column=3)

# Creating Checkbox
checkBtn = Checkbutton(text="Remember Me", variable=checkValue).grid(row=5, column=3)

# Submit Button
Button(text="Submit", command=getVal).grid(row=6, column=3)

# Looped the main loop 
root.mainloop()