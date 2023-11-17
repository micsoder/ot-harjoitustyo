import customtkinter
from main import Main

def main():

    window = customtkinter.CTk()
    window.title('Atlas')
    window.after(0, lambda:window.state('zoomed'))
    window.config(bg='#001220')

    Main(window)

    window.mainloop()


if __name__ == "__main__":
    main()
