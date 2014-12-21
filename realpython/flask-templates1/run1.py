from flask import Flask,render_template

app=Flask('__name__')

@app.route('/')
def main():
	return render_template('main.html',message="How are you?",mylist=[10,20,30,40,50])

if __name__ == '__main__':
	app.run(debug=True)
