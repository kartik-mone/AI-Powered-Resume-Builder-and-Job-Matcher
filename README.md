
# AI-Powered Resume Builder and Job Matcher

## Project Description
A web application to create professional resumes and match users with job opportunities using Machine Learning. It analyzes job descriptions and user profiles to provide personalized recommendations.

---

## Features
### 1. Resume Builder
- Create customized resumes with pre-designed templates.
- Export to PDF with ATS-friendly keyword suggestions.

### 2. Job Matching System
- Recommends jobs based on user skills and preferences using ML (e.g., TF-IDF, BERT).
- Filters for location, job type, and salary.

### 3. Skill Gap Analysis
- Highlights missing skills and suggests relevant courses via APIs (e.g., Udemy, Coursera).

### 4. Job Applications Dashboard
- Tracks applications and statuses (e.g., applied, under review).

### 5. Admin Panel
- Employers can post jobs and view matched candidates.

---

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask, REST APIs
- **Database**: SQLAlchemy (MySQL)
- **ML Models**: NLP (spaCy, Scikit-learn, TF-IDF)
- **PDF Export**: `xhtml2pdf`, `reportlab`

---

## Folder Structure
```
/resume-job-matcher
│
├── /static
│   ├── /css
│   │   └── styles.css                # Main CSS file for the app
│   ├── /js
│   │   └── app.js                   # JavaScript for dynamic functionality
│   └── /images                      # Store static images and icons
│
├── /templates
│   ├── base.html                    # Base layout for all pages
│   ├── job_match.html               # Displays job matches and allows applying to them
│   ├── home.html                    # Homepage
│   ├── register.html                # User registration form
│   ├── login.html                   # User login page
│   ├── dashboard.html               # User dashboard with resume creation
│   ├── job_match.html               # Job recommendations page
│   ├── admin.html                   # Admin panel for employers
│   └── error.html                   # Error page
│
├── /models
│   └── ml_model.pkl                 # Trained machine learning model for job matching
│
├── train_model.py
├── /data
│   └── jb_df.csv                    # CSV File of Job data
│
├── app.py                           # Main Flask application file
├── database.py                      # Database models and connection
├── requirements.txt                 # Python dependencies
├── README.md                        # Documentation
└── .gitignore                       # Git ignore file

```

---

## How to Run
1. Clone the repo and navigate to the project directory:
   ```bash
   git clone <repo-url> && cd resume-job-matcher
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database in `app.py` and run:
   ```bash
   python database.py
   ```
4. Train the ML model (optional):
   ```bash
   python train_model.py
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000`.

---

## Additional Features
- Drag-and-drop resume sections.
- Job market analytics dashboard.
- AI Cover Letter Generator.
- LinkedIn integration for pre-filling user profiles.

---


Let me know if you need further edits!
