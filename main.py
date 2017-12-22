from flask import Flask, url_for

app = Flask(__name__)



@app.route('/')
def index(): 
	return '''Cooking main page
	<a href="/sendingURL/">go to URL sending</a>'''

@app.route('/sendingURL', methods=['GET', 'POST'])#allow both GET and POST requests
def sendingURL():
	if request.method == 'POST': #this block is only entered when the form is submitted
			url_input = request.form.get('url_input') #get the url input
			webbrowser.open(str(url_input)) # open the browser with the URL
			return '''<h1>The entered URL is: {}</h1>'''.format(url_input)
	return '''<form method="POST">
				URL: <input type="text" name="url_input"><br>
				<input type="submit" value="Submit"><br>
				</form>'''
	
if __name__ == '__main__':
	# starting the app in debug with local host with port 5555
	app.run(debug=True, host='0.0.0.0') #advanced port=80