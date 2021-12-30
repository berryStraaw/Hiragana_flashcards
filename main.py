import PySimpleGUI
import dearpygui.dearpygui as dpg


def save_callback():
    print("Save Clicked")

def nextImg():
    print("Next")

def giveAnswer():
    print("answer")

def checkInput():
    print("checking")


dpg.create_context()

with dpg.window(tag="Primary Window", label="Hiragana Flashcards"):


    with dpg.window(label="Main Image", pos=(0, 0), width=420,height=200):
        dpg.add_text("Image Here")

    with dpg.window(label="Secondary Window", tag="secondary_window", pos=(0, 200), width=420, height=220):
        dpg.add_input_text(label="Your Choice", default_value="Input a value here")
        dpg.add_button(label="Check", callback=checkInput())
        dpg.add_input_text(label="Result", default_value="")
        dpg.add_button(label="Next", callback=nextImg())
        dpg.add_button(label="Answer", callback=giveAnswer())


dpg.setup_dearpygui()
dpg.create_viewport(title='Hiragana Flashcards', width=420, height=420)
dpg.set_primary_window("Primary Window", True)
dpg.show_viewport()
dpg.start_dearpygui()




