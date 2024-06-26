import tkinter as Calculator  


calculation = ""

def add_to_calculation(symbol):
    global calculation
    
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evalutate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        pass
    
    
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = Calculator.Tk()
root.geometry("300x275")
text_result = Calculator.Text(root, height=2, width=16, font=("New Time Roman", 24))
text_result.grid(columnspan=5)

btn_1 = Calculator.Button(root, text="1", command = lambda: add_to_calculation(1), width = 5, font ="TimesNewRoman 14")
btn_1.grid( row=2 , column=1)
btn_2 = Calculator.Button(root, text="2", command = lambda: add_to_calculation(2), width = 5, font ="TimesNewRoman 14")
btn_2.grid( row=2 , column=2)
btn_3 = Calculator.Button(root, text="3", command = lambda: add_to_calculation(3), width = 5, font ="TimesNewRoman 14")
btn_3.grid( row=2 , column=3)
btn_4 = Calculator.Button(root, text="4", command = lambda: add_to_calculation(4), width = 5, font ="TimesNewRoman 14")
btn_4.grid( row=3 , column=1)
btn_5 = Calculator.Button(root, text="5", command = lambda: add_to_calculation(5), width = 5, font ="TimesNewRoman 14")
btn_5.grid( row=3 , column=2)
btn_6 = Calculator.Button(root, text="6", command = lambda: add_to_calculation(6), width = 5, font ="TimesNewRoman 14")
btn_6.grid( row=3 , column=3)
btn_7 = Calculator.Button(root, text="7", command = lambda: add_to_calculation(7), width = 5, font ="TimesNewRoman 14")
btn_7.grid( row=4 , column=1)
btn_8 = Calculator.Button(root, text="8", command = lambda: add_to_calculation(8), width = 5, font ="TimesNewRoman 14")
btn_8.grid( row=4 , column=2)
btn_9 = Calculator.Button(root, text="9", command = lambda: add_to_calculation(9), width = 5, font ="TimesNewRoman 14")
btn_9.grid( row=4 , column=3)
btn_0 = Calculator.Button(root, text="0", command = lambda: add_to_calculation(0), width = 5, font ="TimesNewRoman 14")
btn_0.grid( row=5 , column=2)
btn_add = Calculator.Button(root, text="+", command = lambda: add_to_calculation("+"), width = 5, font ="TimesNewRoman 14")
btn_add.grid( row=2 , column=4)
btn_minus = Calculator.Button(root, text="-", command = lambda: add_to_calculation("-"), width = 5, font ="TimesNewRoman 14")
btn_minus.grid( row=3 , column=4)
btn_multiply = Calculator.Button(root, text="*", command = lambda: add_to_calculation("*"), width = 5, font ="TimesNewRoman 14")
btn_multiply.grid( row=4 , column=4)
btn_divide = Calculator.Button(root, text="/", command = lambda: add_to_calculation("/"), width = 5, font ="TimesNewRoman 14")
btn_divide.grid( row=5 , column=4)
btn_open = Calculator.Button(root, text="(", command = lambda: add_to_calculation("("), width = 5, font ="TimesNewRoman 14")
btn_open.grid( row=5 , column=1)
btn_close = Calculator.Button(root, text=")", command = lambda: add_to_calculation(")"), width = 5, font ="TimesNewRoman 14")
btn_close.grid( row=5 , column=3)
btn_clear = Calculator.Button(root, text="C", command = clear_field, width = 11, font ="TimesNewRoman 14")
btn_clear.grid( row=6 , column=4, columnspan= 2)
btn_eqauls = Calculator.Button(root, text="=", command = evalutate_calculation, width = 11, font ="TimesNewRoman 14")
btn_eqauls.grid( row=6 , column=0, columnspan= 4)



root.mainloop()
