import tkinter as tk
import random
result = []
def dispLabel():
    kuji = ["大吉","中吉","小吉","吉","末吉","凶","大凶"]
    lbl.configure(text=random.choice(kuji))
    result.append(lbl.pack())
    lbl2.configure(text=result)
root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="おみくじアプリ")
btn = tk.Button(text="おみくじ！", command = dispLabel)
lbl2 = tk.Label(text="")

lbl.pack()
btn.pack()
lbl2.pack()
tk.mainloop()
