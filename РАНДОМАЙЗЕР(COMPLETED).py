from tkinter import *
import random
from PIL import Image, ImageTk

def btn_click():
    if textEntry.get().isdigit() == True and textEntry2.get().isdigit() == True:
        if int(textEntry2.get()) > int(textEntry.get()):
            a = random.randint(int(textEntry.get()), int(textEntry2.get()))
            textLabelResWindow['text'] = a
        else:
            textLabelResWindow['text'] = 'Первое число\n Больше второго'
    else:
        textLabelResWindow['text'] = 'Укажите число'

Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
Length = None

OrbAnswers = ['Да', 'Нет', 'Думаю, да', 'Думаю, нет', 'Скорее да, чем нет', 'Скорее нет, чем да', 'Затрудняюсь ответить', 'Боюсь, нет', 'Несомненно!', 'Это правда!', 'Это ложь!', 'Это не может быть правдой', 'Вероятно, да', 'По моим данным - нет', 'Карты говорят - да', 'Весьма спорно', 'Перспективы хорошие', 'Перспективы не очень хорошие', 'Определённо да!', 'Точно нет!', 'Даже не думай!', 'Будь уверен - это ложь!', 'Будь уверен - это правда!']
Ask = None

def PasClick():
    def GenPas():
        if Length == None:
            return
        Number = 0
        Password = ''
        if Length == 'Short':
            Number = random.randint(6, 8)
        elif Length == 'Medium':
            Number = random.randint(9, 12)
        elif Length == 'Long':
            Number = random.randint(13, 16)
        for i in range(Number):
            Password = Password + random.choice(Alphabet)
        GentdPas = Label(framePas, bg='gray', font='Courier 20')
        GentdPas['text'] = Password
        GentdPas.place(rely=0.1, relx=0, relheight=0.3, relwidth=1)

    framePas = Frame(root, bg='gray')
    framePas.place(relwidth=0.7, relheight=0.5, rely=0, relx=0.15)

    frame.place_forget()
    btnOrb.place_forget()
    btnPas.place_forget()

    textPas = Label(framePas, bg='white', font='Courier 15', text='Пароль: ')
    textPas.place(rely=0, relx=0.12, relheight=0.1, relwidth=0.8)

    btn = Button(framePas, bg='white', text='Сгенерировать', font='Courier 15', command=GenPas)
    btn.place(rely=0.7, relx=0, relheight=0.3, relwidth=1)

    textPasGen = Label(framePas, bg='gray', font='Courier 20', text='')
    textPasGen.place(relheight=0.3, relwidth=1, rely=0.15, relx=0)

    textPasLen = Label(framePas, bg='gray', font='Courier 15', text='Выберите длину пароля')
    textPasLen.place(relheight=0.3, relwidth=1, rely=0.15, relx=0)

    btn = Button(framePas, bg='white', text='Сгенерировать', font='Courier 15', command=GenPas)
    btn.place(rely=0.7, relx=0, relheight=0.3, relwidth=1)

    def blss():
        global Length
        textPasLen = Label(framePas, bg='gray', font='Courier 13',
                           text='Нажмите\nСгенерировать')
        textPasLen.place(relheight=0.3, relwidth=1, rely=0.15, relx=0)
        Length = 'Short'
    def blsm():
        global Length
        textPasLen = Label(framePas, bg='gray', font='Courier 13',
                           text='Нажмите\nСгенерировать')
        textPasLen.place(relheight=0.3, relwidth=1, rely=0.15, relx=0)
        Length = 'Medium'
    def blsl():
        global Length
        textPasLen = Label(framePas, bg='gray', font='Courier 13',
                           text='Нажмите\nСгенерировать')
        textPasLen.place(relheight=0.3, relwidth=1, rely=0.15, relx=0)
        Length = 'Long'

    btnLabelSymShort = Button(framePas, bg='white', font='Courier 12', text='6-8', command=blss)
    btnLabelSymShort.place(rely=0.5, relx=0, relwidth=0.2, relheight=0.2)

    btnLabelSymMedium = Button(framePas, bg='white', font='Courier 12', text='9-12', command=blsm)
    btnLabelSymMedium.place(rely=0.5, relx=0.4, relwidth=0.2, relheight=0.2)

    btnLabelSymLong = Button(framePas, bg='white', font='Courier 12', text='13-16', command=blsl)
    btnLabelSymLong.place(rely=0.5, relx=0.8, relwidth=0.2, relheight=0.2)

    def BackClick():
        framePas.place_forget()
        frame.place(relwidth=0.7, relheight=0.5, rely=0, relx=0.15)
        btnOrb.place(rely=0.9, relx=0.7, relheight=0.1, relwidth=0.3)
        btnPas.place(rely=0.9, relx=0, relheight=0.1, relwidth=0.3)
        btnBack.place_forget()
        textPas.destroy()

    btnBack = Button(root, bg='white', font='Courier 15', text='Назад', command=BackClick)
    btnBack.place(rely=0.9, relx=0, relheight=0.1, relwidth=0.3)

root = Tk()
root.geometry('400x350')
root['bg'] = '#8d7a96'
root.resizable(0, 0)
root.title('Рандомайзер')
root.wm_attributes('-alpha', 0.9)

frame = Frame(root, bg='gray')
frame.place(relwidth=0.7, relheight=0.5, rely=0, relx=0.15)
img = ImageTk.PhotoImage(file='Dorae.png')
labelImg = Label(root, height=200, width=155, image=img, font='Courier 15', text='')
labelImg.place(rely=0.50, relx=0.30)
def OrbClick():
    def BackClick():
        frameOrb.place_forget()
        frame.place(relwidth=0.7, relheight=0.5, rely=0, relx=0.15)
        btnOrb.place(rely=0.9, relx=0.7, relheight=0.1, relwidth=0.3)
        btnPas.place(rely=0.9, relx=0, relheight=0.1, relwidth=0.3)
        btnBack.place_forget()
        textOrb.destroy()

    btnBack = Button(root, bg='white', font='Courier 15', text='Назад', command=BackClick)
    btnBack.place(rely=0.9, relx=0, relheight=0.1, relwidth=0.3)

    frameOrb = Frame(root, bg='gray')
    frameOrb.place(relwidth=0.7, relheight=0.5, rely=0, relx=0.15)

    frame.place_forget()
    btnOrb.place_forget()
    btnPas.place_forget()

    textOrb = Label(frameOrb, bg='white', font='Courier 15', text='Шар говорит: ')
    textOrb.place(rely=0, relx=0.12, relheight=0.1, relwidth=0.8)
    def genAnswer():

        textOrbAnswer = Label(frameOrb, bg='gray', font='Courier 12')
        textOrbAnswer['text'] = random.choice(OrbAnswers)
        textOrbAnswer.place(rely=0.1, relx=0, relheight=0.3, relwidth=1)

    LabelOrbAsk = Label(frameOrb, bg='gray', font='Courier 15', text='Задайте вопрос')
    LabelOrbAsk.place(rely=0.1, relx=0, relheight=0.3, relwidth=1)

    btnF = Button(frameOrb, bg='white', text='Сгенерировать', font='Courier 15', command=genAnswer)
    btnF.place(rely=0.7, relx=0, relheight=0.3, relwidth=1)

    textEntryOrb = Entry(frameOrb, bg='white', font='Courier 10')
    textEntryOrb.place(relheight=0.15, relwidth=1, rely=0.6, relx=0)


btn = Button(frame, bg='white', text='Сгенерировать', font='Courier 15', command=btn_click)
btn.place(rely=0.7, relx=0, relheight=0.3, relwidth=1)

btnPas = Button(root, bg='white', text='Сгенерировать\nпароль', font='Courier 10', command=PasClick)
btnPas.place(rely=0.9, relx=0, relheight=0.1, relwidth=0.3)

btnOrb = Button(root, bg='white', text='Магический\nшар', font='Courier 10', command=OrbClick)
btnOrb.place(rely=0.9, relx=0.7, relheight=0.1, relwidth=0.3)

textLabel = Label(frame, bg='white', font='Courier 10', text='ОТ')
textLabel.place(rely=0.5, relx=0, relwidth=0.1, relheight=0.2)

textLabel2 = Label(frame, bg='white', font='Courier 10', text='ДО')
textLabel2.place(rely=0.5, relx=0.5, relwidth=0.1, relheight=0.2)

textLabelRes = Label(frame, bg='white', font='Courier 15', text='Случайное число: ')
textLabelRes.place(rely=0, relx=0.12, relheight=0.1, relwidth=0.8)

textLabelResWindow = Label(frame, bg='gray', font='Courier 20', text='0')
textLabelResWindow.place(relheight=0.3, relwidth=1, rely=0.15, relx=0)

textEntry = Entry(frame, bg='white', font='Courier 10')
textEntry.place(rely=0.5, relx=0.1, relwidth=0.4, relheight=0.2)

textEntry2 = Entry(frame, bg='white', font='Courier 10')
textEntry2.place(rely=0.5, relx=0.6, relwidth=0.4, relheight=0.2)

root.mainloop()