# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:51:39 2023

@author: User
"""

        
import tkinter
from tkinter import ttk
import calendar
from datetime import datetime
#取得するカレンダー、日曜日が週の最初になるように設定
calendar.setfirstweekday(calendar.SUNDAY)

#グローバル変数の定義
list_selected_date=[]
list_selected_time=[]

class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title(u"Event CSV Setting")
        self.minsize(500, 500)
        self.geometry("800x600")

        # タブウィジェットを追加
        tab_parent = ttk.Notebook(self)
        styleA=ttk.Style()
        styleA.configure('styleA.TFrame', background='#ffffee')
        tab_1 = ttk.Frame(tab_parent,style='styleA.TFrame')
        styleB=ttk.Style()
        styleB.configure('styleB.TFrame', background='#eeffff')
        tab_2 = ttk.Frame(tab_parent,style='styleB.TFrame')
        styleC=ttk.Style()
        styleC.configure('styleC.TFrame', background='#ffeeff')
        tab_3 = ttk.Frame(tab_parent,style='styleC.TFrame')
        tab_parent.add(tab_1, text="tab_1")
        tab_parent.add(tab_2, text="tab_2")
        tab_parent.add(tab_3, text="tab_3")
        tab_parent.pack(expand=True, fill="both")

        # クラスAとクラスBでそれぞれ異なるウィジェットを配置する
        self.A(tab_1)
        self.B(tab_2)
        self.C(tab_3)
        
        Button_new_window = tkinter.Button(tab_parent, text = "ウインドウ追加", font = ("Arial", "10", "bold"),
                                            command = lambda : App())
        Button_new_window.place(x = 580, y = 20)
        
        Button_close_window = tkinter.Button(tab_parent, text = "閉じる", font = ("Arial", "10", "bold"),
                                            command = lambda : self.close_window())
        Button_close_window.place(x = 700, y = 20)
        
    def close_window(self):
        self.destroy()
        
        
    class Commons:
        def common_function(self):
            print("共通して実行する関数です")
            
        def use_calendar(self,parent_info):
            print("カレンダー起動")
            print(parent_info)
            #print(isinstance(parent_info, App.A))
            #print(isinstance(parent_info, App.B))
            #print(isinstance(parent_info, App.C))
            self.popup_window=tkinter.Toplevel()
            self.popup_window.title("Aのカレンダー")
            self.popup_window.geometry("400x280")
            #print(calendar.month(2023,5))
            list_selected_date=[]
            
            self.button_close_calendar=ttk.Button(self.popup_window, text='カレンダーを閉じる',command = lambda : self.close_calendar())
            self.button_close_calendar.place(x=100,y=20)
            
            # 日付エントリーとボタンを作成
            self.form_year_month()
            
            
        def form_year_month(self):
            now=datetime.now()
            current_year=now.year
            current_month=now.month
            
            #年のリスト
            year_list=[str(current_year-1),str(current_year),str(current_year+1)]
            #月のリスト
            month_list=[]
            for i in range(current_month,13):
                month_list.append(str(i))
            for i in range(1,current_month):
                month_list.append(str(i))
            
            #年のCombobox
            self.year_combobox=ttk.Combobox(self.popup_window, width=4, height=10, values=year_list)
            self.year_combobox.current(1)
            self.year_combobox.bind("<<ComboboxSelected>>", self.form_date)
            self.year_combobox.place(x = 10, y = 20)
            #月のCombobox
            self.month_combobox=ttk.Combobox(self.popup_window, width=2, height=10, values=month_list)
            self.month_combobox.current(0)
            self.month_combobox.bind("<<ComboboxSelected>>", self.form_date)
            self.month_combobox.place(x = 60, y = 20)
            
            self.form_date()
            
            
        def form_date(self, event=None):
            frame_calendar_tile=ttk.Frame(self.popup_window, width=180, height=190, borderwidth=5, relief = 'solid')
            frame_calendar_tile.place(x = 5, y = 45)
            self.calendar_header=ttk.Label(self.popup_window,text='日',background='#ff0000',foreground='#ffffff',font=('bold'))
            self.calendar_header.place(x=13,y=50)
            self.calendar_header=ttk.Label(self.popup_window,text='月　火　水　木　金')
            self.calendar_header.place(x=37,y=50)
            self.calendar_header=ttk.Label(self.popup_window,text='土',background='#0000ff',foreground='#ffffff',font=('bold'))
            self.calendar_header.place(x=157,y=50)
            
            
            self.selected_year_str=self.year_combobox.get()
            self.selected_month_str=self.month_combobox.get()
            
            selected_year=int(self.selected_year_str)
            selected_month=int(self.selected_month_str)
            # カレンダーの日付を取得
            cal = calendar.monthcalendar(selected_year, selected_month)
            #print(cal)
            self.date_buttons=[]
            
            if self.date_buttons!=[]:
                for d in self.date_buttons:
                    d.destroy()
                self.date_buttons=[]
            
            # カレンダーの日付と祝日を表示
            for i,week in enumerate(cal):
                for j,day in enumerate(week):
                    if day!=0:
                        self.calendar_button=tkinter.Button(self.popup_window, text=f'{day:02}', bg='white',
                                                           command = lambda selected_day=day, selected_month=selected_month, selected_year=selected_year,i=int(i),j=int(j): self.add_selected_date(selected_day,selected_month,selected_year,i,j))
                        self.calendar_button.place(x = 10+int(j)*24, y = 70+int(i)*26)
                        self.date_buttons.append(self.calendar_button)


        def add_selected_date(self,selected_day,selected_month,selected_year,i,j):
            #print(selected_year)
            #print(selected_month)
            #print(selected_day)
            change_list=[]
            for k, button in enumerate(self.date_buttons):
                #print("------")
                #print(k)
                #print(i)
                #print(j)
                #print(i*7+j)
                #print(button)
                if k==selected_day-1 and button['bg']=='white':
                    button.configure(bg='aqua')
                    change_list.append(['add',selected_year,selected_month,selected_day])
                elif k==selected_day-1 and button['bg']=='aqua':
                    button.configure(bg='white')
                    change_list.append(['delete',selected_year,selected_month,selected_day])
                elif k!=selected_day-1 and button['bg']=='aqua':
                    button.configure(bg='aqua')
                else:
                    button.configure(bg='white')
            
            #print(change_list)
            for m, item in enumerate(change_list):
                if item[0]=='add':
                    #print(f'add {i} {j}')
                    list_selected_date.append([selected_year,selected_month,selected_day])
                else:
                    #print(f'delete {i} {j}')
                    for data in list_selected_date:
                        if data==[selected_year,selected_month,selected_day]:
                            list_selected_date.remove(data)
            print(list_selected_date)
            
            #list_selected_dateの整理と表示
            frame_selected_date=ttk.Frame(self.popup_window, width=180, height=190, borderwidth=5, relief = 'solid')
            frame_selected_date.place(x = 190, y = 45)
            if len(list_selected_date)>0:
                for index,data in enumerate(list_selected_date):
                    label_selected=ttk.Label(self.popup_window,text=data,font=('Arial','6'))
                    label_selected.place(x=200,y=50+int(index)*10)
            
        
        def close_calendar(self):
            self.popup_window.destroy()

    
    class A(Commons):
        def __init__(self, parent):
            titleLabel = tkinter.Label(parent, text = "tab_1",
                                            font = ("Times New Roman", "20", "bold italic"))
            titleLabel.place(x = 20, y = 10)
    
            frame_A1 = ttk.Frame(parent, width = 250, height = 65, borderwidth = 5, relief = 'solid')
            frame_A1.place(x = 15, y = 55)
            frame_A1 = ttk.Frame(parent, width = 250, height = 65, borderwidth = 5, relief = 'solid')
            frame_A1.place(x = 15, y = 125)
            frame_A1 = ttk.Frame(parent, width = 250, height = 65, borderwidth = 5, relief = 'solid')
            frame_A1.place(x = 15, y = 195)
            frame_A1 = ttk.Frame(parent, width = 250, height = 65, borderwidth = 5, relief = 'solid')
            frame_A1.place(x = 15, y = 265)
            frame_A1 = ttk.Frame(parent, width = 250, height = 65, borderwidth = 5, relief = 'solid')
            frame_A1.place(x = 15, y = 335)
            frame_A1 = ttk.Frame(parent, width = 250, height = 65, borderwidth = 5, relief = 'solid')
            frame_A1.place(x = 15, y = 405)
            frame_A1 = ttk.Frame(parent, width = 250, height = 45, borderwidth = 5, relief = 'solid')
            frame_A1.place(x = 15, y = 475)
            frame_A1 = ttk.Frame(parent, width = 250, height = 65, borderwidth = 5, relief = 'solid')
            frame_A1.place(x = 15, y = 525)
            
            Button_calendar = tkinter.Button(parent, text = "カレンダー", font = ("Arial", "10", "bold"),
                                                command = lambda : self.use_calendar(self))
            Button_calendar.place(x = 20, y = 60)
                   
            
            
            self.common_function()
            #self.common_function()
    
        def specific_function(self):
            print("A独自の関数")
    
    
    
    class B(Commons):
        def __init__(self, parent):
            label = tkinter.Label(parent, text="ここはタブ2です")
            label.pack()
            self.common_function()
    
        def specific_function(self):
            print("B独自の関数")
    
    
    
    class C(Commons):
        def __init__(self, parent):
            label = tkinter.Label(parent, text="ここはタブ3です")
            label.pack()
            self.common_function()
    
        def specific_function(self):
            print("C独自の関数")


app = App()
app.mainloop()


