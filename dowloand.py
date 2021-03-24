from tkinter import *

from pytube import YouTube

class Application:
   def __init__(self, master=None):
       self.fontePadrao = ("Arial", "10")
       self.primeiroContainer = Frame(master)
       self.primeiroContainer["pady"] = 20
       self.primeiroContainer.pack()

       self.segundoContainer = Frame(master)
       self.segundoContainer["padx"] = 20
       self.segundoContainer.pack()

       self.quartoContainer = Frame(master)
       self.quartoContainer["pady"] = 20
       self.quartoContainer.pack()

       self.titulo = Label(self.primeiroContainer, text="Download Youtube")
       self.titulo["font"] = ("Arial", "20", "bold")
       self.titulo.pack()

       self.nomeLabel = Label(self.segundoContainer,text="Link", font=self.fontePadrao)#login
       self.nomeLabel.pack(side=LEFT)

       self.nome = Entry(self.segundoContainer)
       self.nome["width"] = 40
       self.nome["font"] = self.fontePadrao
       self.nome.pack(side=LEFT)

     


       self.autenticar = Button(self.quartoContainer)
       self.autenticar["text"] = "baixar"
       self.autenticar["font"] = ("Calibri", "8")
       self.autenticar["width"] = 12
       self.autenticar["command"] = self.verificaSenha
       self.autenticar.pack()

       self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
       self.mensagem.pack()
       
        #pach = "/home/alisson/Vídeos"
   def verificaSenha(self):    
       nome = self.nome.get()
       yt = YouTube(nome)
       ys = yt.streams.get_highest_resolution()
       self.mensagem["text"] = "Baixando..."
       ys.download("/home/alisson/Vídeos")

       self.mensagem["text"] = "Download completo!"

root = Tk()
Application(root)
root.mainloop()