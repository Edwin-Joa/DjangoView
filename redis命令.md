## redis命令

---



redis支持的数据结构：redis的数据结构为：key-value

* 字符串：String
* 散列：hash
* 列表：list
* 无序集合：set
* 有序集合：zset



不同数据的数据操作：

* String
  * set:如果数据存在，则为复写，如果不存在，则为添加
    * 语法：set key value
    * 如：set name mike
    
  * mset:语法：mset key1 value1 key2 value2 ...
  
  * get key
  
  * mget key1 key2 ...
  
  * setex key second value——设定有效时长的元素
  
    ---
  
* keys
  * keys pattern——keys + 正则表达式
  * exists key
  * type key
  * del key
  * expire key
  * ttl key
  
  ---
  
* hash
  * hset key field value
  * hget key field
  * hmset key field1 value1 field2 value2 ...
  * hmget key field1 field2 ...
  * hgetall key——返回key对应的所有field-value
  * hdel key field1 ...——删除key中的一个或多个指定的域
  
  ---
  
* list
  * lpush key value1 value2 ...——将一个或多个value的值插入到表头
  
  * rpush key value2 value2 ...——将一个或多个value的值插入到表尾
  
  * lrange key start stop——根据start和stop下标取出value值，下标从0开始
    
    * 如：lrange list1 0 -1
    
  * lrem key count value
    
    * count: 大于0——从左往右删count个；小于0——从右往左删count个；等于0——删除所有指定值；
    
    * 如：lrem list3 1 a——删除从表头开始数删除一个a
    
  * lset key index value
  
    * index：下标，从0开始计，如：lset list3 3 c  
  
  ---
  
* set:元素为string，无序，无重复，无修改操作

  * sadd key member1 member2 ...
  * smembers key
  * srem key member ...

  ---

* zset:有序集合，元素为string类型，无重复，每个元素都会关联一个double类型的score，表示权重，通过权重从小到大排序，无修改操作

  * zadd key score1 member1 ...
  * zrange key start stop——按下标计算，左一为0，右一为-1
  * zrangebyscore key min max——按权重获取
  * zscore key member——获取权重值
  * zrem key member1 member2 ...
  * zremrangebyscore key min max——删除指定权重范围的元素