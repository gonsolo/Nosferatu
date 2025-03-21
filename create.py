file = open("nosferatu.ly", "w")

notes = "\\version \"2.24.4\"\n"
notes += "\\score {\n"
notes += "  { "
for i in 'Nosferatu'.lower():
    o = ord(i) - ord('a') # get number in alphabet
    o  %= 8 # get back to a - h
    c = chr(o + ord('a')) # get char again
    notes += c
    notes += " "
notes += " }\n"
notes += "  \\midi {}"
notes += "}\n"
file.write(notes)
