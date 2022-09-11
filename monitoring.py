from app import app, db
from app.models import User, Address

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Address': Address}