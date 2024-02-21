import curses
from curses import wrapper
import time
import random
wpm=0

def start_screen(stdscr):
        stdscr.clear()
        stdscr.addstr("Welcome to the Speed Typing Test!")
        stdscr.addstr("\nPress any key to begin!")
        stdscr.refresh()
        stdscr.getkey()

def display_text(stdscr, target, current):
        stdscr.addstr(target)
        stdscr.addstr(2, 0, f"WPM: {wpm}")

        for i, char in enumerate(current):
                correct_char = target[i]
                color = curses.color_pair(1)
                if char != correct_char:
                        color = curses.color_pair(2)

                stdscr.addstr(0, i, char, color)


def wpm_test(stdscr):
        sample_text=[
    "The sun shines brightly in the clear blue sky, casting its warm rays upon the earth.",
    "She danced gracefully on the stage, her movements fluid and elegant..",
    "The curious cat chased the small mouse through the maze of bushes and trees, determined to catch",
    "He enjoys reading books of all genres, immersing himself in different worlds and gaining knowledge",
    "They went for a leisurely walk in the park, enjoying the tranquility of nature and the beauty of flowers.",
    "The homemade chocolate cake tasted delicious, its rich flavor melting in the mouth and leaving ",
    "I love listening to music, as it soothes my soul and uplifts my spirits, transporting me to a world of rhythms.",
    "They planted colorful flowers in the garden, carefully tending to each plant with love and dedication.",
    "He played the guitar beautifully, his fingers dancing effortlessly across the strings, producinng joy.",
    "She wrote a heartfelt letter expressing her deepest emotions and thoughts, pouring her soul onto the paper."
]

        target_text = random.choice(sample_text)
        current_text = []
        start_time = time.time()
        global wpm

        while True:
                time_elapsed = max(time.time() - start_time, 1)

                #calculating the wpm
                wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

                stdscr.clear()
                display_text(stdscr, target_text, current_text) # overwriting the current text over the target text
                stdscr.refresh()

                if "".join(current_text) == target_text:
                        break

                try:
                        key = stdscr.getkey()
                except:
                        continue
                try:


                        if key in ("KEY_BACKSPACE", '\b', "\x08"): #if backspace is pressed
                                if len(current_text) > 0:
                                        current_text.pop()

                        elif ord(key) == 27:   #if ESC is pressed
                                break

                        elif len(current_text) < len(target_text): #if the given text is not completed
                                current_text.append(key)
                except:
                        continue


def main(stdscr):


        #These are used for setting the color of the text for different conditions
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

        start_screen(stdscr) # This function is used to start the screen with the welcome message
        while True:
                try:
                        wpm_test(stdscr)

                        #After completing the test.
                        stdscr.addstr(3, 0, "You completed the text!")
                        stdscr.addstr(4,0,f"Your Typing speed is : {wpm}")
                        stdscr.addstr(5,0,"Press any key to continue or ESC to exit ")
                        key = stdscr.getkey()
                        if ord(key) == 27:
                                break
                except:
                        continue

wrapper(main)