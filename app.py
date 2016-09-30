from Tkinter import *
import os.path
import sys
import tkFileDialog
import tkMessageBox

root = Tk()
root.wm_title("Create Folders")
root.resizable(width=False, height=False)
frame = Frame(root, padx = 20, pady = 10)
frame.grid()

number = StringVar()
numparts = StringVar()

def create_folders(event):
    jobname = number.get()
    partquantity = numparts.get()
    try:
        # Sets a limit of part quantity to 49
        if int(partquantity) < 50:
            count = 0
            while (count < int(partquantity)):
                jobpart = count + 1
                if jobpart < 10:
                    newpath = os.path.join(directory + jobname + 'P0' + str(jobpart))
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                        os.makedirs(newpath + '/mmt_hires')
                        os.makedirs(newpath + '/original_client_creative')
                        os.makedirs(newpath + '/paint_files')
                        os.makedirs(newpath + '/prep_art')
                        os.makedirs(newpath + '/prep_art/LOW')
                else:
                    newpath = os.path.join(directory + jobname + 'P' + str(jobpart))
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                        os.makedirs(newpath + '/mmt_hires')
                        os.makedirs(newpath + '/original_client_creative')
                        os.makedirs(newpath + '/paint_files')
                        os.makedirs(newpath + '/prep_art')
                        os.makedirs(newpath + '/prep_art/LOW')
                count = count + 1
            btn_canvas.itemconfig(selected_dir_label, text='Folders created successfully.')
        else:
            btn_canvas.itemconfig(selected_dir_label, text='You have selected too many parts')
    except NameError:
        tkMessageBox.showerror('Error!', 'Please select a directory')


def clear_num_field(event):
    number_field.delete(0, END)
    return

def clear_part_field(event):
    part_field.delete(0, END)
    return

def select_dir(event):
    global directory
    directory = tkFileDialog.askdirectory(initialdir='~/Desktop') + "/"
    btn_canvas.itemconfig(selected_dir_label, text=directory)
    print directory

def close_program(event):
    sys.exit("Closed")

btn_canvas = Canvas(root, width = 400, height = 100, background = '#242D3B', bd = 0, highlightthickness = 0)
btn_canvas.grid(row = 1, column = 0)

select_dir_btn = btn_canvas.create_rectangle(20, 0, 115, 30, fill = "#243041", activefill = '#546A82', outline = '#D5E1EB')
select_dir_label = btn_canvas.create_text(27, 7, anchor = NW, fill = '#D5E1EB', text = 'Select Folder', state = DISABLED)
btn_canvas.tag_bind(select_dir_btn, '<ButtonPress-1>', select_dir)

selected_dir_label = btn_canvas.create_text(125, 7, anchor = NW, fill = '#D5E1EB', state = DISABLED)

quit_btn = btn_canvas.create_rectangle(20, 50, 115, 80, fill = "#243041", activefill = '#546A82', outline = '#D5E1EB')
quit_label = btn_canvas.create_text(54, 57, anchor = NW, fill = '#D5E1EB', text = 'Quit', state = DISABLED)
btn_canvas.tag_bind(quit_btn, '<ButtonPress-1>', close_program)

create_folders_btn = btn_canvas.create_rectangle(280, 50, 380, 80, fill = "#243041", activefill = '#546A82', outline = '#D5E1EB')
create_folders_label = btn_canvas.create_text(285, 57, anchor = NW, fill = '#D5E1EB', text = 'Create Folders', state = DISABLED)
btn_canvas.tag_bind(create_folders_btn, '<ButtonPress-1>', create_folders)

number_label = Label(frame, text="Job Number  ")
number_label.grid(row = 0, column = 0, sticky = E, pady = 10)
number_field = Entry(frame, bd = 0, relief = FLAT, textvariable = number)
number_field.bind('<Button-1>', clear_num_field)
number_field.insert(0, '123456')
number_field.grid(row = 0, column = 1)

part_label = Label(frame, text="Parts  ")
part_label.grid(row = 1, column = 0, sticky = E, pady = 10)
part_field = Entry(frame, bd = 0, relief = FLAT, textvariable = numparts)
part_field.bind('<Button-1>', clear_part_field)
part_field.insert(0, '1')
part_field.grid(row = 1, column = 1)

root.configure(background='#242D3B')
frame.configure(background='#242D3B')
number_label.configure(background='#242D3B', fg='#D5E1EB')
number_field.configure(highlightthickness=1, highlightbackground='#D5E1EB')
part_label.configure(background='#242D3B', fg='#D5E1EB')
part_field.configure(highlightthickness=1, highlightbackground='#D5E1EB')
root.mainloop()
