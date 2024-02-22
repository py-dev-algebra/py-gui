import tkinter as tk

from event_handlers.btn_get_customers_handler import on_click


main_window = tk.Tk()

main_window.title('Algebra - Python desktop app')
main_window.geometry('600x400')


# Naziv konstruirati od widget_funkcija
lbl_title = tk.Label(main_window,
                     text='NASLOV',
                     font=('Segoe UI', 18))
lbl_title.pack()

btn_get_customers = tk.Button(main_window,
                       text='Dohvati sve korisnike',
                       font=('Segoe UI', 15),
                       command=on_click).pack()



main_window.mainloop()
