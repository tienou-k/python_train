import  tkinter as tk

root = tk.Tk()


root.geometry('400x800')
root.title('TP Python Groupe 3 ')

Label = tk.Label(root, text = 'Hello !', font=('Arial', 18))
Label.pack(padx=10, pady=10)

Textbox = tk.Text(root, height=5, font=('Arial', 18))
Textbox.pack(padx=10)

button = tk.Button(root, text='Click ! ', font=('Arial', 18))
button.pack(pady=10)
root.mainloop()
