import pymysql
from tkinter import *
import random
import tkinter.messagebox as MessageBox
import tkinter as tk
from PIL import ImageTk
import tkinter.ttk as ttk



#colors
login_col = "#21325E"
title_col = '#3E497A'

BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = '#3E497A'
BTN_COLOR = '#F0F0F0'
EASY_COL = '#39ED63'
HARD_COL = '#F83333'




def data_inter():
    window = tk.Toplevel()
    window.geometry("1000x500")
    window.title("규정이")
    window.resizable(False, False)


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

    cadets_info=[]
    for i in range(len(rows)):
        c=[]
        c.append((rows[i])[0])
        c.append((rows[i])[1])
        c.append((rows[i])[2])
        c.append((rows[i])[3])
        c.append((rows[i])[4])
        c.append((rows[i])[5])
        c.append((rows[i])[6])
        b=("금박권 " + str((rows[i])[7]) + "회,"+ " 상점 2점 " + str((rows[i])[8]) + "회,"+ " 제빵소 5천원권 " + str((rows[i])[9]) + "회,"+ " 아침구보 열외권 " + str((rows[i])[10]) + "회")
        c.append(b)
        c.append((rows[i])[-1])
        cadets_info.append(c)
    #treelist=rows


    lbl = tk.Label(window, text="")
    lbl.pack(pady=50)
    lbl_right_x = tk.Label(window, text="")
    lbl_right_x.pack(side="right", fill="y", padx=21)
    lbl_bottom_y = tk.Label(window, text="")
    lbl_bottom_y.pack(side="bottom", fill="x", pady=11)


    s = ttk.Style()
    s.theme_use('clam')

    # Configure the style of Heading in Treeview widget
    s.configure('Treeview.Heading',foreground="white", background=BGCOLOR, font=("나눔바른펜", 11, "bold"))

    scroll_bar = tk.Scrollbar(window)
    treeview=tk.ttk.Treeview(window, columns=["id", "grade","name", "num", "score","mileage", "voucher"], displaycolumns=["id", "grade","name", "num", "score","mileage", "voucher"],show='headings', height=9, yscrollcommand=scroll_bar.set)
    scroll_bar.pack(side="right", fill="y")
    treeview.pack(side="right",fill="y")


    scroll_bar.config( command = treeview.yview)
    
    treeview.column("id", width=80, anchor="center")
    treeview.heading("id", text="교번", anchor = "center")
    
    treeview.column("grade", width=50, anchor="center")
    treeview.heading("grade", text="기수", anchor="center")

    treeview.column("name", width=70, anchor="center")
    treeview.heading("name", text="이름", anchor="center")

    treeview.column("num", width=75, anchor="center")
    treeview.heading("num", text="게임 횟수", anchor="center")


    treeview.column("score", width=75, anchor="center")
    treeview.heading("score", text="평균 점수", anchor="center")

    treeview.column("mileage", width=75, anchor="center")
    treeview.heading("mileage", text="마일리지", anchor="center")

    treeview.column("voucher", width=465, anchor="center")
    treeview.heading("voucher", text="보유 교환권", anchor="center")


    Squadron_list=["1중대","2중대","3중대","4중대","5중대","6중대","7중대","8중대"]
    combobox=ttk.Combobox(window)
    combobox.config(width=10, height=1, values=Squadron_list, font=("나눔바른펜", 18), state="readonly")
    combobox.set("Select")
    combobox.pack()
    combobox.place(x=130, y=46)
    
    table_names = Label(window, text = "중대", font=("나눔바른펜", 19, "bold"), fg=title_col)
    table_names.place(x=55, y=45)

    def showbox():
        treelist = []
        for row in treeview.get_children():
            treeview.delete(row)
        a = combobox.current()
        for i in range(len(cadets_info)):
            if (cadets_info[i])[-1] == a+1:
                treelist.append(cadets_info[i])     
        for i in range(len(treelist)):
            treeview.insert('', 'end', values=(treelist[i][1:8]), iid=str(i)+"번")
        treelist = []

                
    show_btn = Button(window, text="조회하기", width=6, height=1, font=("나눔바른펜", 13, "bold"),fg="white", bg=BGCOLOR, command=showbox)
    show_btn.place(x=305, y=45)
