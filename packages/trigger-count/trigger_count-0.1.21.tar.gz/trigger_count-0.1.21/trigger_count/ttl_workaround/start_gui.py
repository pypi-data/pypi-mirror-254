"""Start GUI for widefield TTL pulses"""
import tkinter as tk


class StartGui:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("TTL pulses")

        self.variables: dict = {}

        self.proceed: bool = False

    def set_up(self) -> None:
        frame = tk.LabelFrame(self.window, text="Settings")
        frame.pack(expand=True, fill="both")

        label = tk.Label(frame, text="Subject ID")
        label.grid(row=0, column=0)
        variable = tk.StringVar()
        variable.set("test")
        self.variables["subject_id"] = variable
        entry = tk.Entry(frame, textvariable=variable)
        entry.grid(row=0, column=1)

        frame = tk.LabelFrame(self.window, text="Control")
        frame.pack(expand=True, fill="both")
        button = tk.Button(frame, text="Run", command=self.run_button)
        button.grid(row=0, column=0)
        button = tk.Button(frame, text="Quit", command=self.quit_button)
        button.grid(row=0, column=1)

    def run(self) -> None:
        self.set_up()
        self.window.mainloop()

    def run_button(self) -> None:
        self.proceed = True
        self.window.destroy()

    def quit_button(self) -> None:
        self.proceed = False
        self.window.destroy()

    def get_settings(self) -> dict:
        settings = {
            "subject_id": self.variables["subject_id"].get(),
        }
        return settings


if __name__ == "__main__":
    gui = StartGui()
    gui.run()