login_col = "#21325E"
title_col = '#3E497A'
BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = '#3E497A'
BTN_COLOR = '#F0F0F0'
EASY_COL = '#39ED63'
HARD_COL = '#F83333'
user_col = '#6D6A6A'
column_col = '#323232'


import pymysql
import database   #module database, quiz, mileage
from tkinter import *
import random
import tkinter.messagebox as MessageBox
import tkinter as tk
from PIL import ImageTk


# MySQL DB 연결
conn =pymysql.connect(host="193.123.231.213", user="st02", password="djm06178RE!", database="db_st02")
# Connection 으로부터 Cursor 생성
cur = conn.cursor()
 
# SQL 쿼리 실행
cur.execute("select * from cadets_info")
 
# 데이타 Fetch
rows = cur.fetchall()



id_pw_info=[]
for i in range(len(rows)):
    c=[]
    c.append((rows[i])[0])
    c.append((rows[i])[1])
    id_pw_info.append(c)

#생도 정보 가져오기
id_pw_num=len(id_pw_info)

# Connection 닫기
conn.close()

#로그인 성공시 메인 인터페이스
def login():
    global mileage
    global user_id
    global play_num
    global score_sum
    
    # MySQL DB 연결
    conn =pymysql.connect(host="193.123.231.213", user="st02", password="djm06178RE!", database="db_st02")
    # Connection 으로부터 Cursor 생성
    cur = conn.cursor()
     
    # SQL 쿼리 실행
    cur.execute("select * from cadets_info")
     
    # 데이타 Fetch
    rows = cur.fetchall()
    
    # Connection 닫기
    conn.close()

    cadets_num=len(rows)
        
    user_info = rows[p]
    user_id = user_info[1]
    user_name = user_info[3]
    play_num = user_info[4]
    score_sum = user_info[5]
    mileage = user_info[6]
    f_info = user_info[7]    #friday
    s_info = user_info[8]    #twoP
    b_info = user_info[9]    #voucher
    m_info = user_info[10]   #morning
    
    
    

    #mileage market btn
    def market():
        # MySQL DB 연결
        conn =pymysql.connect(host="193.123.231.213", user="st02", password="djm06178RE!", database="db_st02")
        # Connection 으로부터 Cursor 생성
        cur = conn.cursor()
         
        # SQL 쿼리 실행
        cur.execute("select * from cadets_info")
         
        # 데이타 Fetch
        rows = cur.fetchall()
        
        cadets_num=len(rows)

            
        user_info = rows[p]
        user_id = user_info[1]
        user_name = user_info[3]
        mileage = user_info[6]
        f_info = user_info[7]    #friday
        s_info = user_info[8]    #twoP
        b_info = user_info[9]    #voucher
        m_info = user_info[10]   #morning

        window = tk.Toplevel(root)
        window.geometry("900x600")
        window.title("규정이")
        window.resizable(False, False)
        
        market_names = Label(window, text = "잔여 마일리지 : " + str(mileage) + " P", font=("나눔바른펜", 21, "bold"))
        market_names.place(x=40, y=50)
        market_names = Label(window, text = "사용자 : " + str(user_id), font=("나눔바른펜", 16, "bold"), fg=user_col)
        market_names.place(x=650, y=24)       
        
        market_names = Label(window, text = "보유 교환권", font=("나눔바른펜", 20, "bold"), fg=title_col)
        market_names.place(x=55, y=123)
        market_names = Label(window, text = "금박권 " + str(f_info) + "회", font=("나눔바른펜", 17, "bold"), fg=column_col)
        market_names.place(x=230, y=125)
        market_names = Label(window, text = "상점 2점 " + str(s_info) + "회", font=("나눔바른펜", 17, "bold"), fg=column_col)
        market_names.place(x=530, y=125)
        market_names = Label(window, text = "제빵소 5천원권 " + str(b_info) + "회", font=("나눔바른펜", 17, "bold"), fg=column_col)
        market_names.place(x=230, y=195)
        market_names = Label(window, text = "아침구보 열외권 " + str(m_info) + "회", font=("나눔바른펜", 17, "bold"), fg=column_col)
        market_names.place(x=530, y=195)
        
        #quit button
        quit_btn = Button(window, text="X", width=1, height=1, font=("나눔바른펜", 14, "bold"), fg="white", bg=HARD_COL, command=lambda: [login(), window.destroy()])
        quit_btn.place(x=840, y=21)
        
        
        #상품 설명
        global instru_image
        instru_image=tk.PhotoImage(file="instru.png")        
        label=tk.Label(window,image=instru_image)
        label.place(x=55,y=285)   


        #%d = 정수  , %s = 문자열  , %f = 소수점
        def buy_friday():
            if mileage-200 < 0:
                MessageBox.showinfo("알림", "마일리지가 부족합니다!")
                return
            sql ="""
            UPDATE cadets_info
            SET
                mileage=%d,
                friday=%d  
            where 
                id=%d
                """                
            cnt = cur.execute(sql % (int(mileage-200), int(f_info+1), int(user_id))) 
            conn.commit()
            market()
            window.destroy()
           # Connection 닫기
            conn.close()
   
   
        def buy_twoP():
            if mileage-50 < 0:
                MessageBox.showinfo("알림", "마일리지가 부족합니다!")
                return
            sql ="""
            UPDATE cadets_info
            SET
                mileage=%d,
                twoP=%d  
            where 
                id=%d
                """                
            cnt = cur.execute(sql % (int(mileage-50), int(f_info+1), int(user_id))) 
            conn.commit()
            market()
            window.destroy()
           # Connection 닫기
            conn.close()


        def buy_voucher():
            if mileage-100 < 0:
                MessageBox.showinfo("알림", "마일리지가 부족합니다!")
                return
            sql ="""
            UPDATE cadets_info
            SET
                mileage=%d,
                voucher=%d  
            where 
                id=%d
                """                
            cnt = cur.execute(sql % (int(mileage-100), int(f_info+1), int(user_id))) 
            conn.commit()
            market()
            window.destroy()
           # Connection 닫기
            conn.close()
            
 
        def buy_morning():
            if mileage-100 < 0:
                MessageBox.showinfo("알림", "마일리지가 부족합니다!")
                return
            sql ="""
            UPDATE cadets_info
            SET
                mileage=%d,
                morning=%d  
            where 
                id=%d
                """                
            cnt = cur.execute(sql % (int(mileage-100), int(f_info+1), int(user_id))) 
            conn.commit()
            market()
            window.destroy()
           # Connection 닫기
            conn.close()
            
    
        #purchase button
        purchase_btn = Button(window, text="교환하기", width=5, height=1, font=("나눔바른펜", 14, "bold"),fg="white", bg=login_col, command = buy_friday)
        purchase_btn.place(x=782, y=335)
        purchase_btn = Button(window, text="교환하기", width=5, height=1, font=("나눔바른펜", 14, "bold"),fg="white", bg=login_col, command = buy_twoP)
        purchase_btn.place(x=782, y=391)
        purchase_btn = Button(window, text="교환하기", width=5, height=1, font=("나눔바른펜", 14, "bold"),fg="white", bg=login_col, command = buy_voucher)
        purchase_btn.place(x=782, y=447)
        purchase_btn = Button(window, text="교환하기", width=5, height=1, font=("나눔바른펜", 14, "bold"),fg="white", bg=login_col, command = buy_morning)
        purchase_btn.place(x=782, y=503)





    #규정 퀴즈게임 - 쉬움

    def quiz_easy():
        global correct_q
        global done_q
        
        correct_q = 0
        done_q = 0
        
        #규정 퀴즈 가져오기
        conn = pymysql.connect(host="193.123.231.213", user="st02",password="djm06178RE!",database="db_st02")
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
                plus_mileage = 0
                new_ave_score = (score_sum * play_num + correct_q * 10)/(play_num + 1)
                
                #마일리지 저장선 설정
                if correct_q >= 8:
                    plus_mileage += correct_q
                
                
                global result_image
                result_image=tk.PhotoImage(file="result.png")
                label=tk.Label(window,image=result_image)
                label.place(x=130, y=1)
                
                correct_q_num = Label(window, text = "점수 : " + str(correct_q * 10), font=("나눔바른펜", 16, "bold"))
                correct_q_num.place(x=50, y=100)
                ave_score = Label(window, text = "평균 점수 : " + str(new_ave_score), font=("나눔바른펜", 16, "bold"))
                ave_score.place(x=50, y=150)
                play_num_l = Label(window, text = "도전 횟수 : " + str(play_num+1), font=("나눔바른펜", 16, "bold"))
                play_num_l.place(x=50, y=200)
                your_mileage = Label(window, text = "마일리지 : " + str(mileage + plus_mileage), font=("나눔바른펜", 16, "bold"))
                your_mileage.place(x=50, y=250)
                
                
                sql ="""
                UPDATE cadets_info
                SET
                    mileage=%d,
                    score=%d,
                    num=%d
                where 
                    id=%d
                    """                
                cnt = cur.execute(sql % (int(mileage +  plus_mileage), int(new_ave_score), int(play_num + 1), int(user_id))) 
                conn.commit()
                conn.close()
                
                #quit button
                quit_btn = Button(window, text="X", width=1, height=1, font=("나눔바른펜", 14, "bold"), fg="white", bg=HARD_COL, command=lambda: [login(), window.destroy()])
                quit_btn.place(x=343, y=16)

            #문제 수 설정
            if done_q == 11:
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
                

        window = tk.Toplevel(root)
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


    #login interface
    window = tk.Toplevel(root)
    window.geometry("400x350")
    window.title("규정이")
    window.resizable(False, False)
    
    table_names = Label(window, text = "퀴즈", font=("나눔바른펜", 16, "bold"), fg=title_col)
    table_names.place(x=30, y=50)
    table_names = Label(window, text = "데이터베이스", font=("나눔바른펜", 16, "bold"), fg=title_col)
    table_names.place(x=30, y=110)
    table_names = Label(window, text = "마일리지 마켓", font=("나눔바른펜", 16, "bold"), fg=title_col)
    table_names.place(x=30, y=170)
    table_names = Label(window, text = str(user_name) + "님의 잔여 마일리지 : " + str(mileage) + " P", font=("나눔바른펜", 17, "bold"))
    table_names.place(x=25, y=245)
    
    quiz_btn = Button(window, text="어려움", width=5, height=1, font=("나눔바른펜", 11, "bold"),fg="white", bg=HARD_COL)
    quiz_btn.place(x=120, y=48)
    quiz_btn = Button(window, text="보 통", width=5, height=1, font=("나눔바른펜", 11, "bold"),fg="white", bg=login_col)
    quiz_btn.place(x=205, y=48)
    quiz_btn = Button(window, text="쉬 움", width=5, height=1, font=("나눔바른펜", 11, "bold"),fg="white", bg=EASY_COL, command = lambda: [quiz_easy(), window.destroy()])
    quiz_btn.place(x=290, y=48)

    database_btn = Button(window, text="바로가기", width=8, height=1, font=("나눔바른펜", 11, "bold"), bg="white", command = database.data_inter)
    database_btn.place(x=275, y=108)

    market_btn = Button(window, text="바로가기", width=8, height=1, font=("나눔바른펜", 11, "bold"), bg="white", command = lambda: [market(), window.destroy()]) 
    market_btn.place(x=275, y=168)

    global data_image
    data_image=tk.PhotoImage(file="규정이_라인.png")
    label=tk.Label(window,image=data_image)
    label.place(x=197, y=121)

    global market_image
    market_image=tk.PhotoImage(file="규정이_라인.png")
    label=tk.Label(window,image=market_image)
    label.place(x=197, y=181)



#로그인 버튼 명령어 - 실패
def warn():
    MessageBox.showinfo("알림", "잘못된 로그인 정보입니다.")


#로그인 버튼 명령어
def login_check():
    global p
    p = 0
    while p <= id_pw_num:
        c = id_pw_info[p]
        if str(e_id.get()) == str(c[1]) and str(e_password.get()) ==str(c[0]):
            login()
            break
        p+=1
        if p == id_pw_num:
            warn()
            break
        

#로그인 창
root = tk.Tk()
root.geometry("330x300")
root.title("규정이")
root.resizable(False, False)

table_names = Label(root, text = "규정이", font=("나눔바른펜", 15, "bold"), fg=title_col)
table_names.place(x=135, y=200)

image=tk.PhotoImage(file="규정이.png")
label=tk.Label(root,image=image)
label.place(x=117, y=22)

table_names = Label(root, text = "교 번", font=("나눔바른펜", 10, "bold"))
table_names.place(x=45, y=240)
table_names = Label(root, text = "비밀번호", font=("나눔바른펜", 10, "bold"))
table_names.place(x=35, y=265)

e_id = Entry(root)
e_id.place(width=120, height=20, x=105, y=240)
e_password = Entry(root)
e_password.place(width=120, height=20, x=105, y=265)

login_btn = Button(text="로그인", width=5, height=2, font=("나눔바른펜", 10, "bold"),fg="white", bg=login_col, command = login_check)
login_btn.place(x=245, y=240)


root.mainloop()




