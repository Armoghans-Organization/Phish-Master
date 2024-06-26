import os
from sqlalchemy import inspect
from app import db ,app
from utilities import *
from models import *

# Get the current working directory
cwd = os.getcwd()

def create_tables_if_not_exists(db, table_names):
    try:
        with app.app_context():
            inspector = inspect(db.engine)
            for table_name in table_names:
                if table_name not in inspector.get_table_names():
                    # Explicitly create the table
                    table_class = globals()[table_name.capitalize()]  # Assuming your table class names are capitalized
                    table_class.__table__.create(db.engine)
                    print()
                    print(color.ColorPrinter.magenta(f"Creating {table_name.capitalize()} Table"), end=" ")
                    dots.print_colored_dots(10 , 'magenta')
                    print()
                    print(color.ColorPrinter.green(f"{table_name.capitalize()} Table Created Successfully"))
                else:
                    print()
                    print(color.ColorPrinter.yellow(f"{table_name.capitalize()} Table already exists"))
    except Exception as e:
        print(color.ColorPrinter.red(f"Error creating tables: {e}"))
    

def create_user():
    print()
    print(color.ColorPrinter.cyan("Create a New User!"))
    print()
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Add new user
    new_user = user.User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    print()
    print(color.ColorPrinter.green("User added successfully!"))

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

with app.app_context():
    # Check if there are any users in the user table
    user_count = user.User.query.count()
    if user_count > 0:
        print()
        print(color.ColorPrinter.yellow("User already exists"))
        print()
        create_new = input("Do you want to create a new user? (yes/no): ").strip().lower()
        if create_new == 'yes':
            create_user()
        else:
            print()
            print(color.ColorPrinter.red("Exiting without creating a new user."))
    else:
        create_user()

        
########################################################
# For Debugging 
########################################################

# table_names = ['user' , 'creds' , 'media' , 'info']
# create_tables_if_not_exists(db, table_names)