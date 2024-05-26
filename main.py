import random
from turtle import *
from words import gameWords

def draw_line(point1, point2, size=10, p_color="black"):
    oldPenSize = pen()["pensize"]
    oldColor = pen()["pencolor"]

    pensize(size)
    pencolor(p_color)

    penup()
    goto(point1[0], point1[1])
    pendown()
    goto(point2[0], point2[1])
    penup()

    pensize(oldPenSize)
    pencolor(oldColor)


def draw_circle(rad, size=10, p_color="black"):
    oldPenSize = pen()["pensize"]
    oldColor = pen()["pencolor"]

    pensize(size)
    pencolor(p_color)

    pendown()
    circle(rad)
    penup()

    pensize(oldPenSize)
    pencolor(oldColor)


def draw_square(top_left, len_edge, size=10, p_color="black"):
    x = top_left[0]
    y = top_left[1]
    points = [[x, y], [x + len_edge, y], [x + len_edge, y - len_edge], [x, y - len_edge]]
    draw_line(points[0], points[1], size, p_color)
    draw_line(points[1], points[2], size, p_color)
    draw_line(points[2], points[3], size, p_color)
    draw_line(points[3], points[0], size, p_color)


def draw_secret(word):
    global secretWordCoords
    lenSquare = 100
    interval = 20
    screenWidth = Screen().window_width()
    wordWidth = (len(word) * lenSquare) + (len(word) - 1) * interval
    x = (screenWidth // 2 * -1) + (screenWidth - wordWidth) // 2
    startPoint = [x, -230]
    for x in range(len(word)):
        draw_square(startPoint, lenSquare)
        secretWordCoords.append([startPoint[0] + (lenSquare // 2), startPoint[1] - lenSquare])
        startPoint[0] += lenSquare + interval

def draw_alphabet():
    global alphabet_dict
    alphabet = ('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
                'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я')
    x = 100
    y = 280
    for i in range(len(alphabet)):
        if i % 5 == 0 and i != 0:
            x = 100
            y -= 80
        goto(x, y)
        write(alphabet[i], align="center", font=("Comic Sans MS", 40, "bold"))
        alphabet_dict[alphabet[i]] = (xcor(), ycor() + 30)
        x += 100



def draw_errors(numError):
    match numError:
        case 1:
            draw_line([-400, -250 + 40], [-100, -250 + 40])
        case 2:
            draw_line([-120, -250 + 40], [-120, 300 + 40])
        case 3:
            draw_line([-120, 300 + 40], [-300, 300 + 40])
        case 4:
            draw_line([-300, 300 + 40], [-300, 230 + 40])
        case 5:
            goto(-300, 230 + 40)
            draw_circle(-50)
        case 6:
            draw_line([-300, 130 + 40], [-300, -50 + 40])
        case 7:
            draw_line([-300, 70 + 40], [-400, 150 + 40])
        case 8:
            draw_line([-300, 70 + 40], [-200, 150 + 40])
        case 9:
            draw_line([-300, -50 + 40], [-400, -200 + 40])
        case 10:
            draw_line([-300, -50 + 40], [-200, -200 + 40])


def check_game_status(scoreWin, scoreUser, numError):
    if scoreUser == scoreWin:
        end_game("green", "ТЫ ПОБЕДИЛ")
    elif numError == 10:
        end_game("red", "ТЫ ПРОИГРАЛ")


def get_letter_onclick(x, y):
    global alphabet_dict
    for key, centerCoord in alphabet_dict.items():
        if abs(centerCoord[0] - x) < 100//2 and abs(centerCoord[1] - y) < 80 // 2:
            print(key)
            goto(alphabet_dict.pop(key))
            dot(84, "white")
            check_letter(key.lower())
            break


def check_letter(letter):
    global countErrors
    global scoreUSER

    if letter in secret:
        for i in range(len(secret)):
            if secret[i] == letter:
                goto(secretWordCoords[i])
                write(letter.upper(), align="center", font=("Comic Sans MS", 55, "bold"))
                scoreUSER += 1
    else:
        countErrors += 1
        draw_errors(countErrors)

    check_game_status(scoreWIN, scoreUSER, countErrors)


def end_game(titleColor, titlePhrase):
    alphabet_dict.clear()
    clear()
    goto(0, 200+50)
    pencolor(titleColor)
    write(titlePhrase, align="center", font=("Comic Sans MS", 55, "bold"))
    pencolor("black")
    goto(0, 0+50)
    write("Загаданное слово:", align="center", font=("Comic Sans MS", 30, "bold"))
    goto(0, -100+50)
    write(secret, align="center", font=("Comic Sans MS", 55, "bold"))
    goto(0, -300+100)
    write("Желаете повторить?", align="center", font=("Comic Sans MS", 55, "bold"))
    goto(-200, -400+100)
    pencolor("green")
    write("ДА", align="center", font=("Comic Sans MS", 55, "bold"))
    goto(200, -400+100)
    pencolor("red")
    write("НЕТ", align="center", font=("Comic Sans MS", 55, "bold"))
    pencolor("black")


secret = random.choice(gameWords)
scoreUSER = 0
scoreWIN = len(secret)
countErrors = 0
alphabet_dict = {}
secretWordCoords = []


Screen().setup(1200, 768)

shape("turtle")
speed(0)
penup()


draw_secret(secret)
draw_alphabet()



onscreenclick(get_letter_onclick)
mainloop()
