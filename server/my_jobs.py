from common import *
from auth import *


class MyJobsHandler(tornado.web.RequestHandler):
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
                jobId = str(jsonBody['jobId'])
            except:
                code = 8493
                status = False
                message = "Invalid Job Id"
                raise Exception
            try:
                accId = str(jsonBody['accId'])
            except:
                code = 8493
                status = False
                message = "Invalid Account Id"
                raise Exception
            jobFind = await applications.find_one(
                {
                    "jobId": jobId,
                    "accountId": accId
                }
            )
            if jobFind == None:
                code = 9032
                status = False
                message = "Job Application Not Found"
                raise Exception
            await applications.update_one(
                {
                    "jobId": jobId,
                    "accountId": accId
                },
                {
                    "$set": {
                        "active": False
                    }
                }
            )
            code = 2000
            status = True
            message = "Job Status has been updated"
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

    async def get(self):
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
                jobId = ObjectId(self.request.arguments['id'][0].decode())
            except:
                jobId = None
            if jobId:
                jobFind = await jobs.find_one(
                    {
                        "_id": jobId,
                        "accountId": account_id
                    }
                )
                if jobFind:
                    jobFind['_id'] = str(jobFind['_id'])
                    jobFind['submitCount'] = await applications.count_documents({"jobId": jobFind['_id'], "active": True})
                    applicants = []
                    applicantList = applications.find(
                        {"jobId": jobFind['_id'], "active": True})
                    async for i in applicantList:
                        v = {}
                        name = ""
                        location = ""
                        qualification = ""
                        cgpa = ""
                        accFind = users.find_one({
                            "_id": ObjectId(i['accountId'])
                        })
                        if accFind:
                            name = accFind['firstName'] + \
                                " " + accFind['lastName']
                        proFind = profile.find_one(
                            {
                                "accountId": ObjectId(i['accountId'])
                            }
                        )
                        if proFind:
                            location = proFind['location']
                            qualification = proFind['qualification']
                            cgpa = proFind['cgpa']
                        v = {
                            "id": i['accountId'],
                            "name": name,
                            "location": location,
                            "qualification": qualification,
                            "cgpa": cgpa,
                            "jobId": str(jobId)
                        }
                        applicants.append(v)
                    jobFind['applicants'] = applicants
                    result.append(jobFind)
                else:
                    code = 9043
                    status = False
                    message = "Job not found"
                    raise Exception
            else:
                jobList = jobs.find(
                    {
                        "accountId": account_id
                    }
                )
                async for i in jobList:
                    i['_id'] = str(i['_id'])
                    i['submitCount'] = await applications.count_documents({"jobId": i['_id'], "active": True})
                    result.append(i)
                if len(result):
                    code = 2000
                    status = True
                    message = "List of jobs"
                else:
                    code = 8943
                    status = False
                    message = "No Jobs found"
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
