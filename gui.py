# Calculator By Brandon Riley
# 11/2/17
# Calculates addition, subtraction, multiplication, division, squares, and square roots
import tkinter

root = tkinter.Tk()
root.title("Calculator")


def tap_one():
    """
    Adds 1 to the answer string
    :return:
    """
    temp_one = answer.get()
    temp_one += "1"
    answer.set(temp_one)


def tap_two():
    """
    Adds 2 to the answer string
    :return:
    """
    temp_two = answer.get()
    temp_two += "2"
    answer.set(temp_two)


def tap_three():
    """
    Adds 3 to the answer string
    :return:
    """
    temp_three = answer.get()
    temp_three += "3"
    answer.set(temp_three)


def tap_four():
    """
    Adds 4 to the answer string
    :return:
    """
    temp_four = answer.get()
    temp_four += "4"
    answer.set(temp_four)


def tap_five():
    """
    Adds 5 to the answer string
    :return:
    """
    temp_five = answer.get()
    temp_five += "5"
    answer.set(temp_five)


def tap_six():
    """
    Adds 6 to the answer string
    :return:
    """
    temp_six = answer.get()
    temp_six += "6"
    answer.set(temp_six)


def tap_seven():
    """
    Adds 7 to the answer string
    :return:
    """
    temp_seven = answer.get()
    temp_seven += "7"
    answer.set(temp_seven)


def tap_eight():
    """
    Adds 8 to the answer string
    :return:
    """
    temp_eight = answer.get()
    temp_eight += "8"
    answer.set(temp_eight)


def tap_nine():
    """
    Adds 9 to the answer string
    :return:
    """
    temp_nine = answer.get()
    temp_nine += "9"
    answer.set(temp_nine)


def tap_zero():
    """
    Adds 0 to the answer string
    :return:
    """
    temp_zero = answer.get()
    temp_zero += "0"
    answer.set(temp_zero)


def tap_divide():
    """
    Adds / to the answer string
    :return:
    """
    temp_divide = answer.get()
    temp_divide += "/"
    answer.set(temp_divide)


def tap_multiply():
    """
    Adds * to the answer string
    :return:
    """
    temp_multiply = answer.get()
    temp_multiply += "*"
    answer.set(temp_multiply)


def tap_subtract():
    """
    Adds - to the answer string
    :return:
    """
    temp_subtract = answer.get()
    temp_subtract += "-"
    answer.set(temp_subtract)


def tap_add():
    """
    Adds + to the answer string
    :return:
    """
    temp_add = answer.get()
    temp_add += "+"
    answer.set(temp_add)


def tap_square_root():
    """
    Takes the square root of the number in the answer string and sets the answer string to the new number
    :return:
    """
    temp_square_root = answer.get()
    temp_square_root += "**(1/2)"
    answer.set(eval(temp_square_root))


def tap_square():
    """
    Squares the number in the answer string and sets the answer string to the new number
    :return:
    """
    temp_square = answer.get()
    temp_square += "**2"
    answer.set(eval(temp_square))


def tap_clear():
    """
    Clears the answer string
    :return:
    """
    temp_clear = ""
    answer.set(temp_clear)


def tap_equal():
    """
    Evaluates the math in the answer string and sets the answer string to the new number
    :return:
    """
    temp_equal = answer.get()
    answer.set(eval(temp_equal))

answer = tkinter.StringVar()


answer_box = tkinter.Entry(root, width=15, textvariable=answer)
answer_box.grid(row=1, column=1, columnspan=4, sticky="EW")

seven = tkinter.Button(root, text="7", command=tap_seven)
seven.grid(row=2, column=1, sticky="EW")
eight = tkinter.Button(root, text="8", command=tap_eight)
eight.grid(row=2, column=2, sticky="EW")
nine = tkinter.Button(root, text="9", command=tap_nine)
nine.grid(row=2, column=3, sticky="EW")
divided = tkinter.Button(root, text="/", command=tap_divide)
divided.grid(row=2, column=4, sticky="EW")

four = tkinter.Button(root, text="4", command=tap_four)
four.grid(row=3, column=1, sticky="EW")
five = tkinter.Button(root, text="5", command=tap_five)
five.grid(row=3, column=2, sticky="EW")
six = tkinter.Button(root, text="6", command=tap_six)
six.grid(row=3, column=3, sticky="EW")
multiply = tkinter.Button(root, text="*", command=tap_multiply)
multiply.grid(row=3, column=4, sticky="EW")

one = tkinter.Button(root, text="1", command=tap_one)
one.grid(row=4, column=1, sticky="EW")
two = tkinter.Button(root, text="2", command=tap_two)
two.grid(row=4, column=2, sticky="EW")
three = tkinter.Button(root, text="3", command=tap_three)
three.grid(row=4, column=3, sticky="EW")
subtract = tkinter.Button(root, text="-", command=tap_subtract)
subtract.grid(row=4, column=4, sticky="EW")

zero = tkinter.Button(root, text="0", command=tap_zero)
zero.grid(row=5, column=1, columnspan=3, sticky="EW")
add = tkinter.Button(root, text="+", command=tap_add)
add.grid(row=5, column=4, sticky="EW")

square_root = tkinter.Button(root, text="√x", command=tap_square_root)
square_root.grid(row=6, column=1)
square = tkinter.Button(root, text="x²", command=tap_square)
square.grid(row=6, column=2)
clear = tkinter.Button(root, text="AC", command=tap_clear)
clear.grid(row=6, column=3)
equals = tkinter.Button(root, text="=", command=tap_equal)
equals.grid(row=6, column=4)
root.bind("<Return>", lambda e: tap_equal())
root.bind("<=>", lambda e: tap_equal())

root.mainloop()
