import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Deal or No Deal")


root.attributes("-fullscreen", True)
root.resizable(True, True)


root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))


root.configure(bg="#f0f0f0")


b = [1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
random.shuffle(b)

p_case = None
p_idx = None


a_lbls = {}
s_a = sorted(b)

def upd_a():
    for a in s_a:
        if a not in b:
            a_lbls[a].config(fg="red", font=("Arial", 10, "overstrike"))
        else:
            a_lbls[a].config(fg="black", font=("Arial", 10))

def choose(i):
    global p_case, p_idx
    if 0 <= i < len(b):
        if p_case is None:
            p_idx = i
            p_case = b[i]
            c_btns[i].config(text="Your Case", state="disabled", bg="#ff9999", fg="#ffffff")
            for btn in btns:
                btn.config(state="normal")
            c_case_btn.config(state="disabled")
        else:
            messagebox.showerror("Error", "Case already chosen")
    else:
        messagebox.showerror("Error", "Invalid case index")

def open(i):
    if 0 <= i < len(b) and c_btns[i]["state"] != "disabled":
        o_case = b[i]
    
        if o_case > 5000:
            c_btns[i].config(text=f"${o_case}", state="disabled", bg="#ff0000", fg="#ffffff")  
        else:
            c_btns[i].config(text=f"${o_case}", state="disabled", bg="#99cc99", fg="#ffffff")  
        
        b[i] = None
        upd_a()
        upd_o()
    else:
        messagebox.showerror("Error", "Invalid case index or case already opened")

def upd_o():
    r_cases = [a for a in b if a is not None]
    if len(r_cases) in [20, 15, 11, 8, 6, 5, 4, 3, 2]:
        o = offer(r_cases)
        if messagebox.askyesno("Banker's Offer", f"Offer: ${o}. Deal or No Deal?"):
            messagebox.showinfo("Congratulations!", f"Accepted the deal and won ${o}\nYour chosen case contains ${p_case}")
            root.quit()
        else:
            messagebox.showinfo("No Deal", "Continue playing.")
    elif len(r_cases) == 1:
        messagebox.showinfo("Game Over", f"No deal. You won ${p_case}.")
        root.quit()

def offer(r_cases):
    return int(sum(r_cases) / len(r_cases))

btns = []
c_btns = []

main_frame = tk.Frame(root, bg="#e0e0e0")
main_frame.grid(row=0, column=0, sticky="nsew")  


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

label = tk.Label(main_frame, text="Welcome to Deal or No Deal", bg="#e0e0e0", font=("Arial", 16, "bold"))
label.grid(row=0, column=0, columnspan=5, pady=10, sticky="ew")  

c_case_btn = tk.Button(main_frame, text="Choose Your Case", command=lambda: choose(p_idx) if p_case is None else None, state="normal", bg="#4CAF50", fg="#ffffff", font=("Arial", 12, "bold"))
c_case_btn.grid(row=1, column=0, columnspan=5, pady=10, sticky="ew") 

for i in range(25):
    btn = tk.Button(main_frame, text=f"Case {i + 1}", width=10, height=2, command=lambda i=i: choose(i) if p_case is None else open(i), bg="#2196F3", fg="#ffffff", font=("Arial", 10, "bold"))
    btn.grid(row=(i // 5) + 2, column=i % 5, padx=5, pady=5, sticky="nsew")  
    btns.append(btn)
    c_btns.append(btn)


for i in range(5):
    main_frame.grid_columnconfigure(i, weight=1)
for i in range(7):
    main_frame.grid_rowconfigure(i, weight=1)


a_frame = tk.Frame(main_frame, bg="#e0e0e0")
a_frame.grid(row=2, column=5, rowspan=6, padx=20, sticky="n")

for idx, a in enumerate(s_a):
    lbl = tk.Label(a_frame, text=f"${a}", font=("Arial", 10), bg="#e0e0e0")
    lbl.grid(row=idx, column=0, sticky="w")
    a_lbls[a] = lbl

footer_label = tk.Label(root, text="Created By Sailesh", font=("Arial", 12), bg="#f0f0f0", fg="#000000")
footer_label.grid(row=1, column=0, padx=10, pady=10, sticky="s")

root.mainloop()
