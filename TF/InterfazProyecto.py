import tkinter
import tkintermapview
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from AlgortimoProyecto import *


customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    
    
    
    APP_NAME = "Find The Shortest Path"
    WIDTH = 800
    HEIGHT = 500
    def __init__(self):

        super().__init__()
        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH)+"x"+str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.maker_list = []


        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, padx=0, sticky="nsew")

        # ================ left =====================

        self.frame_left.grid_rowconfigure(2, weight=1)

        self.button_1=customtkinter.CTkButton(master=self.frame_left, text="Search", command= self.search_event)

        def boton_llamada(self):
            x1 = self.entry.get()

        self.button_1.grid(pady=(20,0), padx=(20,20), row=0, column=0)

        # ======== Entry ==========
        self.entry1 = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="Origin Coordinate: Source")

        self.entry1.grid(row=5, column=0, sticky="we", padx=(20,20), pady=(20, 0))

        self.entry2 = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="Origin Coordinate: Target")

        self.entry2.grid(row=4, column=0, sticky="we", padx=(20,20), pady=(20, 0))

        self.entry3 = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="Arrival Coordinate: Source")

        self.entry3.grid(row=3, column=0, sticky="we", padx=(20,20), pady=(20, 0))

        self.entry4 = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="Arrival Coordinate: Target")

        self.entry4.grid(row=3, column=0, sticky="we", padx=(20,20), pady=(120, 0))

        

        PlacesList = ['','("Plaza 2 de Mayo",31035122)']
        self.button_option = customtkinter.CTkOptionMenu(self.frame_left, values = PlacesList)


        self.button_option.grid(row=6, column=0, padx=(20, 20), pady=(10, 50))



        # ============== create map widget ===============

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)

        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)


        self.map_widget = tkintermapview.TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0,0), pady=(0,0))

        # ======= set current widget address in this case is Perú (Lima Metropolitana) ==============
        self.map_widget.set_address("Perú, Lima, Lima")

        # ===== prueba de marca ====
        prueba = [(-12.0459308,-77.0427831),(-12.0460958,-77.0430896)]
        #polygon_1 = self.map_widget.set_polygon(prueba, name="Prueba_pues")


        

        

    def search_event(self):
        prueba1 = []
        loadData('./data/Lima_streets.csv', time, dataIntersections, rushHour = True)
        intersectionsList(dataIntersections, intersectionList, intersectionID, adjList)
        change()
        adjl(dataIntersections, adjList)
        source1 = self.entry1.get()
        target1 = self.entry2.get()
        source2 = self.entry3.get()
        target2 = self.entry4.get()
        sourceIndex = intersectionList.index([source1, target1])
        targetIndex = intersectionList.index([source2, target2])
        path = Dijkstra(adjList, sourceIndex, targetIndex)
        print(path)
        prueba1 = PathFind(path)
        polygon_1 = self.map_widget.set_polygon(prueba1, name="Prueba_pues")
        print("Listo we")
        intersectionID.clear()
        intersectionList.clear()
        adjList.clear()

      

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__=="__main__":
    app = App()
    app.start()

                




