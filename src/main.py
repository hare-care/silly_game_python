import random
import ctypes
import win32api, win32con
import os
import time
from pathlib import Path

def screen_off():
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)

def fill_bar(delay):
    for i in range(101):
        print("|", end='')
        time.sleep(delay)
        for j in range(i):
            print("=", end='')
        print(">", end='')
        for k in range(100-i):
            print(" ", end='')
        print(f"|{i}%", end='\r')
    print("")



def delete_files(path, depth, max_depth = None):
    if max_depth is not None:
        if depth > max_depth:
            return
    
    entries = Path(path)
    for entry in entries.iterdir():
        if entry.is_dir():
            try:
                if entry.name == "Documents":
                    max_depth = None
                    depth = 0
                delete_files(str(entry), int(depth)+1, max_depth)
            except:
                pass
            print(f"deleting {entry.name}")

            # if entry.name == "Windows":
            if str(entry) == "\Windows":
                print(str(entry))
                fill_bar(0.5)
                return
            else:
                fill_bar(min(entry.stat().st_size * 0.0000005, 0.005)+0.0005)

def check_guess(user_guess, correct_answer):
    if (user_guess == correct_answer):
        print("You won!\n\r")
        return True
    else:
        print("You lost! Say goodbye to your laptop.")
        delete_files('/', 0, 1)
        screen_off()
        return False

def game_loop(level):
    answer = random.randrange(10**level)
    # See what the answer is supposed to be
    if (level == 1):
        print("Silly game!")
    else:
        print(f"Level {level}!")
    guess = int(input(f"Guess a number between 0 and {10**level}: "))
    result = check_guess(guess, answer)
    return result

def main():
    level = 1
    while (game_loop(level)):
        level = level + 1
    

if __name__ == "__main__":
    main()
