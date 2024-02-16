def generate_5letter_word(seed_value = 10):
    # This function will return a 5-lette
    r word from gutenburg corpus, the following section
    # we import necessary packages for you.
    import nltk
    nltk.download('gutenberg')
    from nltk.corpus import gutenberg
    import random
    #random.seed(seed_value)
    words = list(nltk.Text(gutenberg.words('melville-moby_dick.txt')))
    # Your task
    # - create a list of 5-letter words, change all words into lowercases
    # - randomly select one word from this list and return it

    # *** Enter your code here ***
    words = list(nltk.Text(gutenberg.words('melville-moby_dick.txt')))
    i = 0
    lst = []
    while (i < len(words)):
      if (len(words[i]) == 5):
        lst.append(words[i].lower())
        i += 1
      else:
        i += 1
    indx = random.randint(0, len(lst))
    return (lst[indx])



def check_matched_chars(random_word, guess):
    # This function will check if the random word matched with the guessed word as using the following rules:
    # if the guessed character matched the random word's character with the same position, mark that guessed character as '@'
    # if the guessed character matched the random word's character but with different position, mark that guessed character as '#'
    # for examples
    # if the random word is 'cried' and the guess word is 'abcde'
    # then the return matched_chars will be 'ab###'
    # if the random word is 'clock' and the guess word is 'cheer'
    # then the return matched_chars will be '@heer'
    # if the random word is 'whole' and the guess word is 'wheel'
    # then the return matched_chars will be '@@#e#'

    # *** Enter your code here ***
    i = 0
    j = 0
    # random_word = list("beans")
    # guess = list("meatb")
    random_word = list(random_word)
    guess = list(guess)
    while (i < len(random_word)):
      while (j < len(guess)):
        if (guess[j] == random_word[i]):
          if (guess[j] == random_word[j]):
            guess[j] = '@'
          else:
            guess[j] = '#'
        j += 1
      j = 0
      i += 1
    guess = ' '.join(guess).replace(" ", "")
    return (guess)



def show_wordle(wordle, matches):
    # This function will print all guesses line by line with the colored described below.
    # where the matched character '@' will be colored with green background and
    #       the matched character '#' will be colored with the pink background.
    # To display a Hello with green background, use this code "\033[1;48;5;118mHello\033[0m"
    # To display a Hello with pink background, use this code "\033[1;48;5;207mHello\033[0m"
    # You can try print("\033[1;48;5;118mHello\033[0m") to see the result
    # Note: to display text in color, we can use ANSI escape sequence.
    # See https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit for more detail.


    # *** Enter your code here ***
    lst = [wordle[i:i + 5] for i in range(0, len(wordle), 5)]
    lst2 = [matches[i:i + 5] for i in range(0, len(matches), 5)]
    i = 0
    while (i < len(lst2)):
      j = 0
      output = []
      while (j < len(lst2[i])):
        if (lst2[i][j] == '@'):
          output.append("\033[1;48;5;118m" + lst[i][j] + "\033[0m")
        elif (lst2[i][j] == '#'):
          output.append("\033[1;48;5;207m" + lst[i][j] + "\033[0m")
        else:
          output.append(lst[i][j])
        j += 1
      i += 1
      print(*output, sep = "")



def check_win(random_word, guess):
    # This function will return True if the random_word and the guess are exactly matched.
    # Otherwise, it will return False

    # *** Enter your code here ***
    if (str(random_word) == str(guess)):
      return (True)
    else:
      return (False)


#
# DO NOT modify the code after this line
#
def main():
    wordle = ''
    # randomly generate a new 5-letter word
    random_word = generate_5letter_word()
    wordle = ''
    matched_chars = ''
    win = False
    for i in range (1, 7):
        print("Guess a 5-letter word tries: (" + str(i) + ")")
        guess = input()
        # show guess
        matched_chars_for_this_guess = check_matched_chars(random_word, guess)
        matched_chars += matched_chars_for_this_guess
        wordle += guess
        show_wordle(wordle, matched_chars)
        if check_win(random_word, guess):
            print("You win!!")
            win = True
            break
    if not win:
        print("random word is .... ", random_word)
        print("Try another time :)")
main()
