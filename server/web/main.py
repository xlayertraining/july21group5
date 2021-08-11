# --> Will import all the variables, settings, functions, classes declared or initialized in common.py
from common import *

# Declaring the API Classes required in the project. Same will be linked to API's in main.py.
# Format will be like --> from filename(without the .py extension) import classname
from sign_in import SignInHandler
from sign_up import SignUpHandler


def make_app():
    return tornado.web.Application([
        (r"/web/api/sign/up", SignUpHandler),
        (r"/web/api/sign/in", SignInHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
