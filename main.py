from backend.__init import create_app
from backend.__init import db
from flask_migrate import Migrate
from backend.models import User
app = create_app('development')
migrate = Migrate(app,db)
@app.shell_context_processor
def make_shell_context():
   return dict(db= db, User=User)