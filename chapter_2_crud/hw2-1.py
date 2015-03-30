import pymongo

__author__ = 'FHY'


connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.students
result = db.grades.find({"type": "exam", "score": {"$gte": 65}}).sort([("score", 1)]).limit(1)
for r in result:
    print r