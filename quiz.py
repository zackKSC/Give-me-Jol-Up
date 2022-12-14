login_col = "#21325E"
title_col = '#3E497A'
BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = '#3E497A'
BTN_COLOR = '#F0F0F0'
EASY_COL = '#39ED63'
HARD_COL = '#F83333'


from tkinter import *
import random
import tkinter.messagebox as MessageBox
import pymysql as mysql
import tkinter as tk
from PIL import ImageTk
import random

    



#규정 퀴즈게임 - 쉬움

def quiz_easy():
    global correct_q
    global done_q
    
    correct_q = 0
    done_q = 0
    
    #규정 퀴즈 가져오기
    conn = mysql.connect(host="193.123.231.213", user="st02",password="djm06178RE!",database="db_st02")
    cur = conn.cursor()
    cur.execute("select * from easy_quiz")
    rows = cur.fetchall()

    #문제 생성
    def next_question():
        global answer
        global done_q
        done_q += 1

        def end_page():
            window = tk.Toplevel()
            window.title("규정이")
            window.geometry("400x350")

            correct_q_btn = Label(window, text = str(correct_q), font=("나눔바른펜", 16, "bold"))
            correct_q_btn.place(x=50, y=100)
            
        
        if done_q == 6:
            window.destroy()
            end_page()
            return              #exit() or die()
        
        question_num = random.sample(range(len(rows)),1)[0]
        your_question = rows[question_num]

        for i in range(4):
            buttons[i].config(bg=BTN_COLOR)
        a=[]
        a.append(your_question[1])
        q_choice = random.sample(your_question[2:5], 3)
        multi_choice =a + q_choice
        print(multi_choice)
        answer = random.randint(0,3)
        cur_question = your_question[0]


        question_label.config(text = cur_question)

        buttons[answer].config(text=multi_choice[0])

        for i in range(answer):
            buttons[i].config(text=q_choice[i])

        for i in range(answer+1,4):
            buttons[i].config(text=q_choice[i-1])

    #정답 체크
    def check_answer(idx):
        global correct_q
        global done_q
        idx = int(idx)
        if answer == idx:
            #버튼 색 변경
            buttons[idx].config(bg=CORRECT_COLOR)
            #맞은 문제 갯수, 푼 문제 갯수 측정
            correct_q += 1
            #정답 맞추면 넘어감
            window.after(60, next_question)
        else:
            buttons[idx].config(bg=WRONG_COLOR)
            window.after(60, next_question)
            

    window = tk.Toplevel()
    window.title("규정이")
    window.config(padx = 30, pady = 10, bg=BGCOLOR)


    question_label = Label(window, width=20, height=2, text="test", font=("나눔바른펜", 25, "bold"), bg=BGCOLOR, fg="white")
    question_label.pack(pady=30)

    buttons = []
    for i in range(4):
        btn = Button(window, text=f"{i}번", width=35, height=2, font=("나눔바른펜", 15, "bold"), bg=BTN_COLOR, command=lambda idx=i: check_answer(idx))
        btn.pack()
        buttons.append(btn)

    next_btn = Button(window, text="다음 문제", width=15, height=2, command=next_question, font=("나눔바른펜", 15, "bold"), bg=CORRECT_COLOR)
    next_btn.pack(pady=30)



    next_question()

    window.mainloop()


