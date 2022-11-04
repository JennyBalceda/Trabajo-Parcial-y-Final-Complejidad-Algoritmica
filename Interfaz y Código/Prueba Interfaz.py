import tkinter
import tkintermapview
from tkinter import *
from PIL import Image, ImageTk
import customtkinter


customtkinter.set_default_color_theme("blue")
# ========== create ventana =============
ventana = tkinter.Tk()
ventana.title("Find The Shortest Path")
ventana.geometry(f"{800}x{500}")

# ========== create to grid ==========
ventana.grid_columnconfigure(0, weight=0)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(0, weight=1)

ventana.frame_left = customtkinter.CTkFrame(master=ventana, width=150, corner_radius=0, fg_color=None)
ventana.frame_left.grid(row=0, column=0, padx=0, sticky="nsew")

ventana.frame_right = customtkinter.CTkFrame(master=ventana, corner_radius=0)
ventana.frame_right.grid(row=0, column=1, rowspan=1, padx=0, sticky="nsew")

# ================ left =====================

ventana.frame_left.grid_rowconfigure(2, weight=1)

ventana.button_1=customtkinter.CTkButton(master=ventana.frame_left, text="Find")

ventana.button_1.grid(pady=(20,0), padx=(20,20), row=0, column=0)

#ventana.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(ventana.frame_left, values=["(Plaza 2 de Mayo,31035122)"], command=ventana.change_appearance_mode)

#ventana.appearance_mode_optionemenu.grid(row=6, column=0, padx=(20, 20), pady=(10, 20))



# ============== create map widget ===============

ventana.frame_right.grid_rowconfigure(1, weight=1)
ventana.frame_right.grid_rowconfigure(0, weight=0)

ventana.frame_right.grid_columnconfigure(0, weight=1)
ventana.frame_right.grid_columnconfigure(1, weight=0)
ventana.frame_right.grid_columnconfigure(2, weight=1)


ventana.map_widget = tkintermapview.TkinterMapView(ventana.frame_right, corner_radius=0)
ventana.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0,0), pady=(0,0))

# ======= set current widget address In this case is Perú (Lima Metropolitana) ==============
ventana.map_widget.set_address("Perú, Lima, Lima")

# ===== prueba de marca ====
prueba = [(-12.0459308,-77.0427831),(-12.0460958,-77.0430896)]
polygon_1 = ventana.map_widget.set_polygon(prueba, name="Prueba_pues")

def change_appearance_mode(ventana, new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)
#Plaza 2 de Mayo,31035122,31035142
ventana.mainloop()

