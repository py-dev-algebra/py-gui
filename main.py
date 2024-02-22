import tkinter as tk

from event_handlers.btn_click_handler import on_click



main_window = tk.Tk()

main_window.title('Algebra - Python desktop app')
main_window.geometry('600x400')

btn_button = tk.Button(main_window,
                       text='Klikni me',
                       command=on_click)
btn_button.pack()



main_window.mainloop()
