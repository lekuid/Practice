#consideirng pre school and mursery, this specific code
#is to help me write a blog because I have terrible memory.
import tkinter as tk

def age(n):
    if n in range(0,4):
        returned['text'] = 'preschool'
    elif n in range(5, 17):
        returned['text'] = 'class {}'.format(n-4)
    elif n in range(17, 21):
        returned['text'] = 'college {}'.format(n-16) + 'year'

win= tk.Tk()
win.title('Which Education?')

base = tk.Canvas(win, height=100, width=400, bg='#181818')
base.pack()

main_frame = tk.Frame(base, bg='#181818')
main_frame.place(relwidth=0.5, relheight=1)

n = tk.Entry(main_frame, bg='#222222', fg='#999999', font=40)
n.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.25)

submit = tk.Button(main_frame, text='Enlighten Me', bg='#555555', fg='white', command = lambda: age(int(n.get())))
submit.place(relx=0.4, rely=0.6, relheight=0.2, relwidth=0.4)

returned = tk.Label(base, bg='#555555')
returned.place(relx=0.5, relheight=1, relwidth=0.5)

win.mainloop()