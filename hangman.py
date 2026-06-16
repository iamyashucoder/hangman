
print("""
 _    _                                         

| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
    """)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''',]
import random
random_words = ['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop',
 'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 
 'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 
 'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider', 
 'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language', 
 'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus', 
 'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful', 'mobile', 'telephone', 'camera', 'guitar', 'piano', 'violin', 'drum', 'flute', 'trumpet',
 'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard', 
 'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser', 
 'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen', 'rectangle', 'triangle', 'circle', 'square', 'diamond', 'pentagon', 'hexagon', 'octagon',
 'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
 'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
 'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph', 
 'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'flower'
 'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete', 'wind'
 'brain', 'control', 'prophet', 'freedom', 'harbour', 'configuration', 'software', 'hardware', 'programming', 'development', 'python', 'java',]
random_word = random.choice(random_words).lower()
print(random_word)
correct_guess = []
game_over = False
lives = 6
while not game_over :
    display = ""
    user_guess = input("Guess a letter: ").lower()
    if user_guess in correct_guess:
        print(f"You have already guessed the letter '{guess}'. Try a different letter.")
        continue
    for letter in random_word:
        if letter == user_guess:
           display += letter
           correct_guess.append(letter)
        elif letter in correct_guess:
           display += letter
        else:
           display += "_"
    print(display)
    if user_guess not in random_word:
        lives -= 1
        print(f"you have {lives} lives left.")
        print(stages[lives])   

        if lives == 0:
           game_over = True
           print("You lose!")

    if display == random_word:
          game_over = True
          print("You win!")
