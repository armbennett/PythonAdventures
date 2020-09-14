import document,time

twinkle = "g3:5,g3,d4,d4,e4,e4,d4,3,c4:5,c4,b3,b3,a3,a3,g3"

tunesList = ['twinkle']
        
def play(arr):
    notes = arr.split(",")
    beat = 0.5
    for note in notes:
        if ":" in note:
            n = note.split(":")
            beat = float(n[1])/10
            note = n[0]
        elif note.isnumeric():
            beat = float(note)/10
        note = note.upper()
        sound = "<audio src='http://pythonadventures.co.uk/piano/"+note+".mp3' autoplay id='sound'></audio>"
        document.getElementById("sounds").innerHTML = sound
        time.sleep(beat)
        document.getElementById("sounds").innerHTML = ""
     
def tunes():
    for tune in tunesList:
        print(tune)