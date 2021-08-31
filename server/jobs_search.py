from common import *
from auth import SecureHeader

class JobsSearchHandler(tornado.web.RequestHandler):

    def options(self):
        self.write({})
        return

    async def get(self):
        code = 4000
        status = False
        message = ""
        result = []

        try:
            account_id = await SecureHeader.decrypt(self.request.headers["Authorization"])
            if account_id == None:
                code = 8765
                status = False
                message = "You're not authorized"
                raise Exception
            try:
                keyword = str(self.request.arguments['keyword'][0].decode())
                if keyword == "" or keyword == None:
                    raise Exception
            except:
                code = 8493
                status = False
                message = "Please enter valid search keyword"
                raise Exception
            jobsList = jobs.find({
                "active": True,
                "$or": [
                    {
                        "companyName": {
                            "$regex": keyword,
                            "$options": "i"
                        }
                    },
                    {
                        "location": {
                            "$regex": keyword,
                            "$options": "i"
                        }
                    },
                    {
                        "designation": {
                            "$regex": keyword,
                            "$options": "i"
                        }
                    }
                ]
            })
            async for i in jobsList:
                i['_id'] = str(i['_id'])
                result.append(i)
            if len(result):
                code = 2000
                status = True
                message = "List of jobs"
                raise Exception
            else:
                code = 9302
                status = False
                message = "No jobs found"
                raise Exception
        except:
            status = False
            # self.set_status(400)
            if not len(message):
                template = 'Exception: {0}. Argument: {1!r}'
                code = 5010
                message = 'Internal Error, Please Contact the Support Team.'
        response = {
            'code': code,
            'status': status,
            'message': message
        }
        try:
            response['result'] = result
            self.write(response)
            self.finish()
            return
        except Exception as e:
            status = False
            code = 5011
            message = 'Internal Error, Please Contact the Support Team.'
            response = {
                'code': code,
                'status': status,
                'message': message
            }
            self.write(response)
            self.finish()
            return
