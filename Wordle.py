########################################
# Name:Kendall
# Collaborators (if any):Tutors, Brooke/Haley,Ayiana
# GenAI Transcript (if any):Chat GPT
# Estimated time spent (hr):20
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random

def wordle():
	gw = WordleGWindow()
	
	def word_generator():
		hidden_word = " "
		while len(hidden_word) !=5:
			hidden_word = random.choice(ENGLISH_WORDS)
		return hidden_word.lower()
		
	secret_word = word_generator()
	print(secret_word)
	
	def display_word():
		for i in range(N_COLS):# n columns=5 0,1,2,3,4
			f = secret_word[i]
			gw.set_square_letter(row,i,f)
		
	def enter_action():
		letter = ""
		row=gw.get_current_row()
		for i in range(N_COLS):
			letter+=gw.get_square_letter(row,i)
		
		word=letter.lower()
		if not is_english_word(word): # NOTE: do NOT make random words yet, different milestone - Tutor Haley
			gw.show_message("Not in word list")
			return
			
		#Variable to keep track of which letters have been "used"
		secret_word_used= secret_word #track the letters of the secret word
		
		#step 1: check for correct (green) letter first
		for col in range(N_COLS):
			if word[col] == secret_word[col]:
				gw.set_square_color(row,col,CORRECT_COLOR)
				gw.set_key_color(word[col], CORRECT_COLOR)
				secret_word_used=secret_word_used.replace(secret_word[col]," ", 1)
				
		#step 2:Check for present (yellow) letters
		for col in range(N_COLS):
			if gw.get_square_color(row,col) != CORRECT_COLOR:
				if word[col] in secret_word_used and gw.get_square_letter(row,col) != CORRECT_COLOR:
					gw.set_square_color(row,col,PRESENT_COLOR)
					if gw.get_key_color(word[col])!= CORRECT_COLOR:
						gw.set_key_color(word[col],PRESENT_COLOR)
					secret_word_used=secret_word_used.replace(word[col]," ", 1) #Mark letter as used
				else:
					gw.set_square_color(row, col, MISSING_COLOR)
					gw.set_key_color(word[col],MISSING_COLOR)
					
					#Not in the word
					#If guess[col] == secret_word[col], color is already set to green, do nothing.
					
		#Step 3: Rows going down
		gw.set_current_row(row+1)

	#enter_action()
	gw.add_enter_listener(enter_action)



# Startup boilerplate
if __name__ == "__main__":
	wordle()
