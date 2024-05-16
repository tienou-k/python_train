from sys import version_info

if version_info.major == 2:
    import tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

app = tk.Tk()
labelExample = tk.Label(app, text="This is a Label")
labelExample.pack()
app.mainloop()