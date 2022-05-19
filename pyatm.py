import tkinter as tk                # python 3
current_balance=1000
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.shared_data={'Balance':tk.IntVar()}

       
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, depositpage, balancepage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        self.controller.title('ATM')
        self.controller.state('zoomed')
        headinglabel1=tk.Label(self,text='ATM MANAGEMENT',font=('orbitron',45,'bold'),fg='white',bg='#3d3d5c')
        headinglabel1.pack(pady=25)
        space_label=tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()
        passwd_label=tk.Label(self,text='ENTER YOUR PASSWORD',font=('orbitron',13),fg='white',bg='#3d3d5c')
        passwd_label.pack(ipadx=10)
        my_password=tk.StringVar()
        passwdentry=tk.Entry(self,textvariable=my_password,font=('orbitron',12),width=22)
        passwdentry.pack(ipady=7)
        def hd(_):
            passwdentry.configure(fg='black',show='*')
        passwdentry.bind('<FocusIn>',hd)
        def ck_pwd():
            if my_password.get() == '123':
                controller.show_frame('MenuPage')
                my_password.set('')
                incrpwd['text']=''
            else:
                incrpwd['text']='incorrect password'
            
        bttn=tk.Button(self,text='ENTER',command=ck_pwd,relief='raised',borderwidth=3,width=40,height=3)
        bttn.pack(pady=10)
        incrpwd=tk.Label(self,text='' ,font=('orbitron',13),fg='white',bg='#33334d',anchor='n')
                         
        incrpwd.pack(fill='both',expand=True)
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        headinglabel1=tk.Label(self,text=' ATM MANAGEMENT',font=('orbitron',45,'bold'),fg='white',bg='#3d3d5c')
        headinglabel1.pack(pady=25)
        menu_label=tk.Label(self,text='MAIN MENU',font=('orbitron',13),fg='white',bg='#3d3d5c')
        menu_label.pack()
        sel_label=tk.Label(self,text='PLEASE MAKE A SELECTION',font=('orbitron',13),fg='white',bg='#3d3d5c',anchor='w')
        sel_label.pack(fill='x')
        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)
        def withdraw():
            controller.show_frame('WithdrawPage')
        wd_button=tk.Button(button_frame,text='WITHDRAW',command=withdraw,relief='raised',borderwidth=3,width=50,height=5)
        wd_button.grid(row=0,column=0,pady=5)
        def deposit():
            controller.show_frame('depositpage')
        deposit_button=tk.Button(button_frame,text='DEPOSIT',command=deposit,relief='raised',borderwidth=3,width=50,height=5)
        deposit_button.grid(row=1,column=0,pady=5)
        def balance():
            controller.show_frame('balancepage')
        balance_button=tk.Button(button_frame,text='CHECKBALANCE',command=balance,relief='raised',borderwidth=3,width=50,height=5)
        balance_button.grid(row=2,column=0,pady=5)
        def exit1():
            controller.show_frame('StartPage')
        exit_button=tk.Button(button_frame,text='EXIT',command=exit1,relief='raised',borderwidth=3,width=50,height=5)
        exit_button.grid(row=3,column=0,pady=5)

class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        headinglabel1=tk.Label(self,text='ATM MANAGEMENT',font=('orbitron',45,'bold'),fg='white',bg='#3d3d5c')
        headinglabel1.pack(pady=25)
        choose_label=tk.Label(self,text='CHOOSE THE AMOUNT TO BE WITHDRAWN',font=('orbitron',13),fg='white',bg='#3d3d5c')
        choose_label.pack()
        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)
        def withdraw(amount):
            global current_balance
            current_balance-=amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
        twenty_button=tk.Button(button_frame,text='20',command=lambda:withdraw(20),relief='raised',borderwidth=3,width=50,height=5)
        twenty_button.grid(row=0,column=0,pady=5)
        forty_button=tk.Button(button_frame,text='40',command=lambda:withdraw(40),relief='raised',borderwidth=3,width=50,height=5)
        forty_button.grid(row=1,column=0,pady=5)
        sixty_button=tk.Button(button_frame,text='60',command=lambda:withdraw(60),relief='raised',borderwidth=3,width=50,height=5)
        sixty_button.grid(row=2,column=0,pady=5)
        eighty_button=tk.Button(button_frame,text='80',command=lambda:withdraw(80),relief='raised',borderwidth=3,width=50,height=5)
        eighty_button.grid(row=3,column=0,pady=5)
        hundred_button=tk.Button(button_frame,text='100',command=lambda:withdraw(100),relief='raised',borderwidth=3,width=50,height=5)
        hundred_button.grid(row=0,column=1,pady=5,padx=555)
        twohund_button=tk.Button(button_frame,text='200',command=lambda:withdraw(200),relief='raised',borderwidth=3,width=50,height=5)
        twohund_button.grid(row=1,column=1,pady=5)
        threehund_button=tk.Button(button_frame,text='300',command=lambda:withdraw(300),relief='raised',borderwidth=3,width=50,height=5)
        threehund_button.grid(row=2,column=1,pady=5)
        cash=tk.StringVar()
        other_amount=tk.Entry(button_frame,textvariable=cash,width=59,justify='right')
        other_amount.grid(row=3,column=1,pady=5,ipady=30)
        def other_am(_):
            global current_balance
            current_balance-=int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MenuPage')
        other_amount.bind('<Return>',other_am)
        
        
class depositpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        headinglabel1=tk.Label(self,text='ATM MANAGEMENT',font=('orbitron',45,'bold'),fg='white',bg='#3d3d5c')
        headinglabel1.pack(pady=25)
        space_label=tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()
        enam_label=tk.Label(self,text='ENTER THE AMOUNT',font=('orbitron',13),fg='white',bg='#3d3d5c')
        enam_label.pack(ipadx=10)
        cash=tk.StringVar()
        depositentry=tk.Entry(self,textvariable=cash,font='orbitron',width=22)
        depositentry.pack(ipady=7)
        def deposit_cash():
            global current_balance
            current_balance +=int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')
        enter_button=tk.Button(self,text='ENTER',command=deposit_cash,relief='raised',borderwidth=3,width=10,height=3)
        enter_button.pack(pady=10)
        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)
class balancepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        headinglabel1=tk.Label(self,text='ATM MANAGEMENT',font=('orbitron',45,'bold'),fg='white',bg='#3d3d5c')
        headinglabel1.pack(pady=25)
        space_label=tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        bl_lbel=tk.Label(self,textvariable=controller.shared_data['Balance'],font=('orbitron',13),fg='white',bg='#3d3d5c',anchor='w')
        bl_lbel.pack(fill='x')
        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)
        def menu():
            controller.show_frame('MenuPage')
        menu_btt=tk.Button(button_frame,command=menu,text='MENU',relief='raised',borderwidth=3,width=50,height=5)
        menu_btt.grid(row=0,column=0,pady=5)
        def exit_():
            controller.show_frame('StartPage')
        exit_btt=tk.Button(button_frame,command=exit_,text='EXIT',relief='raised',borderwidth=3,width=50,height=5)
        exit_btt.grid(row=1,column=0,pady=5)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
