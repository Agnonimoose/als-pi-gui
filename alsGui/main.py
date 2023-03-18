import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import time
import pygame

admin_window = None
appointments_config_window = None


def open_main_window():
    global main_window
    if main_window:
        main_window.destroy()
    main_window = tk.Toplevel()
    main_window.title("Main Interface")
    main_window.attributes("-fullscreen", True)
    main_label = tk.Label(main_window, text="Main Interface")
    main_label.pack()
    admin_button = tk.Button(main_window, text="Admin Interface", command=toggle_admin_interface)
    admin_button.pack()
    pictures_button = tk.Button(main_window, text="Pictures Interface", command=toggle_pictures_interface)
    pictures_button.pack()
    music_button = tk.Button(main_window, text="Music Interface", command=toggle_music_interface)
    music_button.pack()


def toggle_appointments_config_interface():
    global appointments_config_window
    try:
        appointments_window.destroy()
    except:
        pass
    try:
        admin_window.destroy()
    except:
        pass
    if appointments_config_window:
        appointments_config_window.destroy()
    appointments_config_window = tk.Toplevel()
    appointments_config_window.attributes("-fullscreen", True)
    appointments_config_label = tk.Label(appointments_config_window, text="Appointments Configuration Interface")
    appointments_config_label.pack()
    go_back_button = tk.Button(appointments_config_window, text="Go Back", command=open_main_window)
    go_back_button.pack()
    name_label = tk.Label(appointments_config_window, text="Name of the appointment:")
    name_label.pack()
    name_entry = tk.Entry(appointments_config_window)
    name_entry.pack()
    location_label = tk.Label(appointments_config_window, text="Location of the appointment:")
    location_label.pack()
    location_entry = tk.Entry(appointments_config_window)
    location_entry.pack()
    time_label = tk.Label(appointments_config_window, text="Time of the appointment:")
    time_label.pack()
    time_entry = tk.Entry(appointments_config_window)
    time_entry.pack()
    info_label = tk.Label(appointments_config_window, text="Additional Information:")
    info_label.pack()
    info_entry = tk.Text(appointments_config_window, height=5, width=30)
    info_entry.pack()
    submit_button = tk.Button(appointments_config_window, text="Submit",
                              command=lambda: submit_appointment(name_entry.get(), location_entry.get(),
                                                                 time_entry.get(), info_entry.get("1.0", 'end-1c')))
    submit_button.pack()


appointments_list = []


def submit_appointment(name, location, time, info):
    global appointments_list
    appointments_list.append({"Name": name, "Location": location, "Time": time, "Additional Information": info})
    appointments_config_window.destroy()


appointments_window = None


def toggle_admin_interface():
    global admin_window
    try:
        appointments_window.destroy()
    except:
        pass
    if admin_window:
        admin_window.destroy()
    admin_window = tk.Toplevel()
    admin_window.title("Admin Interface")
    admin_window.attributes("-fullscreen", True)
    admin_label = tk.Label(admin_window, text="Admin Interface")
    admin_label.pack()
    go_back_button = tk.Button(admin_window, text="Go Back", command=admin_window.destroy)
    go_back_button.pack()
    appointments_config_button = tk.Button(admin_window, text="Appointments Configuration",
                                           command=toggle_appointments_config_interface)
    appointments_config_button.pack()
    directions_config_button = tk.Button(admin_window, text="Directions Configuration",
                                         command=toggle_directions_config_interface)
    directions_config_button.pack()


directions_config_window = None


def toggle_directions_config_interface():
    global directions_config_window
    try:
        admin_window.destroy()
    except:
        pass
    if directions_config_window:
        directions_config_window.destroy()
    directions_config_window = tk.Toplevel()
    directions_config_window.attributes("-fullscreen", True)
    directions_config_label = tk.Label(directions_config_window, text="Directions Configuration Interface")
    directions_config_label.pack()
    go_back_button = tk.Button(directions_config_window, text="Go Back", command=toggle_admin_interface)
    go_back_button.pack()
    place_name_label = tk.Label(directions_config_window, text="Place Name:")
    place_name_label.pack()
    place_name_entry = tk.Entry(directions_config_window)
    place_name_entry.pack()
    place_location_label = tk.Label(directions_config_window, text="Place Location:")
    place_location_label.pack()
    place_location_entry = tk.Entry(directions_config_window)
    place_location_entry.pack()
    info_label = tk.Label(directions_config_window, text="Additional Information:")
    info_label.pack()
    info_entry = tk.Text(directions_config_window, height=5, width=30)
    info_entry.pack()
    submit_button = tk.Button(directions_config_window, text="Submit",
                              command=lambda: submit_directions(name_entry.get(), location_entry.get(),
                                                                info_entry.get("1.0", 'end-1c')))
    submit_button.pack()


directions_list = []


def submit_directions(name, location, info):
    global directions_list
    directions_list.append({"Place Name": name, "Place Location": location, "Additional Information": info})
    directions_config_window.destroy()
    open_main_window()


def toggle_pictures_interface():
    global main_interface_visible
    global pictures_interface
    if main_interface_visible:
        root.withdraw()
        pictures_interface = tk.Toplevel(root)
        pictures_interface.title("Pictures Interface")
        back_button = ttk.Button(pictures_interface, text="Go back", command=lambda: toggle_pictures_interface())
        back_button.pack()
        images_frame = tk.Frame(pictures_interface)
        images_frame.pack()
        # Get the list of images from the specified directory
        images_folder = r"/home/gasu/Desktop/pictures"
        images = os.listdir(images_folder)
        # Load the images into memory and create a label for each one
        for i, image in enumerate(images):
            image_path = os.path.join(images_folder, image)
            try:
                with Image.open(image_path) as img:
                    img = img.resize((100, 100))
                    tk_img = ImageTk.PhotoImage(img)
                    image_label = ttk.Label(images_frame, image=tk_img)
                    image_label.image = tk_img  # Keep a reference to prevent garbage collection
                    image_label.grid(row=i // 4, column=i % 4)
            except:
                pass
        pictures_interface.attributes("-fullscreen", True)
        main_interface_visible = False
    else:
        pictures_interface.destroy()
        root.deiconify()
        root.attributes("-fullscreen", True)
        main_interface_visible = True


# Global mp3_folder variable
mp3_folder = r"/home/gasu/Desktop/music"


def play_mp3(mp3_file):
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(mp3_folder, mp3_file))
    pygame.mixer.music.play()


def toggle_music_interface():
    global main_interface_visible
    global music_interface
    if main_interface_visible:
        root.withdraw()
        music_interface = tk.Toplevel(root)
        music_interface.title("Music Interface")
        back_button = ttk.Button(music_interface, text="Go back",
                                 command=lambda: [music_interface.destroy(), root.deiconify()])
        back_button.grid(row=0, column=0)
        mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith('.mp3')]
        for i, mp3_file in enumerate(mp3_files):
            mp3_file_button = ttk.Button(music_interface, text=mp3_file, command=lambda file=mp3_file: play_mp3(file))
            mp3_file_button.grid(row=i + 1, column=0)
        stop_button = ttk.Button(music_interface, text="Stop", command=pygame.mixer.music.stop)
        stop_button.grid(row=0, column=1)
        music_interface.attributes("-fullscreen", True)
        main_interface_visible = False
    else:
        music_interface.destroy()
        root.deiconify()
        root.attributes("-fullscreen", True)
        main_interface_visible = True


def toggle_appointments_interface():
    try:
        appointments_config_window.destroy()
    except:
        pass
    try:
        admin_window.destroy()
    except:
        pass

    appointments_window = tk.Toplevel()
    appointments_window.attributes("-fullscreen", True)
    appointments_label = tk.Label(appointments_window, text="Appointments Interface")
    appointments_label.pack()
    go_back_button = tk.Button(appointments_window, text="Go Back", command=appointments_window.destroy)
    go_back_button.pack()

    # New label to display the next appointment information
    next_appointment_label = tk.Label(appointments_window, text="Next Appointment Information:")
    next_appointment_label.pack()

    global appointments_info
    appointments_info = tk.StringVar()
    appointments_info.set("")
    appointments_info_label = tk.Label(appointments_window, textvariable=appointments_info)
    appointments_info_label.pack()

    # Get the next appointment from the appointments list
    if len(appointments_list) > 0:
        appointments_info.set("\n".join(["Name: " + appointment['Name'] + "\nLocation: " + appointment[
            'Location'] + "\nTime: " + appointment['Time'] + "\nAdditional Information: " + appointment[
                                             'Additional Information'] for appointment in appointments_list]))
    else:
        appointments_info.set("No upcoming appointments.")


def toggle_directions_interface():
    global main_interface_visible
    global directions_interface
    if main_interface_visible:
        root.withdraw()
        directions_interface = tk.Toplevel(root)
        directions_interface.title("Directions Interface")
        back_button = ttk.Button(directions_interface, text="Go back", command=lambda: toggle_directions_interface())
        back_button.pack()
        directions_interface.attributes("-fullscreen", True)
        main_interface_visible = False
    else:
        directions_interface.destroy()
        root.deiconify()
        root.attributes("-fullscreen", True)
        main_interface_visible = True


root = tk.Tk()
root.title("Main Interface")
root.attributes("-fullscreen", True)

clock_label = tk.Label(root, font=("TkDefaultFont", 20))
clock_label.pack(side=tk.TOP, pady=10)


def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)


update_clock()

# Create the main interface with buttons to access the other interfaces
main_interface_visible = True
header_frame = ttk.Frame(root)
header_frame.pack(side=tk.TOP, fill=tk.X)
admin_button = ttk.Button(header_frame, text="Admin", command=lambda: toggle_admin_interface())
admin_button.pack(side=tk.RIGHT)

interface_frame = ttk.Frame(root)
interface_frame.pack()
pictures_button = ttk.Button(interface_frame, text="Pictures", command=lambda: toggle_pictures_interface())
pictures_button.grid(row=0, column=0)
music_button = ttk.Button(interface_frame, text="Music", command=lambda: toggle_music_interface())
music_button.grid(row=0, column=1)
appointments_button = tk.Button(root, text="Appointments", command=toggle_appointments_interface)
appointments_button.pack()
directions_button = ttk.Button(interface_frame, text="Directions", command=lambda: toggle_directions_interface())
directions_button.grid(row=1, column=1)

root.mainloop()