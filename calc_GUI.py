from tkinter import *
from tkinter.ttk import *

tk = Tk()
tk.title("테스트")
tk.geometry("700x300")

btn = Button(tk)

l1 = Label(tk, text="계산기 타입:").grid(row=0, column=0)
l2 = Label(tk, text="숫자:").grid(row=2, column=0)
l3 = Label(tk, text="결과:").grid(row=3, column=0)

entry1 = Entry()    #숫자
entry2 = Entry()    #결과
entry1.grid(row=2, column=1)
entry2.grid(row=3, column=1)

#---------------------------계산기 선택------------------------------#
combo = Combobox(tk)
combo['values'] = ("길이", "넓이", "무게", "부피", "온도", "속도")
combo.config(state="readonly")
combo.current(0)
combo.grid(column=1,row=0)
#-------------------------------------------------------------------#

def btnpress():
    Label(tk, text=combo.get()+"가 선택되었습니다").grid(column=3,row=0)
    if combo.get() == "길이":
        def mm2cm():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.1, 4))
        btn = Button(tk, text="mm->cm", command=mm2cm).grid(row=4,column=0)
        def mm2m():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.001, 4))
        btn = Button(tk, text="mm->m", command=mm2m).grid(row=5,column=0)
        def mm2km():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.000001, 4))
        btn = Button(tk, text="mm->km", command=mm2km).grid(row=6,column=0)
        def mm2ft():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.003281, 4))
        btn = Button(tk, text="mm->ft", command=mm2ft).grid(row=7,column=0)
        def mm2inch():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.03937, 4))
        btn = Button(tk, text="mm->inch", command=mm2inch).grid(row=8,column=0)
        #----------------------------------------------------------------------#
        def cm2mm():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 10, 4))
        btn = Button(tk, text="cm->mm", command=cm2mm).grid(row=4,column=1)
        def cm2m():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.01, 4))
        btn = Button(tk, text="cm->m", command=cm2m).grid(row=5,column=1)
        def cm2km():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.00001, 4))
        btn = Button(tk, text="cm->km", command=cm2km).grid(row=6,column=1)
        def cm2ft():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.032808, 4))
        btn = Button(tk, text="cm->ft", command=cm2ft).grid(row=7,column=1)
        def cm2inch():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.393701, 4))
        btn = Button(tk, text="cm->inch", command=cm2inch).grid(row=8,column=1)
        #----------------------------------------------------------------------#
        def m2mm():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1000, 4))
        btn = Button(tk, text="m->mm", command=m2mm).grid(row=4,column=2)
        def m2cm():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 100, 4))
        btn = Button(tk, text="m->cm", command=m2cm).grid(row=5,column=2)
        def m2km():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.001, 4))
        btn = Button(tk, text="m->km", command=m2km).grid(row=6,column=2)
        def m2ft():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 3.28084, 4))
        btn = Button(tk, text="m->ft", command=m2ft).grid(row=7,column=2)
        def m2inch():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 39.370079, 4))
        btn = Button(tk, text="m->inch", command=m2inch).grid(row=8,column=2)
        #----------------------------------------------------------------------#
        def km2mm():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1000000, 4))
        btn = Button(tk, text="km->mm", command=km2mm).grid(row=4,column=3)
        def km2cm():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 100000, 4))
        btn = Button(tk, text="km->cm", command=km2cm).grid(row=5,column=3)
        def km2m():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1000, 4))
        btn = Button(tk, text="km-km", command=km2m).grid(row=6,column=3)
        def km2ft():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 3280.8399, 4))
        btn = Button(tk, text="km->ft", command=km2ft).grid(row=7,column=3)
        def km2inch():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 39370.0787, 4))
        btn = Button(tk, text="km->inch", command=km2inch).grid(row=8,column=3)
        #----------------------------------------------------------------------#
        def ft2mm():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 304.8, 4))
        btn = Button(tk, text="ft->mm", command=ft2mm).grid(row=4,column=4)
        def ft2cm():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 30.48, 4))
        btn = Button(tk, text="ft->cm", command=ft2cm).grid(row=5,column=4)
        def ft2m():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.3048, 4))
        btn = Button(tk, text="ft->m", command=ft2m).grid(row=6,column=4)
        def ft2km():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.000305, 4))
        btn = Button(tk, text="ft->km", command=ft2km).grid(row=7,column=4)
        def ft2inch():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 12, 4))
        btn = Button(tk, text="ft->inch", command=ft2inch).grid(row=8,column=4)
        #----------------------------------------------------------------------#
        def inch2mm():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 304.8, 4))
        btn = Button(tk, text="inch->mm", command=inch2mm).grid(row=4,column=5)
        def inch2cm():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 30.48, 4))
        btn = Button(tk, text="inch->cm", command=inch2cm).grid(row=5,column=5)
        def inch2m():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.3048, 4))
        btn = Button(tk, text="inch->m", command=inch2m).grid(row=6,column=5)
        def inch2km():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.000305, 4))
        btn = Button(tk, text="inch->km", command=inch2km).grid(row=7,column=5)
        def inch2ft():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 12, 4))
        btn = Button(tk, text="inch->ft", command=inch2ft).grid(row=8,column=5)
    #----------------------------------------------------------------------#  
    if combo.get() == "넓이":
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
          
   
btn = Button(tk, text="선택", command=btnpress).grid(row=0,column=2)
#--------------------------------------------------------------------#


tk.mainloop()
