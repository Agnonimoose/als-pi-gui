import os
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as font
from tkinter import ttk
import time
import pygame
import json

# admin_window = None
# appointments_config_window = None
#
#
#
#
# def open_main_window():
#     global main_window
#     if main_window:
#         main_window.destroy()
#     main_window = tk.Toplevel()
#     main_window.title("Main Interface")
#     main_window.attributes("-fullscreen", True)
#     main_label = tk.Label(main_window, text="Main Interface")
#     main_label.pack()
#     admin_button = tk.Button(main_window, text="Admin Interface", command=toggle_admin_interface)
#     admin_button.pack()
#
#     image = Image.open(r'C:\Users\PC User\PycharmProjects\alsGui\als-pi-gui\alsGui\j.jpg')
#     image = image.resize((50, 50), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(image)
#     pictures_button = tk.Button(main_window, text="Pictures Interface", image=img, compound = tk.LEFT, command=toggle_pictures_interface)
#     pictures_button.pack()
#
#     music_button = tk.Button(main_window, text="Music Interface", command=toggle_music_interface)
#     music_button.pack()
#
#
# def toggle_appointments_config_interface():
#     global appointments_config_window
#     try:
#         appointments_window.destroy()
#     except:
#         pass
#     try:
#         admin_window.destroy()
#     except:
#         pass
#     if appointments_config_window:
#         appointments_config_window.destroy()
#     appointments_config_window = tk.Toplevel()
#     appointments_config_window.attributes("-fullscreen", True)
#     appointments_config_label = tk.Label(appointments_config_window, text="Appointments Configuration Interface")
#     appointments_config_label.pack()
#     go_back_button = tk.Button(appointments_config_window, text="Go Back", command=open_main_window)
#     go_back_button.pack()
#     name_label = tk.Label(appointments_config_window, text="Name of the appointment:")
#     name_label.pack()
#     name_entry = tk.Entry(appointments_config_window)
#     name_entry.pack()
#     location_label = tk.Label(appointments_config_window, text="Location of the appointment:")
#     location_label.pack()
#     location_entry = tk.Entry(appointments_config_window)
#     location_entry.pack()
#     time_label = tk.Label(appointments_config_window, text="Time of the appointment:")
#     time_label.pack()
#     time_entry = tk.Entry(appointments_config_window)
#     time_entry.pack()
#     info_label = tk.Label(appointments_config_window, text="Additional Information:")
#     info_label.pack()
#     info_entry = tk.Text(appointments_config_window, height=5, width=30)
#     info_entry.pack()
#     submit_button = tk.Button(appointments_config_window, text="Submit",
#                               command=lambda: submit_appointment(name_entry.get(), location_entry.get(),
#                                                                  time_entry.get(), info_entry.get("1.0", 'end-1c')))
#     submit_button.pack()
#
#
# appointments_list = []
#
#
# def submit_appointment(name, location, time, info):
#     global appointments_list
#     appointments_list.append({"Name": name, "Location": location, "Time": time, "Additional Information": info})
#     appointments_config_window.destroy()
#
#
# appointments_window = None
#
#
# def toggle_admin_interface():
#     global admin_window
#     try:
#         appointments_window.destroy()
#     except:
#         pass
#     if admin_window:
#         admin_window.destroy()
#     admin_window = tk.Toplevel()
#     admin_window.title("Admin Interface")
#     admin_window.attributes("-fullscreen", True)
#     admin_label = tk.Label(admin_window, text="Admin Interface")
#     admin_label.pack()
#     go_back_button = tk.Button(admin_window, text="Go Back", command=admin_window.destroy)
#     go_back_button.pack()
#     appointments_config_button = tk.Button(admin_window, text="Appointments Configuration",
#                                            command=toggle_appointments_config_interface)
#     appointments_config_button.pack()
#     directions_config_button = tk.Button(admin_window, text="Directions Configuration",
#                                          command=toggle_directions_config_interface)
#     directions_config_button.pack()
#
#
# directions_config_window = None
#
#
# def toggle_directions_config_interface():
#     global directions_config_window
#     try:
#         admin_window.destroy()
#     except:
#         pass
#     if directions_config_window:
#         directions_config_window.destroy()
#     directions_config_window = tk.Toplevel()
#     directions_config_window.attributes("-fullscreen", True)
#     directions_config_label = tk.Label(directions_config_window, text="Directions Configuration Interface")
#     directions_config_label.pack()
#     go_back_button = tk.Button(directions_config_window, text="Go Back", command=toggle_admin_interface)
#     go_back_button.pack()
#     place_name_label = tk.Label(directions_config_window, text="Place Name:")
#     place_name_label.pack()
#     place_name_entry = tk.Entry(directions_config_window)
#     place_name_entry.pack()
#     place_location_label = tk.Label(directions_config_window, text="Place Location:")
#     place_location_label.pack()
#     place_location_entry = tk.Entry(directions_config_window)
#     place_location_entry.pack()
#     info_label = tk.Label(directions_config_window, text="Additional Information:")
#     info_label.pack()
#     info_entry = tk.Text(directions_config_window, height=5, width=30)
#     info_entry.pack()
#     submit_button = tk.Button(directions_config_window, text="Submit",
#                               command=lambda: submit_directions(name_entry.get(), location_entry.get(),
#                                                                 info_entry.get("1.0", 'end-1c')))
#     submit_button.pack()
#
#
# directions_list = []
#
#
# def submit_directions(name, location, info):
#     global directions_list
#     directions_list.append({"Place Name": name, "Place Location": location, "Additional Information": info})
#     directions_config_window.destroy()
#     open_main_window()
#
#
# def toggle_pictures_interface():
#     global main_interface_visible
#     global pictures_interface
#     if main_interface_visible:
#         root.withdraw()
#         pictures_interface = tk.Toplevel(root)
#         pictures_interface.title("Pictures Interface")
#         back_button = ttk.Button(pictures_interface, text="Go back", command=lambda: toggle_pictures_interface())
#         back_button.pack()
#         images_frame = tk.Frame(pictures_interface)
#         images_frame.pack()
#         # Get the list of images from the specified directory
#         images_folder = r"/home/gasu/Desktop/pictures"
#         images = os.listdir(images_folder)
#         # Load the images into memory and create a label for each one
#         for i, image in enumerate(images):
#             image_path = os.path.join(images_folder, image)
#             try:
#                 with Image.open(image_path) as img:
#                     img = img.resize((100, 100))
#                     tk_img = ImageTk.PhotoImage(img)
#                     image_label = ttk.Label(images_frame, image=tk_img)
#                     image_label.image = tk_img  # Keep a reference to prevent garbage collection
#                     image_label.grid(row=i // 4, column=i % 4)
#             except:
#                 pass
#         pictures_interface.attributes("-fullscreen", True)
#         main_interface_visible = False
#     else:
#         pictures_interface.destroy()
#         root.deiconify()
#         root.attributes("-fullscreen", True)
#         main_interface_visible = True
#
#
# # Global mp3_folder variable
# mp3_folder = r"/home/gasu/Desktop/music"
#
#
# def play_mp3(mp3_file):
#     pygame.mixer.init()
#     pygame.mixer.music.load(os.path.join(mp3_folder, mp3_file))
#     pygame.mixer.music.play()
#
#
# def toggle_music_interface():
#     global main_interface_visible
#     global music_interface
#     if main_interface_visible:
#         root.withdraw()
#         music_interface = tk.Toplevel(root)
#         music_interface.title("Music Interface")
#         back_button = ttk.Button(music_interface, text="Go back",
#                                  command=lambda: [music_interface.destroy(), root.deiconify()])
#         back_button.grid(row=0, column=0)
#         mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith('.mp3')]
#         for i, mp3_file in enumerate(mp3_files):
#             mp3_file_button = ttk.Button(music_interface, text=mp3_file, command=lambda file=mp3_file: play_mp3(file))
#             mp3_file_button.grid(row=i + 1, column=0)
#         stop_button = ttk.Button(music_interface, text="Stop", command=pygame.mixer.music.stop)
#         stop_button.grid(row=0, column=1)
#         music_interface.attributes("-fullscreen", True)
#         main_interface_visible = False
#     else:
#         music_interface.destroy()
#         root.deiconify()
#         root.attributes("-fullscreen", True)
#         main_interface_visible = True
#
#
# def toggle_appointments_interface():
#     try:
#         appointments_config_window.destroy()
#     except:
#         pass
#     try:
#         admin_window.destroy()
#     except:
#         pass
#
#     appointments_window = tk.Toplevel()
#     appointments_window.attributes("-fullscreen", True)
#     appointments_label = tk.Label(appointments_window, text="Appointments Interface")
#     appointments_label.pack()
#     go_back_button = tk.Button(appointments_window, text="Go Back", command=appointments_window.destroy)
#     go_back_button.pack()
#
#     # New label to display the next appointment information
#     next_appointment_label = tk.Label(appointments_window, text="Next Appointment Information:")
#     next_appointment_label.pack()
#
#     global appointments_info
#     appointments_info = tk.StringVar()
#     appointments_info.set("")
#     appointments_info_label = tk.Label(appointments_window, textvariable=appointments_info)
#     appointments_info_label.pack()
#
#     # Get the next appointment from the appointments list
#     if len(appointments_list) > 0:
#         appointments_info.set("\n".join(["Name: " + appointment['Name'] + "\nLocation: " + appointment[
#             'Location'] + "\nTime: " + appointment['Time'] + "\nAdditional Information: " + appointment[
#                                              'Additional Information'] for appointment in appointments_list]))
#     else:
#         appointments_info.set("No upcoming appointments.")
#
#
# def toggle_directions_interface():
#     global main_interface_visible
#     global directions_interface
#     if main_interface_visible:
#         root.withdraw()
#         directions_interface = tk.Toplevel(root)
#         directions_interface.title("Directions Interface")
#         back_button = ttk.Button(directions_interface, text="Go back", command=lambda: toggle_directions_interface())
#         back_button.pack()
#         directions_interface.attributes("-fullscreen", True)
#         main_interface_visible = False
#     else:
#         directions_interface.destroy()
#         root.deiconify()
#         root.attributes("-fullscreen", True)
#         main_interface_visible = True


# root = tk.Tk()
# root.title("Main Interface")
# root.attributes("-fullscreen", True)
#
# clock_label = tk.Label(root, font=("TkDefaultFont", 20))
# clock_label.pack(side=tk.TOP, pady=10)
#
#
# def update_clock():
#     current_time = time.strftime("%H:%M:%S")
#     clock_label.config(text=current_time)
#     root.after(1000, update_clock)
#


# class Window:
#     def __init__(self):
#         "Use a new image for the button"
#         self.root = tk.Tk()
#         self.root.title("Main Interface")
#         # self.root.attributes("-fullscreen", True)
#         self.clock_label = tk.Label(self.root, font=("TkDefaultFont", 20))
#         self.clock_label.pack(side=tk.TOP, pady=10)
#
#         self.root.mainloop()
#
#     def update_clock(self):
#         current_time = time.strftime("%H:%M:%S")
#         self.clock_label.config(text=current_time)
#         self.root.after(1000, update_clock)


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        tk.Tk.__init__(self, *args, **kwargs)
        self.style = ttk.Style(self)
        self.style.configure('homeButton.TButton', font =
                   ('calibri', 10, 'bold', 'underline'),
                    foreground = 'red', background='#31363b')

        self.style.configure('Main.TFrame',
                    background='#c1e5ff')

        self.title("Main Interface")
        # self.attributes("-fullscreen", True)
        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, ImagePage, MusicPage, AdminPage, DirectionsPage, AppointmentsPage):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        if hasattr(frame, "_reloadPage"):
            frame._reloadPage()
        frame.tkraise()


class MainPage(ttk.Frame):
    def __init__(self, parent, controller, style =  'Main.TFrame'):
        ttk.Frame.__init__(self, parent, style =  'Main.TFrame')
        label = tk.Label(self, text="Main Page")

        self.style =  'Main.TFrame'

        frame33 = ttk.Frame(self, style='Main.TFrame')
        
        frame33.configure(height=50, width=200)
        frame42 = ttk.Frame(frame33)
        frame42.configure(height=50, width=1000)

        switch_adminPae_button = adminButton(
            frame42,
            text="Admin",
            bg='#000000',
            fg='white',
            relief='flat',
            font = font.Font(size=30, weight="bold"),
            command=lambda: controller.show_frame(AdminPage),
        )
        switch_adminPae_button.pack(anchor="n", side="top")

        frame42.pack(anchor="e", side="top")
        frame45 = ttk.Frame(frame33)
        frame45.configure(height=200, width=200)
        self.clock_label = tk.Label(frame45, font=("TkDefaultFont", 20))
        self.clock_label.pack(side="top")
        frame45.pack(side="top")
        frame33.pack(expand="false", fill="x", side="top")
        frame33.pack_propagate(0)
        frame31 = ttk.Frame(self, style='Main.TFrame')
        frame31.configure(height=200, width=200)
        frame2 = ttk.Frame(frame31, style='Main.TFrame')
        frame2.grid(column=0, row=0)
        frame5 = ttk.Frame(frame31, style='Main.TFrame')
        frame5.configure(height=200, width=200)
        frame5.grid(column=0, row=1)
        frame6 = ttk.Frame(frame31, style='Main.TFrame')
        frame6.configure(height=200, width=200)
        frame6.grid(column=0, row=2)
        frame7 = ttk.Frame(frame31, style='Main.TFrame')
        frame7.configure(height=200, width=200)
        frame7.grid(column=0, row=3)
        frame18 = ttk.Frame(frame31, style='Main.TFrame')
        frame18.configure(height=200, width=200)
        frame18.grid(column=1, row=0)
        frame19 = ttk.Frame(frame31, style='Main.TFrame')
        frame19.configure(height=200, width=200)

        switch_imagePae_button = homeButton(
            frame19,
            text="Images",
            image=r'C:\Users\PC User\PycharmProjects\alsGui\als-pi-gui\alsGui\imgBtn.png',
            bg='#c1e5ff',
            relief='flat',
            command=lambda: controller.show_frame(ImagePage),
        )
        switch_imagePae_button.pack(expand="true", fill="both", padx=20, pady=20, side="top")


        frame19.grid(column=1, row=1, sticky="nsew")
        frame20 = ttk.Frame(frame31, style='Main.TFrame')
        frame20.configure(height=200, width=200)


        switch_directionsPage_button = homeButton(
            frame20,
            text="Directions",
            image=r'C:\Users\PC User\PycharmProjects\alsGui\als-pi-gui\alsGui\dirBtn.png',
            bg='#c1e5ff',
            relief='flat',
            command=lambda: controller.show_frame(DirectionsPage),
        )
        switch_directionsPage_button.pack(expand="true", fill="both", padx=20, pady=20, side="top")


        frame20.grid(column=1, row=2, sticky="nsew")
        frame21 = ttk.Frame(frame31, style='Main.TFrame')
        frame21.configure(height=200, width=200)
        frame21.grid(column=1, row=3)
        frame22 = ttk.Frame(frame31, style='Main.TFrame')
        frame22.configure(height=200, width=200)
        frame22.grid(column=2, row=0)
        frame23 = ttk.Frame(frame31, style='Main.TFrame')
        frame23.configure(height=200, width=200)


        switch_musicPage_button = homeButton(
            frame23,
            text="Music",
            image=r'C:\Users\PC User\PycharmProjects\alsGui\als-pi-gui\alsGui\musicBtn.png',
            bg='#c1e5ff',
            relief='flat',
            command=lambda: controller.show_frame(MusicPage),
        )
        switch_musicPage_button.pack(expand="true", fill="both", padx=20, pady=20, side="top")


        frame23.grid(column=2, row=1, sticky="nsew")
        frame24 = ttk.Frame(frame31, style='Main.TFrame')
        frame24.configure(height=200, width=200)

        switch_appointmentsPage_button = homeButton(
            frame24,
            text="Appointments",
            image=r'C:\Users\PC User\PycharmProjects\alsGui\als-pi-gui\alsGui\calBtn.png',
            bg='#c1e5ff',
            relief='flat',
            command=lambda: controller.show_frame(AppointmentsPage),
        )

        switch_appointmentsPage_button.pack(expand="true", fill="both", padx=20, pady=20, side="top")

        frame24.grid(column=2, row=2, sticky="nsew")
        frame25 = ttk.Frame(frame31, style='Main.TFrame')
        frame25.configure(height=200, width=200)
        frame25.grid(column=2, row=3)
        frame26 = ttk.Frame(frame31, style='Main.TFrame')
        frame26.configure(height=200, width=200)
        frame26.grid(column=3, row=0)
        frame27 = ttk.Frame(frame31, style='Main.TFrame')
        frame27.configure(height=200, width=200)
        frame27.grid(column=3, row=1)
        frame28 = ttk.Frame(frame31, style='Main.TFrame')
        frame28.configure(height=200, width=200)
        frame28.grid(column=3, row=2)
        frame29 = ttk.Frame(frame31, style='Main.TFrame')
        frame29.configure(height=200, width=200)
        frame29.grid(column=3, row=3)
        frame31.pack(side="top")
        self.configure(height=200, width=200)
        self.pack(expand="true", fill="both", side="top")

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.after(1000, self.update_clock)


class ImagePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Image Page")

        frame6 = ttk.Frame(self)
        frame6.configure(height=200, width=200)
        frame7 = ttk.Frame(frame6)
        frame7.configure(height=200, width=200)
        button1 = ttk.Button(frame7, command=lambda: self.backed())
        button1.configure(text='last')
        button1.pack(side="top")
        frame7.pack(side="left")
        frame11 = ttk.Frame(frame6)
        frame11.configure(height=200, width=200)
        self.picLabel = ttk.Label(frame11)
        self.picLabel.configure()
        self.picLabel.pack(side="top")
        frame11.pack(expand="true", fill="both", side="left")
        frame12 = ttk.Frame(frame6)
        frame12.configure(height=200, width=200)
        button2 = ttk.Button(frame12, command=lambda: self.nexted())
        button2.configure(text='next')
        button2.pack(side="top")
        frame12.pack(side="left")
        frame6.pack(expand="true", fill="both", side="top")
        frame8 = ttk.Frame(self)
        frame8.configure(height=50, width=200)

        switch_homePage_button =  ttk.Button(self, command=lambda: controller.show_frame(MainPage))
        switch_homePage_button.configure(text='Exit')
        switch_homePage_button.pack(side="top")

        frame8.pack(expand="false", fill="y", side="top")
        self.configure(height=200, width=200)

        self.picRoot = json.load(open("directories.json", "r"))["images"]



        self.files = os.listdir(self.picRoot)
        self.currentFile = 0
        self.totalFiles = len(self.files)
        self.loadedPic = None
        self.loadedTk = None

        self.loadPic()

    def backed(self):
        if self.currentFile == 0:
            self.currentFile = self.totalFiles
        else:
            self.currentFile -= 1
        self.loadPic()

    def nexted(self):
        if self.currentFile == self.totalFiles:
            self.currentFile = 0
        else:
            self.currentFile += 1
        self.loadPic()


    def loadPic(self):
        self.loadedPic = Image.open(self.picRoot + r"\\" + self.files[self.currentFile])
        self.loadedTk = ImageTk.PhotoImage(self.loadedPic)
        self.picLabel.configure(image=self.loadedTk)
        self.picLabel.image = self.loadedTk


class MusicPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Image Page")

        frame6 = ttk.Frame(self)
        frame6.configure(height=200, width=200)
        frame7 = ttk.Frame(frame6)
        frame7.configure(height=200, width=200)

        button1 = ttk.Button(frame7, command=lambda: self.backed())
        button1.configure(text='previous')
        button1.pack(side="top")

        frame7.pack(side="left")
        frame11 = ttk.Frame(frame6)
        frame11.configure(height=200, width=200)

        self.stopButton = ttk.Button(frame11, command=lambda: self.stop())
        self.stopButton.configure(text='stop')
        self.stopButton.pack(side="top")

        frame11.pack(expand="true", fill="both", side="left")
        frame12 = ttk.Frame(frame6)
        frame12.configure(height=200, width=200)

        button2 = ttk.Button(frame12, command=lambda: self.nexted())
        button2.configure(text='next')
        button2.pack(side="top")

        frame12.pack(side="left")
        frame6.pack(expand="true", fill="both", side="top")
        frame8 = ttk.Frame(self)
        frame8.configure(height=50, width=200)

        switch_homePage_button =  ttk.Button(self, command=lambda: controller.show_frame(MainPage))
        switch_homePage_button.configure(text='Exit')
        switch_homePage_button.pack(side="top")

        frame8.pack(expand="false", fill="y", side="top")
        self.configure(height=200, width=200)
        # self.pack(expand="true", fill="both", side="top")

        self.musicRoot = json.load(open("directories.json", "r"))["music"]

        self.files = os.listdir(self.musicRoot)
        self.currentFile = 0
        self.totalFiles = len(self.files)
        self.loadedMusic = None
        self.loadedTk = None

        self.loadMusic()

    def backed(self):
        if self.currentFile == 0:
            self.currentFile = self.totalFiles
        else:
            self.currentFile -= 1
        self.loadMusic()

    def nexted(self):
        if self.currentFile == self.totalFiles:
            self.currentFile = 0
        else:
            self.currentFile += 1
        self.loadMusic()


    def loadMusic(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.musicRoot + r"\\" + self.files[self.currentFile])
        pygame.mixer.music.play()


    def stop(self):
        pygame.mixer.music.stop()


class AdminPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        frame2 = ttk.Frame(self)
        frame2.configure(height=200, width=200)
        frame19 = ttk.Frame(frame2)
        frame19.configure(height=200, width=200)
        self.DirectionsConfig = ttk.Label(frame19)
        self.DirectionsConfig.configure(text='Directions Config')
        self.DirectionsConfig.pack(side="top")
        frame19.grid(column=0, columnspan=2, row=0, sticky="nsew")
        frame20 = ttk.Frame(frame2)
        frame20.configure(height=200, width=200)
        self.PlaceNameLab = ttk.Label(frame20)
        self.PlaceNameLab.configure(text='Place Name')
        self.PlaceNameLab.pack(side="top")
        frame20.grid(column=0, row=1, sticky="nsew")
        frame21 = ttk.Frame(frame2)
        frame21.configure(height=200, width=200)
        self.placeName = ttk.Entry(frame21)
        self.placeName.pack(side="top")
        frame21.grid(column=1, row=1, sticky="nsew")
        frame22 = ttk.Frame(frame2)
        frame22.configure(height=200, width=200)
        self.placeLocLab = ttk.Label(frame22)
        self.placeLocLab.configure(text='Place Location')
        self.placeLocLab.pack(side="top")
        frame22.grid(column=0, row=2, sticky="nsew")
        frame23 = ttk.Frame(frame2)
        frame23.configure(height=200, width=200)
        self.placeLoc = ttk.Entry(frame23)
        self.placeLoc.pack(side="top")
        frame23.grid(column=1, row=2, sticky="nsew")
        frame24 = ttk.Frame(frame2)
        frame24.configure(height=200, width=200)
        self.plaeAddInfoLab = ttk.Label(frame24)
        self.plaeAddInfoLab.configure(text='Additional Info')
        self.plaeAddInfoLab.pack(side="top")
        frame24.grid(column=0, row=3, sticky="nsew")
        frame25 = ttk.Frame(frame2)
        frame25.configure(height=200, width=200)
        self.plaeAddInfo = ttk.Entry(frame25)
        self.plaeAddInfo.pack(side="top")
        frame25.grid(column=1, row=3, sticky="nsew")
        frame26 = ttk.Frame(frame2)
        frame26.configure(height=200, width=200)
        self.addDir = ttk.Button(frame26, command=lambda: self.addDirection())
        self.addDir.configure(text='+ Add Direction')
        self.addDir.pack(side="top")
        frame26.grid(column=0, columnspan=2, row=4, sticky="nsew")
        frame2.pack(side="top")
        frame3 = ttk.Frame(self)
        frame3.configure(height=200, width=200)
        frame5 = ttk.Frame(frame3)
        frame5.configure(height=200, width=200)
        self.appNameLab = ttk.Label(frame5)
        self.appNameLab.configure(text='Name of Appointment')
        self.appNameLab.pack(side="top")
        frame5.grid(column=0, row=1, sticky="nsew")
        frame7 = ttk.Frame(frame3)
        frame7.configure(height=200, width=200)
        self.appointmentName = ttk.Entry(frame7)
        self.appointmentName.pack(side="top")
        frame7.grid(column=1, row=1, sticky="nsew")
        frame8 = ttk.Frame(frame3)
        frame8.configure(height=200, width=200)
        self.appPlaceLab = ttk.Label(frame8)
        self.appPlaceLab.configure(text='Place of Appointment')
        self.appPlaceLab.pack(side="top")
        frame8.grid(column=0, row=2, sticky="nsew")
        frame9 = ttk.Frame(frame3)
        frame9.configure(height=200, width=200)
        self.appPlace = ttk.Entry(frame9)
        self.appPlace.pack(side="top")
        frame9.grid(column=1, row=2, sticky="nsew")
        frame10 = ttk.Frame(frame3)
        frame10.configure(height=200, width=200)
        self.appTimeLab = ttk.Label(frame10)
        self.appTimeLab.configure(text='Time of Appointment')
        self.appTimeLab.pack(side="top")
        frame10.grid(column=0, row=3, sticky="nsew")
        frame11 = ttk.Frame(frame3)
        frame11.configure(height=200, width=200)
        self.appTime = ttk.Entry(frame11)
        self.appTime.pack(side="top")
        frame11.grid(column=1, row=3, sticky="nsew")
        frame12 = ttk.Frame(frame3)
        frame12.configure(height=200, width=200)
        self.appAdditionalInfoLab = ttk.Label(frame12)
        self.appAdditionalInfoLab.configure(text='Additional Info')
        self.appAdditionalInfoLab.pack(side="top")
        frame12.grid(column=0, row=4, sticky="nsew")
        frame13 = ttk.Frame(frame3)
        frame13.configure(height=200, width=200)
        self.appAddIndo = ttk.Entry(frame13)
        self.appAddIndo.pack(side="top")
        frame13.grid(column=1, row=4, sticky="nsew")
        frame14 = ttk.Frame(frame3)
        frame14.configure(height=200, width=200)
        self.appAppointment = ttk.Button(frame14, command=lambda: self.addAppointment())
        self.appAppointment.configure(text='+ Add Appointment')
        self.appAppointment.pack(side="top")
        frame14.grid(column=0, columnspan=2, row=5, sticky="nsew")
        frame18 = ttk.Frame(frame3)
        frame18.configure(height=200, width=200)
        self.Appointments = ttk.Label(frame18)
        self.Appointments.configure(text='Appointments Config')
        self.Appointments.pack(side="top")
        frame18.grid(column=0, columnspan=2, row=0, sticky="nsew")
        frame3.pack(pady=50, side="top")
        frame28 = ttk.Frame(self)
        frame28.configure(height=200, width=200)
        frame29 = ttk.Frame(frame28)
        frame29.configure(height=200, width=200)
        self.clockTimeLabel = ttk.Label(frame29)
        self.clockTimeLabel.configure(text='Clock Time')
        self.clockTimeLabel.pack(side="top")
        frame29.grid(column=0, row=1, sticky="nsew")
        frame30 = ttk.Frame(frame28)
        frame30.configure(height=200, width=200)
        self.clockTime = ttk.Entry(frame30)
        self.clockTime.pack(side="top")
        frame30.grid(column=1, row=1, sticky="nsew")
        frame37 = ttk.Frame(frame28)
        frame37.configure(height=200, width=200)
        self.clockButton = ttk.Button(frame37)
        self.clockButton.configure(text='Set Clock')
        self.clockButton.pack(side="top")
        frame37.grid(column=0, columnspan=2, row=5, sticky="nsew")
        frame38 = ttk.Frame(frame28)
        frame38.configure(height=200, width=200)
        self.clockSettingsLab = ttk.Label(frame38)
        self.clockSettingsLab.configure(text='Clock Settings')
        self.clockSettingsLab.pack(side="top")
        frame38.grid(column=0, columnspan=2, row=0, sticky="nsew")
        frame28.pack(pady=50, side="top")
        frame39 = ttk.Frame(self)
        frame39.configure(height=200, width=200)
        self.exitButton = ttk.Button(frame39, command=lambda: controller.show_frame(MainPage))
        self.exitButton.configure(text='Exit')
        self.exitButton.pack(side="top")
        frame39.pack(side="top")
        self.configure(height=200, width=200)

    def addAppointment(self):
        appointements = json.load(open("appointments.json", "r"))
        tmp = {
            'name': self.appointmentName.get(),
            'place': self.appPlace.get(),
            'time': self.appTime.get(),
            'info': self.appAddIndo.get()
        }
        self.appointmentName.delete(0, 'end')
        self.appPlace.delete(0, 'end')
        self.appTime.delete(0, 'end')
        self.appAddIndo.delete(0, 'end')

        appointements.append(tmp)
        json.dump(appointements, open("appointments.json", "w"))

    def addDirection(self):
        directions = json.load(open("directions.json", "r"))
        tmp = {
            'name': self.placeName.get(),
            'location': self.placeLoc.get(),
            'info': self.plaeAddInfo.get()
        }
        self.placeName.delete(0, 'end')
        self.placeLoc.delete(0, 'end')
        self.plaeAddInfo.delete(0, 'end')

        directions.append(tmp)
        json.dump(directions, open("directions.json", "w"))

class DirectionsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.directionLabel = ttk.Label(self)
        self.directionLabel.configure(text='Directions to add')
        self.directionLabel.pack(side="top")

        self.homButton = ttk.Button(self, command=lambda: controller.show_frame(MainPage))
        self.homButton.configure(text='Exit')
        self.homButton.pack(side="top")

    def _reloadPage(self):
        directions = json.load(open("directions.json", "r"))
        if len(directions) > 0:
            self.directionLabel["text"] = ("\n\n".join(["Name: " + x['name'] + "\nLocation: " + x['location'] + "\nAdditional Information: " + x['info'] for x in directions])) + "\n\n"
        else:
            self.directionLabel["text"] = ("no directions recorded yet\n\n")

class AppointmentsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.appointmentsLabel = ttk.Label(self)
        self.appointmentsLabel.configure(text='Appointments to add')
        self.appointmentsLabel.pack(side="top")

        self.homButton = ttk.Button(self, command=lambda: controller.show_frame(MainPage))
        self.homButton.configure(text='Exit')
        self.homButton.pack(side="top")

    def _reloadPage(self):
        appointments = json.load(open("appointments.json", "r"))
        if len(appointments) > 0:
            self.appointmentsLabel["text"] = ("\n\n".join(["Name: " + x['name'] + "\nPlace: " + x['place'] + "\nTime: " + x['time'] + "\nAdditional Information: " + x['info'] for x in appointments])) + "\n\n"
        else:
            self.appointmentsLabel["text"] = ("no appointments recorded yet\n\n")

class homeButton(tk.Button):
    def __init__(self, parent, **kwargs):
        if "image" in kwargs:
            self.image = Image.open(kwargs['image'])
            self.image = self.image.resize((60, 60), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.image)
            kwargs['image']=self.img
            kwargs['compound'] = tk.TOP
        super().__init__(parent, **kwargs)



class adminButton(tk.Button):
    def __init__(self, parent, **kwargs):
        if "image" in kwargs:
            self.image = Image.open(kwargs['image'])
            self.image = self.image.resize((50, 50), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self, self.image)

            kwargs['image'] = self.img

        super().__init__(parent, **kwargs)


#
# update_clock()
#
# # Create the main interface with buttons to access the other interfaces
# main_interface_visible = True
# header_frame = ttk.Frame(root)
# header_frame.pack(side=tk.TOP, fill=tk.X)
# admin_button = ttk.Button(header_frame, text="Admin", command=lambda: toggle_admin_interface())
# admin_button.pack(side=tk.RIGHT)
#
# interface_frame = ttk.Frame(root)
# interface_frame.pack()
#
# # image = Image.open(r'C:\Users\PC User\PycharmProjects\alsGui\als-pi-gui\alsGui\j.jpg')
# # image = image.resize((50, 50), Image.ANTIALIAS)
# # img = ImageTk.PhotoImage(image)
# pictures_button = homeButton(interface_frame, text="Images", style="homeButtons", image=r'C:\Users\PC User\PycharmProjects\alsGui\als-pi-gui\alsGui\j.jpg', compound=tk.TOP, command=toggle_pictures_interface)
# # pictures_button = ttk.Button(interface_frame, text="Images", style="homeButtons", image=img, compound=tk.TOP, command=toggle_pictures_interface)
# # pictures_button = ttk.Button(interface_frame, text="Pictures", command=lambda: toggle_pictures_interface())
# pictures_button.grid(row=0, column=0)
#
# music_button = ttk.Button(interface_frame, text="Music", command=lambda: toggle_music_interface())
# music_button.grid(row=0, column=1)
# appointments_button = tk.Button(root, text="Appointments", command=toggle_appointments_interface)
# appointments_button.pack()
# directions_button = ttk.Button(interface_frame, text="Directions", command=lambda: toggle_directions_interface())
# directions_button.grid(row=1, column=1)
#
# root.mainloop()

if __name__ == "__main__":
    w = Window()
    w.mainloop()






