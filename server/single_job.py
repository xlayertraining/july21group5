from common import *
from auth import *


class SingleJobHandler(tornado.web.RequestHandler):

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
                jobId = ObjectId(self.request.arguments['id'][0].decode())
            except:
                code = 9043
                status = False
                message = "Invalid Job Id"
                raise Exception
            jobFind = await jobs.find_one({"_id": jobId})
            if jobFind:
                jobFind['_id'] = str(jobFind['_id'])
                jobFind['submittedBy'] = ""
                jobFind['submitCount'] = await applications.count_documents({"jobId": jobFind['_id'], "active": True})
                accFind = await users.find_one({"_id": ObjectId(jobFind['accountId'])})
                if accFind:
                    jobFind['submittedBy'] = accFind['firstName'] + \
                        " " + accFind['lastName']
                result.append(jobFind)
            if len(result):
                code = 2000
                status = True
                message = "Job Information"
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
