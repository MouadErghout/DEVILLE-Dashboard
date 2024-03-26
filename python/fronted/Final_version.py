from tkinter import *
from tkinter import filedialog

class AppWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("DEVILLE GROUP APP")
        self.master.geometry("1080x720")
        self.master.minsize(900, 480)
        self.master.config(background='#41B77F')
        self.master.iconbitmap("./1707045446052-removebg-preview.ico")
        self.file_paths = []

    def build(self):
        self.label_title = Label(self.master, text="Bienvenue sur l'application", font=("Courier", 40), bg='#41B77F', fg='white')
        self.label_title.pack(side='top', pady=20)

        frame = Frame(self.master, bg='#41B77F')
        frame.pack(expand=1)

        label_subtitle = Label(frame, text="Entrez le/les fichier(s) Excel(s)", font=("Courier", 20), bg='#41B77F', fg='white')
        label_subtitle.pack()

        charge_button = Button(frame, text="Sélectionner le(s) fichier(s) .xlsx/.xlsm", font=("Courier", 20), bg='white', fg='#41B77F', command=self.select_file)
        charge_button.pack(pady=20, fill='x')

    def select_file(self):
        self.file_paths = filedialog.askopenfilenames(filetypes=[("Fichiers Excel", "*.xlsx;*.xlsm")])
        if self.file_paths:
            for file_path in self.file_paths:
                print(f"Le chemin du fichier sélectionné est : {file_path}")
            self.build_interface_selection()
        else:
            print("Aucun fichier sélectionné.")
            
    def build_interface_selection(self):
        self.label_title.pack_forget()
        for widget in self.master.winfo_children():
            widget.destroy()

        self.label_title = Label(self.master, text="Sélectionner l'interface que vous voulez afficher :", font=("Helvetica", 25), bg='#41B77F', fg='white')
        self.label_title.pack(side=TOP, pady=100)

        button_interface01 = Button(self.master, text="Interface 01", font=("Verdana", 20), command=lambda: self.open_interface(1))
        button_interface01.pack(padx=5, pady=5)

        button_interface02 = Button(self.master, text="Interface 02", font=("Verdana", 20), command=lambda: self.open_interface(2))
        button_interface02.pack(padx=5, pady=5)

        button_interface03 = Button(self.master, text="Interface 03", font=("Verdana", 20), command=lambda: self.open_interface(3))
        button_interface03.pack(padx=5, pady=5)

    def open_interface(self, interface_num):
        self.label_title.pack_forget()
        for widget in self.master.winfo_children():
            widget.destroy()

        if interface_num == 1:
            label = Label(self.master, text="Interface 01 : Comparaison complète des rapports sélectionnés", font=("Helvetica", 20), bg='#41B77F', fg='white' )
            label.pack(pady=20)
        elif interface_num == 2:
            label = Label(self.master, text="Interface 02 : Nombre de dimensions nok par rapport sélectionné ", font=("Helvetica", 20), bg='#41B77F', fg='white' )
            label.pack()
        elif interface_num == 3:
            label = Label(self.master, text="Interface 03 : Affichage des conformes et des non conformes ", font=("Helvetica", 20), bg='#41B77F', fg='white' )
            label.pack()

        button_return = Button(self.master, text="Retour", font=("Courier", 20), command=self.build_interface_selection)
        button_return.pack(side="bottom", pady=20)

def main():
    window = Tk()
    app = AppWindow(window)
    app.build()
    window.mainloop()

if __name__ == "__main__":
    main()
