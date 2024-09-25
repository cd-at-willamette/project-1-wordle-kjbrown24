########################################
# Name:Kendall
# Collaborators (if any):Tutors, Brooke/Haley
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random

def wordle():
	gw = WordleGWindow()
	
	def display_word():
		secret_word="pizza"
		for i in range(N_COLS):
			f = secret_word[i]
			gw.set_square_letter(0,i,f)
	display_word()
		
	def enter_action():
		gw.show_message("You need to implement this method")
	
	
	gw.add_enter_listener(enter_action)



# Startup boilerplate
if __name__ == "__main__":
	wordle()
