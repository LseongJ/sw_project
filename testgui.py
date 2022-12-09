from tkinter import *

window = Tk()
window.title('길이 변환 계산기')
label = Label(window, text="길이 변환 계산기")
label.pack()

b1 = Button(window, text='길이')
b1.pack(side = LEFT, padx=10)
b2 = Button(window, text='넓이')
b2.pack(side = LEFT, padx=10)
b3 = Button(window, text='무게')
b3.pack(side = LEFT, padx=10)
b4 = Button(window, text='부피')
b4.pack(side = LEFT, padx=10)
b5 = Button(window, text='온도')
b5.pack(side = LEFT, padx=10)
b6 = Button(window, text='속도')
b6.pack(side = LEFT, padx=10)

window.mainloop()