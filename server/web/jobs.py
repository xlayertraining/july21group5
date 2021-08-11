from common import *


class JobsHandler(tornado.web.RequestHandler):
    async def post(self):
        code = 4000
        status = False
        message = ""
        result = []
        try:
            try:
                jsonBody = json.loads(self.request.body.decode())
            except:
                code = 4732
                status = False
                message = "Invalid JSON Body"
                raise Exception
            # Fields will be designation, company name, description, minimum qualification, preferred qual, salary, location, remote job
            try:
                designation = jsonBody['designation']
                if designation == None or designation == "" or len(designation) < 3 or len(designation) > 30:
                    raise Exception
            except:
                code = 8493
                status = False
                message = "Please enter valid designation (3-30 characters)"
                raise Exception
            try:
                companyName = jsonBody['companyName']
                if companyName == None or companyName == "" or len(companyName) < 3 or len(companyName) > 30:
                    raise Exception
            except:
                code = 8493
                status = False
                message = "Please enter valid company name (3-30 characters)"
                raise Exception
            try:
                description = jsonBody['description']
                if description == None or description == "" or len(description) < 3 or len(description) > 1000:
                    raise Exception
            except:
                code = 8493
                status = False
                message = "Please enter valid description (3-1000 characters)"
                raise Exception
            try:
                minimumQualification = jsonBody['minimumQualification']
                if minimumQualification == None or minimumQualification == "" or len(minimumQualification) < 3 or len(minimumQualification) > 30:
                    raise Exception
            except:
                code = 8493
                status = False
                message = "Please enter valid minimum qualification (3-30 characters)"
                raise Exception
            try:
                preferredQualification = jsonBody['preferredQualification']
                if preferredQualification == None or preferredQualification == "" or len(preferredQualification) < 3 or len(preferredQualification) > 30:
                    raise Exception
            except:
                code = 8493
                status = False
                message = "Please enter valid preferred qualification (3-30 characters)"
                raise Exception
            try:
                salary = int(jsonBody['salary'])
                if salary == None or salary <= 0:
                    raise Exception
            except:
                code = 8493
                status = False
                message = "Please enter valid salary"
                raise Exception
            try:
                location = jsonBody['location']
                if location == None or location == "" or len(location) < 3 or len(location) > 30:
                    raise Exception
            except:
                code = 8493
                status = False
                message = "Please enter valid location (3-30 characters)"
                raise Exception
            try:
                remoteJob = jsonBody['remoteJob']
                if remoteJob not in [True, False]:
                    raise Exception
            except:
                code = 8493
                status = False
                message = "Please enter valid option for remote job"
                raise Exception
            jobs.insert_one(
                {
                    "designation": designation,
                    "companyName": companyName,
                    "description": description,
                    "minimumQualification": minimumQualification,
                    "preferredQualification": preferredQualification,
                    "salary": salary,
                    "location": location,
                    "remoteJob": remoteJob,
                    "active": True
                }
            )
            code = 2000
            status = True
            message = "Job has been posted"
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
        try:
            jobsList = jobs.find({"active": True})
            async for i in jobsList:
                i['_id'] = str(i['_id'])
                result.append(i)
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
