import turtle, textwrap, document, time

#defines bitmap patterns for letters
A='2,0000000:0011100:0100010:0100010:0111110:0100010:0100010:0100010:0000000'
B='2,0000000:0111100:0100010:0100010:0111100:0100010:0100010:0111100:0000000'
C='2,0000000:0011100:0100010:0100000:0100000:0100000:0100010:0011100:0000000'
D='2,0000000:0111100:0100010:0100010:0100010:0100010:0100010:0111100:0000000'
E='2,0000000:0111110:0100000:0100000:0111100:0100000:0100000:0111110:0000000'
F='2,0000000:0111110:0100000:0100000:0111100:0100000:0100000:0100000:0000000'
G='2,0000000:0011100:0100010:0100000:0100000:0100110:0100010:0011100:0000000'
H='2,0000000:0100010:0100010:0100010:0111110:0100010:0100010:0100010:0000000'
I='2,0000000:0011100:0001000:0001000:0001000:0001000:0001000:0011100:0000000'
J='2,0000000:0001110:0000100:0000100:0000100:0000100:0100100:0011000:0000000'
K='2,0000000:0100010:0100100:0101000:0110000:0101000:0100100:0100010:0000000'
L='2,0000000:0100000:0100000:0100000:0100000:0100000:0100000:0111110:0000000'
M='2,0000000:0100010:0110110:0101010:0101010:0100010:0100010:0100010:0000000'
N='2,0000000:0100010:0100010:0110010:0101010:0100110:0100010:0100010:0000000'
O='2,0000000:0011100:0100010:0100010:0100010:0100010:0100010:0011100:0000000'
P='2,0000000:0111100:0100010:0100010:0111100:0100000:0100000:0100000:0000000'
Q='2,0000000:0011100:0100010:0100010:0100010:0101010:0100100:0011010:0000000'
R='2,0000000:0011100:0100010:0100010:0111100:0101000:0100100:0100010:0000000'
S='2,0000000:0011110:0100000:0100000:0011100:0000010:0000010:0111100:0000000'
T='2,0000000:0111110:0001000:0001000:0001000:0001000:0001000:0001000:0000000'
U='2,0000000:0100010:0100010:0100010:0100010:0100010:0100010:0011100:0000000'
V='2,0000000:0100010:0100010:0100010:0100010:0010100:0010100:0001000:0000000'
W='2,0000000:0100010:0100010:0100010:0101010:0101010:0101010:0010100:0000000'
X='2,0000000:0100010:0100010:0010100:0001000:0010100:0100010:0100010:0000000'
Y='2,0000000:0100010:0100010:0010100:0001000:0001000:0001000:0001000:0000000'
Z='2,0000000:0111110:0000010:0000100:0001000:0010000:0100000:0111110:0000000'
a='2,0000000:0011100:0000010:0000010:0011110:0100010:0100010:0011110:0000000'
b='2,0000000:0100000:0100000:0100000:0111100:0100010:0100010:0111100:0000000'
c='2,0000000:0000000:0011100:0100000:0100000:0100000:0100000:0011100:0000000'
d='2,0000000:0000010:0000010:0000010:0011110:0100010:0100010:0011110:0000000'
e='2,0000000:0000000:0011100:0100010:0111110:0100000:0100010:0011100:0000000'
f='2,0000000:0000000:0011000:0100000:0100000:0111000:0100000:0100000:0000000'
g='2,0000000:0011110:0100010:0100010:0100010:0011110:0000010:0011100:0000000'
h='2,0000000:0100000:0100000:0100000:0111100:0100010:0100010:0100010:0000000'
i='2,0000000:0001000:0000000:0001000:0001000:0001000:0001000:0001000:0000000'
j='2,0000000:0000100:0000000:0001100:0000100:0000100:0000100:0001000:0000000'
k='2,0000000:0100000:0100000:0100100:0101000:0110000:0101000:0100100:0000000'
l='2,0000000:0001000:0001000:0001000:0001000:0001000:0001000:0001000:0000000'
m='2,0000000:0000000:0000000:0110100:0101010:0101010:0101010:0101010:0000000'
n='2,0000000:0000000:0000000:0111100:0100010:0100010:0100010:0100010:0000000'
o='2,0000000:0000000:0011100:0100010:0100010:0100010:0100010:0011100:0000000'
p='2,0000000:0000000:0111000:0100100:0100100:0111000:0100000:0100000:0000000'
q='2,0000000:0000000:0001110:0010010:0010010:0001110:0000010:0000010:0000000'
r='2,0000000:0000000:0101000:0110000:0100000:0100000:0100000:0100000:0000000'
s='2,0000000:0000000:0011100:0100000:0110000:0001100:0000100:0111000:0000000'
t='2,0000000:0010000:0010000:0011100:0010000:0010000:0010000:0001100:0000000'
u='2,0000000:0000000:0100010:0100010:0100010:0100010:0100010:0011110:0000000'
v='2,0000000:0000000:0100010:0100010:0010100:0010100:0001000:0001000:0000000'
w='2,0000000:0000000:0100010:0100010:0101010:0101010:0010100:0010100:0000000'
x='2,0000000:0000000:0100010:0010100:0001000:0001000:0010100:0100010:0000000'
y='2,0000000:0000000:0100010:0010100:0010100:0001000:0001000:0010000:0000000'
z='2,0000000:0000000:0011110:0000010:0000100:0001000:0010000:0011110:0000000'
#defines bitmap patterns for standard images
happy='3,111111111000000000000111111111:111111000110110110110000111111:111000110110110110110110000111:000110110000110110000110110000:000110110110110110110110110000:000110000110110110110000110000:000110110000000000000110110000:111000110110110110110110000111:111111000110110110110000111111:111111111000000000000111111111'
sad='3,111111111000000000000111111111:111111000110110110110000111111:111000110110110110110110000111:000110110000110110000110110000:000110110110110110110110110000:000110110110000000110110110000:000110110000110110000110110000:111000110110110110110110000111:111111000110110110110000111111:111111111000000000000111111111'
heart='3,111111000111111111000111111:111000100000111000100000111:000100100100000100100100000:000100100100100100100100000:111000100100100100100000111:111111000100100100000111111:111111111000100000111111111:111111111111000111111111111'

#list of pre-defined bitmaps
images = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,happy,sad,heart]

#colour depth details
bit1 = {0:'rgb(255, 255, 255)',1:'rgb(0, 0, 0)'}
bit2 = {0:'rgb(0, 0, 0)',1:'rgb(85, 255, 255)',2:'rgb(255, 85, 255)',3:'rgb(255, 255, 255)'}
bit3 = [1,1,1]
bit6 = [3,3,3]
bit8 = [7,3,7]
bit9 = [7,7,7]
bit12 = [15,15,15]
depths = {1:bit1,2:bit2,3:bit3,6:bit6,8:bit8,9:bit9,12:bit12}

#dictionary mapping ASCII codes to appropriate bitmap
letter = {65:A,66:B,67:C,68:D,69:E,70:F,71:G,72:H,73:I,74:J,75:K,76:L,77:M,78:N,79:O,80:P,81:Q,82:R,83:S,84:T,85:U,86:V,87:W,88:X,89:Y,90:Z,97:a,98:b,99:c,100:d,101:e,102:f,103:g,104:h,105:i,106:j,107:k,108:l,109:m,110:n,111:o,112:p,113:q,114:r,115:s,116:t,117:u,118:v,119:w,120:x,121:y,122:z}

#takes a set of rgb values and a colour depth and calculates the equivalent 24bit RGB value
def getColour(rgb,depth):
    hx = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    newRGB = []
    bits = depths[depth]
    for cx in range(len(rgb)):
        px = rgb[cx]
        if px.isalpha():
            px = hx[px.upper()]
        newRGB.append((255//bits[cx])*int(px))
    return 'rgb('+str(newRGB[0])+", "+str(newRGB[1])+", "+str(newRGB[2])+")"

#splits string into list
def splitchar(word): 
    return [char for char in word]

#lists pre-defined images
def listimages(): 
    for im in images:
        print(im, end = '')
    print("")

#clears the screen
def clear():
    document.getElementById("image").innerHTML = ""

#the Bitmap class for displaying a bitmap pattern
class Bitmap:
    def __init__(self, image="",depth=1,width=6,height=6):
        self.tx = turtle.Turtle()
        self.image = []
        self.depth = depth
        self.width = width
        self.height = height
        self.total = width * height
        self.next = 0
        if len(image) < 1:
            for rx in range(height):
                line = []
                for cx in range(width):
                    if self.depth<3:
                        line.append("0")
                    else:
                        line.append("000")
                self.image.append(line)
        else:
            length = 3
            lines = []
            if "," in image:
                spl1 = image.split(",")
                self.depth = int(spl1[0])
                temp = spl1[1].split(":")
            else:
                temp = image.split(":")
            for rx in temp:
                if self.depth < 3:
                    line = splitchar(rx)
                else:
                    line = textwrap.wrap(rx, length)
                lines.append(line)
            self.image = lines
    
    #draws the bitmap using the turtle
    def draw(self,size=300,xx=-200,yx=200):
        tx = self.tx
        length = 3
        if self.depth < 3:
            length = 1
        tx.hideturtle()
        tx.speed(0)
        tx.penup()
        tx.goto(xx,yx)
        xstart = xx
        ystart = yx
        imgl = self.image
    
        px = size/(len(imgl[0]))
        for rx in imgl:
            for cx in rx:
                if self.depth < 3:
                    bits = depths[self.depth]
                    tx.color(bits[int(cx)])
                else:
                    tx.color(getColour(cx,self.depth))
                for sx in range(4):
                    tx.begin_fill()
                    tx.forward(px)
                    tx.right(90)
                tx.fd(px)
                tx.end_fill()
            yx -= px
            tx.goto(xx,yx)
        tx.goto(xstart,ystart)
        tx.pendown()
        tx.color('black')
        for sx in range(2):
            tx.fd(size)
            tx.rt(90)
            tx.fd((size/(len(imgl[0])))*len(imgl))
            tx.rt(90)
    
    #sets an individual pixel in the bitmap image
    def pixel(self,value,number=0,row=-1,col=-1):
        if row > -1 and col > -1:
            number = row*col
        pix = 0
        for rx in range(len(self.image)):
            for cx in range(len(self.image[rx])):
                if pix == number:
                    self.image[rx][cx] = value
                pix += 1

    #plays the bitmap pattern as music, each colour code represents a different note
    def play(self,speed=0.3):
        notes = ['C2','Db2','D2','Eb2','E2','F2','Gb2','G2','Ab2','A2','Bb2','B2','C3','Db3','D3','Eb3','E3','F3','Gb3','G3','Ab3','A3','Bb3','B3','C4','Db4','D4','Eb4','E4','F4','Gb4','G4','Ab4','A4','Bb4','B4','C5','Db5','D5','Eb5','E5','F5','Gb5','G5','Ab5','A5','Bb5','B5','C6','Db6','D6','Eb6','E6','F6','Gb6','G6','Ab6','A6','Bb6','B6','C7','Db7','D7','Eb7']
        
        hx = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        
        for rx in range(len(self.image)):
            for cx in range(len(self.image[rx])):
                total = 0
                for ix in self.image[rx][cx]:
                    nx = ix
                    if nx.isalpha():
                        nx = hx[nx.upper()]
                    total+=int(nx)
                note = notes[total]
                sound = "<audio src='http://pythonadventures.co.uk/piano/"+note+".mp3' autoplay id='sound'></audio>"
                document.getElementById("sounds").innerHTML = sound
                time.sleep(speed)
                document.getElementById("sounds").innerHTML = ""
    
    #cycles through all the colours available in the given colour depth            
    def nextColour(self):
        if self.depth < 3:
            col = str(self.next)
            self.next += 1
            if self.next > self.depth**2-(self.depth-1):
                self.next = 0
            return col
        val = bin(self.next)[2:]
        hx = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        col = ""
        while len(val) < self.depth:
            val = "0" + val
        if self.depth < 3:
            nums = splitchar(val)
        else:
            nums = textwrap.wrap(val, (self.depth//3))
        for nx in nums:
            dx = int(nx,2)
            if dx > 9:
                dx = hx[dx]
            col += str(dx)
        self.next += 1
        if self.next > self.depth**2-(self.depth-1):
            self.next = 0
        return col
    
    #resets the next colour to the start
    def resetColour(self):
        self.next = 0