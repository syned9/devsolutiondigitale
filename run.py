from app import create_app, db
from sqlalchemy import exc

flask_app = create_app('prod')
with flask_app.app_context():
    from app import routes
    engine = db.get_connection()
    db.createTable(engine)
if __name__ == "__main__":
    flask_app.run()