import tkinter as tk

from event_handlers.btn_get_customers_handler import on_click
from constants.gui_constants import (TITLE_FONT,
                                     BUTTON_FONT,
                                     DEFAULT_PAD)


main_window = tk.Tk()

main_window.title('Algebra - Python desktop app')
main_window.geometry('600x400') # Pocetna velicina glavnog prozora


# Naziv konstruirati od widget_funkcija
lbl_title = tk.Label(main_window,
                     text='NASLOV',
                     font=TITLE_FONT)
lbl_title.pack(padx=DEFAULT_PAD, pady=DEFAULT_PAD)

btn_get_customers = tk.Button(main_window,
                       text='Dohvati sve korisnike',
                       font=BUTTON_FONT,
                       command=on_click).pack(padx=DEFAULT_PAD, pady=DEFAULT_PAD)


main_window.mainloop()
