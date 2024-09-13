#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import yaml
import os

defaultSize = 32 # This is the defai;t output size for the png that will be the font, not the size of the font used to generate the bmp

fontFile = {
    "fontFredoka": "./ttf/Fredoka-Medium.ttf",
    "fontText": "./ttf/Noto_Sans/static/NotoSans-Medium.ttf",
    "fontEmoji": "./ttf/Noto_Emoji/static/NotoEmoji-Medium.ttf",
    "fontSymbols": "./ttf/Noto_Sans_Symbols/static/NotoSansSymbols-Medium.ttf",
    "fontSymbols2": "./ttf/Noto_Sans_Symbols_2/NotoSansSymbols2-Regular.ttf",
}

try:
    with open("./charset.yaml", "r") as read_file:
        charset = yaml.safe_load(read_file)
        print(charset)
except:
    print("Character set file missing")
    exit()

for setName in charset.keys():
    set = charset[setName]

    # If there is no directory to store the data create it
    if not os.path.exists("./png/" + setName):
        os.mkdir("./png/" + setName)
    
    if "canvasSize" in set and set["canvasSize"] is not None:
        canvasSize = set["canvasSize"]
    else:
        canvasSize = defaultSize

    if "scale" in set and set["scale"] is not None:
        fontSize = int(canvasSize * (set["scale"] / 100))
    else:
        fontSize = int(canvasSize * (7 / 8))

    if "voffset" in set and set["voffset"] is not None:
        fontVOffset = set["voffset"]
    else:
        fontVOffset = 0

    font = ImageFont.truetype(fontFile[set["font"]], fontSize)
    
    index = 0

    for character in set["chars"]:

        if "variableWidth" in set and set["variableWidth"]:
            canvasWidth = int(font.getlength(character))
        else:
            canvasWidth = canvasSize

        symbol = Image.new(mode="1", size=(canvasWidth, canvasSize), color=(1))
        drawing = ImageDraw.Draw(symbol)
        drawing.text((canvasWidth/2, (canvasSize / 2 ) + fontVOffset), character, fill=0, font=font, anchor="mm")

        if "names" in set and set["names"][index] is not None:
            fileName = "./png/" + setName + "/" + str(set["names"][index]) + ".png"
        else:
            fileName = "./png/" + setName + "/" + str(index) + ".png"
        
        symbol.save(fileName)
        index = index + 1