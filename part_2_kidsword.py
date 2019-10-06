# Import Libraries
import re
import nltk
import pandas as pd
import pygame
from pygame import mixer
import os
import string
import random
from PIL import Image

image_dir = 'Image'
audio_dir = 'Audio'

# Open Word List
with open("word_list.txt", "r") as f:
    word_list = [word.replace('\n', '') for word in f.readlines()]

# Substitute Symbols with Spaces
word_list = [re.sub('[-.]', ' ', word) for word in word_list]
# Remove Words with Spaces
word_list = list(filter(lambda x: ' ' not in x, word_list))
# Change to Lower Cases
word_list = [word.lower() for word in word_list]
# Keep the Words with 3 or 4 Characters
word_list = list(filter(lambda x: len(x) in [3, 4], word_list))
# List of Part-of-Speech
pos_list = [nltk.pos_tag([word])[0][1] for word in word_list]
# List of Word Length
len_list = [len(word) for word in word_list]
# Data Frame
word_df = pd.DataFrame({'Word': word_list, 'POS': pos_list, 'Len': len_list})
# Keep CD / JJ / NN / VB
word_df = word_df[word_df['POS'].isin(['CD', 'JJ', 'NN', 'VB'])]

# Game Init
pygame.init()
win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("KidsWord presented by cyda")

mixer.init()

pygame.font.init()
font_1 = pygame.font.SysFont('impact', 55)
font_2 = pygame.font.SysFont('Arial', 25)
font_3 = pygame.font.SysFont('roboto', 30)
font_4 = pygame.font.SysFont('Arial', 20)
font_5 = pygame.font.SysFont('impact', 25)
font_6 = pygame.font.SysFont('impact', 120)
font_7 = pygame.font.SysFont('impact', 90)

clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

#############
# Main Page #
#############

page = 0

# Background
win.fill((59, 89, 152))  # title
pygame.draw.rect(win, (117, 138, 182), (0, 200, 640, 110))  # word length
pygame.draw.rect(win, (176, 188, 213), (0, 310, 640, 110))  # time limit
pygame.draw.rect(win, (235, 238, 244), (0, 420, 640, 60))  # game start

# Title
win.blit(font_1.render('KidsWord', False,(242, 242, 242)),(215, 45))
win.blit(font_2.render('Presented by cyda', False, (212, 216, 232)), (350, 135))

# Word Length
word_length = 3
win.blit(font_3.render('CHOOSE WORD LENGTH', False, (212, 216, 232)), (150, 210))

pygame.draw.rect(win, (59, 89, 152), (170, 250, 85, 40))
word_length_button_three = pygame.Rect(170, 250, 85, 40)
win.blit(font_4.render('Three', False, (255, 255, 255)), (185, 257))

pygame.draw.rect(win, (255, 255, 255), (270, 250, 85, 40))
word_length_button_four = pygame.Rect(270, 250, 85, 40)
win.blit(font_4.render('Four', False, (59, 89, 152)), (292, 257))

pygame.draw.rect(win, (255, 255, 255), (370, 250, 85, 40))
word_length_button_random = pygame.Rect(370, 250, 85, 40)
win.blit(font_4.render('Random', False, (59, 89, 152)), (375, 257))

# Time Limit
time_limit = 3
win.blit(font_3.render('CHOOSE TIME LIMIT', False, (212, 216, 232)), (180, 320))

pygame.draw.rect(win, (59, 89, 152), (170, 360, 85, 40))
time_limit_button_three = pygame.Rect(170, 360, 85, 40)
win.blit(font_4.render('Three', False, (255, 255, 255)), (185, 367))

pygame.draw.rect(win, (255, 255, 255), (270, 360, 85, 40))
time_limit_button_five = pygame.Rect(270, 360, 85, 40)
win.blit(font_4.render('Five', False, (59, 89, 152)), (292, 367))

pygame.draw.rect(win, (255, 255, 255), (370, 360, 85, 40))
time_limit_button_ten = pygame.Rect(370, 360, 85, 40)
win.blit(font_4.render('Eight', False, (59, 89, 152)), (390, 367))

# Game Start
win.blit(font_5.render('Game Start !!!', False, (59, 89, 152)), (247, 433))
game_start_button = pygame.Rect(0, 420, 640, 60)


# Action
def word_length_button_three_pressed():
    pygame.draw.rect(win, (117, 138, 182), (0, 200, 640, 110))
    win.blit(font_3.render('CHOOSE WORD LENGTH', False, (212, 216, 232)), (150, 210))
    pygame.draw.rect(win, (59, 89, 152), (170, 250, 85, 40))
    win.blit(font_4.render('Three', False, (255, 255, 255)), (185, 257))
    pygame.draw.rect(win, (255, 255, 255), (270, 250, 85, 40))
    win.blit(font_4.render('Four', False, (59, 89, 152)), (292, 257))
    pygame.draw.rect(win, (255, 255, 255), (370, 250, 85, 40))
    win.blit(font_4.render('Random', False, (59, 89, 152)), (375, 257))


def word_length_button_four_pressed():
    pygame.draw.rect(win, (117, 138, 182), (0, 200, 640, 110))
    win.blit(font_3.render('CHOOSE WORD LENGTH', False, (212, 216, 232)), (150, 210))
    pygame.draw.rect(win, (255, 255, 255), (170, 250, 85, 40))
    win.blit(font_4.render('Three', False, (59, 89, 152)), (185, 257))
    pygame.draw.rect(win, (59, 89, 152), (270, 250, 85, 40))
    win.blit(font_4.render('Four', False, (255, 255, 255)), (292, 257))
    pygame.draw.rect(win, (255, 255, 255), (370, 250, 85, 40))
    win.blit(font_4.render('Random', False, (59, 89, 152)), (375, 257))


def word_length_button_random_pressed():
    pygame.draw.rect(win, (117, 138, 182), (0, 200, 640, 110))
    win.blit(font_3.render('CHOOSE WORD LENGTH', False, (212, 216, 232)), (150, 210))
    pygame.draw.rect(win, (255, 255, 255), (170, 250, 85, 40))
    win.blit(font_4.render('Three', False, (59, 89, 152)), (185, 257))
    pygame.draw.rect(win, (255, 255, 255), (270, 250, 85, 40))
    win.blit(font_4.render('Four', False, (59, 89, 152)), (292, 257))
    pygame.draw.rect(win, (59, 89, 152), (370, 250, 85, 40))
    win.blit(font_4.render('Random', False, (255, 255, 255)), (375, 257))


def time_limit_button_three_pressed():
    pygame.draw.rect(win, (176, 188, 213), (0, 310, 640, 110))
    win.blit(font_3.render('CHOOSE TIME LIMIT', False, (212, 216, 232)), (180, 320))
    pygame.draw.rect(win, (59, 89, 152), (170, 360, 85, 40))
    win.blit(font_4.render('Three', False, (255, 255, 255)), (185, 367))
    pygame.draw.rect(win, (255, 255, 255), (270, 360, 85, 40))
    win.blit(font_4.render('Five', False, (59, 89, 152)), (292, 367))
    pygame.draw.rect(win, (255, 255, 255), (370, 360, 85, 40))
    win.blit(font_4.render('Eight', False, (59, 89, 152)), (390, 367))


def time_limit_button_five_pressed():
    pygame.draw.rect(win, (176, 188, 213), (0, 310, 640, 110))
    win.blit(font_3.render('CHOOSE TIME LIMIT', False, (212, 216, 232)), (180, 320))
    pygame.draw.rect(win, (255, 255, 255), (170, 360, 85, 40))
    win.blit(font_4.render('Three', False, (59, 89, 152)), (185, 367))
    pygame.draw.rect(win, (59, 89, 152), (270, 360, 85, 40))
    win.blit(font_4.render('Five', False, (255, 255, 255)), (292, 367))
    pygame.draw.rect(win, (255, 255, 255), (370, 360, 85, 40))
    win.blit(font_4.render('Eight', False, (59, 89, 152)), (390, 367))


def time_limit_button_eight_pressed():
    pygame.draw.rect(win, (176, 188, 213), (0, 310, 640, 110))
    win.blit(font_3.render('CHOOSE TIME LIMIT', False, (212, 216, 232)), (180, 320))
    pygame.draw.rect(win, (255, 255, 255), (170, 360, 85, 40))
    win.blit(font_4.render('Three', False, (59, 89, 152)), (185, 367))
    pygame.draw.rect(win, (255, 255, 255), (270, 360, 85, 40))
    win.blit(font_4.render('Five', False, (59, 89, 152)), (292, 367))
    pygame.draw.rect(win, (59, 89, 152), (370, 360, 85, 40))
    win.blit(font_4.render('Eight', False, (255, 255, 255)), (390, 367))

# -----------------------------------------------------

##############
# Game Start #
##############

# Game Set Up


life = 3


def adj_en_char(en_char, en_char_x):
    if (en_char == "f") | (en_char == "i") | (en_char == "j") | (en_char == "l") | (en_char == "t"):
        return en_char_x + 15
    if (en_char == "r") | (en_char == "z"):
        return en_char_x + 5
    if en_char == "m":
        return en_char_x - 16
    if en_char == "w":
        return en_char_x - 10
    return en_char_x


def adj_en_char2(en_char, en_char_x):
    if (en_char == "f") | (en_char == "i") | (en_char == "j") | (en_char == "l") | (en_char == "t"):
        return en_char_x + 10
    if (en_char == "r") | (en_char == "z"):
        return en_char_x + 5
    if en_char == "m":
        return en_char_x - 10
    if en_char == "w":
        return en_char_x - 10
    return en_char_x


def show_card_three():
    win.fill((59, 89, 152))
    win.blit(font_1.render('Time', False, (242, 242, 242)), (215, 55))
    win.blit(font_1.render('Countdown', False, (242, 242, 242)), (145, 120))

    win.blit(font_2.render('Remember the words below :', False, (212, 216, 232)), (155, 235))
    pygame.draw.rect(win, (242, 242, 242), (150, 280, 100, 160))
    pygame.draw.rect(win, (176, 188, 213), (140, 270, 100, 160))
    pygame.draw.rect(win, (242, 242, 242), (280, 280, 100, 160))
    pygame.draw.rect(win, (176, 188, 213), (270, 270, 100, 160))
    pygame.draw.rect(win, (242, 242, 242), (410, 280, 100, 160))
    pygame.draw.rect(win, (176, 188, 213), (400, 270, 100, 160))
    en_char_0_x = 160
    en_char_1_x = 290
    en_char_2_x = 420
    en_char_0_x = adj_en_char(correct_ans[0], en_char_0_x)
    en_char_1_x = adj_en_char(correct_ans[1], en_char_1_x)
    en_char_2_x = adj_en_char(correct_ans[2], en_char_2_x)
    win.blit(font_6.render(correct_ans[0], False, (255, 255, 255)), (en_char_0_x, 270))
    win.blit(font_6.render(correct_ans[1], False, (255, 255, 255)), (en_char_1_x, 270))
    win.blit(font_6.render(correct_ans[2], False, (255, 255, 255)), (en_char_2_x, 270))


def show_card_four():
    win.fill((59, 89, 152))
    win.blit(font_1.render('Time', False, (242, 242, 242)), (215, 55))
    win.blit(font_1.render('Countdown', False, (242, 242, 242)), (145, 120))

    win.blit(font_2.render('Remember the words below :', False, (212, 216, 232)), (155, 235))
    pygame.draw.rect(win, (242, 242, 242), (85, 280, 100, 160))
    pygame.draw.rect(win, (176, 188, 213), (75, 270, 100, 160))
    pygame.draw.rect(win, (242, 242, 242), (215, 280, 100, 160))
    pygame.draw.rect(win, (176, 188, 213), (205, 270, 100, 160))
    pygame.draw.rect(win, (242, 242, 242), (345, 280, 100, 160))
    pygame.draw.rect(win, (176, 188, 213), (335, 270, 100, 160))
    pygame.draw.rect(win, (242, 242, 242), (475, 280, 100, 160))
    pygame.draw.rect(win, (176, 188, 213), (465, 270, 100, 160))
    en_char_0_x = 95
    en_char_1_x = 225
    en_char_2_x = 355
    en_char_3_x = 485
    en_char_0_x = adj_en_char(correct_ans[0], en_char_0_x)
    en_char_1_x = adj_en_char(correct_ans[1], en_char_1_x)
    en_char_2_x = adj_en_char(correct_ans[2], en_char_2_x)
    en_char_3_x = adj_en_char(correct_ans[3], en_char_3_x)
    win.blit(font_6.render(correct_ans[0], False, (255, 255, 255)), (en_char_0_x, 270))
    win.blit(font_6.render(correct_ans[1], False, (255, 255, 255)), (en_char_1_x, 270))
    win.blit(font_6.render(correct_ans[2], False, (255, 255, 255)), (en_char_2_x, 270))
    win.blit(font_6.render(correct_ans[3], False, (255, 255, 255)), (en_char_3_x, 270))


word_one_button = pygame.Rect(30, 270, 80, 120)
word_two_button = pygame.Rect(130, 270, 80, 120)
word_three_button = pygame.Rect(230, 270, 80, 120)
word_four_button = pygame.Rect(330, 270, 80, 120)
word_five_button = pygame.Rect(430, 270, 80, 120)
word_six_button = pygame.Rect(530, 270, 80, 120)
confirm_button = pygame.Rect(200, 415, 110, 40)
reset_button = pygame.Rect(330, 415, 110, 40)


def three_choose_from_six():
    win.fill((59, 89, 152))

    win.blit(font_2.render('Please choose the words below :', False, (212, 216, 232)), (140, 50))
    pygame.draw.rect(win, (148, 148, 148), (140, 85, 100, 160))
    pygame.draw.rect(win, (148, 148, 148), (270, 85, 100, 160))
    pygame.draw.rect(win, (148, 148, 148), (400, 85, 100, 160))

    pygame.draw.rect(win, (242, 242, 242), (35, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (30, 270, 80, 120))

    pygame.draw.rect(win, (242, 242, 242), (135, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (130, 270, 80, 120))

    pygame.draw.rect(win, (242, 242, 242), (235, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (230, 270, 80, 120))

    pygame.draw.rect(win, (242, 242, 242), (335, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (330, 270, 80, 120))

    pygame.draw.rect(win, (242, 242, 242), (435, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (430, 270, 80, 120))

    pygame.draw.rect(win, (242, 242, 242), (535, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (530, 270, 80, 120))

    en_char_0_x = 47
    en_char_1_x = 147
    en_char_2_x = 247
    en_char_3_x = 347
    en_char_4_x = 447
    en_char_5_x = 547
    en_char_0_x = adj_en_char2(six_eng_characters_display[0], en_char_0_x)
    en_char_1_x = adj_en_char2(six_eng_characters_display[1], en_char_1_x)
    en_char_2_x = adj_en_char2(six_eng_characters_display[2], en_char_2_x)
    en_char_3_x = adj_en_char2(six_eng_characters_display[3], en_char_3_x)
    en_char_4_x = adj_en_char2(six_eng_characters_display[4], en_char_4_x)
    en_char_5_x = adj_en_char2(six_eng_characters_display[5], en_char_5_x)
    win.blit(font_7.render(six_eng_characters_display[0], False, (255, 255, 255)), (en_char_0_x, 270))
    win.blit(font_7.render(six_eng_characters_display[1], False, (255, 255, 255)), (en_char_1_x, 270))
    win.blit(font_7.render(six_eng_characters_display[2], False, (255, 255, 255)), (en_char_2_x, 270))
    win.blit(font_7.render(six_eng_characters_display[3], False, (255, 255, 255)), (en_char_3_x, 270))
    win.blit(font_7.render(six_eng_characters_display[4], False, (255, 255, 255)), (en_char_4_x, 270))
    win.blit(font_7.render(six_eng_characters_display[5], False, (255, 255, 255)), (en_char_5_x, 270))

    pygame.draw.rect(win, (255, 255, 255), (200, 415, 110, 40))
    win.blit(font_4.render('Confirm', False, (59, 89, 152)), (220, 422))
    pygame.draw.rect(win, (255, 255, 255), (330, 415, 110, 40))
    win.blit(font_4.render('Reset', False, (59, 89, 152)), (360, 422))
    win.blit(font_2.render('Mark : '+str(mark), False, (212, 216, 232)), (510, 10))
    win.blit(font_2.render('Life : '+str(life), False, (212, 216, 232)), (20, 10))


def four_choose_from_six():
    win.fill((59, 89, 152))

    win.blit(font_2.render('Please choose the words below :', False, (212, 216, 232)), (140, 50))
    pygame.draw.rect(win, (148, 148, 148), (75, 85, 100, 160))
    pygame.draw.rect(win, (148, 148, 148), (205, 85, 100, 160))
    pygame.draw.rect(win, (148, 148, 148), (335, 85, 100, 160))
    pygame.draw.rect(win, (148, 148, 148), (465, 85, 100, 160))

    pygame.draw.rect(win, (242, 242, 242), (35, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (30, 270, 80, 120))

    pygame.draw.rect(win, (242, 242, 242), (135, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (130, 270, 80, 120))

    pygame.draw.rect(win, (242, 242, 242), (235, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (230, 270, 80, 120))

    pygame.draw.rect(win, (242, 242, 242), (335, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (330, 270, 80, 120))

    pygame.draw.rect(win, (242, 242, 242), (435, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (430, 270, 80, 120))

    pygame.draw.rect(win, (242, 242, 242), (535, 275, 80, 120))
    pygame.draw.rect(win, (176, 188, 213), (530, 270, 80, 120))

    en_char_0_x = 47
    en_char_1_x = 147
    en_char_2_x = 247
    en_char_3_x = 347
    en_char_4_x = 447
    en_char_5_x = 547
    en_char_0_x = adj_en_char2(six_eng_characters_display[0], en_char_0_x)
    en_char_1_x = adj_en_char2(six_eng_characters_display[1], en_char_1_x)
    en_char_2_x = adj_en_char2(six_eng_characters_display[2], en_char_2_x)
    en_char_3_x = adj_en_char2(six_eng_characters_display[3], en_char_3_x)
    en_char_4_x = adj_en_char2(six_eng_characters_display[4], en_char_4_x)
    en_char_5_x = adj_en_char2(six_eng_characters_display[5], en_char_5_x)
    win.blit(font_7.render(six_eng_characters_display[0], False, (255, 255, 255)), (en_char_0_x, 270))
    win.blit(font_7.render(six_eng_characters_display[1], False, (255, 255, 255)), (en_char_1_x, 270))
    win.blit(font_7.render(six_eng_characters_display[2], False, (255, 255, 255)), (en_char_2_x, 270))
    win.blit(font_7.render(six_eng_characters_display[3], False, (255, 255, 255)), (en_char_3_x, 270))
    win.blit(font_7.render(six_eng_characters_display[4], False, (255, 255, 255)), (en_char_4_x, 270))
    win.blit(font_7.render(six_eng_characters_display[5], False, (255, 255, 255)), (en_char_5_x, 270))

    pygame.draw.rect(win, (255, 255, 255), (200, 415, 110, 40))
    win.blit(font_4.render('Confirm', False, (59, 89, 152)), (220, 422))
    pygame.draw.rect(win, (255, 255, 255), (330, 415, 110, 40))
    win.blit(font_4.render('Reset', False, (59, 89, 152)), (360, 422))
    win.blit(font_2.render('Mark : '+str(mark), False, (212, 216, 232)), (510, 10))
    win.blit(font_2.render('Life : '+str(life), False, (212, 216, 232)), (20, 10))


def word_one_button_pressed():
    pygame.draw.rect(win, (100, 100, 100), (30, 270, 80, 120))


def word_two_button_pressed():
    pygame.draw.rect(win, (100, 100, 100), (130, 270, 80, 120))


def word_three_button_pressed():
    pygame.draw.rect(win, (100, 100, 100), (230, 270, 80, 120))


def word_four_button_pressed():
    pygame.draw.rect(win, (100, 100, 100), (330, 270, 80, 120))


def word_five_button_pressed():
    pygame.draw.rect(win, (100, 100, 100), (430, 270, 80, 120))


def word_six_button_pressed():
    pygame.draw.rect(win, (100, 100, 100), (530, 270, 80, 120))


correct_ans = []
position = 0
choose_ans = []
word_one_idx = 0
word_two_idx = 0
word_three_idx = 0
word_four_idx = 0
word_five_idx = 0
word_six_idx = 0


def word_selected(pos, en_char):
    if len(correct_ans) == 3:
        if pos == 0:
            pygame.draw.rect(win, (255, 255, 255), (140, 85, 100, 160))
            en_char_x = 160
            en_char_x = adj_en_char(en_char, en_char_x)
            win.blit(font_6.render(en_char, False, (59, 89, 152)), (en_char_x, 85))
        if pos == 1:
            pygame.draw.rect(win, (255, 255, 255), (270, 85, 100, 160))
            en_char_x = 290
            en_char_x = adj_en_char(en_char, en_char_x)
            win.blit(font_6.render(en_char, False, (59, 89, 152)), (en_char_x, 85))
        if pos == 2:
            pygame.draw.rect(win, (255, 255, 255), (400, 85, 100, 160))
            en_char_x = 420
            en_char_x = adj_en_char(en_char, en_char_x)
            win.blit(font_6.render(en_char, False, (59, 89, 152)), (en_char_x, 85))

    if len(correct_ans) == 4:
        if pos == 0:
            pygame.draw.rect(win, (255, 255, 255), (75, 85, 100, 160))
            en_char_x = 95
            en_char_x = adj_en_char(en_char, en_char_x)
            win.blit(font_6.render(en_char, False, (59, 89, 152)), (en_char_x, 85))
        if pos == 1:
            pygame.draw.rect(win, (255, 255, 255), (205, 85, 100, 160))
            en_char_x = 225
            en_char_x = adj_en_char(en_char, en_char_x)
            win.blit(font_6.render(en_char, False, (59, 89, 152)), (en_char_x, 85))
        if pos == 2:
            pygame.draw.rect(win, (255, 255, 255), (335, 85, 100, 160))
            en_char_x = 355
            en_char_x = adj_en_char(en_char, en_char_x)
            win.blit(font_6.render(en_char, False, (59, 89, 152)), (en_char_x, 85))
        if pos == 3:
            pygame.draw.rect(win, (255, 255, 255), (465, 85, 100, 160))
            en_char_x = 485
            en_char_x = adj_en_char(en_char, en_char_x)
            win.blit(font_6.render(en_char, False, (59, 89, 152)), (en_char_x, 85))


next_button = pygame.Rect(0, 420, 640, 60)
music_three_button = pygame.Rect(60, 314, 80, 80)
music_four_button = pygame.Rect(30, 314, 80, 80)


def correct_match():
    win.fill((255, 255, 255))
    file_path = [item for item in [item for item in os.listdir(image_dir) if ''.join(correct_ans) in item] if os.path.splitext(item)[0] == ''.join(correct_ans)][0]
    image_path = os.path.join(image_dir, file_path)
    im = Image.open(image_path)
    width, height = im.size
    new_width = int(280*width/height)
    word_image = pygame.image.load(image_path)
    word_image = pygame.transform.scale(word_image, (new_width, 280))
    new_x = int((640 - new_width)/2)
    win.blit(word_image, (new_x, 10))
    pygame.draw.rect(win, (235, 238, 244), (0, 420, 640, 60))
    win.blit(font_5.render('Next', False, (59, 89, 152)), (310, 433))
    if len(correct_ans) == 3:
        en_char_0_x = 180
        en_char_1_x = 290
        en_char_2_x = 400
        en_char_0_x = adj_en_char(correct_ans[0], en_char_0_x)
        en_char_1_x = adj_en_char(correct_ans[1], en_char_1_x)
        en_char_2_x = adj_en_char(correct_ans[2], en_char_2_x)
        win.blit(font_6.render(correct_ans[0], False, (100, 100, 100)), (en_char_0_x, 270))
        win.blit(font_6.render(correct_ans[1], False, (100, 100, 100)), (en_char_1_x, 270))
        win.blit(font_6.render(correct_ans[2], False, (100, 100, 100)), (en_char_2_x, 270))
        music_button = pygame.image.load('music_button.png')
        music_button = pygame.transform.scale(music_button, (80, 80))
        win.blit(music_button, (60, 314))

    if len(correct_ans) == 4:
        en_char_0_x = 125
        en_char_1_x = 235
        en_char_2_x = 345
        en_char_3_x = 465
        en_char_0_x = adj_en_char(correct_ans[0], en_char_0_x)
        en_char_1_x = adj_en_char(correct_ans[1], en_char_1_x)
        en_char_2_x = adj_en_char(correct_ans[2], en_char_2_x)
        en_char_3_x = adj_en_char(correct_ans[3], en_char_3_x)
        win.blit(font_6.render(correct_ans[0], False, (100, 100, 100)), (en_char_0_x, 270))
        win.blit(font_6.render(correct_ans[1], False, (100, 100, 100)), (en_char_1_x, 270))
        win.blit(font_6.render(correct_ans[2], False, (100, 100, 100)), (en_char_2_x, 270))
        win.blit(font_6.render(correct_ans[3], False, (100, 100, 100)), (en_char_3_x, 270))
        music_button = pygame.image.load('music_button.png')
        music_button = pygame.transform.scale(music_button, (80, 80))
        win.blit(music_button, (30, 314))


restart_button = pygame.Rect(200, 265, 110, 40)
quit_button = pygame.Rect(330, 265, 110, 40)


def game_over():
    win.fill((59, 89, 152))
    win.blit(font_6.render('Game Over', False, (212, 216, 232)), (50, 10))
    win.blit(font_1.render('Total Mark', False, (212, 216, 232)), (130, 160))
    win.blit(font_1.render(str(mark), False, (212, 216, 232)), (430, 160))
    pygame.draw.rect(win, (255, 255, 255), (200, 265, 110, 40))
    win.blit(font_4.render('Restart', False, (59, 89, 152)), (220, 272))
    pygame.draw.rect(win, (255, 255, 255), (330, 265, 110, 40))
    win.blit(font_4.render('Quit', False, (59, 89, 152)), (365, 272))


def restart():
    # Background
    win.fill((59, 89, 152))  # title
    pygame.draw.rect(win, (117, 138, 182), (0, 200, 640, 110))  # word length
    pygame.draw.rect(win, (176, 188, 213), (0, 310, 640, 110))  # time limit
    pygame.draw.rect(win, (235, 238, 244), (0, 420, 640, 60))  # game start

    # Title
    win.blit(font_1.render('KidsWord', False, (242, 242, 242)), (215, 45))
    win.blit(font_2.render('Presented by cyda', False, (212, 216, 232)), (350, 135))

    # Word Length
    win.blit(font_3.render('CHOOSE WORD LENGTH', False, (212, 216, 232)), (150, 210))
    pygame.draw.rect(win, (59, 89, 152), (170, 250, 85, 40))
    win.blit(font_4.render('Three', False, (255, 255, 255)), (185, 257))
    pygame.draw.rect(win, (255, 255, 255), (270, 250, 85, 40))
    win.blit(font_4.render('Four', False, (59, 89, 152)), (292, 257))
    pygame.draw.rect(win, (255, 255, 255), (370, 250, 85, 40))
    win.blit(font_4.render('Random', False, (59, 89, 152)), (375, 257))

    # Time Limit
    win.blit(font_3.render('CHOOSE TIME LIMIT', False, (212, 216, 232)), (180, 320))
    pygame.draw.rect(win, (59, 89, 152), (170, 360, 85, 40))
    win.blit(font_4.render('Three', False, (255, 255, 255)), (185, 367))
    pygame.draw.rect(win, (255, 255, 255), (270, 360, 85, 40))
    win.blit(font_4.render('Five', False, (59, 89, 152)), (292, 367))
    pygame.draw.rect(win, (255, 255, 255), (370, 360, 85, 40))
    win.blit(font_4.render('Eight', False, (59, 89, 152)), (390, 367))

    # Game Start
    win.blit(font_5.render('Game Start !!!', False, (59, 89, 152)), (247, 433))

# -------------------------------------------------------


run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if life == 0:
            page = 4
            game_over()

        if page == 1:
            if event.type == pygame.USEREVENT:
                time_count -= 1
            time_text = int(time_count)
            if time_text > time_limit:
                time_text = time_limit
            pygame.draw.rect(win, (59, 89, 152), (420, 50, 100, 160))
            win.blit(font_6.render(str(time_text), True, (242, 242, 242)), (440, 50))
            pygame.display.flip()
            clock.tick(60)
            if time_count <= 0:
                page = 2
                position = 0
                choose_ans = []
                if len(correct_ans) == 3:
                    three_choose_from_six()
                if len(correct_ans) == 4:
                    four_choose_from_six()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if (word_length_button_three.collidepoint(mouse_pos)) & (page == 0):
                word_length = 3
                word_length_button_three_pressed()
            if (word_length_button_four.collidepoint(mouse_pos)) & (page == 0):
                word_length = 4
                word_length_button_four_pressed()
            if (word_length_button_random.collidepoint(mouse_pos)) & (page == 0):
                word_length = 5
                word_length_button_random_pressed()

            if (time_limit_button_three.collidepoint(mouse_pos)) & (page == 0):
                time_limit = 3
                time_limit_button_three_pressed()
            if (time_limit_button_five.collidepoint(mouse_pos)) & (page == 0):
                time_limit = 5
                time_limit_button_five_pressed()
            if (time_limit_button_ten.collidepoint(mouse_pos)) & (page == 0):
                time_limit = 8
                time_limit_button_eight_pressed()

            if (game_start_button.collidepoint(mouse_pos)) & (page == 0):
                game_df = word_df.copy()
                if word_length == 3:
                    game_df = game_df[game_df['Len'] == 3]
                if word_length == 4:
                    game_df = game_df[game_df['Len'] == 4]
                game_df = game_df.reset_index()
                sequence = list(range(len(game_df)))  # number of words to play
                random.shuffle(sequence)
                idx = 0
                mark = 0
                print(sequence[idx])
                print(game_df['Word'][sequence[idx]])
                correct_ans = list(game_df['Word'][sequence[idx]])
                print(correct_ans)
                random_idx = 6 - len(correct_ans)
                eng_character = set(string.ascii_lowercase)
                random_eng_character = list(eng_character.difference(set(correct_ans)))
                random.shuffle(random_eng_character)
                six_eng_characters_display = random_eng_character[:random_idx] + correct_ans
                random.shuffle(six_eng_characters_display)
                print(six_eng_characters_display)
                page = 1
                time_count = time_limit + 1
                if len(correct_ans) == 3:
                    show_card_three()
                if len(correct_ans) == 4:
                    show_card_four()

            if (word_one_button.collidepoint(mouse_pos)) & (page == 2) & (word_one_idx == 0):
                if position < len(correct_ans):
                    word_one_button_pressed()
                    word_selected(position, six_eng_characters_display[0])
                    choose_ans = choose_ans + [six_eng_characters_display[0]]
                    word_one_idx += 1
                    position += 1

            if (word_two_button.collidepoint(mouse_pos)) & (page == 2) & (word_two_idx == 0):
                if position < len(correct_ans):
                    word_two_button_pressed()
                    word_selected(position, six_eng_characters_display[1])
                    choose_ans = choose_ans + [six_eng_characters_display[1]]
                    word_two_idx += 1
                    position += 1

            if (word_three_button.collidepoint(mouse_pos)) & (page == 2) & (word_three_idx == 0):
                if position < len(correct_ans):
                    word_three_button_pressed()
                    word_selected(position, six_eng_characters_display[2])
                    choose_ans = choose_ans + [six_eng_characters_display[2]]
                    word_three_idx += 1
                    position += 1

            if (word_four_button.collidepoint(mouse_pos)) & (page == 2) & (word_four_idx == 0):
                if position < len(correct_ans):
                    word_four_button_pressed()
                    word_selected(position, six_eng_characters_display[3])
                    choose_ans = choose_ans + [six_eng_characters_display[3]]
                    word_four_idx += 1
                    position += 1

            if (word_five_button.collidepoint(mouse_pos)) & (page == 2) & (word_five_idx == 0):
                if position < len(correct_ans):
                    word_five_button_pressed()
                    word_selected(position, six_eng_characters_display[4])
                    choose_ans = choose_ans + [six_eng_characters_display[4]]
                    word_five_idx += 1
                    position += 1

            if (word_six_button.collidepoint(mouse_pos)) & (page == 2) & (word_six_idx == 0):
                if position < len(correct_ans):
                    word_six_button_pressed()
                    word_selected(position, six_eng_characters_display[5])
                    choose_ans = choose_ans + [six_eng_characters_display[5]]
                    word_six_idx += 1
                    position += 1

            if (confirm_button.collidepoint(mouse_pos)) & (page == 2):
                if position == (len(correct_ans)):
                    print(choose_ans)
                    print(correct_ans)
                    if choose_ans == correct_ans:
                        mark += 10
                        page = 3
                        delay = 1
                        correct_match()
                    else:
                        life -= 1
                        word_one_idx = 0
                        word_two_idx = 0
                        word_three_idx = 0
                        word_four_idx = 0
                        word_five_idx = 0
                        word_six_idx = 0
                        position = 0
                        choose_ans = []
                        if len(correct_ans) == 3:
                            three_choose_from_six()
                        if len(correct_ans) == 4:
                            four_choose_from_six()

            if (reset_button.collidepoint(mouse_pos)) & (page == 2):
                word_one_idx = 0
                word_two_idx = 0
                word_three_idx = 0
                word_four_idx = 0
                word_five_idx = 0
                word_six_idx = 0
                position = 0
                choose_ans = []
                if len(correct_ans) == 3:
                    three_choose_from_six()
                if len(correct_ans) == 4:
                    four_choose_from_six()

            if (music_three_button.collidepoint(mouse_pos)) & (page == 3) & (len(correct_ans) == 3):
                music_file = ''.join(correct_ans) + '.mp3'
                music_path = os.path.join(audio_dir, music_file)
                mixer.music.load(music_path)
                mixer.music.play()

            if (music_four_button.collidepoint(mouse_pos)) & (page == 3) & (len(correct_ans) == 4):
                music_file = ''.join(correct_ans) + '.mp3'
                music_path = os.path.join(audio_dir, music_file)
                mixer.music.load(music_path)
                mixer.music.play()

            if (next_button.collidepoint(mouse_pos)) & (page == 3):
                if delay == 0:
                    idx += 1
                    word_one_idx = 0
                    word_two_idx = 0
                    word_three_idx = 0
                    word_four_idx = 0
                    word_five_idx = 0
                    word_six_idx = 0
                    choose_ans = []
                    print(mark)
                    correct_ans = list(game_df['Word'][sequence[idx]])
                    print(correct_ans)
                    random_idx = 6 - len(correct_ans)
                    eng_character = set(string.ascii_lowercase)
                    random_eng_character = list(eng_character.difference(set(correct_ans)))
                    random.shuffle(random_eng_character)
                    six_eng_characters_display = random_eng_character[:random_idx] + correct_ans
                    random.shuffle(six_eng_characters_display)
                    print(six_eng_characters_display)
                    page = 1
                    time_count = time_limit + 1
                    if len(correct_ans) == 3:
                        show_card_three()
                    if len(correct_ans) == 4:
                        show_card_four()
                else:
                    delay = 0

            if (restart_button.collidepoint(mouse_pos)) & (page == 4):
                page = 0
                life = 3
                word_length = 3
                time_limit = 3
                restart()

            if (quit_button.collidepoint(mouse_pos)) & (page == 4):
                run = False

    pygame.display.update()

pygame.quit()
