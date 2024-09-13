# fontConvert
A simple script to convert individual characters from a ttf into a 1 bit bmp, for use with eink displays

## Configuration values

chars - list of characters that should be output
canvasSize - the x,y of the outputted image canvas
font - which font to use
scale - font size as a percentage of canvasSize
voffset - vertical offset from centre in pixels
names - list of filenames to use for the ouputted images
variableWidth - true if canvases should have a width based on the character width, false if canvas width and height should be the same

## Fonts used

https://github.com/PanicKk/Fredoka-Font/raw/main/static/Fredoka-Medium.ttf