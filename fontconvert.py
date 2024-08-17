#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import yaml
import os

defaultSize = 32 # This is the output size for the bmp that will be the font, not the size of the font used to generate the bmp

fontFile = {
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
    if not os.path.exists("./bmp/" + setName):
        os.mkdir("./bmp/" + setName)
    
    if "size" in set and set["size"] is not None:
        outputSize = set["size"]
    else:
        outputSize = defaultSize

    if "scale" in set and set["scale"] is not None:
        fontSize = int(outputSize * (set["scale"] / 100))
    else:
        fontSize = int(outputSize * (7 / 8))

    if "voffset" in set and set["voffset"] is not None:
        fontVOffset = set["voffset"]
    else:
        fontVOffset = 0

    font = ImageFont.truetype(fontFile[set["font"]], fontSize)
    
    index = 0

    for character in set["chars"]:

        symbol = Image.new(mode="1", size=(outputSize, outputSize), color=(1))
        drawing = ImageDraw.Draw(symbol)
        drawing.text((outputSize/2, (outputSize / 2 ) + fontVOffset), character, fill=0, font=font, anchor="mm")

        if "names" in set and set["names"][index] is not None:
            fileName = "./bmp/" + setName + "/" + str(set["names"][index]) + ".png"
        else:
            fileName = "./bmp/" + setName + "/" + str(index) + ".png"
        
        symbol.save(fileName)
        index = index + 1