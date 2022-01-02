import random

import PySimpleGUI
import dearpygui.dearpygui as dpg
import os,glob

test="string.png"
print(test[0:-4])

folder_path = 'Images'
cards= []
answer=""

dpg.create_context()
with dpg.texture_registry(show=False):
    for filename in glob.glob(os.path.join(folder_path, '*.png')):
        cards.append(filename[7:])
        width, height, channels, data = dpg.load_image(filename)
        dpg.add_dynamic_texture(width, height, data, tag=filename[7:])


def getRandomCard():
    return cards[random.randrange(len(cards))]

def deleteCard():
    dpg.delete_item("card")

def giveAnswer():
    dpg.set_value("output", answer[0:-4])

def checkInput():
    #print(dpg.get_value("inp"))
    if(dpg.get_value("inp").lower()==answer[0:-4]):
        dpg.set_value("output", "True")
    else:
        dpg.set_value("output", "False")

def drawCard(card):
    dpg.add_image(card, width=100, height=100, tag="card")

def nextCard(sender, app_data, user_data):
    answer = getRandomCard()
    dpg.set_value("card", answer[data])

with dpg.window(tag="Primary Window", label="Hiragana Flashcards"):

    #Display group
    with dpg.group():
        answer=getRandomCard()
        drawCard(answer)
        #dpg.add_image(answer, width=100,height=100)
        #img = dpg.add_image(answer, width=100, height=100, tag="card")
        #dpg.delete_item(img)

    #First interface row
    #user input
    #check answer
    #output
    with dpg.group(horizontal=True):
        dpg.add_input_text(label="Your Choice", hint="Input a value here", width=100, no_spaces=True, tag="inp")
        dpg.add_button(label="Check",width=100, height=50, tag="checkButton")
        dpg.add_input_text(label="Result", tag="output")

    #Second interface row
    #next card
    #give answer
    with dpg.group(horizontal=True):
        dpg.add_button(label="Next",width=100, height=50, tag="nextCardButton")
        dpg.add_button(label="Answer",width=100, height=50, tag="giveAnswer")
    #Handlers

    #checker handler
    with dpg.item_handler_registry(tag="check") as handler:
        dpg.add_item_clicked_handler(callback=checkInput)

    #answer handler
    with dpg.item_handler_registry(tag="ansHandler") as handler:
        dpg.add_item_clicked_handler(callback=giveAnswer)

    #Next Card handler
    with dpg.item_handler_registry(tag="nextCardHandler") as handler:
        dpg.add_item_clicked_handler(callback=nextCard)

    #Binding buttons to handlers
    dpg.bind_item_handler_registry("checkButton", "check")
    dpg.bind_item_handler_registry("giveAnswer", "ansHandler")
    dpg.bind_item_handler_registry("nextCardButton", "nextCardHandler")

print(dpg.get_item_configuration("card"))


#Runing the app
dpg.create_viewport(title='Hiragana Flashcards', width=420, height=420)
dpg.setup_dearpygui()
dpg.set_primary_window("Primary Window", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()




