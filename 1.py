from tkinter import *
window = Tk()
window.title("단위 변환 계산기")
window.geometry("500x300")

entry = Entry(window)
#----------------------------------------------------------#완
def MM2CM():
    mm2cm = entry.get()
    entry.insert(0, round(float(mm2cm) * 0.1, 4))
btn = Button(window, text='mm->cm', bg='black', fg='white', command=MM2CM).grid(row=6,column=0)
label1 = Label(window, text='number:').grid(row=0,column=0)
entry.grid(row=0,column=1)

def MM2M():
    mm2m = entry.get()
    entry.insert(0, round(float(mm2m) * 0.001, 4))
btn = Button(window, text='mm->m', bg='black', fg='white', command=MM2M).grid(row=7,column=0)

def MM2KM():
    mm2km = entry.get()
    entry.insert(0, round(float(mm2km) * 0.000001, 4))
btn = Button(window, text='mm->km', bg='black', fg='white', command=MM2KM).grid(row=8,column=0)

def MM2FT():
    mm2ft = entry.get()
    entry.insert(0, round(float(mm2ft) * 0.003281, 4))
btn = Button(window, text='mm->ft', bg='black', fg='white', command=MM2FT).grid(row=9,column=0)

def MM2INCH():
    mm2inch = entry.get()
    entry.insert(0, round(float(mm2inch) * 0.03937, 4))
btn = Button(window, text='mm->inch', bg='black', fg='white', command=MM2INCH).grid(row=10,column=0)
#----------------------------------------------------------#완
def M2MM():
    m2mm = entry.get()
    entry.insert(0, round(float(m2mm) * 1000, 4))
btn = Button(window, text='cm->mm', bg='black', fg='white', command=M2MM).grid(row=6,column=1)

def M2CM():
    m2cm = entry.get()
    entry.insert(0, round(float(m2cm) * 100, 4))
btn = Button(window, text='cm->m', bg='black', fg='white', command=M2CM).grid(row=7,column=1)

def M2KM():
    m2km = entry.get()
    entry.insert(0, round(float(m2km) * 0.001, 4))
btn = Button(window, text='cm->km', bg='black', fg='white', command=M2KM).grid(row=8,column=1)

def M2FT():
    m2ft = entry.get()
    entry.insert(0, round(float(m2ft) * 3.28084, 4))
btn = Button(window, text='cm->ft', bg='black', fg='white', command=M2FT).grid(row=9,column=1)

def M2INCH():
    m2inch = entry.get()
    entry.insert(0, round(float(m2inch) * 39.370079, 4))
btn = Button(window, text='cm->inch', bg='black', fg='white', command=M2INCH).grid(row=10,column=1)
#----------------------------------------------------------#

















window.mainloop()


