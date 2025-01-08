from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
import pickle
import os

app = Flask(__name__)

# MySQL URI connection string (with XAMPP configuration)
# Replace `root` with your MySQL username, and the password is usually empty by default unless you set one.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/resume_project'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional to disable track modifications warning
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
db = SQLAlchemy(app)

# Load pre-trained ML model for job matching
with open('models/ml_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    skills = db.Column(db.String(500), nullable=False)
    experience = db.Column(db.String(500), nullable=False)
    resume = db.Column(db.String(500), nullable=True)  # Path to resume file

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    status = db.Column(db.String(100), default='Applied', nullable=False)

# Create tables in MySQL
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='sha256')
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            flash("Login failed. Please check your credentials.", "danger")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.filter_by(id=session['user_id']).first()
    return render_template('dashboard.html', user=user)

@app.route('/create_resume', methods=['GET', 'POST'])
def create_resume():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        user = User.query.filter_by(id=session['user_id']).first()
        skills = request.form['skills']
        experience = request.form['experience']
        user.skills = skills
        user.experience = experience
        db.session.commit()
        flash("Resume updated successfully!", "success")
        return redirect(url_for('dashboard'))
    return render_template('create_resume.html')

@app.route('/job_match')
def job_match():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.filter_by(id=session['user_id']).first()
    jobs = Job.query.all()

    # Implement job matching using the pre-trained model
    job_scores = []
    for job in jobs:
        # Use model to score job matching based on user's skills
        score = model.predict([user.skills, job.description])
        job_scores.append((job, score))

    # Sort jobs based on score
    job_scores.sort(key=lambda x: x[1], reverse=True)
    return render_template('job_match.html', job_scores=job_scores)

@app.route('/apply/<job_id>', methods=['POST'])
def apply(job_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.filter_by(id=session['user_id']).first()
    job = Job.query.get(job_id)
    new_application = Application(user_id=user.id, job_id=job.id)
    db.session.add(new_application)
    db.session.commit()
    flash("Application submitted successfully!", "success")
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
