import os
from app import db ,app
from utilities import *
# from models import *

# Get the current working directory
cwd = os.getcwd()
    
clear.TerminalClear.clear()
banner.print_banner()

# Check if the database file exists, create if not
db_path = os.path.join(cwd, 'PhishMaster.sqlite3')
try:
    with app.app_context():
        if not os.path.exists(db_path):
            db.create_all()
            print()
            print(color.ColorPrinter.magenta("Creating Database"), end=" ")
            dots.print_colored_dots(10 , 'magenta')
            print()
            print(color.ColorPrinter.green("Database Created Successfully"))
        else:
            print()
            print(color.ColorPrinter.yellow("Database already exists"))
except Exception as e:
    print(color.ColorPrinter.red(f"Error creating database: {e}"))