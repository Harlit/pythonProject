import tkinter as tk


class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")

        # Crear widget de entrada
        self.entry = tk.Entry(self.master, width=20, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=4, pady=5)

        # Crear botones
        self.create_button('7', 1, 0, "#d1d1d1")
        self.create_button('8', 1, 1, "#d1d1d1")
        self.create_button('9', 1, 2, "#d1d1d1")
        self.create_button('/', 1, 3)

        self.create_button('4', 2, 0, "#d1d1d1")
        self.create_button('5', 2, 1, "#d1d1d1")
        self.create_button('6', 2, 2, "#d1d1d1")
        self.create_button('*', 2, 3)

        self.create_button('1', 3, 0, "#d1d1d1")
        self.create_button('2', 3, 1, "#d1d1d1")
        self.create_button('3', 3, 2, "#d1d1d1")
        self.create_button('-', 3, 3)

        self.create_button('0', 4, 0, "#d1d1d1")
        self.create_button('.', 4, 1, "#d1d1d1")
        self.create_button('C', 4, 2, "#d1d1d1")
        self.create_button('+', 4, 3)

        self.create_button('=', 5, 0, columnspan=4)

    def create_button(self, text, row, column, color=None, columnspan=1):
        kwargs = {'width': 5, 'height': 2, 'font': ('Arial', 12), 'command': lambda: self.button_click(text)}
        if color:
            kwargs['bg'] = color
        button = tk.Button(self.master, text=text, **kwargs)
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
            except SyntaxError:
                result = "Error de sintaxis"
            except ZeroDivisionError:
                result = "Error de división por cero"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        elif text == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
app = Calculadora(root)
root.mainloop()