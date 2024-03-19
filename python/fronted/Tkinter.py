from tkinter import *
from tkinter import filedialog

class AppWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("DEVILLE GROUP APP")
        self.master.geometry("1080x720")
        self.master.minsize(900, 480)
        self.master.config(background='#41B77F')
        self.master.iconbitmap("1707045446052-removebg-preview.ico")
        
    def build(self):
        label_title = Label(self.master, text="Bienvenue sur l'application", font=("Courier", 40), bg='#41B77F', fg='white')
        label_title.pack(side=TOP, pady=20)
        
        image = PhotoImage(file="Charger_excell-removebg-preview.png")
        label_image = Label(self.master, image=image, bg='#41B77F')
        label_image.image = image  
        label_image.pack()
        
        frame = Frame(self.master, bg='#41B77F')
        frame.pack(expand=YES)
        
        label_subtitle = Label(frame, text="Entrez le/les fichier(s) Excel(s)", font=("Courier", 20), bg='#41B77F', fg='white')
        label_subtitle.pack()
        
        charge_button = Button(frame, text="Sélectionner le fichier .xlsx/.xlsm", font=("Courier", 20), bg='white', fg='#41B77F', command=self.select_file)
        charge_button.pack(pady=20, fill=X)
        
    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers Excel", "*.xlsx;*.xlsm")])
        if file_path:
            print("Chemin du fichier sélectionné :", file_path)
            # Vous pouvez ajouter ici le traitement que vous souhaitez effectuer avec le fichier sélectionné

def main():
    window = Tk()
    app = AppWindow(window)
    app.build()
    window.mainloop()

if __name__ == "__main__":
    main()
