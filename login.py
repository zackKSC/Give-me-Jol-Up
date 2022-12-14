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

from 규정이 import p
import pymysql
import database   #module database, quiz, mileage
import quiz
from tkinter import *
import random
import tkinter.messagebox as MessageBox
import tkinter as tk
from PIL import ImageTk


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
    quiz_btn = Button(window, text="쉬 움", width=5, height=1, font=("나눔바른펜", 11, "bold"),fg="white", bg=EASY_COL, command = quiz.quiz_easy)
    quiz_btn.place(x=290, y=48)

    database_btn = Button(window, text="바로가기", width=8, height=1, font=("나눔바른펜", 11, "bold"), bg="white", command = database.data_inter)
    database_btn.place(x=275, y=108)

    market_btn = Button(window, text="바로가기", width=8, height=1, font=("나눔바른펜", 11, "bold"), bg="white", command=lambda: [market(), window.destroy()]) 
    market_btn.place(x=275, y=168)

    global data_image
    data_image=tk.PhotoImage(file="규정이_라인.png")
    label=tk.Label(window,image=data_image)
    label.place(x=197, y=121)

    global market_image
    market_image=tk.PhotoImage(file="규정이_라인.png")
    label=tk.Label(window,image=market_image)
    label.place(x=197, y=181)

