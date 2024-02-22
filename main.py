import tkinter as tk

from event_handlers.btn_get_customers_handler import on_click


main_window = tk.Tk()

main_window.title('Algebra - Python desktop app')
main_window.geometry('600x400')

# Naziv konstruirati od widget_funkcija
btn_get_customers = tk.Button(main_window,
                       text='Dohvati sve korisnike',
                       command=on_click)
btn_get_customers.pack()



main_window.mainloop()
