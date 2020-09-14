import document,time
colors = ['rgb(0, 0, 0)','rgb(0, 0, 255)','rgb(0, 255, 0)','rgb(0, 255, 255)','rgb(255, 0, 0)','rgb(255, 0, 255)','rgb(255, 255, 0)','rgb(255, 255, 255)']
piano = ['C4','D4','E4','F4','G4','A4','B4','C5']
notes = ['do','re','mi','fa','so','la','ti','do5']

house = "7777777007777777:7777700440077777:7777004444007777:7770044334400777:7700443333440077:7004444444444007:0043344334433400:7443344334433447:7443344334433447:7444444444444447:7443342222433447:7443342222433447:7443342222433447:7444442222444447:7444442222444447:7444442222444447"
castle = "3300030000300033:3307030770307033:3307000770007033:3307777777777033:0000770000770000:0770770770770770:0770770770770770:0770000770000770:0777777777777770:0777770000777770:0777700000077770:0777700000077770:0777700000077770:0777700000077770:0777700000077770:0000000000000000"
heart = "777007777700777:770440777044077:704444070444407:044444404444440:044444444444440:044444444444440:044444444444440:704444444444407:770444444444077:777044444440777:777704444407777:777770444077777:777777040777777:777777707777777"
happy = "777777000777777:777700666007777:777066666660777:770666666666077:706666666666607:706600666006607:066600666006660:066666666666660:066666666666660:706606666606607:706660666066607:770666000666077:777066666660777:777700666007777:777777000777777"
sad = "777777000777777:777700666007777:777066666660777:770666666666077:706600666006607:706600666006607:066666666666660:066666666666660:066666000666660:706660666066607:706606666606607:770666666666077:777066666660777:777700666007777:777777000777777"
star = "777777707777777:777777060777777:777777060777777:777770666077777:000000666000000:706666666666607:770666666666077:777066666660777:777706666607777:777706666607777:777066666660777:777066606660777:770666070666077:770600777006077:700077777770007"
island = "333333333333333:333363333333333:333666333663333:336666636666333:366666666666633:366666666666663:366666666666663:336666666666633:333666666666333:333366666666333:333336666663333:333336666666333:333333666666333:333333333663333:333333333333333"

imagesList = ['house','castle','heart','happy','sad','star','island']

curColor = 1

def size(r,c):
    tab = "<table id='grid'>"
    for row in range(r):
        tab += "<tr>"
        for col in range(c):
            tab += "<td id= 'r"+str(row)+"c"+str(col)+"' style='width: "+str(100//c)+"%; padding-bottom: "+str(100//c)+"%; background-color: rgb(0, 0, 0);'></td>"
        tab += "</tr>"

    document.getElementById("image").innerHTML = tab

def custom(a):
    arr = a.split(":")
    try:
        for row in range(len(arr)):
            for col in range(len(arr[row])):
                document.getElementById("r"+str(row)+"c"+str(col)).setCSS("background-color",colors[int(arr[row][col])])
    except:
        print("Pattern does not match image dimensions")
        
def load(a):
    arr = a.split(":")
    size(len(arr),len(arr[0]))
    try:
        for row in range(len(arr)):
            for col in range(len(arr[row])):
                document.getElementById("r"+str(row)+"c"+str(col)).setCSS("background-color",colors[int(arr[row][col])])
    except:
        print("Pattern does not match image dimensions")

def pixel(p,c):
    try:
        cells = document.getElementsByTagName('td')
        cells.reverse()
        cells[p].setCSS("background-color",colors[c])
    except:
        pass
        
def play():
    cells = document.getElementsByTagName('td')
    cells.reverse()
    for cell in range(len(cells)):
        col = cells[cell].getCSS("background-color")
        note = colors.index(col)
        sound = "<audio src='http://pythonadventures.co.uk/piano/"+piano[note]+".mp3' autoplay id='sound'></audio>"
        document.getElementById("sounds").innerHTML = sound
        time.sleep(0.3)
        document.getElementById("sounds").innerHTML = ""
        
def sing():
    cells = document.getElementsByTagName('td')
    cells.reverse()
    for cell in range(len(cells)):
        col = cells[cell].getCSS("background-color")
        note = colors.index(col)
        sound = "<audio src='http://pythonadventures.co.uk/notes/"+notes[note]+".mp3' autoplay id='sound'></audio>"
        document.getElementById("sounds").innerHTML = sound
        time.sleep(1)
        document.getElementById("sounds").innerHTML = ""
        
def images():
    for image in imagesList:
        print(image)
        
def nextColor():
    global curColor
    c = curColor
    if curColor >= 7:
        curColor = 1
    else:
        curColor += 1
    return c
