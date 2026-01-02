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

#P4

def two_verses(n):
    many=str(n)
    print(many + " bottles of beer on the wall,\n" + many + " bottles of "
                                                            "beer.")

def last_verse(n):
    many=str(n-1)
    print(many + " bottles of beer on the wall. \n")

def bottle_verse(n):
    two_verses(n)
    print("Take one down, pass it around,")
    last_verse(n)

def bottle_wall(n):
    for i in range(n, 0, -1):
        bottle_verse(i)

bottle_wall(99)