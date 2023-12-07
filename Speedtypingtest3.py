import time
import random
from colorama import Fore, Style
from threading import Thread

def calculate_wpm(start_time, end_time, text):
    words = text.split()
    num_words = len(words)
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60
    wpm = num_words / minutes if minutes > 0 else 0
    return wpm

def calculate_accuracy(original_text, typed_text):
    original_words = original_text.split()
    typed_words = typed_text.split()
    
    correct_words = sum(1 for ow, tw in zip(original_words, typed_words) if ow == tw)
    total_words = len(original_words)
    
    accuracy = (correct_words / total_words) * 100 if total_words > 0 else 0
    return accuracy

def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def countdown():
    print(Fore.YELLOW + "Get ready! Starting in:")
    for i in range(3, 0, -1):
        print(Fore.YELLOW + str(i))
        time.sleep(1)
    print(Style.RESET_ALL)

def typing_test():
    print(Fore.CYAN + "Welcome to the Speed Typing Test!")
    print("Type the following text as fast as you can:")
    text = "The quick brown fox jumps over the lazy dog"
    print(Fore.GREEN + text)
    input("Press Enter when you're ready to start...")

    countdown_thread = Thread(target=countdown)
    countdown_thread.start()

    time.sleep(4)  # Adjust time for countdown + user readiness
    print(Fore.GREEN + "Start typing:")
    start_time = time.time()
    user_input = input(Style.RESET_ALL)
    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, user_input)
    accuracy = calculate_accuracy(text, user_input)

    print(f"\nYour typing speed is approximately {wpm:.2f} words per minute")
    print(f"Your accuracy is {accuracy:.2f}%")

    # Highlight incorrect words
    original_words = text.split()
    typed_words = user_input.split()
    highlighted_text = ""

    for ow, tw in zip(original_words, typed_words):
        if ow != tw:
            highlighted_text += Fore.RED + tw + " "
        else:
            highlighted_text += Fore.GREEN + tw + " "
    print("\nHighlighted Incorrect Words:")
    print(highlighted_text + Style.RESET_ALL)

typing_test()
