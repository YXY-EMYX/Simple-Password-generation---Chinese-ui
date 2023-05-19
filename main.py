import random
import string
from tkinter import *
from tkinter.ttk import *

def generate_password():
    password_length = int(entry_length.get())
    uppercase_count = int(entry_uppercase_count.get()) if var_uppercase.get() else 0
    lowercase_count = int(entry_lowercase_count.get()) if var_lowercase.get() else 0
    number_count = int(entry_numbers_count.get()) if var_numbers.get() else 0
    special_char_count = int(entry_special_char_count.get()) if var_special_char.get() else 0

    password_characters = (
        [random.choice(string.ascii_uppercase) for _ in range(uppercase_count)] +
        [random.choice(string.ascii_lowercase) for _ in range(lowercase_count)] +
        [random.choice(string.digits) for _ in range(number_count)] +
        [random.choice(string.punctuation) for _ in range(special_char_count)]
    )

    if len(password_characters) > password_length:
        return "错误：密码长度太短，无法包含所有的字符"

    while len(password_characters) < password_length:
        if var_uppercase.get() and len([char for char in password_characters if char in string.ascii_uppercase]) < uppercase_count:
            password_characters.append(random.choice(string.ascii_uppercase))
        elif var_lowercase.get() and len([char for char in password_characters if char in string.ascii_lowercase]) < lowercase_count:
            password_characters.append(random.choice(string.ascii_lowercase))
        elif var_numbers.get() and len([char for char in password_characters if char in string.digits]) < number_count:
            password_characters.append(random.choice(string.digits))
        elif var_special_char.get() and len([char for char in password_characters if char in string.punctuation]) < special_char_count:
            password_characters.append(random.choice(string.punctuation))

    random.shuffle(password_characters)
    password = "".join(password_characters)

    listbox.insert(END, password)

window = Tk()

row = 0
Label(window, text = "密码长度").grid(row = row, column = 0)
entry_length = Entry(window)
entry_length.grid(row = row, column = 1)

row += 1
var_uppercase = BooleanVar()
Checkbutton(window, text="包含大写字母", variable=var_uppercase).grid(row=row, column=0, sticky=W)
entry_uppercase_count = Entry(window)
entry_uppercase_count.grid(row = row, column = 1)

row += 1
var_lowercase = BooleanVar()
Checkbutton(window, text="包含小写字母", variable=var_lowercase).grid(row=row, column=0, sticky=W)
entry_lowercase_count = Entry(window)
entry_lowercase_count.grid(row = row, column = 1)

row += 1
var_numbers = BooleanVar()
Checkbutton(window, text="包含数字", variable=var_numbers).grid(row=row, column=0, sticky=W)
entry_numbers_count = Entry(window)
entry_numbers_count.grid(row = row, column = 1)

row += 1
var_special_char = BooleanVar()
Checkbutton(window, text="包含特殊字符", variable=var_special_char).grid(row=row, column=0, sticky=W)
entry_special_char_count = Entry(window)
entry_special_char_count.grid(row = row, column = 1)

row += 1
Button(window, text = "生成密码", command = generate_password).grid(row=row, column=0)

row += 1
listbox = Listbox(window)
listbox.grid(row=row, column=0, columnspan=2)

window.mainloop()
