import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Virtual.py")
        self.geometry("800x600")

        self.label = tk.Label(self, text="Bienvenue sur Virtual.py", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.frame_buttons = tk.Frame(self)
        self.frame_buttons.pack(side=tk.TOP, pady=10)

        self.button_create = tk.Button(self.frame_buttons, text="Créer une nouvelle machine virtuelle", command=self.create_vm)
        self.button_create.pack(side=tk.LEFT, padx=10)

        self.button_launch = tk.Button(self.frame_buttons, text="Lancer une machine virtuelle existante", command=self.launch_vm)
        self.button_launch.pack(side=tk.LEFT, padx=10)

        self.button_manage = tk.Button(self.frame_buttons, text="Gérer les machines virtuelles", command=self.manage_vms)
        self.button_manage.pack(side=tk.LEFT, padx=10)

    def create_vm(self):
        # Code pour créer une nouvelle machine virtuelle
        print("Création d'une nouvelle machine virtuelle")

    def launch_vm(self):
        # Code pour lancer une machine virtuelle existante
        print("Lancement d'une machine virtuelle")

    def manage_vms(self):
        # Code pour gérer les machines virtuelles
        print("Gestion des machines virtuelles")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
