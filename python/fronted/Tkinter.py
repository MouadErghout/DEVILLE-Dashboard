from tkinter import *
from tkinter import filedialog

class AppWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("DEVILLE GROUP APP")
        self.master.geometry("1080x720")
        self.master.minsize(900, 480)
        self.master.config(background='#41B77F')
        self.master.iconbitmap("python/fronted/1707045446052-removebg-preview.ico")
        
    def build(self):
        label_title = Label(self.master, text="Bienvenue sur l'application", font=("Courier", 40), bg='#41B77F', fg='white')
        label_title.pack(side='top', pady=20)

        frame = Frame(self.master, bg='#41B77F')
        frame.pack(expand='yes')

        label_subtitle = Label(frame, text="Entrez le/les fichier(s) Excel(s)", font=("Courier", 20), bg='#41B77F', fg='white')
        label_subtitle.pack()

        charge_button = Button(frame, text="Sélectionner le fichier .xlsx/.xlsm", font=("Courier", 20), bg='white', fg='#41B77F', command=self.select_file)
        charge_button.pack(pady=20, fill='x')

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers Excel", "*.xlsx;*.xlsm")])
        if file_path:
            print(f"Le chemin du fichier sélectionné est : {file_path}")
            self.show_interface2(file_path)
        else:
            print("Aucun fichier sélectionné.")
    
    def show_interface2(self, file_path):
        self.selection_window = Toplevel(self.master)
        self.selection_window.title("Interface 2")
        self.selection_window.geometry("1080x720")
        self.selection_window.minsize(900, 480)
        self.selection_window.config(background='#41B77F')
        self.selection_window.iconbitmap("python/fronted/1707045446052-removebg-preview.ico")

        frame = Frame(self.selection_window, bg='#41B77F')
        frame.pack(expand=YES)

        label_title = Label(frame, text="Sélectionner l'interface que vous voulez afficher :", font=("Helvetica", 25), bg='#41B77F', fg='white')
        label_title.pack(side=TOP, pady=100)

        button_interface01 = Button(frame, text="Interface 01", font=("Verdana", 20), command=lambda: self.open_interface(1))
        button_interface01.pack(padx=5, pady=5)

        button_interface02 = Button(frame, text="Interface 02", font=("Verdana", 20), command=lambda: self.open_interface(2))
        button_interface02.pack(padx=5, pady=5)

        button_interface03 = Button(frame, text="Interface 03", font=("Verdana", 20), command=lambda: self.open_interface(3))
        button_interface03.pack(padx=5, pady=5)

    def open_interface(self, interface_num):

        self.selection_window.withdraw()

        new_root = Toplevel(self.master)
        new_root.title(f"DEVILLE GROUP APP")
        new_root.geometry("1080x720")
        new_root.minsize(900, 480)
        new_root.config(background='#41B77F')
        if interface_num == 1:
            label = Label(new_root, text=f"Interface 0{interface_num} : Comparaison complète des rapports sélectionnés", font=("Helvetica", 20),bg='#41B77F', fg='white' )
            label.pack(pady=20)
        elif interface_num == 2:
            label = Label(new_root, text=f"Interface 0{interface_num} : Nombre de dimensions nok par rapport sélectionné ", font=("Helvetica", 20),bg='#41B77F', fg='white' )
            label.pack()
        elif interface_num == 3:
            label = Label(new_root, text=f"Interface 0{interface_num} : Affichage des conformes et des non conformes ", font=("Helvetica", 20),bg='#41B77F', fg='white' )
            label.pack()

        button_return = Button(new_root, text="Retour", font=("Courier", 20), command=lambda: self.return_to_selection(new_root))
        button_return.pack(side="bottom", pady=20)

    def return_to_selection(self, new_window):
        new_window.destroy()
        self.selection_window.deiconify()

def main():
    window = Tk()
    app = AppWindow(window)
    app.build()
    window.mainloop()

if __name__ == "__main__":
    main()

