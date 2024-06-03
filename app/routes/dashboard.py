from flask import Blueprint, render_template, session, redirect
import sqlite3

# Define the Blueprint
dashboard_bp = Blueprint('dashboard', __name__)

# Route for dashboard page
@dashboard_bp.route("/dashboard")
def dashboard():
    # Check if the user is logged in
    if session.get('logged_in'):
        username = session.get('username')
        return render_template('dashboard.html', username=username)
    else:
        # User is not logged in, redirect to login page
        return redirect('/')
