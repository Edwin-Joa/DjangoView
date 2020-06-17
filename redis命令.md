## redis命令

---

redis 命令不区分大小写

redis支持的数据结构：redis的数据结构为：key-value

* 字符串：String
* 散列：hash
* 列表：list
* 无序集合：set
* 有序集合：zset



不同数据的数据操作：

* String
  * set

    > 如果数据存在，则为复写，如果不存在，则为添加
    >
    > 语法：set key value
    >
    > 如：set name mike

  * mset

    > 语法：mset key1 value1 key2 value2 ...

  * get key

  * mget key1 key2 ...

  * setex key second value——设定有效时长的元素

    ---

* keys
  * keys pattern——keys + 正则表达式
  
    > 如：
    >
    > keys ?
    >
    > keys a?
    >
    > keys ??c
  
  * exists key
  
    > 判断是否存在
    >
    > 如：exists a
  
  * type key
  
    > 查看key对应的value的数据类型
    >
    > 如：type abc
  
  * del key
  
    > 删除key及对应的value值
  
  * expire key second
  
    > 设置过期时间，单位为秒
    >
    > 如：expire abc 5
  
  * ttl key
  
    > 查看有效时间
    >
    > 如：ttl abc
  
  ---
  
* hash
  * hset key field value
  
    > hset key 属性名 属性对应值
    >
    > 如：hset user name mike
  
  * hget key field
  
    > hset key 属性名
    >
    > 如：hset user name
  
  * hmset key field1 value1 field2 value2 ...
  
    > 如：hmset user age 18 gender male
  
  * hmget key field1 field2 ...
  
    > 如：hmget user name age gender
  
  * hgetall key——返回key对应的所有field-value
  
    > 如：hgetall user
    >
    > 返回结果为：
    >
    > 1) "name"
    > 2) "mike"
    > 3) "age"
    > 4) "18"
    > 5) "gender"
    > 6) "male"
  
  * hdel key field1 ...
  
    > 删除key中的一个或多个指定的域
    >
    > 如：hdel user gender age
  
  ---
  
* list
  * lpush key value1 value2 ...

    > 将一个或多个value的值插入到表头
    >
    > 如：lpush name mike tom rose bill

  * rpush key value2 value2 ...

    > 将一个或多个value的值插入到表尾

  * linsert key before/after value value

    > linsert key before/after 现有value 插入的value
    >
    > 如： linsert name after bill lily

  * lrange key start stop

    > 根据start和stop下标取出value值，下标从0开始
    >
    > 如：lrange list1 0 -1

  * lrem key count value

    > count: 大于0——从左往右删count个；小于0——从右往左删count个；等于0——删除所有指定值；
    >
    > 如：lrem list3 1 a——删除从表头开始数删除一个a

  * lset key index value

    > 修改指定下标value值
    >
    > index：下标，从0开始计，如：lset list3 3 c  
    >
    > 注意： 这里的下标不等同于查询结果前面的序号，而是序号-1
    >
    > 如：lset name 6 jerry

  * ltrim key start stop

    > 对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除。
    >
    > 应用场景如，历史浏览记录

  ---

* set

  > 元素为string，无序，无重复，无修改操作

  * sadd key member1 member2 ...

    > 向集合中插入数据
    >
    > 如：sadd name mike tom rose

  * smembers key

    > 查询集合数据
    >
    > 如：smembers name

  * srem key member ...

    > 删除集合元素
    >
    > 如：srem name tom

  ---

* zset

  > 有序集合
  >
  > 元素为string类型，无重复，无修改操作
  >
  > 每个元素都会关联一个double类型的score，表示权重，通过权重从小到大排序
  
  * zadd key score1 member1 ...
  
    > zadd key 权重 元素1 权重 元素2 ...
    >
    > 如：zadd books 100 triple_kingdoms 60 red_house 120 west_trip 90 heros
  
  * zrange key start stop
  
    > 按下标计算，左一为0，右一为-1
    >
    > 如：zrange books 0 -1
  
  * zrangebyscore key min max
  
    > 按权重获取
    >
    > 如：zrangebyscore books 100 200
  
  * zscore key member
  
    > 获取权重值
    >
    > 如：zscore books triple_kingdoms
  
  * zrem key member1 member2 ...
  
    > 
  
  * zremrangebyscore key min max
  
    > 删除指定权重范围的元素



---



## redis 在Python中的使用

1. pip3安装redis

   > sudo pip3 install redis

2. 使用StricRedis对象创建redis数据库的连接实例对象

   > from redis import StrictRedis

3. 创建实例对象

   > conn = StrictRedis(host='localhost',port=6379,db=0)
   >
   > 默认参数为上：若使用默认参数
   >
   > 可以简写为：conn = StrictRedis()

4. 使用实例对象对redis数据库进行指定操作

   

