import tkinter as tk
from tkinter import simpledialog, messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Virtual.py")
        self.geometry("800x600")
        self.vm_list = []

        self.label = tk.Label(self, text="Bienvenue sur Virtual.py", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.frame_buttons = tk.Frame(self)
        self.frame_buttons.pack(side=tk.TOP, pady=10)

        self.button_create = tk.Button(self.frame_buttons, text="Créer une nouvelle machine virtuelle", command=self.create_vm)
        self.button_create.pack(side=tk.LEFT, padx=10)

        self.button_launch = tk.Button(self.frame_buttons, text="Lancer une machine virtuelle", command=self.launch_vm)
        self.button_launch.pack(side=tk.LEFT, padx=10)

        self.button_manage = tk.Button(self.frame_buttons, text="Gérer les machines virtuelles", command=self.manage_vms)
        self.button_manage.pack(side=tk.LEFT, padx=10)

    def create_vm(self):
        name = simpledialog.askstring("Nom de la machine virtuelle", "Entrez le nom de la machine virtuelle:")
        if name:
            self.vm_list.append(name)
            messagebox.showinfo("Création de machine virtuelle", f"Machine virtuelle '{name}' créée avec succès!")

    def launch_vm(self):
        if not self.vm_list:
            messagebox.showwarning("Aucune machine virtuelle", "Il n'y a aucune machine virtuelle disponible.")
            return

        vm_to_launch = simpledialog.askstring("Lancer une machine virtuelle", "Entrez le nom de la machine virtuelle à lancer:")
        if vm_to_launch in self.vm_list:
            messagebox.showinfo("Lancement de machine virtuelle", f"La machine virtuelle '{vm_to_launch}' est lancée!")
        else:
            messagebox.showerror("Erreur de lancement", f"La machine virtuelle '{vm_to_launch}' n'existe pas.")

    def manage_vms(self):
        if not self.vm_list:
            messagebox.showwarning("Aucune machine virtuelle", "Il n'y a aucune machine virtuelle disponible.")
            return

        vm_list_str = "\n".join(self.vm_list)
        messagebox.showinfo("Liste des machines virtuelles", f"Liste des machines virtuelles :\n{vm_list_str}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
