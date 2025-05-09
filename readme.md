Forza Cup Tracker

A web app for creating and simulating custom single-player racing cups in Forza Motorsport. Track your race times, simulate AI competitors, and view evolving championship standings, all in one place.

---
Features

- Create custom cups with up to 30 races  
- Choose from all official Forza Motorsport tracks (plus some fictional ones)  
- Enter your race results and finish times  
- Simulated AI competitors with realistic times based on your performance  
- Dynamic leaderboard and standings tracking  
- Supports custom racer names or name generation  

---

Live App

This app is hosted on [Netlify](https://www.netlify.com/) using serverless functions with Flask.

---

Project Structure

.
├── netlify.toml # Netlify config file
├── requirements.txt # Python dependencies
├── /functions # All server-side Python code
│ ├── app.py # Flask app entry point
│ ├── models.py # Data models
│ ├── simulate.py # AI simulation logic
│ ├── track_data.py # Track list and info
│ ├── /templates # HTML templates
│ └── /static # CSS and other static files
├── /public # Optional static index.html for Netlify
└── README.md # You're reading it

yaml
Copy
Edit

---

🛠 How to Run Locally

1. Clone the repo:
bash
git clone https://github.com/yourusername/forza-cup-tracker.git
cd forza-cup-tracker/functions
Create a virtual environment and install dependencies:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r ../requirements.txt
Run the Flask app:

bash
Copy
Edit
flask run

Deployment Notes (Netlify)
Netlify runs functions/app.py as a serverless function.

All routes are redirected through this function via netlify.toml.

The app uses Flask's template system to render pages dynamically.

Roadmap
Add user login (optional)

Support for lap-based scoring

Shareable cup summaries

Export results as CSV

AI Sim Notes
AI finish times are generated based on your result. For example, if you finish 8th, AI times near you (7th, 9th) will be close to yours to maintain realism.


License
MIT — feel free to fork, share, and improve.
