from common import *
from auth import *


class ApplyJobsHandler(tornado.web.RequestHandler):
    async def post(self):
        code = 4000
        status = False
        message = ""
        result = []
        account_id = await SecureHeader.decrypt(self.request.headers["Authorization"])
        if account_id == None:
            code = 8765
            status = False
            message = "You're not authorized"
            raise Exception
        try:
            try:
                jsonBody = json.loads(self.request.body.decode())
            except:
                code = 4732
                status = False
                message = "Invalid JSON Body"
                raise Exception
            try:
                jobId = ObjectId(jsonBody['jobId'])
            except:
                code = 8493
                status = False
                message = "Please select the job"
                raise Exception
            jobFind = await applications.find_one(
                {
                    "jobId": jobId,
                    "accountId": account_id
                }
            )
            if jobFind:
                code = 9032
                status = False
                message = "You have already submitted"
                raise Exception
            await applications.insert_one(
                {
                    "jobId": jobId,
                    "accountId": account_id,
                    "time": timeNow(),
                    "active": True,
                }
            )
            code = 2000
            status = True
            message = "Thank you for applying to the job"
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

    async def delete(self):
        code = 4000
        status = False
        message = ""
        result = []
        account_id = await SecureHeader.decrypt(self.request.headers["Authorization"])
        if account_id == None:
            code = 8765
            status = False
            message = "You're not authorized"
            raise Exception
        try:
            try:
                jobId = ObjectId(self.request.arguments['jobId'][0].decode())
            except:
                code = 8493
                status = False
                message = "Please select the job"
                raise Exception
            jobFind = await applications.find_one(
                {
                    "jobId": jobId,
                    "accountId": account_id
                }
            )
            if jobFind == None:
                code = 9032
                status = False
                message = "You have not applied for the job"
                raise Exception
            await applications.update_one(
                {
                    "jobId": jobId,
                    "accountId": account_id
                },
                {
                    "$set": {
                        "active": False
                    }
                }
            )
            code = 2000
            status = True
            message = "Application has been removed"
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
