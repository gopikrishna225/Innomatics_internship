from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/personal')
def personal():
    return render_template('personal.html')
@app.route('/education')
def education():
    return render_template('education.html')

if(__name__=='__main__'):
    app.run(debug=True)
