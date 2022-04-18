from tkinter import *
import random

# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGT = 800
MARGIN = 100
BG_COLOR = 'white'
LINES_COLOR = 'orange'
BTN_COLOR = 'light gray'
TXT_COLOR = 'black'
SPEC_COLOR = 'red'
HEAD_COLOR = '#696969'
HAND_COLOR = '#66101f'
FOOT_COLOR = '#417B5A'
FG_COLOR = '#FFD400'
label_word = []
btn_alpha = []


def start_pos_man():
    line_1 = canvas.create_line(
        MARGIN, WINDOW_HEIGT - MARGIN, MARGIN, MARGIN, width=5, fill=LINES_COLOR)
    line_2 = canvas.create_line(
        MARGIN, MARGIN, WINDOW_WIDTH // 3, MARGIN * 1, width=5, fill=LINES_COLOR)
    line_3 = canvas.create_line(
        WINDOW_WIDTH // 3, MARGIN, WINDOW_WIDTH // 3, MARGIN * 2, width=5, fill=LINES_COLOR)


def start_pos_alphabet():
    shift_x = shift_y = 0
    count = 0
    alphabet_list = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUVWXYZŹŻ"

    for c in alphabet_list:
        btn = Button(text=(c), bg=BTN_COLOR,
                     foreground=TXT_COLOR, font='Arial 19', relief=SOLID)
        btn.place(x=WINDOW_HEIGT - MARGIN*2 + shift_x, y=MARGIN*4.5 - shift_y)
        btn.bind('<Button-1>', lambda event: check_alpha(event, word))
        btn_alpha.append(btn)
        shift_x += 65
        count += 1

        if (count == 8):
            shift_x = count = 0
            shift_y -= 65


def start_word():
    f = open('words.txt')
    count = 0

    for s in f:
        count += 1

    num_word = random.randint(1, count)
    word = ''
    count = 0

    f = open('words.txt', encoding='utf-8')

    for s in f:
        count += 1

        if (count == num_word):
            word = s[:len(s) - 1:]

    word = word.upper()

    return word


def start_pos_word(word):
    shift = 0

    for i in range(len(word)):
        label_under = Label(window, text='__',
                            font="Arial 24", bg=BG_COLOR, fg=FG_COLOR)
        label_under.place(x=WINDOW_HEIGT-MARGIN*2 + shift, y=MARGIN*3.5)
        shift += 50
        label_word.append(label_under)


def draw(lifes):
    if (lifes == 4):
        head = canvas.create_oval(
            WINDOW_WIDTH // 3 - 60, MARGIN * 1.5, WINDOW_WIDTH // 3 + 60, MARGIN * 2.5, fill=HEAD_COLOR)
    elif (lifes == 3):
        body = canvas.create_oval(
            WINDOW_WIDTH // 3 - 25, MARGIN * 2.5, WINDOW_WIDTH // 3 + 25, MARGIN * 5, fill=HEAD_COLOR)
    elif (lifes == 2):
        l_hand = canvas.create_line(
            WINDOW_WIDTH // 3 - 15, MARGIN * 3.5, WINDOW_WIDTH // 3 - 105, MARGIN * 2.4, width=6, fill=HAND_COLOR)
        r_hand = canvas.create_line(
            WINDOW_WIDTH // 3 + 15, MARGIN * 3.5, WINDOW_WIDTH // 3 + 105, MARGIN * 2.4, width=6, fill=HAND_COLOR)
    elif (lifes == 1):
        l_foot = canvas.create_line(
            WINDOW_WIDTH // 3 - 15, MARGIN * 4.5, WINDOW_WIDTH // 3 - 110, MARGIN * 7, width=7, fill=FOOT_COLOR)
        r_foot = canvas.create_line(
            WINDOW_WIDTH // 3 + 15, MARGIN * 4.5, WINDOW_WIDTH // 3 + 110, MARGIN * 7, width=7, fill=FOOT_COLOR)
    elif (lifes == 0):
        game_over('lose')


def check_alpha(event, word):
    alpha = event.widget['text']
    pos = []

    for i in range(len(word)):
        if (word[i] == alpha):
            pos.append(i)

    if (pos):
        for i in pos:
            label_word[i].config(text='{}'.format(word[i]))

        count_alpha = 0

        for i in label_word:
            if (i['text'].isalpha()):
                count_alpha += 1

        if (count_alpha == len(word)):
            game_over('win')
    else:
        lifes = int(label_life.cget('text')) - 1

        if (lifes != 0):
            label_life.config(text=' {}'.format(lifes))

        draw(lifes)


def game_over(status):
    for btn in btn_alpha:
        btn.destroy()

    if (status == 'win'):
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 100,
                           font=('Futura PT Heave', 50), text='Wygrałeś!\n    Jestes zwycięzcą! :)', fill=SPEC_COLOR)

    else:
        canvas.create_text(canvas.winfo_width()/2 + 100, canvas.winfo_height()/2,
                           font=('Futura PT Heave', 50), text='Spróbuj jeszcze raz! :(', fill=SPEC_COLOR)


window = Tk()
window.title('Wisielec')
window.resizable(False, False)

lifes = 5

lebel_text = Label(window, text='lifes:', font=(
    'Futura PT Heave', 40), foreground=TXT_COLOR)
lebel_text.place(x=930, y=10)
label_life = Label(window, text=' {}'.format(
    lifes), font=('Futura PT Heave', 40))
label_life.place(x=1110, y=10)

canvas = Canvas(window, bg=BG_COLOR, height=WINDOW_HEIGT, width=WINDOW_WIDTH)
canvas.place(x=0, y=70)

window.geometry('1200x800')

start_pos_man()
start_pos_alphabet()
word = start_word()
start_pos_word(word)
print(word)


window.mainloop()
