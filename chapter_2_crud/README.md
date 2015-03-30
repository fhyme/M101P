## CHAPTER 2: CRUD ##

### HANDOUTS ###
CRUD (Creating, Reading and Updating Data) - Mongo shell, query operators, update operators and a few commands

### HOMEWORK ANSWER ###

- HOMEWORK: HOMEWORK 2.1
<!-- -->
    mongoimport -d students -c grades < grades.json
    use students
    db.grades.find({"type":"exam","score":{$gte:65}}).sort({"score":1}).limit(1)

- HOMEWORK: HOMEWORK 2.2
<!-- -->
    python hw2-2.py
    db.grades.aggregate({'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1})

- HOMEWORK: HOMEWORK 2.3

int the `userDAO.py`

    user = self.users.find_one({'_id': username})

    self.users.insert(user)

there are something wrong in the `sessionDAO.py`

> self.sessions.insert_one(session)

should be changed to

    self.sessions.insert(session)

> self.sessions.delete_one({'_id': session_id})

should be changed to

    self.sessions.remove({'_id': session_id})