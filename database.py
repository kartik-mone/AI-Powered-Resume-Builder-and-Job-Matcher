from app import db
import app

# Create the tables in the database
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    create_tables()
