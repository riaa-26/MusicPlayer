from tkinter import *
import pygame
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title('Music Player')
root.iconbitmap('c:/gui/i1.ico')
root.configure(background = "black")
root.geometry("500x500")
pygame.mixer.init()

def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))

    # strip out the directory info and .mp3 extension from the song name
    song = song.replace("C:/GUI/audio/", "")
    song = song.replace(".mp3", "")

    # Add song to listbox
    song_box.insert(END, song)

# Add many songs to playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))

    # Loop through song list and replace directory info and mp3
    for song in songs:
        song = song.replace("C:/GUI/audio/", "")
        song = song.replace(".mp3", "")
        # Insert into playlist
        song_box.insert(END, song)


def play():
	# Set Stopped Variable To False So Song Can Play
	global stopped
	stopped = False
	song = song_box.get(ACTIVE)
	song = f'C:/GUI/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

# Stop playing current song
global stopped
stopped = False

def stop():

    # Stop Song From Playing
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    # Set Stop Variable To True
    global stopped
    stopped = True

# Delete A Song
def delete_song():
    stop()
    # Delete Currently Selected Song
    song_box.delete(ANCHOR)
    # Stop Music if it's playing
    pygame.mixer.music.stop()

# Delete All Songs from Playlist
def delete_all_songs():
    stop()
    # Delete All Songs
    song_box.delete(0, END)
    # Stop Music if it's playing
    pygame.mixer.music.stop()

# Create Global Pause Variable
global paused
paused = False

# Pause and Unpause The Current Song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True

# Create Master Frame
master_frame = Frame(root)
master_frame.pack(pady=40)

# Create Playlist Box
song_box = Listbox(master_frame, bg="purple", fg="white", width=60, selectbackground="white", selectforeground="black")
song_box.grid(row=0, column=0)

# Define Player Control Button Images
play_modify = Image.open("Images/play50.png")
resized1 = play_modify.resize((80,80))
play_btn_img = ImageTk.PhotoImage(resized1)
pause_modify = Image.open("images/pause50.png")
resized2 = pause_modify.resize((80,80))
pause_btn_img = ImageTk.PhotoImage(resized2)
stop_modify = Image.open("images/stop50.png")
resized3 = stop_modify.resize((80,80))
stop_btn_img = ImageTk.PhotoImage(resized3)

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

# Define Player Control Buttons
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
# Add Many Songs to playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

# Create Delete Song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

root.mainloop()