import tkinter as tk
from tkinter import font
from tkinter.constants import DISABLED
from PIL import Image
from PIL import ImageTk
import requests
import json
import math

HEIGHT = 1080
WIDTH = 1920

token = "#######################################"

def lifx_api_commands():
  global headers
  headers = {
    "Authorization": "Bearer %s" % token,
    }
  response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)

  lights = response.json()

  global light_one
  light_one = lights[0]["id"]

  global light_one_on_off
  def light_one_on_off():
    
    payload = {
    "states": [
        {
            "selector" : f"id:{light_one}",
            "power": "off"
        }
      ]
    }

    response = requests.post('https://api.lifx.com/v1/lights/all/toggle', headers=headers)


  #All the colors api command
  global color_number_one
  def color_number_one():
    payload = {
      "power": "on",
      "color": "white",
      "fast": True 
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    
  global color_number_two
  def color_number_two():
    payload = {
      "power": "on",
      "color": "red",
      "fast": True
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

  global color_number_three
  def color_number_three():
    payload = {
      "power": "on",
      "color": "blue",
      "fast": True
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

  global color_number_four
  def color_number_four():
    payload = {
      "power": "on",
      "color": "green",
      "fast": True
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    
  global color_number_five
  def color_number_five():
    payload = {
      "power": "on",
      "color": "purple",
      "fast": True
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

  global color_number_six
  def color_number_six():
    payload = {
      "power": "on",
      "color": "#89CFF0",
      "fast": True
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)


  global light_one_colors
  def light_one_colors():
    root_light_one_colors=tk.Tk()

    #Colors
    popup_window = tk.Frame(root_light_one_colors, bg="grey")
    popup_window.place()
    



def lifx_back_button():
  root_main_lifx.destroy(),
  main_page()

def ring_back_button():
    root_main_ring.destroy(),
    main_page()

def main_lifx_button():
  def lifx_exit_button_func():
    root_main_lifx.destroy()
  root_main_page.destroy(),
  global root_main_lifx
  root_main_lifx=tk.Tk()
  root_main_lifx.title(" ")
  root_main_lifx.attributes("-fullscreen", True)

  #Colors
  global color_image
  color_image = tk.PhotoImage(file=r"C:\Users\Sean\Desktop\Python photos\Color_picker.png")
  global light_one_colors
  def light_one_colors():
    popup_window = tk.Frame(root_main_lifx, bg="#111111", highlightthickness=3, highlightcolor="white")
    popup_window.place(relheight=.35, relwidth=.450, relx=.2, rely=.25)


    def close_window():
      popup_window.destroy()
    
    colors_frame = tk.Label(popup_window, bg="#111111")
    colors_frame.place(relheight=1, relwidth=1, relx=0, rely=0)

    colors_top = tk.Frame(popup_window, bg="#111111")
    colors_top.place(relheight=.09, relwidth=1, relx=0, rely=0)

    colors_title = tk.Button(popup_window, bg="#111111", text="Color Picker", font="Hind, 20", fg="white", command=close_window, bd=0)
    colors_title.place(relheight=.1, relwidth=.2, relx=.4, rely=.001)

    color_one= tk.Button(colors_frame, bg="#e3e5e8", bd=0, text="White", anchor="s", fg="black", command=color_number_one, font=('Hind', 13,'bold'))
    color_one.place(relheight=.150, relwidth=.135, relx=.025, rely=.15)

    color_two = tk.Button(colors_frame, bg="#e8150e", bd=0, text="Red", anchor="s", fg="black", command=color_number_two, font=('Hind', 13,'bold'))
    color_two.place(relheight=.150, relwidth=.135, relx=.16, rely=.15)

    color_three = tk.Button(colors_frame, bg="#103cb5", bd=0, text="Blue", anchor="s", fg="black", command=color_number_three, font=('Hind', 13,'bold'))
    color_three.place(relheight=.150, relwidth=.135, relx=.297, rely=.15)

    color_four = tk.Button(colors_frame, bg="#16de31", bd=0, text="Green", anchor="s", fg="black", command=color_number_four ,font=('Hind', 13,'bold'))
    color_four.place(relheight=.150, relwidth=.135, relx=.57, rely=.15)
    
    color_five = tk.Button(colors_frame, bg="#6310b5", bd=0, text="Purple", anchor="s", fg="black", command=color_number_five, font=('Hind', 13,'bold'))
    color_five.place(relheight=.150, relwidth=.135, relx=.705, rely=.15)

    color_six = tk.Button(colors_frame, bg="#89CFF0", bd=0, text="Baby Blue", anchor="s", fg="black", command=color_number_six, font=('Hind', 13,'bold'))
    color_six.place(relheight=.150, relwidth=.135, relx=.84, rely=.15)
    
    sliders = tk.Frame(colors_frame, bg="#111111")
    sliders.place(relheight=.5, relwidth=.407, relx=.025, rely=.50)

    R_Label = tk.Label(sliders, bg="#111111", text="R:", fg="white")
    R_Label.place(relheight=.09, relwidth=.06, relx=.005, rely=.4)

    def R_Slide(v):
      R_value_label = tk.Label(sliders, fg="white", bg="#111111", text=R_Scale.get())
      R_value_label.place(relheight=.09, relwidth=.09, relx=.9, rely=.4)

      global R_Value
      R_Value = R_Scale.get()
      print("R_Scale " + str(R_Scale.get()))
      BegRValue = R_Value / 16
      #The R value divided by 16 and then rounded to the base number
      global FirstRMath
      FirstRMath = math.floor(BegRValue)
      FirstRMathRemainder = str(BegRValue).split(".")
      FirstRMathRemainder = int(FirstRMathRemainder[1])
      FirstRMathRemainder = FirstRMathRemainder / 100
      FirstRMathRemainder = FirstRMathRemainder * 16


      G_value_label = tk.Label(sliders, fg="white", bg="#111111", text=G_Scale.get())
      G_value_label.place(relheight=.09, relwidth=.09, relx=.9, rely=.6)
      global G_Value
      G_Value = G_Scale.get()
      print("G_Scale " +str(G_Scale.get()))
      BegGValue = G_Value / 16
      #The R value divided by 16 and then rounded to the base number
      global FirstGMath
      FirstGMath = math.floor(BegGValue)

      FirstGMathRemainder = str(BegGValue).split(".")
      FirstGMathRemainder = int(FirstGMathRemainder[1])
      FirstGMathRemainder = FirstGMathRemainder / 100
      FirstGMathRemainder = FirstGMathRemainder * 16


      B_value_label = tk.Label(sliders, fg="white", bg="grey", text=B_Scale.get())
      B_value_label.place(relheight=.09, relwidth=.09, relx=.9, rely=.8)

      global B_value
      B_Value = B_Scale.get()
      print("B_Scale " + str(B_Scale.get()))
      BegBValue = B_Value / 16
      #The R value divided by 16 and then rounded to the base number
      
      FirstBMath = math.floor(BegBValue)
      FirstBMathRemainder = str(BegBValue).split(".")
      FirstBMathRemainder = int(FirstBMathRemainder[1])
      FirstBMathRemainder = FirstBMathRemainder / 100
      FirstBMathRemainder = FirstBMathRemainder * 16
      print("Remainder of B " + str(FirstBMathRemainder))

      global tested_l
      tested_l = (FirstRMath, round(FirstRMathRemainder), FirstGMath, round(FirstGMathRemainder) ,FirstBMath, round(FirstBMathRemainder))
      print(tested_l)
      class Encoded:
        def __init__(self, Lett, Numb,):
          self.Letter = Lett
          self.Number = Numb
      l0  = Encoded(0, 0)
      l1  = Encoded(1, 1)
      l2  = Encoded(2, 2)
      l3  = Encoded(3, 3)
      l4  = Encoded(4, 4)
      l5  = Encoded(5, 5)
      l6  = Encoded(6, 6)
      l7  = Encoded(7, 7)
      l8  = Encoded(8, 8)
      l9  = Encoded(9, 9)
      l10 = Encoded("A", 10)
      l11 = Encoded("B", 11)
      l12 = Encoded("C", 12)
      l13 = Encoded("D", 13)
      l14 = Encoded("E", 14)
      l15 = Encoded("F", 15)
      l16 = Encoded("G", 16)
      l17 = Encoded("H", 17)
      l18 = Encoded("I", 18)
      l19 = Encoded("J", 19)
      l20 = Encoded("K", 20)
      l21 = Encoded("L", 21)
      l22 = Encoded("M", 22)
      l23 = Encoded("N", 23)
      l24 = Encoded("O", 24)
      l25 = Encoded("P", 25)
      l26 = Encoded("Q", 26)
      l27 = Encoded("R", 27)
      l28 = Encoded("S", 28)
      l29 = Encoded("T", 29)
      l30 = Encoded("U", 30)
      l31 = Encoded("V", 31)
      l32 = Encoded("W", 32)
      l33 = Encoded("X", 33)
      l34 = Encoded("Y", 34)
      l35 = Encoded("Z", 35)
      l36 = Encoded(0, 100)
      w_count = len(tested_l)
      global count
      count = 0
      global count2
      count2 = 0
      tested_l = list(tested_l)
      global new_word
      new_word = []

      def encoded_func():
        global count
        global count2
        global tested_l
        print(tested_l[0])
        print("test encoded")
        print(tested_l)
        while w_count > count2:
          if tested_l[0] == 00:
            tested_l = tested_l[0,(0)]
          else:
            tested_l.pop(0)
            count2 = count2 + 1

        while w_count > count:
          if tested_l[0] == l0.Number:
            new_word.append(l0.Letter)
          elif tested_l[0] == l1.Number:
            new_word.append(l1.Letter)
          elif tested_l[0] == l2.Number:
            new_word.append(l2.Letter)
          elif tested_l[0] == l3.Number:
            new_word.append(l3.Letter)
          elif tested_l[0] == l4.Number:
            new_word.append(l4.Letter)
          elif tested_l[0] == l5.Number:
            new_word.append(l5.Letter)
          elif tested_l[0] == l6.Number:
            new_word.append(l6.Letter)
          elif tested_l[0] == l7.Number:
            new_word.append(l7.Letter)
          elif tested_l[0] == l8.Number:
            new_word.append(l8.Letter)
          elif tested_l[0] == l9.Number:
            new_word.append(l9.Letter)
          elif tested_l[0] == l10.Number:
            new_word.append(l10.Letter)
          elif tested_l[0] == l11.Number:
            new_word.append(l11.Letter)
          elif tested_l[0] == l12.Number:
            new_word.append(l12.Letter)
          elif tested_l[0] == l13.Number:
            new_word.append(l13.Letter)
          elif tested_l[0] == l14.Number:
            new_word.append(l14.Letter)
          elif tested_l[0] == l15.Number:
            new_word.append(l15.Letter)
          elif tested_l[0] == l16.Number:
            new_word.append(l16.Letter)
          elif tested_l[0] == l17.Number:
            new_word.append(l17.Letter)
          elif tested_l[0] == l18.Number:
            new_word.append(l18.Letter)
          elif tested_l[0] == l19.Number:
            new_word.append(l19.Letter)
          elif tested_l[0] == l20.Number:
            new_word.append(l20.Letter)
          elif tested_l[0] == l21.Number:
            new_word.append(l21.Letter)
          elif tested_l[0] == l22.Number:
            new_word.append(l22.Letter)
          elif tested_l[0] == l23.Number:
            new_word.append(l23.Letter)
          elif tested_l[0] == l24.Number:
            new_word.append(l24.Letter)
          elif tested_l[0] == l25.Number:
            new_word.append(l25.Letter)
          elif tested_l[0] == l26.Number:
            new_word.append(l26.Letter)
          elif tested_l[0] == l27.Number:
            new_word.append(l27.Letter)
          elif tested_l[0] == l28.Number:
            new_word.append(l28.Letter)
          elif tested_l[0] == l29.Number:
            new_word.append(l29.Letter)
          elif tested_l[0] == l30.Number:
            new_word.append(l30.Letter)
          elif tested_l[0] == l31.Number:
            new_word.append(l31.Letter)
          elif tested_l[0] == l32.Number:
            new_word.append(l32.Letter)
          elif tested_l[0] == l33.Number:
            new_word.append(l33.Letter)
          elif tested_l[0] == l34.Number:
            new_word.append(l34.Letter)
          elif tested_l[0] == l35.Number:
            new_word.append(l35.Letter)
          elif tested_l[0] == l36.Number:
            new_word.append(l36.Letter)
          tested_l.pop(0)
          count = count + 1
      encoded_func()
      print(new_word)
      s2 = new_word
      lts = ''.join(map(str, s2))
      print("#"+ lts)
      Hex = tk.Label(popup_window, text=("#"+ lts),fg="black", font=("Arial, 20"))
      Hex.place(relheight=.3, relwidth=.3, relx=.7, rely=.7)

    R_Scale = tk.Scale(sliders, from_=0, to=256, orient='horizontal', command=R_Slide, bg="#403E41", troughcolor="#1E1E1E", highlightthickness=0, activebackground ="#403E41", showvalue=0, bd=0)
    R_Scale.place(relwidth=.80, relx=.075, rely=.4)

    R_value_label = tk.Label(sliders, fg="white", bg="#111111", text=R_Scale.get())
    R_value_label.place(relheight=.09, relwidth=.09, relx=.9, rely=.4)

    #Green Slider
    G_Label = tk.Label(sliders, bg="#111111", text="G:", fg="white")
    G_Label.place(relheight=.09, relwidth=.06, relx=.005, rely=.6)


    G_Scale = tk.Scale(sliders, from_=0, to=256, orient='horizontal', command=R_Slide, bg="#403E41", troughcolor="#1E1E1E", highlightthickness=0, activebackground ="#403E41", showvalue=0, bd=0)
    G_Scale.place(relwidth=.80, relx=.075, rely=.6)

    G_value_label = tk.Label(sliders, fg="white", bg="#111111", text=G_Scale.get())
    G_value_label.place(relheight=.09, relwidth=.09, relx=.9, rely=.6)

    #Blue Slider
    B_Label = tk.Label(sliders, bg="#111111", text="B:", fg="white")
    B_Label.place(relheight=.09, relwidth=.06, relx=.005, rely=.8)

    B_Scale = tk.Scale(sliders, from_=0, to=256, orient='horizontal', command=R_Slide, bg="#403E41", troughcolor="#1E1E1E", highlightthickness=0, activebackground ="#403E41", showvalue=0, bd=0)
    B_Scale.place(relwidth=.80, relx=.075, rely=.8)

    B_value_label = tk.Label(sliders, fg="white", bg="#111111", text=B_Scale.get())
    B_value_label.place(relheight=.09, relwidth=.09, relx=.9, rely=.8)



  #Converting RGB to Hex









  
  light_bulb_image = tk.PhotoImage(file=r"C:\Users\Sean\Desktop\Python photos\light_bulb_image.png")
  light_bulb_image_resize = light_bulb_image.zoom((1), Image.ANTIALIAS)

  lifx_cavnvas = tk.Canvas(root_main_lifx, highlightthickness=0, height=HEIGHT,width=WIDTH, bg="black")
  lifx_cavnvas.pack()

  lifx_exit_button = tk.Button(lifx_cavnvas, bg="black", bd=0, command=lifx_exit_button_func)
  lifx_exit_button.place(relheight=.05, relwidth=.05, relx=.95, rely=0)

  lifx_label = tk.Button(lifx_cavnvas, text="LIFX", bg="black", fg="#44194B", font=("Helvatical bold",30), bd=0, highlightthickness=0, activeforeground="grey", activebackground="black", command=lifx_back_button)
  lifx_label.place(relwidth=.5, relheight=.08, relx=.25, rely=.02)

  frame_one = tk.Frame(lifx_cavnvas, bg="#0d1421", highlightthickness=2)
  frame_one.place(relwidth=.83,relheight=.3, rely=.1, relx=.08)
  
  light_one_image = tk.Label(frame_one, bg="#0d1421", image=light_bulb_image_resize)
  light_one_image.place(relwidth=.2, relheight=.7, rely=.22, relx=.06)

  light_one_on_off_button = tk.Button(light_one_image, command=light_one_on_off, image=light_bulb_image_resize, bg="#0d1421", bd=0, activebackground="#0d1421")
  light_one_on_off_button.place(relwidth=1, relheight=1, rely=0, relx=0)

  light_one_brightness = tk.Scale(frame_one, from_=0, to=100, orient='horizontal', bg="#403E41", troughcolor="#1E1E1E", highlightthickness=0, activebackground ="#403E41", showvalue=0, bd=0)
  light_one_brightness.place(relwidth=.60, relx=.3, rely=.65)
  
  lifx_more_button = tk.Button (frame_one, text="More", font=("Helvatical bold",20), activebackground="grey", bg="#1E1E1E", bd=0, highlightthickness=0,)
  lifx_more_button.place(relwidth=.25, relheight=.25, relx=.65, rely=.3)

  lifx_fav_color_button = tk.Button (frame_one, command=light_one_colors, text="Colors", font=("Helvatical bold",20), activebackground="grey", bg="#1E1E1E", bd=0,highlightthickness=0)
  lifx_fav_color_button.place(relwidth=.25, relheight=.25, relx=.30, rely=.3)

  lifi_light_one = tk.Label (frame_one, text="Light One", font=("Helvatical bold",20), bg="#0d1421", fg="grey")
  lifi_light_one.place(relheight=.15, relwidth=.25, relx=.48, rely=.09)
  
  #Seond Frame
  frame_two = tk.Frame(lifx_cavnvas, bg="#0d1421", highlightthickness=2)
  frame_two.place(relwidth=.83,relheight=.3, rely=.45, relx=.08)
  
  light_two_image = tk.Label(frame_two, image=light_bulb_image_resize, bg="#0d1421", font=("Times New Roman", 10))
  light_two_image.place(relwidth=.2, relheight=.7, rely=.22, relx=.06)

  light_two_image_color = tk.Button(light_two_image, image=light_bulb_image_resize, bg="#0d1421", bd=0, activebackground="#0d1421")
  light_two_image_color.place(relwidth=1, relheight=1, rely=0, relx=0)

  light_two_brightness = tk.Scale(frame_two, from_=0, to=100, orient='horizontal', bg="#403E41", troughcolor="#1E1E1E", highlightthickness=0, activebackground ="#403E41", showvalue=0, bd=0)
  light_two_brightness.place(relwidth=.60, relx=.3, rely=.65)
  
  lifx_more_button_two = tk.Button (frame_two, text="More", font=("Helvatical bold",20), activebackground="grey", bg="#1E1E1E", bd=0, highlightthickness=0,)
  lifx_more_button_two.place(relwidth=.25, relheight=.25, relx=.65, rely=.3)

  lifx_fav_color_button_two = tk.Button (frame_two, text="Colors", font=("Helvatical bold",20), activebackground="grey", bg="#1E1E1E", bd=0,highlightthickness=0)
  lifx_fav_color_button_two.place(relwidth=.25, relheight=.25, relx=.30, rely=.3)

  lifx_light_two = tk.Label (frame_two, text="Light Two", font=("Helvatical bold",20), bg="#0d1421", fg="grey")
  lifx_light_two.place(relheight=.15, relwidth=.25, relx=.48, rely=.09)
  root_main_lifx.mainloop()

def main_ring_button():
  root_main_page.destroy()
  global root_main_ring
  root_main_ring = tk.Tk()
  ring_canvas = tk.Canvas(root_main_ring, height=HEIGHT,width=WIDTH, bg="black")
  ring_canvas.pack()
  
  ring_frame = tk.Frame(ring_canvas, bg="black" )
  ring_frame.place(relwidth=.95, relheight=.91, relx=.025, rely=.05)

  ring_frame_top = tk.Frame(ring_frame, bg="#123845")
  ring_frame_top.place(relwidth=.95, relheight=.2, relx=.025, rely=.013)

  ring_label_top = tk.Button(ring_canvas, command=ring_back_button, bg="black", fg="#0096c9", text="Ring", font=("Times New Roman",35), bd=0, highlightthickness=0, activebackground="black", activeforeground="#0096c9")
  ring_label_top.place(relwidth=.25, relheight=.06, relx=.4, rely=.002)


  root_main_ring.mainloop()
  
  

def main_page():
  def mainbuttonfunc():
    root_main_page.destroy()
  global root_main_page
  root_main_page=tk.Tk()
  root_main_page.title(" ")
  root_main_page.attributes("-fullscreen", True)
  
  main_canvas = tk.Canvas (root_main_page, height=HEIGHT, width=WIDTH, bg="#262626", bd=0, highlightthickness=0)
  main_canvas.pack()

  main_frame = tk.Frame (main_canvas, bg="black")
  main_frame.place(relheight=.2, relwidth=.9, relx=.04, rely=.05)

  main_button = tk.Button (main_frame, bd=0, text="Remote Control System", fg="grey", bg="black", font=("Times New Roman",35), command=mainbuttonfunc)
  main_button.place(relheight=1, relwidth=1)


  #MAIN_LIFX_PAGE
  light_frame = tk.Frame (main_canvas, bg="#44194B")

  light_frame.place(relheight=.7, relwidth=.45, relx=.04, rely=.25)

  lifx_button = tk.Button (
    light_frame,
    text="LIFX",
    activebackground="#483553",
    bg="#44194B",
    bd=0,
    highlightthickness=0,
    font=("Times New Roman", 25),
    command=main_lifx_button)
  lifx_button.place(relheight=1, relwidth=1)

  #MAIN_RING_PAGE
  ring_frame = tk.Frame (main_canvas, bg="#226A83")

  ring_frame.place(relheight=.7, relwidth=.45, relx=.49, rely=.25)

  ring_button = tk.Button (
    ring_frame,
    text="RING",
    activebackground="#1D7DA8",
    bg="#226A83",
    bd=0,
    highlightthickness=0,
    font=("Times New Roman", 25), 
    command=main_ring_button)
  ring_button.place(relheight=1,   relwidth=1)
  root_main_page.mainloop()
lifx_api_commands()
main_page()