file = open("nosferatu.ly", "w")

notes = "\\version \"2.24.4\"\n"
notes += "\\score {\n"

notes += "\\new Staff {\n"
notes += "  \\set Staff.midiInstrument = \"tenor sax\"\n"

notes += "  { "
notes += "\\time 3/4\n"
notes += "\\tempo 4. = 96\n"
theme = " "
for i in 'Nosferatu'.lower():
    o = ord(i) - ord('a') # get number in alphabet
    o  %= 8 # get back to a - h
    c = chr(o + ord('a')) # get char again
    theme += c
    theme += " "

krebs = theme[::-1]


def kehr_um(thema):
    tonleiter = "abcdefg "
    umkehrung = " "
    for i in thema:
        index = tonleiter.find(i)
        index = 6 - index
        if index > -1:
            umkehrung += tonleiter[index] + " "
    return umkehrung

umkehrung = kehr_um(theme)
krebs_umkehrung = kehr_um(krebs)

for _ in range(4):
    notes += theme + "\n"
    notes += krebs + "\n"
    notes += umkehrung + "\n"
    notes += krebs_umkehrung + "\n"
notes += " }\n"

notes += " }\n" # Staff

notes += "  \\midi {}\n"
notes += "}\n"
file.write(notes)
