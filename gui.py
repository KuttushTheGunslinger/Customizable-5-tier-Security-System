import tkinter as tk
import time

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(40, GPIO.OUT)
# GPIO.output(40, GPIO.LOW)

o = 'abcd123'


def code(value, o):
    global pin
    global tries
    if value == 'X':
        pin = pin[:-1]
        e.delete('0', 'end')
        e.insert('end', pin)

    elif value == 'Enter':
        if pin == o:
            root.destroy()

        else:
            Label2 = tk.Label(root, text='PIN ERROR')
            Label2.place(relx=0.0, rely=1.0, anchor='sw')
            tries = tries + 1
            Label1 = tk.Label(root, text='Attempts left: ' + str(3 - tries))
            Label1.place(relx=1.0, rely=0.0, anchor='ne')
            if tries < 3:
                pin = ''
                e.delete('0', 'end')
            else:
                root.destroy()

    else:

        pin += value
        e.insert('end', value)

keys = [
    ['a', 'b', 'c', 'd', 'e', 'f'],
    ['g', 'h', 'i', 'j', 'k', 'l'],
    ['n', 'o', 'p', 'q', 'r', 's'],
    ['t', 'u', 'v', 'w', 'x', 'y', 'z'],
    ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ['X', '0', 'Enter'],
]

pin = ''
tries = 0
root = tk.Tk()

root.geometry("480x320")

e = tk.Entry(root)
e.grid(row=0, column=0, columnspan=3, ipady=5)

# create buttons using `keys`
for y, row in enumerate(keys, 1):
    for x, key in enumerate(row):
        b = tk.Button(root, text=key, command=lambda val=key: code(val, o))
        b.grid(row=y, column=x, ipadx=10, ipady=10)

root.mainloop()

