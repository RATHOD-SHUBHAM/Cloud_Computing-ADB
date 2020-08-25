import os
import shutil
import csv
import sys
from flask import Flask,render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

import pymysql
import requests
import operator
#import nltk
import string
from collections import Counter
from flask import Flask,render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

import re
from collections import Counter 


application = Flask(__name__)
bootstrap = Bootstrap(application)

# Configurations
application.config['SECRET_KEY'] = 'blah blah blah blah'

class NameForm(FlaskForm):
    name = StringField('Name', default="Bruce Springsteen")
    submit = SubmitField('Submit')

# ROUTES!
@application.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return render_template('index.html',form=form,name=name)
    return render_template('index.html',form=form,name=None)


@application.route('/six',methods=['GET','POST'])
def six():
    filename = 'SpanishStopWords.csv'
    file = open(filename, 'rt',encoding="latin1")
    text = file.read()
    file.close()
    stopWords = text.split()
    print("\n\n\n\n")
    print("the stop word is : ",stopWords)

    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    words2 = text.split()
    print("\n\n\n")
    print("the words are : ",words2)

    punc = str.maketrans('', '', string.punctuation)
    print("\n\n\n\n")
    print("the punctuation is : ",punc)

    f_words2 = [w.translate(punc) for w in words2]
    print("\n\n\n\n")
    print("The f_words is : ",f_words2)

    f_words2 = [word.lower() for word in f_words2]
    print("\n\n\n\n")
    print("The F_words2 is : ",f_words2)

    count=0
    f_names=[]
    for name in stopWords:
        for word in f_words2:
            if(name==word):
                count+=1
        if(count!=0):
            f_names.append(name)
        count=0
    return render_template('name_record.html',ans=f_names)



@application.route('/eight',methods=['GET','POST'])
def eight():
    num = int(request.args.get('num'))

    filename = 'SpanishStopWords.csv'
    file = open(filename, 'rt',encoding="latin1")
    text = file.read()
    file.close()
    words_stop = text.split()

    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    words = text.split()

    punc = str.maketrans('', '', string.punctuation)
    f_words2 = [w.translate(punc) for w in words]
    f_words2 = [word.lower() for word in f_words2]

    flag=0
    c = Counter(f_words2)
    print("counter is : ",c)
    most_occur = c.most_common()
    print("\n\n\n")
    print("most occuring words is : ",most_occur)

    frequent_words=[]
    length=len(most_occur)

    for i in range(length-1,0,-1):
        for word in words_stop:
            if(most_occur[i][0]==word):
                flag=1
        if(flag==0):
            frequent_words.append(most_occur[i][0])
        flag=0
    print(frequent_words)
    f_names=[]
    for i in range(num):
        f_names.append(frequent_words[i])
    print(f_names)
    return render_template('search_record.html',ans=f_names)





@application.route('/quizsix',methods=['GET','POST'])
def quizsix():
    num = int(request.args.get('num'))
    print(num)

    filename = 'try.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    splitWord = text.split(".")
    print("\n\n\n")
    print("the words are : ",splitWord)

    nospace = []
    for i in splitWord:
        i = i.replace("\r", "").replace("\n", "")
        nospace.append(i)
    print("\n\n\n")
    print(nospace)

    sentenceSplit = []
    for i in nospace:
        i = i.split(" ")
        sentenceSplit.append(i)
    print("\n\n\n")
    print(sentenceSplit)

    charSplit = []
    for i in sentenceSplit:
        for j in i:
            j = j.split(",")
            charSplit.append(j)
    print("\n\n\n")
    print(charSplit)


     # Python3 program to Split string into characters 
    def split(word): 
        return [char for char in word]

    wordSplit = []
    for i in charSplit:
        for j in i:
            print("j",j)
            word = j
    #         j = split(j)
            wordSplit.append(split(word))
    print("\n\n\n")
    print("the word split is : ",wordSplit)


    letterSplit = []
    for i in wordSplit:
        for j in i:
            letterSplit.append(j)
    print("\n\n\n")
    print("letter split is : ",letterSplit)


    LetterCount = Counter(letterSplit)
    mostCommon = LetterCount.most_common(num)
    print("\n\n\n")
    print("the most common word is : ",mostCommon)
    leastCommon = LetterCount.most_common()[-num:]
    print("\n\n\n")
    print("the least Common word is ",leastCommon)

    return render_template('name_record.html',output=mostCommon,output1 =leastCommon )



# Assignment Question


# Question One

@application.route('/assOne',methods=['GET','POST'])
def assOne():
    userNumber = int(request.args.get('k'))
    print("The user entered number is : ",userNumber)
    print("\n\n\n")

    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    splitWord = text.split()
    print("\n\n\n")
    print("the words are : ",splitWord)

    myPunctuation = string.punctuation
    print("\n\n")
    print("the punctuations are: ",myPunctuation)
    print("\n\n")

    # map the punctuations to None

    mapString = str.maketrans('','',myPunctuation)
    print("\n\n")
    print("the none string is : ",mapString)
    
    translatedWord = [i.translate(mapString) for i in splitWord]
    print("\n\n")
    print("the tanslated word is : ",translatedWord)

    toLower = [i.lower() for i in translatedWord]
    print("\n\n")
    print("the lower case word is : ",toLower)



    # most frequency word

    counter = Counter(toLower)
    most_occur = counter.most_common(userNumber)

    # least frequency word


    least_occur = counter.most_common()[:-userNumber-1:-1]

    return render_template('assignmentOne.html',num = userNumber,output = most_occur,output1 = least_occur)


# Question Two

@application.route('/assTwo',methods=['GET','POST'])
def assTwo():
    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    splitWord = text.split()
    print("\n\n\n")
    print("the words are : ",splitWord)

    myPunctuation = string.punctuation
    print("\n\n")
    print("the punctuations are: ",myPunctuation)
    print("\n\n")

    # map the punctuations to None

    mapString = str.maketrans('','',myPunctuation)
    print("\n\n")
    print("the none string is : ",mapString)
    
    translatedWord = [i.translate(mapString) for i in splitWord]
    print("\n\n")
    print("the tanslated word is : ",translatedWord)

    toLower = [i.lower() for i in translatedWord]
    print("\n\n")
    print("the lower case word is : ",toLower)

    # stopWords 

    
    filename = 'SpanishStopWords.csv'
    file = open(filename, 'rt',encoding="latin1")
    text = file.read()
    file.close()
    stopWords = text.split()
    print("\n\n\n\n")
    print("the stop word is : ",stopWords)

    # import nltk
    # nltk.download('punkt')
    
    # from nltk.tokenize import word_tokenize
    
    # text_without_sw = [word for word in toLower if not word in stopWords ]

    for i in toLower:
        for j in stopWords:
            if i == j :
                toLower.remove(i)


    
    return render_template('assignmentTwo.html',output = toLower)





# Assignment 3

@application.route('/assThree',methods=['GET','POST'])
def assThree():

    substring = request.args.get('text')
    print("the substring is : ",substring)
    print("\n\n")


    frequency = int(request.args.get('k'))
    print("The user entered frequency is : ",frequency)
    print("\n\n\n")

    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    splitWord = text.split()
    # print("\n\n\n")
    # print("the words are : ",splitWord)

    myPunctuation = string.punctuation
    # print("\n\n")
    # print("the punctuations are: ",myPunctuation)
    # print("\n\n")

    # map the punctuations to None

    mapString = str.maketrans('','',myPunctuation)
    # print("\n\n")
    # print("the none string is : ",mapString)
    
    translatedWord = [i.translate(mapString) for i in splitWord]
    # print("\n\n")
    # print("the tanslated word is : ",translatedWord)

    toLower = [i.lower() for i in translatedWord]
    print("\n\n")
    print("the lower case word is : ",toLower)

    count = 0
    similar_match = []


    for i in toLower:
        if substring in i:
            # print("the string is :",i)
            # print("the substring is : ",substring)
            count = i.count(substring)
            # print(count)
            if count == frequency:
                # print(frequency)
                similar_match.append(i)
    
    return render_template('assignmentThree.html',output = similar_match)




# Question four
# import json

@application.route('/assFour',methods=['GET','POST'])
def assFour():

    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    splitWord = text.split()
    print("\n\n\n")
    print("the words are : ",splitWord)

    myPunctuation = string.punctuation
    print("\n\n")
    print("the punctuations are: ",myPunctuation)
    print("\n\n")

    # map the punctuations to None

    mapString = str.maketrans('','',myPunctuation)
    print("\n\n")
    print("the none string is : ",mapString)
    
    translatedWord = [i.translate(mapString) for i in splitWord]
    print("\n\n")
    print("the tanslated word is : ",translatedWord)

    toLower = [i.lower() for i in translatedWord]
    print("\n\n")
    print("the lower case word is : ",toLower)
   

    # nltk method to bigram
    # import nltk
    # print(list(nltk.bigrams(toLower)))

    # merge the list elements into one element
    test_list = [','.join(toLower)]


    bigraph = [ i for j in test_list for i in zip(j.split(",")[:-1],j.split(",")[1:])]

    # return render_template('assignmentFour.html',output = str(bigraph))
    return render_template('assignmentFour.html',output = bigraph)


@application.route('/assFour2',methods=['GET','POST'])
def assFour2():
    userNumber = int(request.args.get('num'))
    print("The user entered number is : ",userNumber)
    print("\n\n\n")

    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    splitWord = text.split()
    print("\n\n\n")
    print("the words are : ",splitWord)

    myPunctuation = string.punctuation
    print("\n\n")
    print("the punctuations are: ",myPunctuation)
    print("\n\n")

    # map the punctuations to None

    mapString = str.maketrans('','',myPunctuation)
    # print("\n\n")
    # print("the none string is : ",mapString)
    
    translatedWord = [i.translate(mapString) for i in splitWord]
    # print("\n\n")
    # print("the tanslated word is : ",translatedWord)

    toLower = [i.lower() for i in translatedWord]
    print("\n\n")
    print("the lower case word is : ",toLower)


    grams = [toLower[i:i+userNumber] for i in range(len(toLower)-userNumber+1)]
    
    # return render_template('assignmentFour.html',output = str(bigraph))
    return render_template('assignmentFour2.html',op = userNumber,output = grams)










# Question Five

@application.route('/assFive',methods=['GET','POST'])
def assFive():
    userChar = request.args.get('cha')
    print("User want to search : ",userChar)
    print(type(userChar))

    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    print("\n\n")
    print(type(text))

    all_freq = {}

    for i in text:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    print(str(all_freq))


    if userChar in all_freq:
        print("\n\n")
        print(str(all_freq[userChar]))
        myResult = str(all_freq[userChar])


    
    return render_template('assignmentFive.html',op = userChar,output = myResult)


# Question Six : 

@application.route('/assSix',methods=['GET','POST'])
def assSix():
    userChar = request.args.get('chapa')
    print("User want to search : ",userChar)
    print(type(userChar))

    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    splitWord = text.split()

    myPunctuation = string.punctuation
    print("\n\n")
    print("the punctuations are: ",myPunctuation)
    print("\n\n")

    # map the punctuations to None

    mapString = str.maketrans('','',myPunctuation)
    print("\n\n")
    print("the none string is : ",mapString)
    
    translatedWord = [i.translate(mapString) for i in splitWord]
    print("\n\n")
    print("the tanslated word is : ",translatedWord)

    toLower = [i.lower() for i in translatedWord]
    print("\n\n")
    print("the lower case word is : ",toLower)


    count = 0
    Foundcharacter = []


    for i in toLower:
        if userChar in i:
            Foundcharacter.append(i)
            count += 1


    
    return render_template('siignmentSix.html',op = userChar,output = count,output2 = Foundcharacter )

@application.route('/assSix2',methods=['GET','POST'])
def assSix2():
    userChar = request.args.get('chapa')
    print("User want to search : ",userChar)
    print(type(userChar))

    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    splitWord = text.split()

    myPunctuation = string.punctuation
    print("\n\n")
    print("the punctuations are: ",myPunctuation)
    print("\n\n")

    # map the punctuations to None

    mapString = str.maketrans('','',myPunctuation)
    print("\n\n")
    print("the none string is : ",mapString)
    
    translatedWord = [i.translate(mapString) for i in splitWord]
    print("\n\n")
    print("the tanslated word is : ",translatedWord)

    toLower = [i.lower() for i in translatedWord]
    print("\n\n")
    print("the lower case word is : ",toLower)

    count = 0
    Foundcharacter = []

    for i in range(len(toLower)):
        if userChar == toLower[i]:
            Foundcharacter.append([toLower[i],i])
            count += 1


    
    return render_template('assignmentSix2.html',op = userChar,output = count,output2 = Foundcharacter )




# Question Seven


@application.route('/assSeven',methods=['GET','POST'])
def assSeven():
    userChar = request.args.get('cha')
    print("User want to search : ",userChar)
    print(type(userChar))


    sideChar = request.args.get('sidecha')
    print("User want to search : ",sideChar)
    print(type(sideChar))

    filename = 'Alamo.txt'
    file = open(filename, 'rt',encoding="utf-8")
    text = file.read()
    file.close()
    print("\n\n")
    print(type(text))
    splitWord = text.split()

    myPunctuation = string.punctuation
    print("\n\n")
    # print("the punctuations are: ",myPunctuation)
    print("\n\n")

    # map the punctuations to None

    mapString = str.maketrans('','',myPunctuation)
    print("\n\n")
    # print("the none string is : ",mapString)
    
    translatedWord = [i.translate(mapString) for i in splitWord]
    print("\n\n")
    # print("the tanslated word is : ",translatedWord)

    toLower = [i.lower() for i in translatedWord]
    print("\n\n")
    print("the lower case word is : ",toLower)

    all_freq = {}

    for i in text:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    print(str(all_freq))


    if userChar in all_freq:
        print("\n\n")
        print(str(all_freq[userChar]))
        myResult = str(all_freq[userChar])


    # Question part two:

    compare = sideChar + userChar
    print("the word to be compared is:  ",compare)

    count = 0
    Foundcharacter = []


    for i in toLower:
        if compare in i:
            Foundcharacter.append(i)
            count += 1

    # next to any word





    
    return render_template('assignmentSeven.html',op = userChar,output = myResult,op1 = compare, output1 = Foundcharacter, output2 = count)


















@application.route('/help')
def help():
    text_list = []
    # Python Version
    text_list.append({
        'label':'Python Version',
        'value':str(sys.version)})
    # os.path.abspath(os.path.dirname(__file__))
    text_list.append({
        'label':'os.path.abspath(os.path.dirname(__file__))',
        'value':str(os.path.abspath(os.path.dirname(__file__)))
        })
    # OS Current Working Directory
    text_list.append({
        'label':'OS CWD',
        'value':str(os.getcwd())})
    # OS CWD Contents
    label = 'OS CWD Contents'
    value = ''
    text_list.append({
        'label':label,
        'value':value})
    return render_template('help.html',text_list=text_list,title='help')

@application.errorhandler(404)
@application.route("/error404")
def page_not_found(error):
    return render_template('404.html',title='404')

@application.errorhandler(500)
@application.route("/error500")
def requests_error(error):
    return render_template('500.html',title='500')


port = os.getenv('PORT', '3000')
if __name__ == '__main__':
    application.debug=True
    application.run(host='0.0.0.0', port=int(port))