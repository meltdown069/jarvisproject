import tkinter as tk
import threading

class JarvisGUI:
    def __init__(self, process_command_func):
        self.root = tk.Tk()
        self.root.title("JARVIS Core")
        self.root.geometry("380x200")
        self.root.configure(bg="#0a0a0a") # Deep black
        self.root.attributes("-topmost", True)
        self.process_command = process_command_func

        # --- NEURAL STATUS LAMP ---
        self.lamp_canvas = tk.Canvas(self.root, width=40, height=40, bg="#0a0a0a", highlightthickness=0)
        self.lamp_canvas.pack(pady=(20, 0))
        # Glowing effect oval
        self.status_lamp = self.lamp_canvas.create_oval(10, 10, 30, 30, fill="#00ffcc", outline="#00ffcc")

        # Status Label
        self.status_label = tk.Label(self.root, text="SYSTEM READY", fg="#00d4ff", bg="#0a0a0a", font=("Segoe UI", 12, "bold"))
        self.status_label.pack(pady=10)

        # --- TEXT INPUT ---
        input_frame = tk.Frame(self.root, bg="#0a0a0a")
        input_frame.pack(fill=tk.X, padx=40, pady=10)
        
        self.user_input = tk.Entry(input_frame, bg="#1a1a1a", fg="white", font=("Segoe UI", 11), borderwidth=0, insertbackground="white")
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        self.user_input.bind("<Return>", self.send_text_command)
        
        # Hidden send logic
        self.root.bind('<Control-Return>', self.send_text_command)

    def update_status(self, text, color="#00d4ff", lamp_color="#00ffcc"):
        self.status_label.config(text=text.upper(), fg=color)
        self.lamp_canvas.itemconfig(self.status_lamp, fill=lamp_color, outline=lamp_color)

    def log(self, message):
        """Logs now print to the console/terminal only"""
        print(f"[JARVIS LOG]: {message}")

    def send_text_command(self, event=None):
        text = self.user_input.get().strip()
        if text:
            self.user_input.delete(0, tk.END)
            threading.Thread(target=self.process_command, args=(text,), daemon=True).start()