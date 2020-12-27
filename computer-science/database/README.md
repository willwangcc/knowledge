<h1 align="center">
<img src="https://i.imgur.com/OZiivZL.png" alt="SQL vs NoSQL" width="300"/ > <br>
Database 
</h1>

> Where do we put our things?
 
## Why 

## What 

> A database is an organized collection of data, generally stored and accessed electronically from a computer system. 
> 
> source: [wiki](https://www.wikiwand.com/en/Database)

* SQLite
* MySQL
* PostgreSQL
* Document databases e.g. MongoDB
* Graph database, e.g. Neo4j
* key-value databases, e.g. Redis
* Wide column stores, e.g. HBase

### MAKE

* [7 Database Paradigms](https://www.youtube.com/watch?v=W2Z7fbCLSTw&feature=youtu.be)
 
## Opinion 

- 90% of Web applications are database frontends. What they do to the end user might be different, how the pieces come together, It is always the same, unless one is doing curriculum driven development. 
- Yes, that is surprising to hear the first time, but it's true.
Space saving is one of the primary advantages of relational databases, the other being tracking complex data relationships. Nowadays, it's not storage that is expensive, but CPU cycles, and RDBMS are processor expensive relative to NOSQLs. I advise clients to avoid RDBMS without a very specific need for complex data relationships

## More 

1. [GraphQL](https://twitter.com/ruanyf/status/1060350454238859264) GraphQL的本质是程序员想对JSON使用SQL。
2. [YAML: probably not so great after all](https://arp242.net/weblog/yaml_probably_not_so_great_after_all.html) : YAML 格式虽然比 JSON 格式易读易写，但也有很多问题。这种格式其实很复杂，并不是配置文件的理想格式。 
Don’t get me wrong, it’s not like YAML is absolutely terrible – it’s certainly not as problematic as using JSON – but it’s not exactly great either. There are some drawbacks and surprises that are not at all obvious at first, and there are a number of better alternatives such as TOML and other more specialized formats.
3. [SQLite vs MySQL vs PostgreSQL](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems): pros, cons, when
