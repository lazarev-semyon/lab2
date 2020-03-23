def calc(key):
    """key identification

    Arguments:
        key {[string]} -- [* / - + ]
    """
    global memory
    if key == "=":
        str1 = "-+0123456789.*/"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")

        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
 
#clear field
    elif key == "C":
        calc_entry.delete(0, END)
#change -+
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "π":
        calc_entry.insert(END, math.pi)
    elif key == "Exit":
        root.after(1,root.destroy)
        sys.exit
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        sin=calc_entry.get()
        calc_entry.delete(0)
        calc_entry.insert(END, math.sin(float(sin)))
    elif key == "cos":
        cos=calc_entry.get()
        calc_entry.delete(0)
        calc_entry.insert(END, math.cos(float(cos)))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
        