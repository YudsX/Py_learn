# GUI -> Graphical User Interface
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
win = tk.Tk()
win.configure(bg ="white")
win.geometry("350x200")
win.resizable(False, False)
win.title("Warung pesanan mas Jowo")

# Input Frame 
input_frame = ttk.Frame(win)
# penempatan ada Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Variable dan fungsi:
JENIS = tk.StringVar()
LEVEL_KEPEDASAN = tk.StringVar()

def tombol_click():
    ''' Ini akan di panggil oleh tombol! '''

    pesan = f"Memesan {JENIS.get()} dengan Level kepedasan: {LEVEL_KEPEDASAN.get()}"
    showinfo(title="Pesanan dalam kiriman! ^_^ ", message= pesan)
    # PR tambahin jumlah pemesanan
    

# Komponen-Komponen:
# 1. Label untuk nama depan
nama_depan_label = ttk.Label(input_frame, text="Jenis nasgor : ")
nama_depan_label.pack(padx=10, pady=10, fill="x", expand=True)

# 2. Entry nama depan 
nama_depan_entry = ttk.Entry(input_frame, textvariable= JENIS)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label untuk nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Level kepedasan : ")
nama_belakang_label.pack(padx=10, pady=10, fill="x", expand=True)

# 4. Entry nama belakang 
nama_belakang_entry = ttk.Entry(input_frame, textvariable= LEVEL_KEPEDASAN)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. Button
tombol_sapa = ttk.Button(input_frame, text= "Selesai", command=tombol_click)
tombol_sapa.pack(pady=10, padx=10, fill="x", expand=True)


# main loop window nya biar ga mati
win.mainloop()