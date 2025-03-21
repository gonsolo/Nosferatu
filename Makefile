all: play
play: Nosferatu.sub
	vlc Nosferatu.webm
Nosferatu.sub:
	python ./generate_subtitles.py
