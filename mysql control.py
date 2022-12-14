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
import quiz
import csv
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



cur.execute(insert into easy_quiz(quiz, answer_1, answer_2, answer_3, answer_4) values("다음 중 옳은 것을 고르시오.", "생활점검은 수요일에 시행한다.", "무용구보는 매주 목요일 7, 8교시에 실시한다.", "전생도는 매주 금요일 1730에 외출에 임한다.", "공사십훈에는 '용두사미'가 포함된다."))

conn.commit()

rows = cur.fetchall()
print(rows)
conn.close()

print(rows)