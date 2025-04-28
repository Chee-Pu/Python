import tkinter as tk
from tkinter.constants import SUNKEN


class temperature_conversion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.geometry('500x300')
        self.resizable(True , True)
        self.main_window()

    def show_input(self):
        frame = tk.Frame(self)
        frame.grid(row=0, sticky="NSEW")
        label = tk.Label(frame, text="Enter Temperature")
        label.grid(row=0, column=0)
        entry = tk.Entry(frame)
        entry.grid(row=0, column=1)
        self.input = entry.get()

    def show_buttons(self):
        frame = tk.Frame(self,width=100,height=100,bg = 'gray', bd= 5, relief = SUNKEN)
        frame.grid(row=1, sticky="NSEW", columnspan=2)
        F_to_C = tk.Button(frame, text="F to C", command=self.F_to_C())
        F_to_C.grid(row=0, column=0, sticky="NSEW", command=self.C_to_F())
        C_to_F = tk.Button(frame, text="C to F")
        C_to_F.grid(row=0,column =1, sticky="NSEW")

    def get_input(self):
        self.input = self.entry.get()
        return self.input

    def main_window(self):
        self.temp = self.show_input()
        self.show_buttons()

    def F_to_C(self):
        self.temp = float(self.get_input())
        C_temp = ((self.temp - 32) *5)/9
        frame = tk.Frame(self)
        frame.grid(row=1, sticky="NSEW")
        label = tk.Label(frame, text="Your Temperature in C is: " + str(C_temp))
        label.grid(row=0, column=0)
        self.show_buttons()

    def C_to_F(self):
        self.temp = float(self.get_input())
        F_temp = self.temp * (9/5) + 32
        frame = tk.Frame(self)
        frame.grid(row=1, sticky="NSEW")
        label = tk.Label(frame, text="Your Temperature in F is: "+ str(F_temp))
        label.grid(row=0, column=0)
        self.show_buttons()
def main():
    temperature_conversion().mainloop()

if __name__ == '__main__':
    main()