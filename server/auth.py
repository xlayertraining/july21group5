from common import *


class SecureHeader():
    async def decrypt(Authorization):
        try:
            Authorization = Authorization.split()
            firstPart = Authorization[0]
            secondPart = Authorization[1]
            if firstPart != "Bearer":
                raise Exception
            userAccountId = jwt.decode(
                secondPart, "icfai", algorithms=["HS256"])
            accFind = await users.find_one(
                {
                    "_id": ObjectId(userAccountId['key'])
                }
            )
            print(accFind)
            if accFind == None:
                raise Exception
            else:
                return str(accFind['_id'])
        except:
            return None
