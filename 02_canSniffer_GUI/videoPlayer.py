import cv2
import tkinter as tk
from PIL import Image, ImageTk

# vytvoření okna pomocí tkinter
root = tk.Tk()
root.title("Kamera")

# vytvoření widgetu pro zobrazení výstupu kamery
label = tk.Label(root)
label.pack()

# inicializace kamery pomocí OpenCV
cap = cv2.VideoCapture(0)

def update_frame():
    # získání snímku z kamery
    ret, frame = cap.read()

    # konverze snímku do formátu, který lze zobrazit v tkinter
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img_tk = ImageTk.PhotoImage(image=img)

    # aktualizace widgetu s obrazem z kamery
    label.img_tk = img_tk
    label.config(image=img_tk)

    # opakování aktualizace každých 10 milisekund
    root.after(10, update_frame)

# spuštění funkce pro aktualizaci obrazovky
update_frame()

# spuštění hlavní smyčky aplikace
root.mainloop()

# uvolnění kamery
cap.release()