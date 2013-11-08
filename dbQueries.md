HW7 :: Databases
==================

- Student : _Shreyas_
- Email: _shreyas@ischool.berkeley.edu_

## Accessing Database

```
$ mysql -h localhost -u i253

mysql> SHOW DATABASES;
mysql> USE i253;
mysql> SHOW TABLES;
mysql> SELECT * FROM LINKS;
```


## HW Questions

### `SELECT`
- How many links were added afer 2013-10-14?

##### Query

```
SELECT COUNT(links.created) FROM links WHERE links.created > '2013-10-14';
```

##### Result
```
13
```

- How many links that were added before 2013-10-14 have fewer than 40 hits

##### Query 
```
SELECT COUNT(links.created) FROM links WHERE links.created > '2013-10-14' AND links.hit_count < 40;
```

##### Result
```
4
```


### `INSERT`

- Insert your own URL with a date before 2013-10-14 with greater than 40 hits


##### Query

```
INSERT 
    INTO links (long_url, short_url, hit_count, created) 
    VALUES ('http://github.com/seekshreyas', 'http://sshr.co', 0, '2012-10-14');
SELECT * FROM links WHERE (links.short_url='http://sshr.co');
```

##### Result
```
+-------------------------------+----------------+-----------+------------+
| long_url                      | short_url      | hit_count | created    |
+-------------------------------+----------------+-----------+------------+
| http://github.com/seekshreyas | http://sshr.co |         0 | 2012-10-14 |
+-------------------------------+----------------+-----------+------------+

1 row in set (0.01 sec)
```


- Is it possible that someone querying the database at the same time could see your insert partially complete (eg. only see some fields filled in)? What database property is this related to?
    - __No__. Its not possible that someone else can see my entry partially entered in the database. This is related to the `Atomicity` property of DATABASES from `A(tomicity) C(onsistency) I(solation) D(urability)`, which relates to __ALL__ or __NOTHING__ property of databases. This means either the whole transaction will complete or the entire transaction would be rolled back in case of partial fail.


### `UPDATE`
- Insert your own URL with a date before 2013-10-14 with greater than 40 hits


##### Query

```
INSERT 
    INTO links (long_url, short_url, hit_count, created) 
    VALUES ('http://github.com/seekshreyas', 'http://sshr.co', 0, '2012-10-14');
SELECT * FROM links WHERE (links.short_url='http://sshr.co');
```

##### Result
```
+-------------------------------+----------------+-----------+------------+
| long_url                      | short_url      | hit_count | created    |
+-------------------------------+----------------+-----------+------------+
| http://github.com/seekshreyas | http://sshr.co |         0 | 2012-10-14 |
+-------------------------------+----------------+-----------+------------+

1 row in set (0.01 sec)
```

### `UPDATE`
- Increment the hit_count for only your new row. What is the new count?

##### Query
```
UPDATE links SET links.hit_count = links.hit_count + 1 WHERE (links.short_url='http://sshr.co');
SELECT * FROM links WHERE (links.short_url='http://sshr.co');
```
##### Result
```
+-------------------------------+----------------+-----------+------------+
| long_url                      | short_url      | hit_count | created    |
+-------------------------------+----------------+-----------+------------+
| http://github.com/seekshreyas | http://sshr.co |         3 | 2012-10-14 |
+-------------------------------+----------------+-----------+------------+
1 row in set (0.00 sec)
```

