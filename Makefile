all: play_audio
play_audio: nosferatu.midi
	timidity $<
nosferatu.midi: nosferatu.ly
	lilypond $<
nosferatu.ly: create.py
	python create.py
play_video: Nosferatu.sub
	vlc Nosferatu.webm
Nosferatu.sub:
	python ./generate_subtitles.py
clean:
	rm -f nosferatu.ly nosferatu.midi Nosferatu.sub
