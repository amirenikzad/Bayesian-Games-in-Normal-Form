import tkinter as tk
from PIL import Image, ImageTk 

def necal(entry1,entry2,nat):
    result = float(nat) * float(entry1) + (1 - float(nat)) * float(entry2)
    return round(result, 2)

def update_row():
    na1=nature1.get()
    na2=nature2.get()
    na3=nature3.get()
    na4=nature4.get()
    LaYR1.config(text=f"{necal( int(A1.get() ) , int(B1.get() ) ,na1)}")
    LaYR2.config(text=f"{necal( int(A1.get() ) , int(B3.get() ) ,na1)}")
    LaYR3.config(text=f"{necal( int(A3.get() ) , int(B1.get() ) ,na1)}")
    LaYR4.config(text=f"{necal( int(A3.get() ) , int(B3.get() ) ,na1)}")
    LaYR5.config(text=f"{necal( int(A5.get() ) , int(B5.get() ) ,na1)}")
    LaYR6.config(text=f"{necal( int(A5.get() ) , int(B7.get() ) ,na1)}")
    LaYR7.config(text=f"{necal( int(A7.get() ) , int(B5.get() ) ,na1)}")
    LaYR8.config(text=f"{necal( int(A7.get() ) , int(B7.get() ) ,na1)}")

    LaNR1.config(text=f"{necal( int(C1.get() ) , int(D1.get() ) ,na2)}")
    LaNR2.config(text=f"{necal( int(C1.get() ) , int(D3.get() ) ,na2)}")
    LaNR3.config(text=f"{necal( int(C3.get() ) , int(D1.get() ) ,na2)}")
    LaNR4.config(text=f"{necal( int(C3.get() ) , int(D3.get() ) ,na2)}")
    LaNR5.config(text=f"{necal( int(C5.get() ) , int(D5.get() ) ,na2)}")
    LaNR6.config(text=f"{necal( int(C5.get() ) , int(D7.get() ) ,na2)}")
    LaNR7.config(text=f"{necal( int(C7.get() ) , int(D5.get() ) ,na2)}")
    LaNR8.config(text=f"{necal( int(C7.get() ) , int(D7.get() ) ,na2)}")

    LaYC1.config(text=f"{necal( int(A2.get() ) , int(C2.get() ) ,na3)}")
    LaYC2.config(text=f"{necal( int(A4.get() ) , int(C4.get() ) ,na3)}")
    LaYC3.config(text=f"{necal( int(A2.get() ) , int(C6.get() ) ,na3)}")
    LaYC4.config(text=f"{necal( int(A4.get() ) , int(C8.get() ) ,na3)}")
    LaYC5.config(text=f"{necal( int(A6.get() ) , int(C2.get() ) ,na3)}")
    LaYC6.config(text=f"{necal( int(A8.get() ) , int(C4.get() ) ,na3)}")
    LaYC7.config(text=f"{necal( int(A6.get() ) , int(C6.get() ) ,na3)}")
    LaYC8.config(text=f"{necal( int(A8.get() ) , int(C8.get() ) ,na3)}")

    LaNC1.config(text=f"{necal( int(B2.get() ) , int(D2.get() ) ,na4)}")
    LaNC2.config(text=f"{necal( int(B4.get() ) , int(D4.get() ) ,na4)}")
    LaNC3.config(text=f"{necal( int(B2.get() ) , int(D6.get() ) ,na4)}")
    LaNC4.config(text=f"{necal( int(B4.get() ) , int(D8.get() ) ,na4)}")
    LaNC5.config(text=f"{necal( int(B6.get() ) , int(D2.get() ) ,na4)}")
    LaNC6.config(text=f"{necal( int(B8.get() ) , int(D4.get() ) ,na4)}")
    LaNC7.config(text=f"{necal( int(B6.get() ) , int(D6.get() ) ,na4)}")
    LaNC8.config(text=f"{necal( int(B8.get() ) , int(D8.get() ) ,na4)}")

def draw_separator(canvas, x, y, length, orientation):
    if orientation == "horizontal":
        canvas.create_line(x, y, x + length, y, width=8)
    elif orientation == "vertical":
        canvas.create_line(x, y, x, y + length, width=8)

window = tk.Tk()
window.title("Bayesian Games in Normal Form Amir H Nikzad")
window.geometry("1100x550")

im = Image.open('car.jpg')
im = im.resize((1366, 768))
tk_im = ImageTk.PhotoImage(im)
label = tk.Label(window, image=tk_im)
label.place(x=-270 , y=-208)
#------------------------------------------------------------t1
col=45
rownum =60
pixel =25

font_size = 15
table_width = 6

canvas = tk.Canvas(window, width=table_width * 40 -65, height=5 * pixel-30)
canvas.place(x=rownum + 2 * pixel, y=col + pixel / 2)

for i in range(1, 4):
    draw_separator(canvas, 0, i * pixel*1.8-37, table_width * 29 , "horizontal")

for i in range(0, 3):
    draw_separator(canvas, i * 3.5 * pixel, 0, 4 * pixel , "vertical")

p2 = tk.Label(window, text="p2", font=("Helvetica", font_size))
p2.place(x=rownum+5*pixel, y=col-1.5*pixel)

B2 = tk.Label(window, text="B2", font=("Helvetica", font_size))
B2.place(x=rownum+3*pixel, y=col-pixel//2)

S2 = tk.Label(window, text="S2", font=("Helvetica", font_size))
S2.place(x=rownum+7*pixel, y=col-pixel//2)

p1 = tk.Label(window, text="p1", font=("Helvetica", font_size))
p1.place(x=rownum-0.75*pixel, y=col+1.5*pixel)

B1 = tk.Label(window, text="B1", font=("Helvetica", font_size))
B1.place(x=rownum+pixel//2, y=col+1*pixel)

S1 = tk.Label(window, text="S1", font=("Helvetica", font_size))
S1.place(x=rownum+pixel//2, y=col+3*pixel)

A1 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
A1.insert(0, "2")
A1.place_configure(width=30, height=30)
A1.place(x=rownum+2*pixel, y=col+1*pixel)
A1.bind("<FocusOut>", lambda event: update_row())

A2 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
A2.insert(0, "1")
A2.place_configure(width=30, height=30)
A2.place(x=rownum+3.5*pixel, y=col+1*pixel)
A2.bind("<FocusOut>", lambda event: update_row())

A3 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
A3.insert(0, "0")
A3.place_configure(width=30, height=30)
A3.place(x=rownum+6*pixel, y=col+1*pixel)
A3.bind("<FocusOut>", lambda event: update_row())

A4 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
A4.insert(0, "0")
A4.place_configure(width=30, height=30)
A4.place(x=rownum+7.5*pixel, y=col+1*pixel)
A4.bind("<FocusOut>", lambda event: update_row())

A5 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
A5.insert(0, "0")
A5.place_configure(width=30, height=30)
A5.place(x=rownum+2*pixel, y=col+3*pixel)
A5.bind("<FocusOut>", lambda event: update_row())

A6 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
A6.insert(0, "0")
A6.place_configure(width=30, height=30)
A6.place(x=rownum+3.5*pixel, y=col+3*pixel)
A6.bind("<FocusOut>", lambda event: update_row())

A7 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
A7.insert(0, "1")
A7.place_configure(width=30, height=30)
A7.place(x=rownum+6*pixel, y=col+3*pixel)
A7.bind("<FocusOut>", lambda event: update_row())

A8 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
A8.insert(0, "2")
A8.place_configure(width=30, height=30)
A8.place(x=rownum+7.5*pixel, y=col+3*pixel)
A8.bind("<FocusOut>", lambda event: update_row())
#-------------------------------------------------------t2
col=45
rownum =360

canvas = tk.Canvas(window, width=table_width * 40 -65, height=5 * pixel-30)
canvas.place(x=rownum + 2 * pixel, y=col + pixel / 2)

for i in range(1, 4):
    draw_separator(canvas, 0, i * pixel*1.8-37, table_width * 29 , "horizontal")

for i in range(0, 3):
    draw_separator(canvas, i * 3.5 * pixel, 0, 4 * pixel , "vertical")

p2 = tk.Label(window, text="p2", font=("Helvetica", font_size))
p2.place(x=rownum+5*pixel, y=col-1.5*pixel)

B2 = tk.Label(window, text="B2", font=("Helvetica", font_size))
B2.place(x=rownum+3*pixel, y=col-pixel//2)

S2 = tk.Label(window, text="S2", font=("Helvetica", font_size))
S2.place(x=rownum+7*pixel, y=col-pixel//2)

p1 = tk.Label(window, text="p1", font=("Helvetica", font_size))
p1.place(x=rownum-0.75*pixel, y=col+1.5*pixel)

B1 = tk.Label(window, text="B1", font=("Helvetica", font_size))
B1.place(x=rownum+pixel//2, y=col+1*pixel)

S1 = tk.Label(window, text="S1", font=("Helvetica", font_size))
S1.place(x=rownum+pixel//2, y=col+3*pixel)

B1 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
B1.insert(0, "2")
B1.place_configure(width=30, height=30)
B1.place(x=rownum+2*pixel, y=col+1*pixel)
B1.bind("<FocusOut>", lambda event: update_row())

B2 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
B2.insert(0, "0")
B2.place_configure(width=30, height=30)
B2.place(x=rownum+3.5*pixel, y=col+1*pixel)
B2.bind("<FocusOut>", lambda event: update_row())

B3 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
B3.insert(0, "0")
B3.place_configure(width=30, height=30)
B3.place(x=rownum+6*pixel, y=col+1*pixel)
B3.bind("<FocusOut>", lambda event: update_row())

B4 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
B4.insert(0, "2")
B4.place_configure(width=30, height=30)
B4.place(x=rownum+7.5*pixel, y=col+1*pixel)
B4.bind("<FocusOut>", lambda event: update_row())

B5 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
B5.insert(0, "0")
B5.place_configure(width=30, height=30)
B5.place(x=rownum+2*pixel, y=col+3*pixel)
B5.bind("<FocusOut>", lambda event: update_row())

B6 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
B6.insert(0, "1")
B6.place_configure(width=30, height=30)
B6.place(x=rownum+3.5*pixel, y=col+3*pixel)
B6.bind("<FocusOut>", lambda event: update_row())

B7 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
B7.insert(0, "1")
B7.place_configure(width=30, height=30)
B7.place(x=rownum+6*pixel, y=col+3*pixel)
B7.bind("<FocusOut>", lambda event: update_row())

B8 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
B8.insert(0, "0")
B8.place_configure(width=30, height=30)
B8.place(x=rownum+7.5*pixel, y=col+3*pixel)
B8.bind("<FocusOut>", lambda event: update_row())
#------------------------------------------------------------t3
col=200
rownum =60

canvas = tk.Canvas(window, width=table_width * 40 -65, height=5 * pixel-30)
canvas.place(x=rownum + 2 * pixel, y=col + pixel / 2)

for i in range(1, 4):
    draw_separator(canvas, 0, i * pixel*1.8-37, table_width * 29 , "horizontal")

for i in range(0, 3):
    draw_separator(canvas, i * 3.5 * pixel, 0, 4 * pixel , "vertical")

p2 = tk.Label(window, text="p2", font=("Helvetica", font_size))
p2.place(x=rownum+5*pixel, y=col-1.5*pixel)

B2 = tk.Label(window, text="B2", font=("Helvetica", font_size))
B2.place(x=rownum+3*pixel, y=col-pixel//2)

S2 = tk.Label(window, text="S2", font=("Helvetica", font_size))
S2.place(x=rownum+7*pixel, y=col-pixel//2)

p1 = tk.Label(window, text="p1", font=("Helvetica", font_size))
p1.place(x=rownum-0.75*pixel, y=col+1.5*pixel)

B1 = tk.Label(window, text="B1", font=("Helvetica", font_size))
B1.place(x=rownum+pixel//2, y=col+1*pixel)

S1 = tk.Label(window, text="S1", font=("Helvetica", font_size))
S1.place(x=rownum+pixel//2, y=col+3*pixel)

C1 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
C1.insert(0, "0")
C1.place_configure(width=30, height=30)
C1.place(x=rownum+2*pixel, y=col+1*pixel)
C1.bind("<FocusOut>", lambda event: update_row())

C2 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
C2.insert(0, "1")
C2.place_configure(width=30, height=30)
C2.place(x=rownum+3.5*pixel, y=col+1*pixel)
C2.bind("<FocusOut>", lambda event: update_row())

C3 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
C3.insert(0, "2")
C3.place_configure(width=30, height=30)
C3.place(x=rownum+6*pixel, y=col+1*pixel)
C3.bind("<FocusOut>", lambda event: update_row())

C4 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
C4.insert(0, "0")
C4.place_configure(width=30, height=30)
C4.place(x=rownum+7.5*pixel, y=col+1*pixel)
C4.bind("<FocusOut>", lambda event: update_row())

C5 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
C5.insert(0, "1")
C5.place_configure(width=30, height=30)
C5.place(x=rownum+2*pixel, y=col+3*pixel)
C5.bind("<FocusOut>", lambda event: update_row())

C6 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
C6.insert(0, "0")
C6.place_configure(width=30, height=30)
C6.place(x=rownum+3.5*pixel, y=col+3*pixel)
C6.bind("<FocusOut>", lambda event: update_row())

C7 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
C7.insert(0, "0")
C7.place_configure(width=30, height=30)
C7.place(x=rownum+6*pixel, y=col+3*pixel)
C7.bind("<FocusOut>", lambda event: update_row())

C8 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
C8.insert(0, "2")
C8.place_configure(width=30, height=30)
C8.place(x=rownum+7.5*pixel, y=col+3*pixel)
C8.bind("<FocusOut>", lambda event: update_row())
#-------------------------------------------------------t4
col=200
rownum =360

canvas = tk.Canvas(window, width=table_width * 40 -65, height=5 * pixel-30)
canvas.place(x=rownum + 2 * pixel, y=col + pixel / 2)

for i in range(1, 4):
    draw_separator(canvas, 0, i * pixel*1.8-37, table_width * 29 , "horizontal")

for i in range(0, 3):
    draw_separator(canvas, i * 3.5 * pixel, 0, 4 * pixel , "vertical")

p2 = tk.Label(window, text="p2", font=("Helvetica", font_size))
p2.place(x=rownum+5*pixel, y=col-1.5*pixel)

B2 = tk.Label(window, text="B2", font=("Helvetica", font_size))
B2.place(x=rownum+3*pixel, y=col-pixel//2)

S2 = tk.Label(window, text="S2", font=("Helvetica", font_size))
S2.place(x=rownum+7*pixel, y=col-pixel//2)

p1 = tk.Label(window, text="p1", font=("Helvetica", font_size))
p1.place(x=rownum-0.75*pixel, y=col+1.5*pixel)

B1 = tk.Label(window, text="B1", font=("Helvetica", font_size))
B1.place(x=rownum+pixel//2, y=col+1*pixel)

S1 = tk.Label(window, text="S1", font=("Helvetica", font_size))
S1.place(x=rownum+pixel//2, y=col+3*pixel)

D1 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
D1.insert(0, "0")
D1.place_configure(width=30, height=30)
D1.place(x=rownum+2*pixel, y=col+1*pixel)
D1.bind("<FocusOut>", lambda event: update_row())

D2 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
D2.insert(0, "0")
D2.place_configure(width=30, height=30)
D2.place(x=rownum+3.5*pixel, y=col+1*pixel)
D2.bind("<FocusOut>", lambda event: update_row())

D3 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
D3.insert(0, "2")
D3.place_configure(width=30, height=30)
D3.place(x=rownum+6*pixel, y=col+1*pixel)
D3.bind("<FocusOut>", lambda event: update_row())

D4 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
D4.insert(0, "2")
D4.place_configure(width=30, height=30)
D4.place(x=rownum+7.5*pixel, y=col+1*pixel)
D4.bind("<FocusOut>", lambda event: update_row())

D5 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
D5.insert(0, "1")
D5.place_configure(width=30, height=30)
D5.place(x=rownum+2*pixel, y=col+3*pixel)
D5.bind("<FocusOut>", lambda event: update_row())

D6 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
D6.insert(0, "1")
D6.place_configure(width=30, height=30)
D6.place(x=rownum+3.5*pixel, y=col+3*pixel)
D6.bind("<FocusOut>", lambda event: update_row())

D7 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
D7.insert(0, "0")
D7.place_configure(width=30, height=30)
D7.place(x=rownum+6*pixel, y=col+3*pixel)
D7.bind("<FocusOut>", lambda event: update_row())

D8 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
D8.insert(0, "0")
D8.place_configure(width=30, height=30)
D8.place(x=rownum+7.5*pixel, y=col+3*pixel)
D8.bind("<FocusOut>", lambda event: update_row())
#-------------------------------------------------------y1
col=380
rownum =5

canvas = tk.Canvas(window, width=table_width * 40 +10, height=5 * pixel-30)
canvas.place(x=rownum + 2 * pixel, y=col + pixel / 2)

for i in range(1, 4):
    draw_separator(canvas, 0, i * pixel*1.8-37, table_width * 43 , "horizontal")

for i in range(0, 5):
    draw_separator(canvas, i * 2.5 * pixel, 0, 4 * pixel , "vertical")

p1 = tk.Label(window, text="y1", font=("Helvetica", font_size))
p1.place(x=rownum+0.5*pixel, y=col-0.75*pixel)

l1 = tk.Label(window, text="(B,B)", font=("Helvetica", font_size))
l1.place(x=rownum+3*pixel-20, y=col-pixel//2)

l2 = tk.Label(window, text="(B,S)", font=("Helvetica", font_size))
l2.place(x=rownum+5*pixel-10, y=col-pixel//2)

l3 = tk.Label(window, text="(S,B)", font=("Helvetica", font_size))
l3.place(x=rownum+7*pixel+5, y=col-pixel//2)

l4 = tk.Label(window, text="(S,S)", font=("Helvetica", font_size))
l4.place(x=rownum+9*pixel+20, y=col-pixel//2)

B1 = tk.Label(window, text="B", font=("Helvetica", font_size))
B1.place(x=rownum+pixel//2, y=col+1*pixel)

S1 = tk.Label(window, text="S", font=("Helvetica", font_size))
S1.place(x=rownum+pixel//2, y=col+3*pixel)

LaYR1 = tk.Label(window, text=f"2", font=("Helvetica", font_size))
LaYR1.place(x=rownum+2.5*pixel, y=col+1*pixel)

LaYR2 = tk.Label(window, text=f"1", font=("Helvetica", font_size))
LaYR2.place(x=rownum+5*pixel, y=col+1*pixel)

LaYR3 = tk.Label(window, text=f"1", font=("Helvetica", font_size))
LaYR3.place(x=rownum+8*pixel, y=col+1*pixel)

LaYR4 = tk.Label(window, text=f"0", font=("Helvetica", font_size))
LaYR4.place(x=rownum+10.5*pixel, y=col+1*pixel)

LaYR5 = tk.Label(window, text=f"0", font=("Helvetica", font_size))
LaYR5.place(x=rownum+2.5*pixel, y=col+3*pixel)

LaYR6 = tk.Label(window, text=f"0.5", font=("Helvetica", font_size))
LaYR6.place(x=rownum+5*pixel, y=col+3*pixel)

LaYR7 = tk.Label(window, text=f"0.5", font=("Helvetica", font_size))
LaYR7.place(x=rownum+8*pixel, y=col+3*pixel)

LaYR8 = tk.Label(window, text=f"1", font=("Helvetica", font_size))
LaYR8.place(x=rownum+10.5*pixel, y=col+3*pixel)
#-------------------------------------------------------n1
col=380
rownum =330

canvas = tk.Canvas(window, width=table_width * 40 +10, height=5 * pixel-30)
canvas.place(x=rownum + 2 * pixel, y=col + pixel / 2)         

for i in range(1, 4):
    draw_separator(canvas, 0, i * pixel*1.8-37, table_width * 43 , "horizontal")

for i in range(0, 5):
    draw_separator(canvas, i * 2.5 * pixel, 0, 4 * pixel , "vertical")

p1 = tk.Label(window, text="n1", font=("Helvetica", font_size))
p1.place(x=rownum+0.5*pixel, y=col-0.75*pixel)

l1 = tk.Label(window, text="(B,B)", font=("Helvetica", font_size))
l1.place(x=rownum+3*pixel-20, y=col-pixel//2)

l2 = tk.Label(window, text="(B,S)", font=("Helvetica", font_size))
l2.place(x=rownum+5*pixel-10, y=col-pixel//2)

l3 = tk.Label(window, text="(S,B)", font=("Helvetica", font_size))
l3.place(x=rownum+7*pixel+5, y=col-pixel//2)

l4 = tk.Label(window, text="(S,S)", font=("Helvetica", font_size))
l4.place(x=rownum+9*pixel+20, y=col-pixel//2)

B1 = tk.Label(window, text="B", font=("Helvetica", font_size))
B1.place(x=rownum+pixel//2, y=col+1*pixel)

S1 = tk.Label(window, text="S", font=("Helvetica", font_size))
S1.place(x=rownum+pixel//2, y=col+3*pixel)

LaNR1 = tk.Label(window, text=f"0", font=("Helvetica", font_size))
LaNR1.place(x=rownum+2.5*pixel, y=col+1*pixel)

LaNR2 = tk.Label(window, text=f"1", font=("Helvetica", font_size))
LaNR2.place(x=rownum+5*pixel, y=col+1*pixel)

LaNR3 = tk.Label(window, text=f"1", font=("Helvetica", font_size))
LaNR3.place(x=rownum+8*pixel, y=col+1*pixel)

LaNR4 = tk.Label(window, text=f"2", font=("Helvetica", font_size))
LaNR4.place(x=rownum+10.5*pixel, y=col+1*pixel)

LaNR5 = tk.Label(window, text=f"1", font=("Helvetica", font_size))
LaNR5.place(x=rownum+2.5*pixel, y=col+3*pixel)

LaNR6 = tk.Label(window, text=f"0.5", font=("Helvetica", font_size))
LaNR6.place(x=rownum+5*pixel, y=col+3*pixel)

LaNR7 = tk.Label(window, text=f"0.5", font=("Helvetica", font_size))
LaNR7.place(x=rownum+8*pixel, y=col+3*pixel)

LaNR8 = tk.Label(window, text=f"0", font=("Helvetica", font_size))
LaNR8.place(x=rownum+10.5*pixel, y=col+3*pixel)
#-------------------------------------------------------y2
col=260
rownum =660

canvas = tk.Canvas(window, width=table_width * 40 -113, height=7 * pixel+15)
canvas.place(x=rownum + 2 * pixel, y=col + pixel / 2)

for i in range(1, 7):
    draw_separator(canvas, 0, i * pixel*1.8-37, table_width * 20 , "horizontal")

for i in range(0, 3):
    draw_separator(canvas, i * 2.5 * pixel, 0, 8 * pixel , "vertical")

p1 = tk.Label(window, text="y2", font=("Helvetica", font_size))
p1.place(x=rownum+0.25*pixel, y=col-pixel)

l1 = tk.Label(window, text="(B,B)", font=("Helvetica", font_size))
l1.place(x=rownum+pixel//2-15, y=col+1*pixel)

l2 = tk.Label(window, text="(B,S)", font=("Helvetica", font_size))
l2.place(x=rownum+pixel//2-15, y=col+3*pixel)

l3 = tk.Label(window, text="(S,B)", font=("Helvetica", font_size))
l3.place(x=rownum+pixel//2-15, y=col+5*pixel)

l4 = tk.Label(window, text="(S,S)", font=("Helvetica", font_size))
l4.place(x=rownum+pixel//2-15, y=col+7*pixel)

B1 = tk.Label(window, text="B", font=("Helvetica", font_size))
B1.place(x=rownum+3*pixel-10, y=col-pixel//2)

S1 = tk.Label(window, text="S", font=("Helvetica", font_size))
S1.place(x=rownum+5*pixel, y=col-pixel//2)

LaYC1 = tk.Label(window, text=f"1", font=("Helvetica", font_size))
LaYC1.place(x=rownum+2.5*pixel, y=col+1*pixel)

LaYC2 = tk.Label(window, text=f"0", font=("Helvetica", font_size))
LaYC2.place(x=rownum+5*pixel, y=col+1*pixel)

LaYC3 = tk.Label(window, text=f"0.66", font=("Helvetica", font_size))
LaYC3.place(x=rownum+2.5*pixel, y=col+3*pixel)

LaYC4 = tk.Label(window, text=f"0.66", font=("Helvetica", font_size))
LaYC4.place(x=rownum+5*pixel, y=col+3*pixel)

LaYC5 = tk.Label(window, text=f"0.33", font=("Helvetica", font_size))
LaYC5.place(x=rownum+2.5*pixel, y=col+4.75*pixel)

LaYC6 = tk.Label(window, text=f"1.33", font=("Helvetica", font_size))
LaYC6.place(x=rownum+5*pixel, y=col+4.75*pixel)

LaYC7 = tk.Label(window, text=f"0", font=("Helvetica", font_size))
LaYC7.place(x=rownum+2.5*pixel, y=col+7*pixel-10)

LaYC8 = tk.Label(window, text=f"2", font=("Helvetica", font_size))
LaYC8.place(x=rownum+5*pixel, y=col+7*pixel-10)
#---------------------------------n2
col=260
rownum =870

canvas = tk.Canvas(window, width=table_width * 40 -113, height=7 * pixel+15)
canvas.place(x=rownum + 2 * pixel, y=col + pixel / 2)

for i in range(1, 7):
    draw_separator(canvas, 0, i * pixel*1.8-37, table_width * 20 , "horizontal")

for i in range(0, 3):
    draw_separator(canvas, i * 2.5 * pixel, 0, 8 * pixel , "vertical")

p1 = tk.Label(window, text="n2", font=("Helvetica", font_size))
p1.place(x=rownum+0.25*pixel, y=col-pixel)

l1 = tk.Label(window, text="(B,B)", font=("Helvetica", font_size))
l1.place(x=rownum+pixel//2-15, y=col+1*pixel)

l2 = tk.Label(window, text="(B,S)", font=("Helvetica", font_size))
l2.place(x=rownum+pixel//2-15, y=col+3*pixel)

l3 = tk.Label(window, text="(S,B)", font=("Helvetica", font_size))
l3.place(x=rownum+pixel//2-15, y=col+5*pixel)

l4 = tk.Label(window, text="(S,S)", font=("Helvetica", font_size))
l4.place(x=rownum+pixel//2-15, y=col+7*pixel)

B1 = tk.Label(window, text="B", font=("Helvetica", font_size))
B1.place(x=rownum+3*pixel-10, y=col-pixel//2)

S1 = tk.Label(window, text="S", font=("Helvetica", font_size))
S1.place(x=rownum+5*pixel, y=col-pixel//2)

LaNC1 = tk.Label(window, text=f"0", font=("Helvetica", font_size))
LaNC1.place(x=rownum+2.5*pixel, y=col+1*pixel)

LaNC2 = tk.Label(window, text=f"2", font=("Helvetica", font_size))
LaNC2.place(x=rownum+5*pixel, y=col+1*pixel)

LaNC3 = tk.Label(window, text=f"0.33", font=("Helvetica", font_size))
LaNC3.place(x=rownum+2.5*pixel, y=col+3*pixel)

LaNC4 = tk.Label(window, text=f"1.33", font=("Helvetica", font_size))
LaNC4.place(x=rownum+5*pixel, y=col+3*pixel)

LaNC5 = tk.Label(window, text=f"0.66", font=("Helvetica", font_size))
LaNC5.place(x=rownum+2.5*pixel, y=col+4.75*pixel)

LaNC6 = tk.Label(window, text=f"0.66", font=("Helvetica", font_size))
LaNC6.place(x=rownum+5*pixel, y=col+4.75*pixel)

LaNC7 = tk.Label(window, text=f"1", font=("Helvetica", font_size))
LaNC7.place(x=rownum+2.5*pixel, y=col+7*pixel-10)

LaNC8 = tk.Label(window, text=f"0", font=("Helvetica", font_size))
LaNC8.place(x=rownum+5*pixel, y=col+7*pixel-10)
#--------------------------------------------label
col=10
rownum =730

S2 = tk.Label(window, text="nature1 Y1", font=("Helvetica", font_size))
S2.place(x=rownum-1*pixel, y=col+1*pixel)

p1 = tk.Label(window, text="nature2 N1", font=("Helvetica", font_size))
p1.place(x=rownum-1*pixel, y=col+2.5*pixel)

B1 = tk.Label(window, text="nature3 Y2", font=("Helvetica", font_size))
B1.place(x=rownum-1*pixel, y=col+4*pixel)

S1 = tk.Label(window, text="nature4 N2", font=("Helvetica", font_size))
S1.place(x=rownum-1*pixel, y=col+5.5*pixel)

nature1 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
nature1.insert(0, "0.5")
nature1.place_configure(width=50, height=30)
nature1.place(x=rownum+3.25*pixel, y=col+1*pixel)
nature1.bind("<FocusOut>", lambda event: update_row())

nature2 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
nature2.insert(0, "0.5")
nature2.place_configure(width=50, height=30)
nature2.place(x=rownum+3.25*pixel, y=col+2.5*pixel)
nature2.bind("<FocusOut>", lambda event: update_row())

nature3 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
nature3.insert(0, "0.66")
nature3.place_configure(width=50, height=30)
nature3.place(x=rownum+3.25*pixel, y=col+4*pixel)
nature3.bind("<FocusOut>", lambda event: update_row())

nature4 = tk.Entry(window, width=table_width, font=("Helvetica", font_size))
nature4.insert(0, "0.66")
nature4.place_configure(width=50, height=30)
nature4.place(x=rownum+3.25*pixel, y=col+5.5*pixel)
nature4.bind("<FocusOut>", lambda event: update_row())

image = Image.open('ZNU.png')
tk_image = ImageTk.PhotoImage(image)
label = tk.Label(window, image=tk_image)
label.place(x=900 , y=10)

window.mainloop()