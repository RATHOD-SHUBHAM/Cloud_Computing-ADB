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

# import dbi 
import ibm_db
import ibm_db_dbi
# import pandas as pd
# import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Configurations
app.config['SECRET_KEY'] = 'blah blah blah blah'



# connect using ibm_db_dbi. Attempt to establish A connection with uncataloged database.
# using service credentials
# here there will be ibm user name and password
# user name will be the one you select like nwe23 or xbr34...
conn = ibm_db_dbi.connect(
		
		)
# fetch data using ibm_db_dbi
myCursor = conn.cursor()


class NameForm(FlaskForm):
	name = StringField('Name', default="Bruce Springsteen")
	submit = SubmitField('Submit')



# ROUTES!
@app.route('/',methods=['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		return render_template('index.html',form=form,name=name)
	return render_template('index.html',form=form,name=None)




# creating  my routes 

@app.route('/try', methods=['GET', 'POST'])
def testing():
	
	# sql = " insert into PeopleTable (\"Name\",\"salary\",\"room\",\"keywords\") values (\'nitiish\',\'2000\',\'1678\',\'niiiice\');"
	# myCursor.execute(sql)
	# print(sql)

	sql = "DELETE FROM PeopleTable WHERE \"Name\" = \'nitiish\';"
	myCursor.execute(sql)
	print(sql)

	sql = " SELECT * from PeopleTable  "
	myCursor.execute(sql)
	print(sql)

	myResult = myCursor.fetchall()
	for i in myResult:
		print(i)
	# outputFile = "\static\\" + myResult[0]
	return render_template('try.html',output = myResult )


@app.route('/one', methods=['GET', 'POST'])
def questionOne():

	# Requesting form
	# request firstname from form
	# name = str(request.form['fname'])
	# print("The name is : ",name)
	
	# sql = " insert into PeopleTable (\"Name\",\"salary\",\"room\",\"keywords\") values (\'nitiish\',\'2000\',\'1678\',\'niiiice\');"
	# myCursor.execute(sql)
	# print(sql)

	# sql = "DELETE FROM PeopleTable WHERE \"Name\" = \'nitiish\';"
	# myCursor.execute(sql)
	# print(sql)


	sql = " SELECT \"picture\" FROM PeopleTable where \"Name\" = \'chris\' ; "
	myCursor.execute(sql)
	print(sql)

	# sql = " SELECT * from PeopleTable  "
	# myCursor.execute(sql)
	# print(sql)

	myResult = myCursor.fetchone()
	print(myResult)

	# if image always add it to static
	outputFile = "\static\\" + myResult[0]
	return render_template('myResult.html',output = outputFile )


# question 2 
@app.route('/two', methods=['GET', 'POST'])
def questionTwo():
	
	# sql = " insert into PeopleTable (\"Name\",\"salary\",\"room\",\"keywords\") values (\'nitiish\',\'2000\',\'1678\',\'niiiice\');"
	# myCursor.execute(sql)
	# print(sql)

	# sql = "DELETE FROM PeopleTable WHERE \"Name\" = \'nitiish\';"
	# myCursor.execute(sql)
	# print(sql)


	sql = " select \"picture\" from PeopleTable where \"salary\" < 99000  ; "
	myCursor.execute(sql)
	print(sql)

	# sql = " SELECT * from PeopleTable  "
	# myCursor.execute(sql)
	# print(sql)

	# each time for loop run. it fetch a value and return only when it has traversed.
	# we got to save a value so that it doesnot forget the previous searched value.

	#  dont keep value == NONE

	# append Values 

	appendFile = []
	dontAppendFile = []
	myResult = myCursor.fetchall()
	print(myResult)
	for i in myResult:
		# print("the value of i is  : ",i)
		# print("value i[0] is : ",i[0])
		if i[0] != None:
			# print(i[0])
			outputFile = "\static\\" + i[0]
			appendFile.append(outputFile)
		else:
			# print(i[0])
			outputFile = ""
			dontAppendFile.append(outputFile)
		# if image always add it to static
	return render_template('myResult2.html',output = appendFile )


# question 3 

@app.route('/three', methods=['GET', 'POST'])
def addPicture():
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	app.config['UPLOAD_DIR'] = os.path.join('static')
	
	send_dir = os.path.join(BASE_DIR,'static/')
	
	userFileName=""
	
	print(request)
	print(request.files)

	# taking the file from user
	# passing name of file
	# only when we specify iD we pass ID.
	for file in request.files.getlist('myfile'):
		print(file)
		print(file.filename)
		userFileName = file.filename
		target = "/".join([send_dir,userFileName])
			
		completeFilePath = os.path.join(app.config['UPLOAD_DIR'],userFileName)
		file.save(target)


	sql = "UPDATE PeopleTable SET \"picture\" = \'"+userFileName+"\' where \"Name\" = \'dave\'"
	myCursor.execute(sql)
	print(sql)

	sql = "SELECT \"picture\" from PeopleTable where \"Name\" = 'dave'"
	myCursor.execute(sql)

	myResult = myCursor.fetchone()
	print(myResult)
	
	outputFile = "\static\\" + myResult[0]
	return render_template('myResult3.html',output = outputFile)



# question 4 
@app.route('/four', methods=['GET', 'POST'])
def questionFour():
	
	sql = " DELETE FROM PeopleTable WHERE  \"Name\" = 'dave'; "
	myCursor.execute(sql)


	sql = " SELECT * from PeopleTable  "
	myCursor.execute(sql)
	print(sql)

	myResult = myCursor.fetchall()
	print(myResult)


	return render_template('myResult6.html',output = myResult )


# question 5 
@app.route('/five', methods=['GET', 'POST'])
def questionFive():
	
	sql = " UPDATE PeopleTable SET \"keywords\" =  \'not so nice anymore \' WHERE \"Name\" = \'jason\'; "
	myCursor.execute(sql)


	sql = " SELECT * from PeopleTable  "
	myCursor.execute(sql)
	print(sql)

	myResult = myCursor.fetchall()
	print(myResult)


	return render_template('myResult5.html',output = myResult )


# question 6

@app.route('/six', methods=['GET', 'POST'])
def questionsix():

	salary = float(request.form['fname'])
	
	sql = " UPDATE PeopleTable SET \"salary\" =  \'"+str(salary)+"\' WHERE \"Name\" = 'someone'; "
	myCursor.execute(sql)


	sql = " SELECT * from PeopleTable  "
	myCursor.execute(sql)
	print(sql)

	myResult = myCursor.fetchall()
	print(myResult)


	return render_template('myResult6.html',output = myResult )













@app.route('/help')
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

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')

port = int(os.getenv('PORT', '3000'))
app.run(host='0.0.0.0', port=port)
