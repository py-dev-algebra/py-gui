import tkinter as tk

from event_handlers.btn_get_customers_handler import on_click
from constants.gui_constants import (TITLE_FONT,
                                     BUTTON_FONT)


main_window = tk.Tk()

main_window.title('Algebra - Python desktop app')
main_window.geometry('600x400') # Pocetna velicina glavnog prozora


# Naziv konstruirati od widget_funkcija
lbl_title = tk.Label(main_window,
                     text='NASLOV',
                     font=TITLE_FONT)
lbl_title.place(x=50, y=20)

btn_get_customers = tk.Button(main_window,
                       text='Dohvati sve korisnike',
                       font=BUTTON_FONT,
                       command=on_click).place(x=300, y=200)


main_window.mainloop()
