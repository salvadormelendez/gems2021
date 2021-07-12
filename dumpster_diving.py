#!/usr/bin/env python3

####################################################
# Dumpster Diving Python Script
# Designed and Written by Salvador Melendez
# WARNING! Any changes made to this file can
#          damage the functionality of the script
####################################################

import os
import random
import glob
import tkinter as tk
from tkinter import ttk

cwd = os.getcwd()
dd_dir = cwd + '/profiles/'
PROFILE_NUM = random.randint(1,12)
subfolder = 'profile_' + '{:02d}'.format(PROFILE_NUM)
input_folders = ['credit_card', 'post_it', 'facebook', 'monthly_bill']
prefix_images = ['cc_set_', 'pi_set_', 'fb_set_', 'mb_set_']
images = {}
for i in range(len(input_folders)):
    images[input_folders[i]] = []
    cwd_folder = dd_dir + subfolder + '/' + input_folders[i] + '/'
    prefix_img = cwd_folder + prefix_images[i]
    tmp_list = []
    for file in glob.glob((cwd_folder + "*.png")):
        tmp_list.append(file)
    images[input_folders[i]] = tmp_list[:]
    random.shuffle(images[input_folders[i]])

APP_TITLE = "DUMPSTER DIVING"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 1600
APP_HEIGHT = 800


class CreateCanvasObject(object):
    def __init__(self, canvas, image_name, xpos, ypos):
        self.canvas = canvas
        self.image_name = image_name
        self.xpos, self.ypos = xpos, ypos
 
        self.tk_image = tk.PhotoImage(
            file="{}".format(image_name))
        self.image_obj= canvas.create_image(
            xpos, ypos, image=self.tk_image)
         
        canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
        canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
        self.move_flag = False
         
    def move(self, event):
        if self.move_flag:
            new_xpos, new_ypos = event.x, event.y
             
            self.canvas.move(self.image_obj,
                new_xpos-self.mouse_xpos ,new_ypos-self.mouse_ypos)
             
            self.mouse_xpos = new_xpos
            self.mouse_ypos = new_ypos
        else:
            self.move_flag = True
            self.canvas.tag_raise(self.image_obj)
            self.mouse_xpos = event.x
            self.mouse_ypos = event.y
 
    def release(self, event):
        self.move_flag = False
                     
class Application(tk.Frame):
 
    def __init__(self, master):
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Frame.__init__(self, master)
 
        #Create Tab Control
        TAB_CONTROL = ttk.Notebook(self.master)
        #Tab1 - Credit Card
        TAB1 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB1, text='Credit Card')
        #Tab2 - Post-It
        TAB2 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB2, text='Post-It')
        #Tab3 - Facebook Screenshot
        TAB3 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB3, text='Facebook Screenshot')
        #Tab4 - Monthly Bill
        TAB4 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB4, text=' Monthly Bill')
        TAB_CONTROL.pack(expand=1, fill="both")
 
 
        #CREDIT CARD
        self.canvas = tk.Canvas(TAB1, width=1600, height=800, bg='steelblue',
            highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.image_1 = CreateCanvasObject(self.canvas, images['credit_card'][0], 150, 100)
        self.image_2 =CreateCanvasObject(self.canvas, images['credit_card'][1], 150, 255)
        self.image_3 =CreateCanvasObject(self.canvas, images['credit_card'][2], 150, 410)
        self.image_4 = CreateCanvasObject(self.canvas, images['credit_card'][3], 389, 100)
        self.image_5 =CreateCanvasObject(self.canvas, images['credit_card'][4], 389, 255)
        self.image_6 =CreateCanvasObject(self.canvas, images['credit_card'][5], 389, 410)
        self.image_7 = CreateCanvasObject(self.canvas, images['credit_card'][6], 628, 100)
        self.image_8 =CreateCanvasObject(self.canvas, images['credit_card'][7], 628, 255)
        self.image_9 =CreateCanvasObject(self.canvas, images['credit_card'][8], 628, 410)
        
        #POST IT
        self.canvas = tk.Canvas(TAB2, width=1600, height=800, bg='steelblue',
            highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.image_1 = CreateCanvasObject(self.canvas, images['post_it'][0], 150, 100)
        self.image_2 =CreateCanvasObject(self.canvas, images['post_it'][1], 150, 265)
        self.image_3 =CreateCanvasObject(self.canvas, images['post_it'][2], 150, 430)
        self.image_4 = CreateCanvasObject(self.canvas, images['post_it'][3], 315, 100)
        self.image_5 =CreateCanvasObject(self.canvas, images['post_it'][4], 315, 265)
        self.image_6 =CreateCanvasObject(self.canvas, images['post_it'][5], 315, 430)
        self.image_7 = CreateCanvasObject(self.canvas, images['post_it'][6], 480, 100)
        self.image_8 =CreateCanvasObject(self.canvas, images['post_it'][7], 480, 265)
        self.image_9 =CreateCanvasObject(self.canvas, images['post_it'][8], 480, 430)
        
        #FACEBOOK SCREENSHOT
        self.canvas = tk.Canvas(TAB3, width=1600, height=800, bg='steelblue',
            highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.image_1 = CreateCanvasObject(self.canvas, images['facebook'][0], 150, 100)
        self.image_2 =CreateCanvasObject(self.canvas, images['facebook'][1], 150, 310)
        self.image_3 =CreateCanvasObject(self.canvas, images['facebook'][2], 150, 520)
        self.image_4 = CreateCanvasObject(self.canvas, images['facebook'][3], 500, 100)
        self.image_5 =CreateCanvasObject(self.canvas, images['facebook'][4], 500, 310)
        self.image_6 =CreateCanvasObject(self.canvas, images['facebook'][5], 500, 520)
        self.image_7 = CreateCanvasObject(self.canvas, images['facebook'][6], 850, 100)
        self.image_8 =CreateCanvasObject(self.canvas, images['facebook'][7], 850, 310)
        self.image_9 =CreateCanvasObject(self.canvas, images['facebook'][8], 850, 520)

        #MONTHLY BILL
        self.canvas = tk.Canvas(TAB4, width=1600, height=800, bg='steelblue',
            highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.image_1 = CreateCanvasObject(self.canvas, images['monthly_bill'][0], 150, 130)
        self.image_2 =CreateCanvasObject(self.canvas, images['monthly_bill'][1], 150, 400)
        self.image_3 =CreateCanvasObject(self.canvas, images['monthly_bill'][2], 150, 670)
        self.image_4 = CreateCanvasObject(self.canvas, images['monthly_bill'][3], 400, 130)
        self.image_5 =CreateCanvasObject(self.canvas, images['monthly_bill'][4], 400, 400)
        self.image_6 =CreateCanvasObject(self.canvas, images['monthly_bill'][5], 400, 670)
        self.image_7 = CreateCanvasObject(self.canvas, images['monthly_bill'][6], 650, 130)
        self.image_8 =CreateCanvasObject(self.canvas, images['monthly_bill'][7], 650, 400)
        self.image_9 =CreateCanvasObject(self.canvas, images['monthly_bill'][8], 650, 670)
             
    def close(self):
        #print("Good-bye!")
        self.master.destroy()
     
def main():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
    #app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
     
    app = Application(app_win).pack(fill='both', expand=True)
     
    app_win.mainloop()
  
  
if __name__ == '__main__':
    main()
    
    

