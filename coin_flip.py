import random
import tkinter
from PIL import ImageTk
import PIL.Image
from tkinter import *
import matplotlib.pyplot as plt

results = []
head = 0
tail = 0

# generating x number of flips function
def coinFlip2():
    # get the text value from the input field
    text = tnum.get("1.0", "end")

    # if the text is empty
    if text == '':
        tnum.insert(INSERT, "ERROR!")
    else:
        # convert the text to an integer
        num = int(text)
        # if the number is greater than 0
        if num > 0:
            # initialize the head and tail counters
            h, t = 0, 0
            # reset the results list
            results.clear()
            # for loop to run the number of times specified by the user
            for i in range(num):
                # flip the coin with the coinFlip function randomly.
                res = random.randint(0, 1)
                # if the result is 1, increment the head counter
                if res == 1:
                    h += 1
                # otherwise, increment the tail counter
                else:
                    t += 1
                # add the result to the results list
                results.append(res)
            # make pie chart of the results h and t and save it
            plt.pie([h, t], labels=['Heads', 'Tails'], autopct='%1.1f%%')
            # save the chart to a file
            plt.savefig(f'coin flip {num} tries.png')
            plt.close()

            # change the Label text value
            tfb.config(text=f'SAVED! "coin flip {num} tries.png"')

        else:
            tnum.insert(INSERT, "ERROR!!")

# flip the coin function when click on the Tossing button
# with a random number generator and return the result
def coinFlip():
    global head
    global tail
    result = random.randint(0, 1)
    # clear the text field
    tfield.delete("1.0", "end")

    # if the result is 1, increment the head counter
    if (result == 1):
        tfield.insert(INSERT, " It's HEAD!")
        i.config(image=heads)
        head += 1
        # add the statistics to the text field
        tfield.insert(
            INSERT, f"\nHeads: {head}\{head+tail} ({round(head*100/(head+tail),1)}) \nTails: {tail}\{head+tail} ({round(tail*100/(head+tail),1)})")

    # otherwise, increment the tail counter
    else:
        tfield.insert(INSERT, " It's TAIL!")
        i.config(image=tails)
        tail += 1
        # add the statistics to the text field
        tfield.insert(
            INSERT, f"\nHeads: {head}\{head+tail} ({round(head*100/(head+tail),1)}) \nTails: {tail}\{head+tail} ({round(tail*100/(head+tail),1)})")


# create the window
root = tkinter.Tk()
root.geometry("500x600")
root.title("TASK_ONE: Coin Flip")

# load heads image
load = PIL.Image.open("head.png")
heads = ImageTk.PhotoImage(load)
# load tails image
load = PIL.Image.open("tail.png")
tails = ImageTk.PhotoImage(load)

# empty 10px space
Label(root, text=" ", padx=5, pady=5).pack()

# display the image
i = Label(root, image=heads)
i.pack()

# empty 10px space
Label(root, text="").pack()

b1 = Button(root, text="Toss the Coin", font=("Roboto", 14), command=coinFlip,
            bg='teal', fg='white', activebackground="lightblue", padx=10, pady=10)
b1.pack()

# empty 10px space
Label(root, text="").pack()

# Text Field for Result
tfield = Text(root, width=55, height=5, wrap='word')
tfield.pack()
tfield.insert(
    INSERT, "Click on the Button.. To Flip the Coin and get the result.")

# empty 10px space
Label(root, text="").pack()

# empty 10px space
Label(root, text="Enter the number of tries below",
      font=("Roboto", 14), fg='blue').pack()
tnum = Text(root, width=10, height=1)
tnum.pack()
tnum.insert(INSERT, "100")

# empty 10px space
Label(root, text="").pack()
b2 = Button(root, text="Generate", font=("Roboto", 14), command=coinFlip2,
            bg='blue', fg='white', activebackground="lightblue", padx=10, pady=10)
b2.pack()

# empty 10px space
tfb = Label(root, text="", padx=10, pady=10, fg='red')
tfb.pack()

root.mainloop()
