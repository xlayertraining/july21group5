from common import *
from auth import *


class ProfileHandler(tornado.web.RequestHandler):
    async def post(self):
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
                jsonBody = json.loads(self.request.body.decode())
            except:
                code = 4732
                status = False
                message = "Invalid JSON Body"
                raise Exception
            # Fields will be firstName, lastName, phoneNumber, emailAddress and password sent from front end.
            try:
                # if in case no variable named firstName was sent, this will be None(null)
                firstName = jsonBody.get('firstName')
                if firstName == None:
                    raise Exception
                if len(firstName) < 3 or len(firstName) > 20:
                    raise Exception
                firstName = firstName.title()
            except:
                code = 9033
                status = False
                message = "Please submit valid first name(3-20 characters)"
                raise Exception
            try:
                lastName = jsonBody.get('lastName')
                if lastName == None:
                    raise Exception
                if len(lastName) < 3 or len(lastName) > 20:
                    raise Exception
                lastName = lastName.title()
            except:
                code = 9033
                status = False
                message = "Please submit valid first name(3-20 characters)"
                raise Exception
            try:
                qualification = jsonBody.get('qualification')
                if qualification == None:
                    raise Exception
                if len(qualification) < 2 or len(qualification) > 30:
                    raise Exception
            except:
                code = 9033
                status = False
                message = "Please submit valid qualification(2-30 characters)"
                raise Exception
            try:
                cgpa = jsonBody.get('cgpa')
                if cgpa not in range(1, 10):
                    raise Exception
            except:
                code = 9033
                status = False
                message = "Please submit valid CGPA"
                raise Exception
            try:
                location = jsonBody.get('location')
                if location == None:
                    raise Exception
                if len(location) < 2 or len(location) > 30:
                    raise Exception
            except:
                code = 9033
                status = False
                message = "Please submit valid location(2-30 characters)"
                raise Exception
            accFind = await users.find_one({"_id": ObjectId(account_id)})
            if accFind:
                await users.update_one(
                    {
                        "_id": ObjectId(account_id)
                    },
                    {
                        "$set": {
                            "firstName": firstName,
                            "lastName": lastName
                        }
                    }
                )
                await profile.update_one(
                    {
                        "accountId": account_id
                    },
                    {
                        "$set": {
                            "accountId": account_id,
                            "qualification": qualification,
                            "location": location,
                            "cgpa": cgpa
                        }
                    }, upsert=True
                )
                code = 2000
                status = True
                message = "Profile has been updated"
            else:
                code = 4004
                status = False
                message = "User not found"
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
            accFind = await users.find_one({
                "_id": ObjectId(account_id)}
            )
            if accFind:
                qualification = ""
                cgpa = ""
                location = ""
                proFind = await profile.find_one({
                    "accountId": account_id
                }
                )
                if proFind:
                    qualification = proFind['qualification']
                    location = proFind['location']
                    cgpa = proFind['cgpa']
                v = {
                    "firstName": accFind['firstName'],
                    "lastName": accFind['lastName'],
                    "qualification": qualification,
                    "location": location,
                    "cgpa": cgpa
                }
                result.append(v)
            if len(result):
                code = 2000
                status = True
                message = "Profile Information"
            else:
                code = 9043
                status = False
                message = "Profile not found"
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
