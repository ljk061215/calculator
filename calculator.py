import tkinter as tk

class GUI:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("490x590")
        self.interface()

    #创建按钮、输入框、捆绑按键
    def interface(self):
        self.entry=tk.Entry(self.root,width=60,font=('Arial',11))
        self.entry.grid(row=0,column=0,columnspan=4,ipady=10)
        
        button=[
            ["绝对值","清空/Shift","撤回/back","/"],
            ["7","8","9","*"],
            ["4","5","6","-"],
            ["1","2","3","+"],
            ["00","0",".","=/enter"]
            ]
        
        for i in range(len(button)):
            for j in range(len(button[i])):
                text=button[i][j]
                btn=tk.Button(self.root,text=text,width=8,height=3,font=("Arial",16),command=lambda t=text:self.add_to_entry(t))
                btn.grid(row=i+1,column=j,padx=5,pady=5)

        self.entry.bind("<Return>",lambda event:self.calculate())
        self.entry.bind("<Alt_L>",lambda event:self.clean())
        self.entry.bind("<Shift_R>",lambda event:self.abs())

    def add_to_entry(self,text):
        if text=="=/enter":
            self.calculate()
        elif text=="清空/Shift":
            self.clean()
        elif text=="绝对值":
            self.abs()
        elif text=="撤回/back":
            self.back()
        else:
            self.entry.insert(tk.END,text)

    #计算
    def calculate(self,event=None):
        cal=self.entry.get()
        self.entry.delete(0,tk.END)
        self.entry.insert(0,eval(cal))

    #清空输入框
    def clean(self):
        self.entry.delete(0,tk.END)

    #绝对值
    def abs(self):
        cal=self.entry.get()
        self.entry.delete(0,tk.END)
        self.entry.insert(0,abs(eval(cal)))

    def back(self):
        cal=self.entry.get()
        self.entry.delete(0,tk.END)
        self.entry.insert(0,cal[:-1])

if __name__=="__main__":
    a=GUI()
    a.root.mainloop()

