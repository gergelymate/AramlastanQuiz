#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'gergelymate'

import json
import random
import math

l_basic_info = ['Ennek a programnak a lenyege,',
              'hogy az Aramlastan vizsgahoz',
              'a beugrora minel jobban',
              'fel tudj keszulni']

l_question_range = [1,11]

test = True

def main():

    welcome_screen()

    s_chosen_point = ''

    while s_chosen_point != 'E':
        s_chosen_point = menu()

        if s_chosen_point == 'T':
            examtest()
        elif s_chosen_point == 'I':
            # infinitytest()
            print('Later ...')
        elif s_chosen_point == 'C':
            # specifiedpart()
            print ('Later ...')
        elif s_chosen_point == 'X':
            print_list(l_basic_info)

        # testing reasons
        s_chosen_point = "E"

    return

def examtest():
    i_sum_points = 0
    i_answers = 0
    l_question_numbers = []

    i_test_len = 10
    for i in range(1,i_test_len + 1):
        i_question_number = "%03d"%i

        # test starts here
        i_ask_quest = ask_questions(i, i_question_number)
        if i_ask_quest != 0:
            i_sum_points += i_ask_quest
        l_question_numbers.append([i_question_number, i_ask_quest])

    print("")
    print("A teszt eredménye:")
    i_correct_answers = 0
    for i in range(0,i_test_len):
        s_sentence = questions_correct(l_question_numbers[i][0])
        if s_sentence[2] == "":
            i_answers = 1
        elif s_sentence[3] == "":
            i_answers = 2
        else:
            i_answers = 3

        for j in range(1,i_answers+1):
            #TODO: find out the method to fill answers correctly
            s_binary_answer = "{0:3b}".format(int(l_question_numbers[i][1]))

            if s_binary_answer[3-j] == "1":
                # check if the answer is correct
                s_sentence[0] = s_sentence[0].replace("_", "\033[32m{}\033[0m".format(s_sentence[j]), 1)
                i_correct_answers += 1
            else:
                s_sentence[0] = s_sentence[0].replace("_", "\033[91m{}\033[0m".format(s_sentence[j]), 1)
        print("{}. {}".format(str(i+1), s_sentence[0]))

    if i_answers >= 10:
        s_passed = "\033[32mBEUGROTTÁL\033[0m"
    else:
        s_passed = "\033[91mMEGBUKTÁL\033[0m"

    print ("{} - Helyes valászok száma: {}".format(s_passed, i_correct_answers))
    return

def questions_correct(i_question_number):

    with open('questions.json') as f:
        d_questions = json.load(f)

    if i_question_number not in d_questions.keys():
        raise KeyError('Invalid question number!')

    return d_questions[i_question_number]

def ask_questions(no, i_question_number):

    print("")

    with open('questions.json') as f:
        d_questions = json.load(f)

    if i_question_number not in d_questions.keys():
        raise KeyError('Invalid question number!')

    # print the question
    print ("{}. {}".format(str(no), d_questions[i_question_number][0].replace('_','..........')))

    # input for answer
    print("Válasz (vesszővel elválasztva):")
    if not test:
        s_given_answer = input("-> ")
    else:
        s_given_answer = "sűrűség, nem függ"

    l_given_answer = []
    l_given_answer = s_given_answer.split(",")

    # check if the answer is correct
    if d_questions[i_question_number][2] == "":
        i_correct_answers = 1
    elif d_questions[i_question_number][3] == "":
        i_correct_answers = 2
    else:
        i_correct_answers = 3

    for i in range(i_correct_answers-len(l_given_answer)):
        l_given_answer.append("...")

    i_result = 0 #i_correct_answers*10
    for i in range(1,i_correct_answers + 1):
        # TODO: make multi answer compatible
        if l_given_answer[i-1].upper().replace(" ","") == d_questions[i_question_number][i].upper().replace(" ",""):
            #if tha answer is correct, increase with place of answer
            i_result += math.pow(2,i-1)
            print(i_result)

    return i_result

def menu():
    l_message = ['',
               'Válasz menüpontot:',
               'T - Vizsga teszt',
               'I - Infinity',
               'C - Valasztott fejezet',
               'X - Reszletes info',
               'E - Kilépés',
               '']

    l_answer_keys = ['T','I','C','X','E']
    s_answer = ''
    b_answer_ok = False

    while not b_answer_ok:
        print_list(l_message)
        if not test:
            s_answer = input('Választott menüpont: ')
        else:
            s_answer = "t"
        s_answer = s_answer.upper()

        for f_anskey in l_answer_keys:
            if f_anskey == s_answer:
                b_answer_ok = True

        if not b_answer_ok:
            print_list(['','ROSSZ BETŰT ADTÁL MEG!'])
    return s_answer

def print_list(l_list):
    for row in l_list:
        print (row)
    return

def welcome_screen():
    l_message = ['===========================',
               '||                       ||',
               '||    Áramlástan quiz    ||',
               '||         v1.0          ||',
               '||    by Gergely Mate    ||',
               '||                       ||',
               '===========================']
    print_list(l_message)
    input("Nyomj egy ENTER-t")
    return

if __name__ == '__main__':
    main()