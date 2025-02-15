import tkinter as tk

def close_window(event):
    if event.char.lower() == "y": 
        root.destroy()

# Create a window
root = tk.Tk()
root.title("Tasnuba Akter") 
root.configure(bg="cyan")
root.geometry("500x300")  


root.bind("<KeyPress>", close_window)


root.mainloop()
