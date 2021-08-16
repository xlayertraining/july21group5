# --> Will import all the variables, settings, functions, classes declared or initialized in common.py
from common import *

# Declaring the API Classes required in the project. Same will be linked to API's in main.py.
# Format will be like --> from filename(without the .py extension) import classname
from sign_in import SignInHandler
from sign_up import SignUpHandler
from jobs import JobsHandler
from jobs_search import JobsSearchHandler
def make_app():
    return tornado.web.Application([
        (r"/julygroup5_web/api/sign/up", SignUpHandler),
        (r"/julygroup5_web/api/sign/in", SignInHandler),
        (r"/julygroup5_web/api/jobs", JobsHandler),
        (r"/julygroup5_web/api/jobs/search", JobsSearchHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8005)
    tornado.ioloop.IOLoop.current().start()
