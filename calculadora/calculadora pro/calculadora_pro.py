import customtkinter as ctk
from logic import *

#Configuración estilo dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CalculadoraPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora Pro")
        self.geometry("350x550")
        self.resizable(False, False)
        self.expression = ""

        self._setup_ui()

    def _setup_ui(self):
        self.display = ctk.CTkEntry(
            self, height=80, corner_radius=15,
            font=("Orbitron", 34), justify="right",
            fg_color="#1a1a1a", border_color="#333333"
        )
        self.display.pack(padx=20, pady=(30, 10), fill="x")

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(padx=15, pady=10, fill="both", expand=True)

        self._render_buttons()

    def _render_buttons(self):
        layout = [
            ('C', 0, 0, "#e74c3c"), ('√', 0, 1, "#3498db"), ('^', 0, 2, "#3498db"), ('/', 0, 3, "#3498db"),
            ('7', 1, 0, None), ('8', 1, 1, None), ('9', 1, 2, None), ('*', 1, 3, "#3498db"),
            ('4', 2, 0, None), ('5', 2, 1, None), ('6', 2, 2, None), ('-', 2, 3, "#3498db"),
            ('1', 3, 0, None), ('2', 3, 1, None), ('3', 3, 2, None), ('+', 3, 3, "#3498db"),
            ('0', 4, 0, None), ('.', 4, 1, None), ('=', 4, 2, "#2ecc71")
        ]

        for (txt, r, c, color) in layout:
            is_equal = txt == '='
            btn = ctk.CTkButton(
                self.btn_frame, text=txt,
                width=150 if is_equal else 70, height=70,
                corner_radius=12, font=("Roboto", 20, "bold"),
                fg_color=color if color else "#2b2b2b",
                hover_color="#3d3d3d",
                command=lambda t=txt: self._on_click(t)
            )
            btn.grid(row=r, column=c, columnspan=2 if is_equal else 1, padx=5, pady=5)

    def _on_click(self, key):
        if key == "C":
            self.expression = ""
        elif key == "=":
            self.expression = calculate_expression(self.expression)
        elif key == "√":
            self.expression = calculate_sqrt(self.display.get())
        elif key == "^":
            self.expression += "**"
        else:
            self.expression += str(key)
        
        self._refresh_display()

    def _refresh_display(self):
        self.display.delete(0, "end")
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    app = CalculadoraPro()
    app.mainloop()