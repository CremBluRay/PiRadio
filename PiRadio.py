# # # # # # # # # # # # #
#						#
#						#
#						#
#		Pi Radio		#
#		By				#
#		Jackson			#
#		Hoggard			#
#	    (c)2018			#
#						#
#						#
#						#
# # # # # # # # # # # # #

import os, argparse, random
from colorama import Fore, Back, Style
from multiprocessing import Process

parser = argparse.ArgumentParser(prog='python PiRadio.py', description='Broadcasts WAV/MP3 file over FM using RPI GPIO #4 pin.')
parser.add_argument("-s", "--song_file", help="Set song to play")
parser.add_argument("-f", "--frequency", help="Set TX frequency. Acceptable range 87.1-108.2", type=float)
arg = parser.parse_args()

playlist = []
frequency = 0

def start():
	os.system("clear")
	print("Starting Pi Radio")
	
	if arg.frequency is None:
		frequency = 0 #raw_input("Enter the frequency (Press Enter/Return for 99.9MHz): ")
		if frequency == 0:
			frequency = '99.9'
	elif 87.1 >= arg.frequency >= 108.2:
		print "Frequency is out of range.";exit()
	else:
		frequency = str(arg.frequency)
	print ("\nFrequency set to " + frequency)
	
	makePlaylist()
	os.system("clear")
	
	begin()
	
	print "Songs in Playlist:\n" + Fore.GREEN + "______________________________\n"
	
	i = 0
	while i < len(playlist):
		print Style.RESET_ALL + playlist[i]
		i += 1
	
	print Fore.GREEN + "______________________________"
	
	print Fore.WHITE + "Type Choice Number:\n1. Shuffle Play\n2. Talk\n3. Exit\n\n\n"
	userInput()
	
def begin():
	print(Fore.RED + Back.WHITE + '#	PiRadio Station v1.1	#')
	print(Style.RESET_ALL)

def play(song):
	print Style.RESET_ALL + "\n"
	arg.song_file = song
	try:
		if ".mp3" in arg.song_file.lower():
			os.system("ffmpeg -i "+arg.song_file+" "+"-f s16le -ar 22.05k -ac 1 - | sudo ./fm_transmitter -f"+" "+frequency+" "+" - ")
		elif ".wav" in arg.song_file.lower():
			os.system("sudo ./fm_transmitter -f"+" "+ "99.9" +" " + "/home/pi/fm_transmitter/music/" + arg.song_file)
		else:
			print "That file extension is not supported."
			print "File name provided: %s" %arg.song_file
			raise IOError
	except Exception:
		print "Something went wrong. Halting."; exit()
	except IOError:
		print "There was an error regarding file selection. Halting."; exit()

def makePlaylist():
	for root, dirs, files, in os.walk("/home/pi/fm_transmitter/music"):
		for file in files:
			if file.endswith(".wav"):
				#print(file)
				playlist.append(file)

def playSongs():
	print Style.RESET_ALL + "\n"
	currentsong = ''
	i = 0
	run = True
	while run == True:
		i = random.randint(0, len(playlist) - 1)
		print Fore.RED + Back.WHITE + "Now Playing: " + playlist[i] + "\n"
		print Style.RESET_ALL
		p1 = Process(target = play(playlist[i]))
		p1.start()
		p2 = Process(target = checkForQuit)
		p2.start()
		
def talk():
	print("Still testing. Please choose a different option")
	userInput()

def userInput():
	choice = input(" > ")
	processInput(choice)
	
def processInput(c):
	if(c == 1): playSongs()
	if(c == 2): talk()
	if(c == 3): exit()
	else:
		userInput()
		
def checkForQuit():
	if(keyboard.is_pressed('q')):
		p1.stop()

start()
