import tkinter
import tkintermapview
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from AlgortimoProyecto import *

class App():
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

    ventana.button_1=customtkinter.CTkButton(master=ventana.frame_left, text="Search")

    def boton_llamada(ventana):
        x1 = ventana.entry.get()

    ventana.button_1.grid(pady=(20,0), padx=(20,20), row=0, column=0)

    # ======== Entry ==========
    ventana.entry1 = customtkinter.CTkEntry(master=ventana.frame_left, placeholder_text="Source: Type Coordinate")

    ventana.entry1.grid(row=3, column=0, sticky="we", padx=(20,20), pady=(40, 0))

    ventana.entry2 = customtkinter.CTkEntry(master=ventana.frame_left, placeholder_text="Target: Type Coordinate")

    ventana.entry2.grid(row=5, column=0, sticky="we", padx=(20,20), pady=(20, 0))

    #ventana.entry2.entry2.bind("<Return>", ventana.search_event)

    PlacesList = ['','("Plaza 2 de Mayo",31035122)']
    ventana.button_option = customtkinter.CTkOptionMenu(ventana.frame_left, values = PlacesList)


    ventana.button_option.grid(row=6, column=0, padx=(20, 20), pady=(10, 50))



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

    #===========================================================================================

    def search1_event(ventana):
        source = ventana.entry1.get()
        target = ventana.entry2.get()

        loadData('data/Lima_streets.csv', time, dataIntersections, rushHour = True)
        intersectionsList(dataIntersections, intersectionList, intersectionID, adjList)
        change()
        adjl(dataIntersections, adjList)

        #sourceIndex = intersectionList.index(['-12.0466783', '-77.0430483'])
        #targetIndex = intersectionList.index(['-12.0466949', '-77.042435'])
        sourceIndex = intersectionList.index([source, target])
        targetIndex = intersectionList.index(['-12.0466949', '-77.042435'])
        path = Dijkstra(adjList, sourceIndex, targetIndex)
        #print(path)
        prueba1 = []
        prueba1.append((int(source), int(target)))
        #prueba = [(-12.0459308,-77.0427831),(-12.0460958,-77.0430896)]
        polygon_1 = ventana.map_widget.set_polygon(prueba1, name="Prueba_pues")
        print("Listo we")
        #intersectionID.clear()
        #intersectionList.clear()
        #adjList.clear()

            



    







if __name__=="__main__":
    app = App()
    app.ventana.mainloop()

