import time
from tkinter import Button, Frame, Label

from Libs.pyImage.Image import Image
from Libs.pyLogger.Logger import Logger
from Libs.pyUtils.pyData import JSON
from System.core.kernel import KRNL_Bug_check
from System.programs.File_manager.File_manager import File_manager
from System.programs.Map.Map import Map
from System.programs.Terminal.Terminal import WM_Terminal, DE_Terminal
from System.shell.Boot.Desktop.Startmenu import startmenu
from System.shell.Boot.Desktop.Taskbar import Taskbar_button
from System.shell.Message_box import MessageBox
from System.utils.utils import Execute
from System.utils.vars import Assets_directory, XCursor_2

__author__ = 'TheBigEye'
__version__ = '2.1'

BOOT_DATA_FILE = (Assets_directory + "/Data/System data/Boot/Boot.json")
DESKTOP_MODE = JSON.get(BOOT_DATA_FILE, "Desktop_mode")


def Terminal_programm(master):
    if DESKTOP_MODE == 0:
        Execute(master, 400, WM_Terminal, master, True)
    elif DESKTOP_MODE == 1:
        Execute(master, 400, DE_Terminal, master, True)


def File_manager_programm(master):
    Execute(master, 1000, File_manager, master, True)


def Browser_programm(master):
    MessageBox(master, "this may not work very well", "Warning", True)
    #Execute(master, 1200, Browser, master, True) # REMOVED: Browser is not working properly and will be fixed in the future.
    for widget in master.winfo_children():
        widget.destroy()

    KRNL_Bug_check(master, "0x00000007", "#ffffff", "#000000")


def Map_programm(master):
    Execute(master, 800, Map, master, True)


class Desktop(Frame):
    def __init__(self, master):

        Frame.__init__(self, master)

        self.master = master

        # Initialize the desktop
        Desktop.desktop_initializer(self)
        Logger.info("### Desktop initialized!")

    # -------------------------------------------------------------[ Desktop ]--------------------------------------------------------------

    def desktop_initializer(self):

        Logger.info("### Loading desktop enviroment ...")

        # Initialize the Wallpaper
        self.Wallpaper_image = Image.setImage("Assets/Shell/Desktop/Wallpapers/Space_panorama.png")
        self.Wallpaper = Label(
            self.master,
            image=self.Wallpaper_image,
            borderwidth="0",
            relief="flat",
            bg="#001023"
        )
        self.Wallpaper.place(x=0, y=0)
        Logger.info("Wallpaper processed and loaded")

        # Initialize the Cursor
        self.master.configure(background="#001023", cursor=XCursor_2)
        Logger.info("Cursor processed and loaded")

        # Initialize the Taskbar
        self.Taskbar_image = Image.setImage("Assets/Shell/Desktop/Taskbar/Taskbar.png")
        self.Taskbar = Label(
            self.master,
            width=740,
            height=29,
            borderwidth="0",
            image=self.Taskbar_image,
            background="black",
            foreground="gray",
            relief="flat",
        )
        self.Taskbar.place(x=109, y=571)
        self.Taskbar.lift()
        Logger.info("Taskbar processed and loaded")

        # Initialize the Start bar
        self.Startbar_image = Image.setImage("Assets/Shell/Desktop/Taskbar/Startbar.png")
        self.Startbar = Label(
            self.master,
            width=109,
            height=29,
            borderwidth="0",
            image=self.Startbar_image,
            background="white",
            foreground="gray",
            relief="flat",
        )
        self.Startbar.place(x=0, y=571)
        self.Startbar.lift()
        Logger.info("Startbar processed and loaded")

        # Initialize the Clockbar
        self.Clockbar_image = Image.setImage("Assets/Shell/Desktop/Taskbar/Clockbar.png")
        self.Clockbar = Label(
            self.master,
            width=284,
            height=29,
            borderwidth="0",
            image=self.Clockbar_image,
            background="white",
            foreground="gray",
            relief="flat",
        )
        self.Clockbar.place(x=849, y=571)
        self.Clockbar.lift()
        Logger.info("Clockbar processed and loaded")

        # Initialize the Start menu
        startmenu(self.master, self.Startbar)

        # -------------------------------------------------------------[ Startbar buttons ]-----------------------------------------------------------

        # Modules icon in startbar
        self.Modules_startbar_button = Taskbar_button(
            self.Startbar,
            button_image_path="Assets/Shell/Desktop/Taskbar/Modules_icon.png",
            master_image_path="Assets/Shell/Desktop/Taskbar/Startbar.png",
            position=(37, 2)
        )
        self.Modules_startbar_button.bind("<Button-1>", lambda event: Map_programm(self.master))
        self.Modules_startbar_button.place(x=37, y=2)
        Logger.info("Modules icon loaded on startbar")

        # Search icon in startbar
        self.Search_startbar_button = Taskbar_button(
            self.Startbar,
            button_image_path="Assets/Shell/Desktop/Taskbar/Search_icon.png",
            master_image_path="Assets/Shell/Desktop/Taskbar/Startbar.png",
            position=(68, 2)
        )
        self.Search_startbar_button.bind("<Button-1>",
                                         lambda event: MessageBox(self.master, "This feature is not yet available",
                                                                  "Warning", True))
        self.Search_startbar_button.place(x=68, y=2)
        Logger.info("Search icon loaded on startbar")

        # -------------------------------------------------------------[ Taskbar buttons ]-----------------------------------------------------------

        # Terminal icon in taskbar
        self.Terminal_taskbar_button = Taskbar_button(
            self.Taskbar,
            button_image_path="Assets/Shell/Programs/Terminal/Terminal_icon.png",
            master_image_path="Assets/Shell/Desktop/Taskbar/Taskbar.png",
            position=(109, 2)
        )
        self.Terminal_taskbar_button.bind("<Button-1>", lambda event: Terminal_programm(self.master))
        self.Terminal_taskbar_button.update_idletasks()
        Logger.info("Terminal icon loaded on taskbar")

        # File manager icon in taskbar
        self.File_manager_taskbar_button = Taskbar_button(
            self.Taskbar,
            button_image_path="Assets/Shell/Programs/File manager/File_manager_icon.png",
            master_image_path="Assets/Shell/Desktop/Taskbar/Taskbar.png",
            position=(109, 2)
        )
        self.File_manager_taskbar_button.bind("<Button-1>", lambda event: File_manager_programm(self.master))
        self.File_manager_taskbar_button.update_idletasks()
        Logger.info("File manager icon loaded on taskbar")

        # Browser icon in taskbar
        self.Browser_taskbar_button = Taskbar_button(
            self.Taskbar,
            button_image_path="Assets/Shell/Programs/Browser/Browser_icon.png",
            master_image_path="Assets/Shell/Desktop/Taskbar/Taskbar.png",
            position=(109, 2)
        )
        self.Browser_taskbar_button.bind("<Button-1>", lambda event: Browser_programm(self.master))
        self.Browser_taskbar_button.update_idletasks()
        Logger.info("Browser icon loaded on taskbar")

        # se crea una lista de los botones de la barra de tarea
        self.taskbar_buttons = [self.Terminal_taskbar_button, self.File_manager_taskbar_button,
                                self.Browser_taskbar_button]

        # los botones se posicionan en la barra de tareas en el orden de la lista
        for i in range(len(self.taskbar_buttons)):
            self.taskbar_buttons[i].place(x=8 + (i * 32), y=2)
        Logger.info("Taskbar buttons loaded and palced")

        # self.master.after(2000, Welcome_dialog(self.master, False))

        # -------------------------------------------------------------[ Clockbar ]-----------------------------------------------------------

        # Clock icon in clockbar
        def clock():
            Time = time.strftime("%I:%M %p")
            Date = time.strftime("%d/%m/%Y")

            ClockStr = ""
            ClockStr += Time
            ClockStr += "\n"
            ClockStr += Date

            self.Clock.config(text=ClockStr)
            self.Clock.after(200, clock)

        self.Clock = Label(
            self.Clockbar,
            width=12,
            height=2,
            borderwidth="0",
            background="#002C4F",
            foreground="#F3F3F3",
            relief="flat",
            font=("Segoe UI Semibold", 7),
            text="",
        )
        self.Clock.place(x=96, y=0.5)
        clock()
        Logger.info("Clock component loaded")

        # Sound volume icon in clockbar
        self.Sound_button = Image.setImage("Assets/Shell/Desktop/Taskbar/high-volume.png", (24, 24), "#ff00ff",
                                           "#002C4F")
        self.Sound_button_light = Image.setImage("Assets/Shell/Desktop/Taskbar/high-volume.png", (24, 24), "#ff00ff",
                                                 "#004C82")
        self.Sound_clockbar_button = Button(
            self.Clockbar,
            width=16,
            height=32,
            borderwidth="0",
            relief="flat",
            bg="#002C4F",
            activebackground="#002C4F",
            image=self.Sound_button
        )
        self.Sound_clockbar_button.bind("<Button-1>",
                                        lambda event: MessageBox(self.master, "In development...", "Info", True))
        self.Sound_clockbar_button.bind("<Enter>",
                                        lambda event: self.Sound_clockbar_button.config(image=self.Sound_button_light))
        self.Sound_clockbar_button.bind("<Leave>",
                                        lambda event: self.Sound_clockbar_button.config(image=self.Sound_button))
        Logger.info("Sound volume icon loaded on clockbar")

        # Battery icon in clockbar
        self.Battery_button = Image.setImage("Assets/Shell/Desktop/Taskbar/high-battery.png", (24, 24), "#ff00ff",
                                             "#002C4F")
        self.Battery_button_light = Image.setImage("Assets/Shell/Desktop/Taskbar/high-battery.png", (24, 24), "#ff00ff",
                                                   "#004C82")
        self.Battery_clockbar_button = Button(
            self.Clockbar,
            width=16,
            height=32,
            borderwidth="0",
            relief="flat",
            bg="#002C4F",
            activebackground="#002C4F",
            image=self.Battery_button
        )
        self.Battery_clockbar_button.bind("<Button-1>",
                                          lambda event: MessageBox(self.master, "Nice error :)", "Error", True))
        self.Battery_clockbar_button.bind("<Enter>", lambda event: self.Battery_clockbar_button.config(
            image=self.Battery_button_light))
        self.Battery_clockbar_button.bind("<Leave>",
                                          lambda event: self.Battery_clockbar_button.config(image=self.Battery_button))
        Logger.info("Battery icon loaded on clockbar")

        # Internet icon in clockbar
        self.Internet_button = Image.setImage("Assets/Shell/Desktop/Taskbar/high-internet.png", (24, 24), "#ff00ff",
                                              "#002C4F")
        self.Internet_button_light = Image.setImage("Assets/Shell/Desktop/Taskbar/high-internet.png", (24, 24),
                                                    "#ff00ff", "#004C82")
        self.Internet_clockbar_button = Button(
            self.Clockbar,
            width=16,
            height=32,
            borderwidth="0",
            relief="flat",
            bg="#002C4F",
            activebackground="#002C4F",
            image=self.Internet_button
        )
        self.Internet_clockbar_button.bind("<Button-1>",
                                           lambda event: MessageBox(self.master, "Nice warning :)", "Warning", True))
        self.Internet_clockbar_button.bind("<Enter>", lambda event: self.Internet_clockbar_button.config(
            image=self.Internet_button_light))
        self.Internet_clockbar_button.bind("<Leave>", lambda event: self.Internet_clockbar_button.config(
            image=self.Internet_button))
        Logger.info("Internet icon loaded on clockbar")

        # se crea una lista de los botones de la barra de tarea
        self.clockbar_buttons = [self.Battery_clockbar_button, self.Internet_clockbar_button,
                                 self.Sound_clockbar_button]

        # los botones se posicionan en la barra de tareas en el orden de la lista
        for i in range(len(self.clockbar_buttons)):
            self.clockbar_buttons[i].place(x=16 + (i * 24), y=-2)
        Logger.info("Clockbar buttons loaded and palced")
