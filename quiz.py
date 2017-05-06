#!/usr/bin/python

import random

def get_question():
    lines = open('questions.md').read().splitlines()
    return random.choice(lines)
   
def main():
    question = get_question()
    print question


if __name__=="__main__":
    main()
