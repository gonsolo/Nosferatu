file = open("nosferatu.ly", "w")

notes = "\\version \"2.24.4\"\n"
notes += "\\score {\n"

notes += "\\new Staff {\n"
notes += "  \\set Staff.midiInstrument = \"tenor sax\"\n"

notes += "  { "
notes += "\\time 3/4\n"
notes += "\\tempo 4. = 96\n"
theme = ""
for i in 'Nosferatu'.lower():
    o = ord(i) - ord('a') # get number in alphabet
    o  %= 8 # get back to a - h
    c = chr(o + ord('a')) # get char again
    theme += c
    theme += " "
for _ in range(4):
    notes += theme
notes += " }\n"

notes += " }\n" # Staff

notes += "  \\midi {}\n"
notes += "}\n"
file.write(notes)
