import tkinter as tk

class GUI:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("210x40")
        self.interface()

    #创建按钮、输入框、捆绑按键
    def interface(self):
        self.entry=tk.Entry(self.root,width=20)
        self.entry.grid(row=0,column=0,columnspan=9,ipady=4)

        self.entry.bind("<Return>",lambda event:self.colculate())

        self.Button0=tk.Button(self.root,text="清空/Shift",command=self.clean)
        self.Button0.grid(row=0,column=10,ipady=1)

        self.Button0.bind("<Shift_L><Shift_R>",lambda event:self.clean())

    #计算
    def calculate(self,event=None):
        cal=self.entry.get()
        self.entry.delete(0,tk.END)
        self.entry.insert(0,eval(cal))

    #清空输入框
    def clean(self):
        self.entry.delete(0,tk.END)

if __name__=="__main__":
    a=GUI()
    a.root.mainloop()