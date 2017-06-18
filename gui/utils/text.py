import pygame as pg
import defs as d
fontCol = (255,255,255)
fontType = 'Arial'
fontSize = 30
font = pg.font.SysFont(fontType, fontSize)

def text(text, coords, disp):
    global font, fontCol
    print(fontCol)
    txt = font.render(text, True, fontCol)
    disp.blit(txt, (txt.get_rect(center=coords)))
def fontCol(col):
    global fontCol
    fontCol = col
def setFont(fontT):
    global font, fontType, fontSize
    fontType = fontT
    font = pg.font.SysFont(fontType, fontSize)
def fontS(fontS):
    global font, fontType, fontSize
    if int(fontS) != fontSize:
        fontSize = int(fontS)
        font = pg.font.SysFont(fontType, fontSize)
############################################################
############################################################
############################################################



def findFontSize(str, fontType, width, height, maxFontSize = 5*d.px):
    fontSize = 0.5*d.px
    maxWidth = 0.9*width
    maxHeight = 0.9*height
    while True:
        font = pg.font.SysFont(fontType, int(fontSize))
        fontWidth, fontHeight = font.size(str)
        if fontWidth < maxWidth and fontHeight < maxHeight and fontSize < maxFontSize:
            fontSize += 0.2*d.px
        else:
            fontSize -= 0.2*d.px
            break
    return int(fontSize)

def findInclString(str, fontType, width, height, fontSize = None, maxFontSize = 5*d.px):
    if fontSize is None:
        fontSize = 0.5*d.px
        maxFontFound = False
    else:
        maxFontFound = True
        
    maxWidth = 0.9*width
    maxHeight = 0.9*height
    
    font = pg.font.SysFont(fontType, int(fontSize))
    fontWidth, fontHeight = font.size(str)
    
    while not maxFontFound:
        if fontHeight < maxHeight and fontSize < maxFontSize:
            fontSize += 0.2*d.px
        else:
            fontSize -= 0.2*d.px
            maxFontFound = True
        font = pg.font.SysFont(fontType, int(fontSize))
        fontWidth, fontHeight = font.size(str)

    ###shrink string so it fits in box with two dots
    if fontWidth <= maxWidth:
        return (str, int(fontSize))
    
    str = str + '..'
    xFit = False
    
    while not xFit:
        font = pg.font.SysFont(fontType, int(fontSize))
        fontWidth, fontHeight = font.size(str)
        if fontWidth > maxWidth:
            str = str[:-3] + '..'
        else:
            xFit = True
    return (str, int(fontSize))
     
     
     