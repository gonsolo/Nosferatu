fps = 25
file = open("Nosferatu.sub", "w")
for i in range(10):
    start = str(fps*i)
    stop = str(fps*(i+1))
    countdown = str(10 - i)
    szene = "01/40"
    text = "C Dur, Tempo 120, Hutter"
    message = "{" + start + "}{" + stop + "}" + countdown + " -- " + szene + " | " + text + "\n"
    file.write(message)
file.close()
