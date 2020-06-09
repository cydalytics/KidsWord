# Import Libraries
from urllib.request import urlopen
import re
import nltk
import pandas as pd
from gtts import gTTS
import os.path
from google_images_download import google_images_download
from shutil import copyfile
from os import listdir
import shutil

# Download Vocabulary List
txt_url = 'https://raw.githubusercontent.com/gokhanyavas/Oxford-3000-Word-List/master/Oxford%203000%20Word%20List.txt'
word_txt = urlopen(txt_url).read().decode('utf-8')
with open("word_list.txt", 'w') as f:
    f.write(word_txt)
word_list = word_txt.split('\n')

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

# Download Vocabulary Pronunciation Audio
if not(os.path.isdir('Audio')):
    os.mkdir('Audio')
    print('Audio is downloading. It may take a few minutes.')
    for word in list(word_df['Word']):
        audio_save_path = 'Audio/' + word + '.mp3'
        gTTS(text=word, lang='en', slow=False).save(audio_save_path)

print('Audio data is downloaded')

# Download  Vocabulary Cartoon Images
if not(os.path.isdir('Image')):
    os.mkdir('Image')
    print('Audio is downloading. It may take a few minutes.')
    for word in list(word_df['Word']):
        response = google_images_download.googleimagesdownload()
        response.download({"keywords": word, "limit": 1, "output_directory": 'Temp_Image',
                           "suffix_keywords": 'cartoon image', "format": 'jpg'})
    img_dir_list = listdir('Temp_Image')
    for img_dir in img_dir_list:
        initial_path = os.path.join('Temp_Image', img_dir)
        file_name = listdir(initial_path)
        if len(file_name) != 0:
            file_path = os.path.join(initial_path, file_name[0])
            final_path = os.path.join('Image', img_dir[:4].rstrip() + os.path.splitext(file_name[0])[1])
            copyfile(file_path, final_path)
    shutil.rmtree('Temp_Image')

print('All data are downloaded.')
