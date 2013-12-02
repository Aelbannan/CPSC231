#################################################################################################
#T2G5 Final Project Submission                                                                  #
#By: The Apocalypse Pirates; Ahmed Elbannan, Hilmi Abou-Saleh, Ahmad Turkmani, Nasir Osman      #
#################################################################################################
#The Audio module has the ability to play files passed onto it.                                 #
#This only works on windows machines. Mac OSX and Linux are NOT supported                       #
#Note: SND_FILENAME pauses the game loop until sound is finished. Using SND_ASYNC               #
#################################################################################################



#Imports
import winsound
import os

def play_music(file):
	script_dir = os.path.dirname(__file__) #Absolute directory the script is in
	rel_path = 'resources/audio/' #The path that will never change, this is where the audio is located
	abs_file_path = os.path.join(script_dir, rel_path, file) #This is combining the three strings together
	winsound.PlaySound(abs_file_path, winsound.SND_ASYNC) #Playing the wave file(SND_ASYNC), and abs_file_path is the location of audio. 
	
