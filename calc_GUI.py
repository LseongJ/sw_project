from tkinter import *
from tkinter.ttk import *

tk = Tk()
tk.title("단위변환 계산기")
tk.geometry("650x300")

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
def reset():
    entry2.delete(0, "end")   
btn = Button(tk, text="결과 초기화", command= reset).grid(row=3,column=2) 
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
        def m2tokm2():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.000001, 4))
        btn = Button(tk, text="m^2->km^2", command=m2tokm2).grid(row=4,column=0)
        def m2top():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.3025, 4))
        btn = Button(tk, text="m^2->평", command=m2top).grid(row=5,column=0)
        #----------------------------------------------------------------------#
        def km2tom2():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1000000, 4))
        btn = Button(tk, text="km^2->m^2", command=km2tom2).grid(row=4,column=1)
        def km2top():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 302500, 4))
        btn = Button(tk, text="km^2->평", command=km2top).grid(row=5,column=1)
        #----------------------------------------------------------------------#
        def ptom2():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 3.305785, 4))
        btn = Button(tk, text="평->m^2", command=ptom2).grid(row=4,column=2)
        def ptokm2():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.0000033, 9))
        btn = Button(tk, text="평->km^2", command=ptokm2).grid(row=5,column=2)
    #----------------------------------------------------------------------#
    if combo.get() == "무게":
        def mg2g():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.001, 9))
        btn = Button(tk, text="mg->g", command=mg2g).grid(row=4,column=0)
        def mg2kg():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1e-6, 9))
        btn = Button(tk, text="mg->kg", command=mg2kg).grid(row=5,column=0)
        def mg2t():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 10e-10, 9))
        btn = Button(tk, text="mg->t", command=mg2t).grid(row=6,column=0)
        def mg2lb():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 2.2046e-6, 9))
        btn = Button(tk, text="mg->lb", command=mg2lb).grid(row=7,column=0)
        #----------------------------------------------------------------------#
        def g2mg():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1000, 9))
        btn = Button(tk, text="g->mg", command=g2mg).grid(row=4,column=1)
        def g2kg():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.001, 9))
        btn = Button(tk, text="g->kg", command=g2kg).grid(row=5,column=1)
        def g2t():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1e-6, 9))
        btn = Button(tk, text="g->t", command=g2t).grid(row=6,column=1)
        def g2lb():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.002205, 9))
        btn = Button(tk, text="g->lb", command=g2lb).grid(row=7,column=1)
        #----------------------------------------------------------------------#
        def kg2mg():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1000000, 5))
        btn = Button(tk, text="kg->mg", command=kg2mg).grid(row=4,column=2)
        def kg2g():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1000, 5))
        btn = Button(tk, text="kg->g", command=kg2g).grid(row=5,column=2)
        def kg2t():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.001, 5))
        btn = Button(tk, text="kg->t", command=kg2t).grid(row=6,column=2)
        def kg2lb():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 2.204623, 5))
        btn = Button(tk, text="kg->lb", command=kg2lb).grid(row=7,column=2)
        #----------------------------------------------------------------------#
        def t2mg():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1e+9, 9))
        btn = Button(tk, text="t->mg", command=t2mg).grid(row=4,column=3)
        def t2g():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1000000, 9))
        btn = Button(tk, text="t->g", command=t2g).grid(row=5,column=3)
        def t2kg():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1000, 9))
        btn = Button(tk, text="t->kg", command=t2kg).grid(row=6,column=3)
        def t2lb():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 2204.62262, 9))
        btn = Button(tk, text="t->lb", command=t2lb).grid(row=7,column=3)
        #----------------------------------------------------------------------#
        def lb2mg():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 453592.37, 9))
        btn = Button(tk, text="lb->mg", command=lb2mg).grid(row=4,column=4)
        def lb2g():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 453.59237, 9))
        btn = Button(tk, text="lb->g", command=lb2g).grid(row=5,column=4)
        def lb2kg():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.453592, 9))
        btn = Button(tk, text="lb->kg", command=lb2kg).grid(row=6,column=4)
        def lb2t():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.000454, 9))
        btn = Button(tk, text="lb->t", command=lb2t).grid(row=7,column=4)
    #----------------------------------------------------------------------#  
    if combo.get() == "부피":
        def ml2l():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.001, 9))
        btn = Button(tk, text="ml->l", command=ml2l).grid(row=4,column=0)
        #----------------------------------------------------------------------#
        def l2ml():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1000, 9))
        btn = Button(tk, text="l->ml", command=l2ml).grid(row=4,column=1)    
    #----------------------------------------------------------------------#
    if combo.get() == "온도":
        def k2c():
            x = entry1.get()
            entry2.insert(0, round(float(x) * -272.15, 9))
        btn = Button(tk, text="K->C", command=k2c).grid(row=4,column=0)
        def k2f():
            x = entry1.get()
            entry2.insert(0, round(float(x) * -457.87, 9))
        btn = Button(tk, text="K->F", command=k2f).grid(row=5,column=0)
        #----------------------------------------------------------------------#
        def ctk():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 274.15, 9))
        btn = Button(tk, text="C->K", command=ctk).grid(row=4,column=1)
        def c2f():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 33.8, 9))
        btn = Button(tk, text="C->F", command=c2f).grid(row=5,column=1)
        #----------------------------------------------------------------------#
        def f2c():
            x = entry1.get()
            entry2.insert(0, round(float(x) * -17.222222, 9))
        btn = Button(tk, text="F->C", command=f2c).grid(row=4,column=2)
        def f2k():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 255.927778, 9))
        btn = Button(tk, text="F->K", command=f2k).grid(row=5,column=2)
    #----------------------------------------------------------------------#    
    if combo.get() == "속도":
        def ms2kh():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 3.6, 9))
        btn = Button(tk, text="m/s->k/h", command=ms2kh).grid(row=4,column=0)
        def ms2kn():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1.943844, 9))
        btn = Button(tk, text="m/s->kn", command=ms2kn).grid(row=5,column=0)
        def ms2mach():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.002941, 9))
        btn = Button(tk, text="m/s->mach", command=ms2mach).grid(row=6,column=0)    
        #----------------------------------------------------------------------#
        def kh2ms():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.277778, 9))
        btn = Button(tk, text="k/h->m/s", command=kh2ms).grid(row=4,column=1)
        def kh2kn():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.539957, 9))
        btn = Button(tk, text="k/h->kn", command=kh2kn).grid(row=5,column=1)
        def kh2mach():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.000817, 9))
        btn = Button(tk, text="k/h->mach", command=kh2mach).grid(row=6,column=1)    
        #----------------------------------------------------------------------#
        def kn2ms():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.514444, 9))
        btn = Button(tk, text="kn->m/s", command=kn2ms).grid(row=4,column=2)
        def kn2kh():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1.852, 9))
        btn = Button(tk, text="kn->k/h", command=kn2kh).grid(row=5,column=2)
        def kn2mach():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 0.001513, 9))
        btn = Button(tk, text="kn->mach", command=kn2mach).grid(row=6,column=2)    
        #----------------------------------------------------------------------#
        def mach2ms():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 340, 9))
        btn = Button(tk, text="mach->m/s", command=mach2ms).grid(row=4,column=3)
        def mach2kh():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 1224, 9))
        btn = Button(tk, text="mach->k/h", command=mach2kh).grid(row=5,column=3)
        def mach2kn():
            x = entry1.get()
            entry2.insert(0, round(float(x) * 660.907127, 9))
        btn = Button(tk, text="mach->kn", command=mach2kn).grid(row=6,column=3)    
        #----------------------------------------------------------------------#
        
btn = Button(tk, text="선택", command=btnpress).grid(row=0,column=2)
#--------------------------------------------------------------------#


tk.mainloop()
