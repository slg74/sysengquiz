#!/usr/bin/python

import random

def get_question():
    lines = open('questions.md').read().splitlines()
    if lines:
        return random.choice(lines)
    else:
        have_question = False
        while not have_question:
            question = random.choice(lines)
            if question:
                have_question = True

                return question
   
def main():
    question = get_question()
    print question


if __name__=="__main__":
    main()
