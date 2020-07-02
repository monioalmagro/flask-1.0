from app create_app
from flask-script import Manager

app = create_app()

if __name__ == '__main__':
    manager = Manager(app)
    manager.run()
    