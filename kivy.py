# import kivy module
#from cProfile import label
from tkinter import Label
import kivy
from kivy.core.audio import SoundLoader

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
#kivy.require("1.9.1")


def printingmachine():
    print("hello world")


# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button


# class in which we are creating the button
class ButtonApp(App):

    def build(self):
        # use a (r, g, b, a) tuple
        btn = Button(text="Push Me !",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(300, 50))

        # bind() use to bind the button to function callback
        btn.bind(on_press=self.callback)
        return btn

    # callback function tells when button pressed
    def callback(self, event):
        printingmachine()


# creating the object root for ButtonApp() class
root = ButtonApp()

# run function runs the whole program
# i.e run() method which calls the target
# function passed to the constructor.
root.run()