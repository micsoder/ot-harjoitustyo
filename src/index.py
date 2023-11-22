import customtkinter
from main import Main


def main():

    window = customtkinter.CTk()
    window.title('Atlas')

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}+0+0")
    window.config(bg='#001220')

    Main(window)

    window.mainloop()


if __name__ == "__main__":
    main()
