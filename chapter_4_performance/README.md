## CHAPTER 4: PERFORMANCE ##

### HANDOUTS ###

Using indexes, monitoring and understanding performance. Performance in sharded environments.

### HOMEWORK ANSWER ###

- [HOMEWORK: HOMEWORK 4.1](hw4-1.md)

- [HOMEWORK: HOMEWORK 4.2](hw4-2.md)


----------


- HOMEWORK: HOMEWORK 4.3

in the `blogPostDAO.py`

the function `get_posts(self, num_posts):` has a query:

	cursor = self.posts.find().sort('date', direction=-1).limit(num_posts)

so, we should creat an index on the `date`

	> db.posts.ensureIndex({ date: -1})

the function `get_posts_by_tag(self, tag, num_posts)` has a query:

	cursor = self.posts.find({'tags':tag}).sort('date', direction=-1).limit(num_posts)

so, we should creat an index on the `tag`

	> db.posts.ensureIndex({ tags: 1})

the function `get_post_by_permalink(self, permalink)` has a query:

	post = self.posts.find_one({'permalink': permalink})

so, we should create an index on the `permalink`

	> db.posts.ensureIndex({ permalink: 1}, {unique: true})

however, when we run `python validate.py`, it point out that:

	…
	Sorry, executing the query to retrieve posts by tag is too slow.
	We should be scanning no more than 10 documents. You scanned 13
	…
so we should add an index on `tag` and `date`

	db.posts.ensureIndex( { tags:1, date: -1})



    
- HOMEWORK: HOMEWORK 4.4

In this problem you will analyze a profile log taken from a mongoDB instance. To start, please download sysprofile.json from Download Handout link and import it with the following command:

	mongoimport -d m101 -c profile < sysprofile.json

Now query the profile data, looking for all queries to the students collection in the database school2, sorted in order of decreasing latency. What is the latency of the longest running operation to the collection, in milliseconds?

<!-- -->

	> db.profile.find({ op:"query", ns:/school2.students/}).sort({ millis: -1}).limit( 1)
	{ "_id" : ObjectId("531604231f113c79eae77957"), "ts" : ISODate("2012-11-20T20:09:49.862Z"), "op" : "query", "ns" : "school2.students", "query" : { "student_id" : 80 }, "ntoreturn" : 0, "ntoskip" : 0, "nscanned" : 10000000, "keyUpdates" : 0, "numYield" : 5, "lockStats" : { "timeLockedMicros" : { "r" : 19776550, "w" : 0 }, "timeAcquiringMicros" : { "r" : 4134067, "w" : 5 } }, "nreturned" : 10, "responseLength" : 2350, "millis" : 15820, "client" : "127.0.0.1", "user" : "" }