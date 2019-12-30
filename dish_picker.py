#OWNER: Abboskhon Alimov
#Project Start Date: 12/29/19
#last edit made 12/29/19

from datetime import date
import calendar
import random

#Hi, this is a program I wrote to choose a random dish from a dinner menu to prepare
#,as my we (my family and I) had problems coming up with  a meal to prepare for everyone.

#I used stack overflow to understand how to grab the date and the day of
#the week


today=date.today()
day_today=calendar.day_name[today.weekday()]
day_today=str(day_today)
sample_dish=''


week_day=['Monday','Tuesday','Wednesday','Thursday','Friday']
weekend=['Saturday','Sunday']

print ('Today is ' + day_today+'.')

entree_list=['pizza','pilav','gretchka pilav','spaghetti','macaroni','chicken burrito','chicken teriyaki','meatloaf',
'fish','kartoshka with beef','dumplings','honim','lasagna','galubtzi','noodles','chili',
'baked chicken','corn beef sandwich','moshkichra']

soup_list=['borsh','mastava','lental soup',]

side_list=['rice','gretchka','baked potatoes','asparagus','corn','ikra','broccoli','fries']

salad_list=['cesar','italian','cabbage-carrot','achichu','onion-vinegar']

if day_today=='Thursday':
    print ('\nTodays meal will be ' +entree_list[1]+ '.\n'+'There will be no side. With a salad of '+salad_list[3]+'. Bon apetit!')

if day_today in week_day:
    sample_dish=random.choice[entree_list]
    sample_salad=random.choice[salad_list]
    sample_side=random.choice[salad_list]
    
    print("Today's meal will consist of "+sample_dish +" with a side of "+ sample_side+".")
    print("Today's salad will be "+ sample_salad+".")

elif day_today in weekend:
    sample_dish=random.choice(soup_list)
    
    print("Today's soup will be " + sample_dish+" for lunch.")
    sample_dish=random.choice(entree_list)
    print("For dinner, the meal will be "  +sample_dish+".")
    
    
    

