from flask import Blueprint, render_template, session, redirect

# Define the Blueprint
logout_bp = Blueprint('logout', __name__)

# Route for logging out
@logout_bp.route("/logout")
def Logout():
    # Clear the session data
    session.clear()
    return redirect('/')