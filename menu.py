#image extraction and translation app

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
import cv2
from matplotlib import pyplot as plt
import importlib
import pytesseract as pytesseract
from pytesseract import image_to_string
from translate import Translator

Builder.load_file('menu.kv')


class MyLayout(Widget):

    def selected(self, filename):

        try:
            self.ids.my_image.source = filename[0]

            img = cv2.imread(filename[0])
            plt.imshow(img)
            plt.show()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            y1 = int(input("Enter upper vertical limit"))
            y2 = int(input("Enter lower vertical limit"))
            x1 = int(input("Enter left horizontal limit"))
            x2 = int(input("Enter right horizontal limit"))
            roi = gray[y1: y2, x1: x2]

            adaptive_threshold = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 95,
                                                       20)
            plt.imshow(adaptive_threshold)
            plt.show()
            text = pytesseract.image_to_string(adaptive_threshold)
            print(text[:-1])

            t = input("Enter source language")
            d = input("Enter target language")
            translator = Translator(from_lang=t, to_lang=d)
            translation = translator.translate(text)
            print(translation)

        except:
            pass


class AwesomeApp(App):
    def build(self):
        return MyLayout()


app= AwesomeApp().run()
