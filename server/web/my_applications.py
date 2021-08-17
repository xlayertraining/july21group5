from common import *
from auth import *


class ApplicationsHandler(tornado.web.RequestHandler):
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
            jobsList = jobs.find({"accountId": account_id})
            async for i in jobsList:
                i['_id'] = str(i['_id'])
                i['submittedBy'] = ""
                i['submitCount'] = await applications.count_documents({"jobId": i['_id'], "active": True})
                accFind = await users.find_one({"_id": ObjectId(i['accountId'])})
                if accFind:
                    i['submittedBy'] = accFind['firstName'] + \
                        " " + accFind['lastName']
                result.append(i)
            if len(result):
                code = 2000
                status = True
                message = "List of Jobs"
            else:
                code = 8943
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
