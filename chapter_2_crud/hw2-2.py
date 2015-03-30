import pymongo

__author__ = 'FHY'


connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.students
result = db.grades.find({"type": "homework"}).sort([("student_id", 1), ("score", 1)])
sid = -1
for r in result:
    if sid != r["student_id"]:
        sid = r["student_id"]
        print r
        db.grades.remove({"_id": r["_id"]})
