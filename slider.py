#!/usr/bin/env python
##############################################################################
# Copyright (c) 2012 Hajime Nakagami<nakagami@gmail.com>
# All rights reserved.
# Licensed under the New BSD License
# (http://www.freebsd.org/copyright/freebsd-license.html)
#
# A image viewer. Require Pillow ( https://pypi.python.org/pypi/Pillow/ ).
##############################################################################
import os
import sys
import PIL.Image
from PIL import Image, ImageTk

try:
    from Tkinter import *
    import tkFileDialog as filedialog
except ImportError:
    from tkinter import *
    from tkinter import filedialog
    from tkinter.ttk import Progressbar
import PIL.ImageTk
import keyboard

ref_dir = sys.argv[1]
num_page_def = 0
if len(sys.argv) >= 3:
    num_page_def = sys.argv[2]

class App(Frame):
    def resize(self, image, maxw, maxh):
        imagew = min(maxw,image.size[0])
        imageh = min(maxh,image.size[1])
        r1 = image.size[0]/imagew # width ratio
        r2 = image.size[1]/imageh # height ratio
        ratio = max(r1, r2)
        newsize = (int(image.size[0]/ratio), int(image.size[1]/ratio)) # keep image aspect ratio
        #print(str(newsize[0]) + " "  +str(newsize[1]))
        image = image.resize(newsize)
        return image  
    def chg_image(self):
        self.im = self.resize(self.im, 1000, 700);
        if self.im.mode == "1": # bitmap image
            self.img = PIL.ImageTk.BitmapImage(self.im, foreground="white")
        else:              # photo image
            self.img = PIL.ImageTk.PhotoImage(self.im)
        self.la.config(image=self.img, bg="#000000",
            width= max(self.img.width(),1000), 
            height= max(self.img.height(),700)
            #height=100
            )
        self.num_page_tv.set(str(self.num_page+1))
        self.num_page_name.set(image_files[self.num_page])
        self.progress['value'] = (self.num_page/self.num_total)*100
        self.status.set(str(self.num_page) + "/" + str(self.num_total-1))
        self.update_idletasks() 

    def open(self):
        filename = filedialog.askopenfilename()
        if filename != "":
            self.im = PIL.Image.open(filename)
        self.chg_image()
        self.num_page=0
    def rename(self,fromFile,toFile):
        os.rename(fromFile, toFile)
        print(fromFile + "  => "  + toFile)

    def seek_prev(self,key):
        #self.valid_key(key);
        self.num_page=self.num_page-1
        if self.num_page < 0:
            self.num_page = 0
        #self.im.seek(self.num_page)
        self.im = PIL.Image.open(ref_dir + "/" + image_files[self.num_page])
        self.chg_image()
        
        self.dir.set("<<<")
    def seek_next(self,key):
        #self.valid_key(key);
        self.num_page=self.num_page+1
        if self.num_page >= self.num_total :
            --self.num_page
            #self.num_page = self.num_total

        try:
            #self.im.seek(self.num_page)
            self.im = PIL.Image.open(ref_dir + "/" + image_files[self.num_page])
        except:
            self.num_page=self.num_page-1
        self.chg_image()        
        self.dir.set(">>>")

    def seek_select(self):
        try:
            #self.im.seek(self.num_page)
            self.im = PIL.Image.open(ref_dir + "/" + image_files[self.num_page])
            self.chg_image()
        except:
            print("Cannot Draw "+str(self.num_page))

    def seek_del(self):
        if self.is_seek_del != True and not os.path.exists(ref_dir+"/_del_"):
            os.makedirs(ref_dir+"/_del_")
            self.is_seek_del = True 
        #del image_files[1:self.num_page]
        self.num_total = image_files.__len__()
        if self.num_total  <= self.num_page:
            --self.num_page
            return
        img = image_files.pop(self.num_page)
        self.rename(ref_dir + "/"+ img, ref_dir + "/_del_/"+ img)
        self.num_total = image_files.__len__()
        self.seek_select()

    def seek_sel(self):
        if self.is_seek_sel != True and not os.path.exists(ref_dir+"/_sel_"):
            os.makedirs(ref_dir+"/_sel_")
            self.is_seek_sel = True 
        #del image_files[1:self.num_page]
        self.num_total = image_files.__len__()
        if self.num_total  <= self.num_page:
            --self.num_page
            return
        img = image_files.pop(self.num_page)
        self.rename(ref_dir + "/"+ img, ref_dir + "/_sel_/"+ img)
        self.num_total = image_files.__len__()
        self.seek_select()

    def seek_a(self):
        fold = "/_ok0"
        if ref_dir.startswith("1_photo"):
            fold = "/_ok"
        if self.is_seek_a != True and not os.path.exists(ref_dir+fold):
            os.makedirs(ref_dir+fold)
            self.is_seek_a = True 
        #del image_files[1:self.num_page]
        self.num_total = image_files.__len__()
        if self.num_total  <= self.num_page:
            --self.num_page
            return
        img = image_files.pop(self.num_page)
        self.rename(ref_dir + "/"+ img, ref_dir + fold + "/"+ img)
        self.num_total = image_files.__len__()
        self.seek_select()

    def seek_zero(self):
        if self.is_seek_zero != True and not os.path.exists(ref_dir+"/_0"):
            os.makedirs(ref_dir+"/_0")
            self.is_seek_zero = True 
        #del image_files[1:self.num_page]
        self.num_total = image_files.__len__()
        if self.num_total  <= self.num_page:
            --self.num_page
            return
        img = image_files.pop(self.num_page)
        self.rename(ref_dir + "/"+ img, ref_dir + "/_0/"+ img)
        self.num_total = image_files.__len__()
        self.seek_select()

    def seek_one(self):
        if self.is_seek_one != True and not os.path.exists(ref_dir+"/_1"):
            os.makedirs(ref_dir+"/_1")
            self.is_seek_one = True 
        #del image_files[1:self.num_page]
        self.num_total = image_files.__len__()
        if self.num_total  <= self.num_page:
            --self.num_page
            return
        img = image_files.pop(self.num_page)
        self.rename(ref_dir + "/"+ img, ref_dir + "/_1/"+ img)
        self.num_total = image_files.__len__()
        self.seek_select()

    def seek_two(self):
        if self.is_seek_two != True and not os.path.exists(ref_dir+"/_2"):
            os.makedirs(ref_dir+"/_2")
            self.is_seek_two = True 
        #del image_files[1:self.num_page]
        self.num_total = image_files.__len__()
        if self.num_total  <= self.num_page:
            --self.num_page
            return
        img = image_files.pop(self.num_page)
        self.rename(ref_dir + "/"+ img, ref_dir + "/_2/"+ img)
        self.num_total = image_files.__len__()
        self.seek_select()

    def seek_link(self):
        if self.is_seek_link != True and not os.path.exists(ref_dir+"/_link"):
            os.makedirs(ref_dir+"/_link")
            self.is_seek_link = True 
        #del image_files[1:self.num_page]
        self.num_total = image_files.__len__()
        if self.num_total  <= self.num_page:
            --self.num_page
            return
        img = image_files.pop(self.num_page)
        os.symlink(ref_dir + "/"+ img, ref_dir + "/_link/"+ img)
        self.num_total = image_files.__len__()
        self.seek_select()
    def valid_key(self,key):
        print("key==" + str(self.key_pressed == key))

    def __init__(self, master=None):
        Frame.__init__(self, master, width=1200, height=800)
        self.master.title('Image Viewer')
        self.num_total = image_files.__len__()
        self.num_page = int(num_page_def)
        self.num_page_tv = StringVar()
        self.num_page_name = StringVar()
        self.dir = StringVar()
        self.status = StringVar()

        fram = Frame(self,width=1200, height=800, relief='raised')
        Button(fram, text="Open File", command=self.open).pack(side=LEFT)
        Button(fram, text="Prev", command=self.seek_prev).pack(side=LEFT)
        Button(fram, text="Next", command=self.seek_next).pack(side=LEFT)
        Button(fram, text="Quit", command=self.destroy).pack(side=RIGHT)
        Label(fram, textvariable=self.num_page_tv).pack(side=LEFT)
        Label(fram, textvariable=self.num_page_name).pack(side=LEFT)
        Label(fram, textvariable=self.dir).pack(side=LEFT)        
        self.progress = Progressbar(fram, orient = HORIZONTAL, 
              length = 100, mode = 'determinate')
        self.progress.pack(side=RIGHT,pady = 10)
        Label(fram, textvariable=self.status).pack(side=RIGHT)
        fram.pack(side=TOP, fill=BOTH, expand=False)

        self.la = Label(self)
        self.la.pack()
        self.pack(fill=None, expand=False)

        myself = self
        self.is_seek_zero = False
        self.is_seek_one = False
        self.is_seek_two = False
        self.is_seek_del = False
        self.is_seek_sel = False
        self.is_seek_a = False
        self.is_seek_link = False
        self.key_pressed = None

        def next(key):
            if keyboard.is_pressed('right') or keyboard.is_pressed('down'):
                self.seek_next(key)    	
        def prev(key):
            if keyboard.is_pressed('left') or keyboard.is_pressed('up'):
                self.seek_prev(key)
        def seek_del(suppress):
            if keyboard.is_pressed('delete') or keyboard.is_pressed('q'):
                self.seek_del()
        def seek_sel(suppress):
            if keyboard.is_pressed('s'):
                self.seek_sel()
        def seek_a(suppress):
            if keyboard.is_pressed('a'):
                self.seek_a()
        def seek_zero(suppress):
            if keyboard.is_pressed('0'):
                self.seek_zero()
        def seek_one(suppress):
            if keyboard.is_pressed('1'):
                self.seek_one()
        def seek_two(suppress):
            if keyboard.is_pressed('2'):
                self.seek_two()
        def seek_link(suppress):
            if keyboard.is_pressed('l'):
                self.seek_link()
        def destroy(suppress):
            if keyboard.is_pressed('esc'):
                self.destroy()
                self.quit()
        def press_all(key):
            self.key_pressed = key
        def release_all(key):
            self.key_pressed = None

        #keyboard.on_press(press_all, suppress=False)
        #keyboard.on_release(release_all, suppress=True)

        keyboard.on_press_key("left", prev, suppress=False)
        keyboard.on_press_key("right", next, suppress=False)
        #self.bind("<Left>", prev)
        #self.bind("<Right>", next)        
        keyboard.on_press_key("up", prev, suppress=False)
        keyboard.on_press_key("down", next, suppress=False)
        #keyboard.on_press_key("space", seek_sel, suppress=False)
        keyboard.on_press_key("delete", seek_del, suppress=False)
        #keyboard.on_press_key("d", seek_del, suppress=False)
        keyboard.on_press_key("q", seek_del, suppress=False)
        #keyboard.on_press_key("x", seek_del, suppress=False)
        keyboard.on_press_key("s", seek_sel, suppress=False)
        keyboard.on_press_key("a", seek_a, suppress=False)
        keyboard.on_press_key("0", seek_zero, suppress=False)
        keyboard.on_press_key("1", seek_one, suppress=False)
        keyboard.on_press_key("2", seek_two, suppress=False)
        keyboard.on_press_key("l", seek_link, suppress=False)
        keyboard.on_press_key("esc", destroy, suppress=False)
        self.seek_select()



image_files = []
image_files = [f for f in os.listdir(ref_dir) if os.path.isfile(os.path.join(ref_dir, f)) and ( f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg")) and not f.startswith(".") ]
image_files.sort()
#for ref_file in image_files:
#	print (ref_file)


if __name__ == "__main__":
    app = App(); app.mainloop()