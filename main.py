from squirdle_solver.app import App
from squirdle_solver.utils.file_utils import file_path

def main() -> None:
    app = App()
    app.iconbitmap(file_path("squirdle.ico"))
    app.mainloop()

if __name__ == "__main__":
    main()
