import tkinter as tk
import random
def dispLabel():
    kuji = ["大吉","中吉","小吉","吉","末吉","凶","大凶"]
    lbl.configure(text=random.choice(kuji))
root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="おみくじアプリ")
btn = tk.Button(text="おみくじ！", command = dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()
