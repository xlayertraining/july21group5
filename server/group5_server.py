# --> Will import all the variables, settings, functions, classes declared or initialized in common.py
from common import *

# Declaring the API Classes required in the project. Same will be linked to API's in main.py.
# Format will be like --> from filename(without the .py extension) import classname
from sign_in import SignInHandler
from sign_up import SignUpHandler
from Offer_jobs import JobsHandler
from jobs_search import JobsSearchHandler
from apply_job import ApplyJobsHandler
from single_job import SingleJobHandler
from user_profile import ProfileHandler
from my_jobs import MyJobsHandler
from my_applications import ApplicationsHandler

def make_app():
    return tornado.web.Application([
        (r"/julygroup5_web/api/sign/up", SignUpHandler),
        (r"/julygroup5_web/api/sign/in", SignInHandler),
        (r"/julygroup5_web/api/Offer/jobs", JobsHandler),
        (r"/julygroup5_web/api/jobs/search", JobsSearchHandler),
        (r"/julygroup5_web/api/apply/jobs", ApplyJobsHandler),
        (r"/julygroup5_web/api/single/job", SingleJobHandler),
        (r"/julygroup5_web/api/profile", ProfileHandler),
        (r"/julygroup5_web/api/my/jobs", MyJobsHandler),
        (r"/julygroup5_web/api/my/applications", ApplicationsHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8005)
    tornado.ioloop.IOLoop.current().start()
