import dearpygui.dearpygui as dpg



def nextImg():
    print("Next")

def giveAnswer():
    print("answer")

def checkInput():
    print("checking")


dpg.create_context()

with dpg.window(tag="Primary Window",label="Main"):

    dpg.add_text("Image Here")
    dpg.add_input_text(label="Your Choice", default_value="Input a value here")
    dpg.add_button(label="Check", callback=checkInput())
    dpg.add_input_text(label="Result", default_value="")
    dpg.add_button(label="Next", callback=nextImg())
    dpg.add_button(label="Answer", callback=giveAnswer())

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.set_primary_window("Primary Window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()