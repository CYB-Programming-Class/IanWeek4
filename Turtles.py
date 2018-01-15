import turtle
import time
# Right below this is where I worked tirelessly on designing (probably an inefficient) way to write letters.


def a_(size, weight, x, y):
    tur.up(), tur.goto(x - 5, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.right(90), tur.forward(50 + size), tur.right(90), tur.forward(30 + size), tur.right(90), tur.forward(50 + size),
    tur.right(180), tur.forward(50 + size), tur.right(90), tur.forward(70)


def b_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.right(120), tur.forward(50 + size), tur.right(120), tur.forward(50 + size), tur.setheading(90), tur.right(120),
    tur.forward(50 + size), tur.right(120), tur.forward(50 + size), tur.right(120), tur.forward(size)


def c_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(0), tur.down(), tur.forward(50 + size),
    tur.back(50 + size), tur.left(90), tur.forward(100 + size), tur.right(90), tur.forward(50 + size)


def d_(size, weight, x, y):
    tur.up(), tur.goto(x - 8, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.right(90),
    for _ in range(18):
        tur.forward(8.8)
        tur.right(10)
    tur.forward(10)


def e_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.right(90), tur.down(),
    tur.forward(50 + size), tur.back(50 + size), tur.left(90), tur.forward(50 + size), tur.right(90),
    tur.forward(50 + size), tur.back(50 + size), tur.left(90), tur.forward(50 + size), tur.right(90),
    tur.forward(50 + size)


def f_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(50 + size),
    tur.right(90), tur.forward(50 + size), tur.back(50 + size), tur.left(90), tur.forward(50 + size), tur.right(90),
    tur.forward(50 + size)


def g_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.forward(100 + size), tur.right(90),
    tur.forward(50 + size), tur.left(180), tur.down(), tur.forward(50), tur.left(90), tur.forward(100 + size),
    tur.left(90), tur.forward(50), tur.left(90), tur.forward(50 + size), tur.left(90), tur.forward(25)


def h_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.back(50 + size), tur.right(90), tur.forward(50 + size), tur.right(90), tur.forward(50 + size),
    tur.back(100 + size)


def i_(size, weight, x, y):
    tur.up(), tur.goto(x - 3, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.right(90),
    tur.forward(50 + size), tur.back(25 + size), tur.left(90), tur.forward(100 + size), tur.left(90),
    tur.forward(25 + size), tur.back(50 + size)


def j_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.right(90),
    tur.forward(25 + size), tur.left(90), tur.forward(100 + size), tur.left(90),
    tur.forward(25 + size), tur.back(50 + size)


def k_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.back(50 + size), tur.right(40), tur.forward(65 + size), tur.back(60 + size), tur.right(105),
    tur.forward(65 + size)


def l_(size, weight, x, y):
    tur.up(), tur.goto(x - 5, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.back(100 + size), tur.right(90), tur.forward(50 + size)


def m_(size, weight, x, y):
    tur.up(), tur.goto(x + 5, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.right(160), tur.forward(65 + size), tur.left(140), tur.forward(65 + size), tur.right(160),
    tur.forward(100 + size)


def n_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.right(155), tur.forward(110 + size), tur.left(155), tur.forward(100 + size)


def o_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.right(90), tur.forward(50 + size), tur.right(90), tur.forward(100 + size), tur.right(90), tur.forward(50 + size)


def p_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.right(90), tur.forward(10 + size)
    for _ in range(19):
        tur.forward(5 + size / 20)
        tur.right(10)
    tur.forward(10 + size)


def q_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.right(90), tur.forward(50 + size), tur.right(90), tur.forward(100 + size), tur.right(90),
    tur.forward(50 + size), tur.back(50 + size), tur.right(45), tur.back(10 + size), tur.forward(35 + size)


def r_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.forward(100 + size),
    tur.right(90), tur.forward(10 + size)
    for _ in range(19):
        tur.forward(5 + size / 20)
        tur.right(10)
    tur.forward(10 + size), tur.left(135), tur.forward(55 + size)


def s_(size, weight, x, y):
    tur.up(), tur.goto(x + 8, y), tur.pensize(1 + weight), tur.setheading(-15), tur.down(),
    for _ in range(18):
        tur.forward(4.5 + size / 20)
        tur.left(10)
    for _ in range(18):
        tur.forward(4.5 + size / 20)
        tur.right(10)


def t_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(0), tur.forward(25 + size), tur.down()
    tur.left(90), tur.forward(100 + size), tur.left(90), tur.forward(25 + size), tur.back(50 + size)


def u_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90),
    tur.forward(100 + size), tur.down(), tur.right(180), tur.forward(75 + size),
    for _ in range(15):
        tur.forward(5 + size / 20)
        tur.left(12)
    tur.forward(79 + size)


def v_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.forward(100 + size), tur.down(),
    tur.right(165), tur.forward(100), tur.setheading(90), tur.right(15), tur.forward(100)


def w_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(92), tur.forward(100 + size), tur.down(),
    tur.right(175), tur.forward(100 + size), tur.setheading(90), tur.right(8), tur.forward(100 + size), tur.left(8),
    tur.right(172), tur.forward(100 + size), tur.setheading(90), tur.right(8), tur.forward(100 + size)


def x_(size, weight, x, y):
    tur.up(), tur.goto(x + 12, y), tur.pensize(1 + weight), tur.setheading(90), tur.down(), tur.right(20),
    tur.forward(106 + size), tur.up(), tur.setheading(90), tur.back(100 + size), tur.down(),
    tur.left(19), tur.forward(106 + size)


def y_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(0), tur.forward(25 + size), tur.down(),
    tur.left(90), tur.forward(50 + size), tur.right(20), tur.forward(53 + size), tur.back(53 + size),
    tur.setheading(90), tur.left(20), tur.forward(53 + size)


def z_(size, weight, x, y):
    tur.up(), tur.goto(x, y), tur.pensize(1 + weight), tur.setheading(90), tur.forward(100 + size), tur.down(),
    tur.right(90), tur.forward(50 + size), tur.right(115), tur.forward(110 + size), tur.setheading(0),
    tur.forward(45 + size)


def comma_(size, weight, x, y):
    tur.up(), tur.goto(x - 15, y), tur.pensize(1 + weight), tur.setheading(0), tur.forward(25 + size), tur.down(),
    tur.right(110), tur.forward(25 + size)


def apostrophe_(size, weight, x, y):
    tur.up(), tur.goto(x - 15, y), tur.pensize(1 + weight), tur.setheading(0), tur.forward(25 + size),
    tur.setheading(90), tur.forward(100 + size), tur.down(), tur.back(25 + size)


# The letters are done, but now to put them all together in a big function I call "Talk Wordy To Me".


def talk_wordy_to_me(text, size, weight, y, color, underline):
    sp = 0 # MAROLSI: what is sp??????
    tur.color(color)
    xp = len(text) * -30 - (size * 2) - 40 # MAROLSI: what is xp??????
    x_memory = xp # MAROLSI: what is x_memory?????
    word = []
    for xx in range(len(text)):
        word.append(ord(text[xx]) - 97) # MAROLSI: what is happening here and what does ord do????
    for I in range(len(word)):
        a_(size, weight, xp + sp, y) if word[I] == 0 else None
        b_(size, weight, xp + sp, y) if word[I] == 1 else None
        c_(size, weight, xp + sp, y) if word[I] == 2 else None
        d_(size, weight, xp + sp, y) if word[I] == 3 else None
        e_(size, weight, xp + sp, y) if word[I] == 4 else None
        f_(size, weight, xp + sp, y) if word[I] == 5 else None
        g_(size, weight, xp + sp, y) if word[I] == 6 else None
        h_(size, weight, xp + sp, y) if word[I] == 7 else None
        i_(size, weight, xp + sp, y) if word[I] == 8 else None
        j_(size, weight, xp + sp, y) if word[I] == 9 else None
        k_(size, weight, xp + sp, y) if word[I] == 10 else None
        l_(size, weight, xp + sp, y) if word[I] == 11 else None
        m_(size, weight, xp + sp, y) if word[I] == 12 else None
        n_(size, weight, xp + sp, y) if word[I] == 13 else None
        o_(size, weight, xp + sp, y) if word[I] == 14 else None
        p_(size, weight, xp + sp, y) if word[I] == 15 else None
        q_(size, weight, xp + sp, y) if word[I] == 16 else None
        r_(size, weight, xp + sp, y) if word[I] == 17 else None
        s_(size, weight, xp + sp, y) if word[I] == 18 else None
        t_(size, weight, xp + sp, y) if word[I] == 19 else None
        u_(size, weight, xp + sp, y) if word[I] == 20 else None
        v_(size, weight, xp + sp, y) if word[I] == 21 else None
        w_(size, weight, xp + sp, y) if word[I] == 22 else None
        x_(size, weight, xp + sp, y) if word[I] == 23 else None
        y_(size, weight, xp + sp, y) if word[I] == 24 else None
        z_(size, weight, xp + sp, y) if word[I] == 25 else None
        comma_(size, weight, xp + sp, y) if word[I] == -53 else None
        apostrophe_(size, weight, xp + sp, y) if word[I] == -58 else None
        xp += 60 + (size * 1.5) + (weight * 2) # MAROLSI: why this brilliant calculation???
    if underline > 0:
        tur.up()
        tur.goto(x_memory - 10, y - 10) # MAROLSI: aahhh.... now I see what it's for. Still needs comment above.
        tur.down()
        tur.goto(xp + 10, y - 10)


# Unnecessary, but still fun, I added a particle generator to make some fun little additions.
def particle(kind, x, y, color):
    tur.color(color)
    tur.pensize(16)
    tur.penup()
    tur.goto(x, y)
    tur.down()
    [(tur.forward(50), tur.right(144)) for _ in range(5)] if kind == "star" else None
    [(tur.forward(50), tur.left(90)) for _ in range(4)] if kind == "square" else None
    [(tur.forward(10), tur.right(20)) for _ in range(18)] if kind == "circle" else None
    [(tur.right(10)) for _ in range(1)] if kind == "spot" else None

tur = turtle.Turtle()
tur.shape('circle')
tur.speed("fastest")
wn = turtle.Screen()
wn.bgcolor("black")
tur.hideturtle()
# MAROLSI: convention is lower case for "Intro" variable
Intro = [talk_wordy_to_me("the challenge", 0, 4, 300, "white", 0),
         talk_wordy_to_me("was to draw my", 0, 4, 160, "white", 0),
         talk_wordy_to_me("initials with", 0, 4, 20, "white", 0),
         talk_wordy_to_me("turtle, but i", 0, 4, -120, "white", 0),
         talk_wordy_to_me("decided to go", 0, 4, -260, "white", 0),
         talk_wordy_to_me("a bit further", 0, 4, -390, "white", 0), time.sleep(2), tur.clear(),
         talk_wordy_to_me("i, instead of", 0, 4, 300, "white", 0),
         talk_wordy_to_me("initials, made", 0, 4, 160, "white", 0),
         talk_wordy_to_me("my own text", 0, 4, 20, "white", 0),
         talk_wordy_to_me("engine, it's", 0, 4, -120, "white", 0),
         talk_wordy_to_me("pretty nice,", 0, 4, -260, "white", 0),
         talk_wordy_to_me("albeit limited", 0, 4, -390, "white", 0), time.sleep(2), tur.clear(),
         talk_wordy_to_me("the text", 0, 4, 300, "white", 0),
         talk_wordy_to_me("automatically", 0, 4, 160, "white", 0),
         talk_wordy_to_me("centers, and", 0, 4, 20, "white", 0),
         talk_wordy_to_me("it can write", 0, 4, -120, "white", 0),
         talk_wordy_to_me("in color", 0, 4, -260, "blue", 0), time.sleep(2), tur.clear(),
         talk_wordy_to_me("it can", 0, 4, 300, "white", 0),
         talk_wordy_to_me("underline,", 0, 4, 160, "white", 1),
         talk_wordy_to_me("and even", 0, 4, 20, "white", 0),
         talk_wordy_to_me("grow,", 30, 4, -120, "grey", 0),
         talk_wordy_to_me("so there you", 0, 4, -260, "white", 0),
         talk_wordy_to_me("go", 0, 4, -390, "white", 0), time.sleep(2), tur.clear(),
         talk_wordy_to_me("but just in", 0, 4, 300, "white", 0),
         talk_wordy_to_me("case,", 0, 4, 160, "white", 0),
         talk_wordy_to_me("project made", 0, 4, 20, "grey", 0),
         talk_wordy_to_me("by", 0, 4, -120, "grey", 0),
         talk_wordy_to_me("ilk", 0, 4, -260, "blue", 0),
         talk_wordy_to_me("", 0, 4, -390, "white", 0), time.sleep(2), tur.clear(), wn.mainloop()]
Sizes = [300, 160, 20, -120, -260, -390] # MAROLSI: what is sizes for?????

# The code below (for some stupid reason) doesn't work.
#
# MAROLSI: likely due to something called multithreading. The turtle screen is probably on a separate thread from the main thread.
# Not sure how to fix this atm, but maybe we can revisit later if we discuss multithreading
exit()
print("Please input your text below! (13 characters per line, only letters, apostrophes, and commas | no numbers)")
while True:
    Initials = input('Text: ')
    tur.color("white")
    if Initials.isdigit() or len(Initials.split("*")) > 13:
        print("letters, commas (,), and apostrophes ('), only! (And keep it under 14 characters and 7 lines)")
    else:
        Initials = Initials.split("*")
        if isinstance(Initials, list):
            for i in range(len(Initials)):
                talk_wordy_to_me(Initials[i], 0, 4, Sizes[i], "white", 0)
        else:
            talk_wordy_to_me(Initials, 0, 4, 0, "white", 0)
        time.sleep(2)
        wn.mainloop()