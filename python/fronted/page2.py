from tkinter import *
from tkinter import Tk, Label, Button, Frame, filedialog


class AppWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("DEVILLE GROUP APP")
        self.master.geometry("1080x720")
        self.master.minsize(900, 480)
        self.master.config(background='#41B77F')
        self.master.iconbitmap("python/fronted/1707045446052-removebg-preview.ico")
        self.selection_window = None  # Fenêtre de sélection des interfaces

    def build_selection_window(self): 
        frame = Frame(self.master, bg='#41B77F')
        frame.pack(expand=YES)

        label_title = Label(frame, text="Sélectionner l'interface que vous voulez afficher :", font=("Helvetica", 25), bg='#41B77F', fg='white')
        label_title.pack(side=TOP, pady=100)

        button_interface01 = Button(frame, text="Interface 01", font=("Verdana", 20), command=lambda: self.select_file_and_open_interface(1))
        button_interface01.pack(padx=5, pady=5)

        button_interface02 = Button(frame, text="Interface 02", font=("Verdana", 20), command=lambda: self.select_file_and_open_interface(2))
        button_interface02.pack(padx=5, pady=5)

        button_interface03 = Button(frame, text="Interface 03", font=("Verdana", 20), command=lambda: self.select_file_and_open_interface(3))
        button_interface03.pack(padx=5, pady=5)

    def select_file_and_open_interface(self, interface_num):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers Excel", "*.xlsx;*.xlsm")])
        if file_path:
            self.open_interface(interface_num, file_path)

    def open_interface(self, interface_num, file_path):
        self.master.withdraw()

        new_root = Tk()
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

        button_return = Button(new_root, text="Retour", font=("Courier", 20), command=self.return_to_selection)
        button_return.pack(side="bottom", pady=20)

        new_root.mainloop()

    def return_to_selection(self):
        self.master.deiconify()

def main():
    window = Tk()
    app = AppWindow(window)
    app.build_selection_window()
    window.mainloop()

if __name__ == "__main__":
    main()
