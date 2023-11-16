import customtkinter
from ui.ui_handler import UiHandler

def main():

    window = customtkinter.CTk()
    window.title('Atlas')
    window.after(0, lambda:window.state('zoomed'))
    window.config(bg='#001220')

    UiHandler(window)

    window.mainloop()


if __name__ == "__main__":
    main()
