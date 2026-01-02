def repeat(string, n):
    print(string * n)

def first_two():
    repeat(spam,4)
    repeat(spam,4)

def last_three():
    repeat(spam,2)
    print("(Lovely Spam, Wonderful Spam!)")
    repeat(spam,2)

def print_verse():
        first_two()
        last_three()

def print_n_verses(n):
    for i in range(n):
        print_verse()
        print()

spam= "Spam,"

#P1

def print_right(string):
    print(" "*(40-len(string)), string)

#P2

def triangle(string, n):
    for i in range(n):
        print(string*(i+1))

#triangle("*",3)

#P3

def rectangle(string, rows, columns):
    for i in range(rows):
        print(string*columns)

rectangle("H",4,4)