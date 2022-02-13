# Package used
MongoEngine - A proper MongoDB ODM

# Why MongoDB
1. Popular
2. Open source and free document database
3. json documents like structure - Easy to work with APIs. 
    It is displayed as json but stored as BSON.
4. Schemaless
5. we can have nested array inside json which is like pre-compiled joins. So, you do not need join hence it is faster.
6. Geo spatial support
7. Can be easily integrated with bigdata

### Limitation of MongoDB
1. If you have high number of transaction, avoid using nosql.
2. Not good for tighly coupled system.
## Ingration database
Database which is shared among multiple application
It should be avoided in NoSQL database. Instead we can have seprate database for each application and we can use some service bus to communicate with different apps.

