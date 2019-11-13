from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

gui = Tk()
gui.geometry("350x250")
gui.title('Renamer')

ch_p = 0
ch_t = 0
ch_m = 0
ch_pp = 0
ch_d = 0
ch_m4 = 0
ch_pdf = 0
resolution = []

# add in list resolutions of file
def on_click_music():
    global ch_m
    if ch_m == 0:
        check = 0
        if len(resolution) == 0:
            ch_m = 1
            resolution.append('.mp3')
        else:
            for i in range(len(resolution)):
                if resolution[i] == '.mp3':
                    check += 1
            if check == 0:
                ch_m = 1
                resolution.append('.mp3')
    else:
        resolution.remove('.mp3')
        ch_m = 0

def on_click_pic():
    global ch_p
    if ch_p == 0:
        check = 0
        if len(resolution) == 0:
            ch_p = 1 
            resolution.append('.jpg')
        else:
            for i in range(len(resolution)):
                if resolution[i] == '.jpg':
                    check +=1
            if check == 0:
                ch_p = 1
                resolution.append('.jpg')
    else:
        ch_p = 0
        resolution.remove('.jpg')

def on_on_click_text():
    global ch_t
    if ch_t == 0:
        check = 0
        if len(resolution) == 0:
            ch_t = 1
            resolution.append('.txt')
        else:
            for i in range(len(resolution)):
                if resolution[i] == '.txt':
                    check += 1
            if check == 0:
                ch_t =1
                resolution.append('.txt')
    else:
        ch_t = 0
        resolution.remove('.txt')

def on_click_mp4():
    global ch_m4
    if ch_m4 == 0:
        check = 0
        if len(resolution) == 0:
            ch_m4 = 1
            resolution.append('.mp4')
        else:
            for i in range(len(resolution)):
                if resolution[i] == '.mp4':
                    check += 1
            if check == 0:
                ch_m4 = 1
                resolution.append('.mp4')
    else:
        resolution.remove('.mp4')
        ch_m4 = 0

def on_click_picp():
    global ch_pp
    if ch_pp == 0:
        check = 0
        if len(resolution) == 0:
            ch_pp = 1 
            resolution.append('.png')
        else:
            for i in range(len(resolution)):
                if resolution[i] == '.png':
                    check +=1
            if check == 0:
                ch_pp = 1
                resolution.append('.png')
    else:
        ch_pp = 0
        resolution.remove('.png')

def on_click_doc():
    global ch_d
    if ch_d == 0:
        check = 0
        if len(resolution) == 0:
            ch_d = 1
            resolution.append('.doc')
            resolution.append('.docx')
        else:
            for i in range(len(resolution)):
                if resolution[i] == '.doc' or resolution[i] == '.docx':
                    check += 1
            if check == 0:
                ch_d = 1
                resolution.append('.doc')
                resolution.append('.docx')
    else:
        ch_d = 0
        resolution.remove('.doc')
        resolution.remove('.docx')

def on_click_pdf():
    global ch_pdf
    if ch_pdf == 0:
        check = 0
        if len(resolution) == 0:
            ch_pdf = 1 
            resolution.append('.pdf')
        else:
            for i in range(len(resolution)):
                if resolution[i] == '.pdf':
                    check +=1
            if check == 0:
                ch_pdf = 1
                resolution.append('.pdf')
    else:
        ch_pdf = 0
        resolution.remove('.pdf')

# choose path to directory and rename file
def select_folder():
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        name = name_file.get()
        check_name(selected_folder, resolution, name)

def check_name(folder_path, resolution, name):
    #count of files which have same name
    checked = 0
    for i in range(len(resolution)):
        for f in os.listdir(folder_path):
            if (f.find(name)*(-1)):
                pass
            else:
                checked += 1
    if checked:
        str_to_print = 'You have already renamed files to this directory!\nPlease try with another files names or in anotger directory!'
        messagebox.showinfo('Ooops!', str_to_print)
    else:
        rename_files(folder_path, resolution, name)

def rename_files(folder_path, resolution, name):
    count = 0
    # we have list of resolutions
    # and with help of this cycle we sorting through values
    for i in range(len(resolution)):
        # searching all files in selected directory
        for file in os.listdir(folder_path):
            # searching files with resolution
            if file.endswith(resolution[i]):
                count += 1
                name_string = name + str(count) + resolution[i]
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path, name_string))
    if count:
        str_to_print = 'Successfully renamed ' + str(count) + ' files in folder ' + str(folder_path) + '!'
        messagebox.showinfo('Success!', str_to_print)
    else:
        messagebox.showerror('Error!', "Can't find files in folder " + str(folder_path) + '!')

name_file = StringVar()
folder_path = StringVar()
label_name = Label(gui, width = 5, font = ('Colibri', 30), text = 'Choose directory')
entr_name = Entry(gui, textvariable=name_file)
btn_choose = Button(gui,text = 'Choose directory', font = ('Colibri', 30), command = select_folder)
cb_pic = Checkbutton(gui, text=".jpg", command=on_click_pic)
cb_music = Checkbutton(gui, text=".mp3", command=on_click_music)
cb_text = Checkbutton(gui, text=".txt", command=on_on_click_text)
cb_picp = Checkbutton(gui, text=".png", command=on_click_picp)
cb_mp4 = Checkbutton(gui, text=".mp4", command=on_click_mp4)
cb_doc = Checkbutton(gui, text=".doc", command=on_click_doc)
cb_pdf = Checkbutton(gui, text=".pdf", command=on_click_pdf)

label_name.grid(row=0, columnspan=3, sticky="ew")
entr_name.grid(row=1, columnspan=3, sticky="ew")
btn_choose.grid(row=2, columnspan=3, sticky="ew")
cb_music.grid(row = 3, column = 0)
cb_pic.grid(row = 3, column = 1)
cb_text.grid(row = 3, column = 2)
cb_mp4.grid(row = 4, column = 0)
cb_picp.grid(row = 4, column = 1)
cb_doc.grid(row = 4, column = 2)
cb_pdf.grid(row = 5, column = 1)

gui.mainloop()