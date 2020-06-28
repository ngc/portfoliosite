from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from bs4 import BeautifulSoup
from django.core.files import File
import requests
import json
import sys

##DJANGO
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

def textColor(rating):
    if(rating == None):
        return (0, 0, 0)
    if(rating < 1000):
        return (145, 145, 145)
    if(rating < 1200):
        return (65, 219, 48)
    if(rating < 1500):
        return (54, 89, 245)
    if(rating < 1800):
        return (169, 54, 245)
    if(rating < 2200):
        return (227, 230, 39)
    if(rating > 2199):
        return (255, 0, 0)

##PLACEHOLDERS##
#These variables are to change after the JSON API data from DMOJ is properly imported

DATA_USERNAME = sys.argv[1]
r = requests.get(
    'https://dmoj.ca/api/user/info/' + DATA_USERNAME,
    headers={'user-agent': 'Mozilla/5.0'})

#print(r.json()['current_rating'])
DATA_POINTS = r.json()['points']
DATA_RATING = r.json()['contests']['current_rating']

r = requests.get(
    'https://dmoj.ca/api/user/submissions/' + DATA_USERNAME,
    headers={'user-agent': 'Mozilla/5.0'})

DATA_MIN_RATING = r.text.count('problem')

################

#Get Profile Picture

page = requests.get("https://dmoj.ca/user/" + DATA_USERNAME)
soup = BeautifulSoup(page.text)
tags = soup.findAll('img')
profile_url = "https://" + tags[1]['src'][8:]


#################

size = 340, 400
img = Image.open('card without detail.png')

profile_loc = 25, 18 
profile_img = Image.open(requests.get(profile_url, stream=True).raw)
profile_img = profile_img.resize((150, 150))
img.paste(profile_img, profile_loc)

#TYPOGRAPHY
# font-file should be present in provided path.
font = ImageFont.truetype("Nirmala.ttf", 38)
draw = ImageDraw.Draw(img)

#Text will be seperated by 53px 
row = 53
draw.text((14, 173 + row * 0), DATA_USERNAME, (0, 0, 0), font=font) 
draw.text((13, 173 + row * 1), "Rating:    ", (0, 0, 0), font=font) 
draw.text((170, 173 + row * 1), str(DATA_RATING), textColor(DATA_RATING), font=font) 
draw.text((14, 173 + row * 2), "Submissions: " + str(DATA_MIN_RATING), (0, 0, 0), font=font) 
draw.text((14, 167 + row * 3), "Points: " + str(DATA_POINTS)[:8], (0, 0, 0), font=font) 
draw.ellipse((130, 232, 170, 272), fill = textColor(DATA_RATING))#outline = textColor(DATA_RATING))
img = img.resize((360, 420), Image.ANTIALIAS)

path = "media/img_JJeyJCW.png"
img.save(path)