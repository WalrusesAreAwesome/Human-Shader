notesStr = """

E1 G1
E2
D2
C2
B1
C2
/ B1 D2 A2


D1






E1 G1
E2
D2
C2
B1
C2
/ B1 E2 A2


G2






C2
A2
G2
F2
E2
F2
G2


/ G1 C2






F#1 A1
E2
D2
C2
B1
C2
/ F1 B1 E2


/ F1 B1 D2






E1 G1
E2
D2
C2
B1
C2
/ B1 D2 A2


D1






E1 G1
E2
D2
C2
B1
C2
/ B1 D2 A2


Bb1 E2 G2


B0
G1


A1 C2
A2
G2
F2
E2
F2
/ G1 G2


/ Eb2 G2 C3


C2
D2
F2
E2
C2
A1

/ F1 D2

/ E1 D2


C1
D1
G1
C1
D1
F1
E1





"""

name = "Test"
beatsPerMeasure = 4
factor = 2

lines = {
  "E3" : 0,
  "D3" : 1,
  "C3" : 2,
  "B2" : 3,
  "Bb2" : 4,
  "A#2" : 4,
  "A2" : 5,
  "Ab2" : 6,
  "G#2" : 6,
  "G2" : 7,
  "Gb2" : 8,
  "F#2" : 8,
  "F2" : 9,
  "E2" : 10,
  "Eb2" : 11,
  "D#2" : 11,
  "D2" : 12,
  "Db2" : 13,
  "C#2" : 13,
  "C2" : 14,
  "B1" : 15,
  "Bb1" : 16,
  "A#1" : 16,
  "A1" : 17,
  "Ab1": 18,
  "G#1" : 18,
  "G1" : 19,
  "Gb1" : 20,
  "F#1" : 20,
  "F1" : 21,
  "E1" : 22,
  "D1" : 23,
  "C1" : 24,
  "B0" : 25,
  "A0" : 26,
  "G0" : 27, 
  "D0" : 28, 
  "C0" : 29 
}


from PIL import Image, ImageDraw
import math



notesTemp = notesStr.split("\n")
notes = []
for i in range(len(notesTemp)):
  notes.append(notesTemp[i].split(" "))
  print(notes[i])

width = len(notes)*10*factor
output = Image.new('RGB', (30+width+10, 184), (240,240,255))
output1 = ImageDraw.Draw(output) 

#arrow
output1.line([(5,10),(25,10)], fill ="black", width = 3)
output1.line([(5,10),(15,5)], fill ="black", width = 3)
output1.line([(5,10),(15,15)], fill ="black", width = 3)

#staff
output1.line([(30,5),(30,179)], fill ="black", width = 3)
for i in range(30):
  w = 1
  if i%6 == 0 and i != 0:
    w = 3
  output1.line([(30, 5+i*6), (30+width, 5+i*6)], fill = "black", width = w)
for b in range(len(notes)*factor):
  if b%2 == 0:
    w = 1
    if b/2 % beatsPerMeasure == 0:
      w=2
    output1.line([(30+b*10, 5), (30+b*10, 179)], fill = "black", width = w)
  else:
    for d in range(1,18):
      output1.line([(30+b*10, d*10), (30+b*10, d*10+5)], fill = "black", width = 1)

#notes
for b in range(len(notes)):
  start = 0
  arp = False
  if notes[b][0] == "/":
    start = 1
    arp = True
  if arp:
    x2 = 30+b*10*factor
    x1 = x2 - len(notes[b])+2
    y1 = lines[notes[b][1]]*6+5
    y2 = lines[notes[b][-1]]*6+5
    output1.line((x1,y1,x2,y2), fill=(128, 0, 0), width=3)
  for n in range(start, len(notes[b])):
    if notes[b][n] != '':
      x = 30+b*10*factor
      if arp:
        x += n-len(notes[b])+1
      y = lines[notes[b][n]]*6+5
      output1.ellipse((x-2, y-2, x+2, y+1), fill=(255, 0, 0))
    

for i in range(20):
  print(i*8+1)

output.save("MusicBox_"+name+".png")