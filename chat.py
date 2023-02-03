import tkinter as tk
from tkinter import font as tkFont
import openai, json, os

with open(os.path.dirname(os.path.realpath(__file__)) + os.sep + "config.json", encoding="utf-8") as config_file:
    config = json.load(config_file)

openai.api_key = config["api_key"]
model_engine = "text-davinci-003"


def gonder_message():
    sohbet.delete("1.0", tk.END)
    questions = textMesaj.get()
    sonuc = openai.Completion.create(engine = model_engine, prompt = questions, max_tokens = 1024, n = 1, stop = None, temperature = 0.9)
    cevap = sonuc.choices[0].text
    sohbet.insert(tk.END, cevap)
    
def mesaj_temizle():
    textMesaj.delete(0, tk.END)
    sohbet.delete("1.0", tk.END)
    

root = tk.Tk()
root.title('Chat GPT')
root.resizable(False,False)
#root.configure(bg='blue')

cerceve = tk.Frame(root)
cerceve.pack()

sohbet = tk.Text(cerceve, width=70, height=30, wrap="word", font=("Helvatica", 16))
scroll = tk.Scrollbar(cerceve)
sohbet.configure(yscrollcommand=scroll.set)
sohbet.pack(side=tk.LEFT)
  
scroll.config(command=sohbet.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)


textMesaj = tk.Entry(root, width=70, font=("Helvatica", 14))
textMesaj.pack()

gonder = tk.Button(root, text='Send', command=gonder_message, cursor="hand1", width=30, height=2, bg='blue', fg='red')
gonder.pack(side=tk.LEFT)


temizle = tk.Button(root, text='Clear', command=mesaj_temizle, cursor="hand1", width=30, height=2, bg='blue', fg='red')
temizle.pack(side=tk.RIGHT)




root.mainloop()
