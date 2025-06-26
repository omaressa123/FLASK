from omar.models import user,projects,course
from flask import render_template, url_for, flash, redirect
from omar.forms import RegistrationFrom, LoginForm
from omar import app


projects = [{
    'name': 'Rock vs Mine',
    'description':'machine learning project',
    'link':'https://www.linkedin.com/posts/omar-mohamed-650104324_machinelearning-ai-projects-activity-7310886262654091264-2w5-?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFHiqpwBwaSidevM-MbGTry_qvmdqiaO8i0'
},
{
    'name':'The Handwritten Generation Project',
    'description':'machine learning project',
    'link':'https://www.linkedin.com/posts/omar-mohamed-650104324_task4-first-sec-activity-7243222722095251456-O3Fb?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFHiqpwBwaSidevM-MbGTry_qvmdqiaO8i0'
},
{
    'name': 'spam sms detection',
    'description':'machine learning project',
    'link':'https://www.linkedin.com/posts/omar-mohamed-650104324_task3-libraries-activity-7242104917916626945-GeZ3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFHiqpwBwaSidevM-MbGTry_qvmdqiaO8i0'
}
]
courses = [
{
        'name': 'Python',
        'icon': 'python.svg',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Data cleaning & preprocessing',
        'icon': 'cleaning.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Machine Learning',
        'icon': 'machine-learning.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'flask & html & css',
        'icon': 'web.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'sql & mysql',
        'icon': 'idea.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'C++ & assembly',
        'icon': 'c++.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",projects=projects,courses=courses)
@app.route("/about")
def about():
   return render_template("about.html",title="About")
@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!")
        return redirect(url_for('home'))
    return render_template("register.html",title="Register",form=form)
@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'omar@gmail.com' and form.password.data == 'omar':
            flash(f"You have been logged in!","success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check email and password","danger")
    return render_template("login.html",title="Login",form=form)
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html',title= 'dashboard')