```
20200417-Python-就业班-直播课

黑马Python就业3期（20200417）-5月18日-晚自习

授课资料网盘地址：
百度盘：链接:https://pan.baidu.com/s/1FX74k3t7C7gRuIvkvXMLzA  密码:cqve
360盘：https://yunpan.360.cn/surl_yYdmCGwuJuX (提取码:c6fe)
```

```
NoSQL介绍
	泛指非关系型数据库，使用key-value数据模型保存数据，不支持关系型SQL语法。
	具备结构简单、易扩展、大数据量、高性能的特点。

Redis介绍
	属于NoSQL的一种，具备NoSQL的特性，使用key-value保存数据。
	是一个开源的，内存型的数据结构存储系统，可以用作数据库、缓存和消息中间件。
	可以存储字符串(strings)，散列(hashes)，列表(lists)，集合(sets)，有序集合(sorted sets)
```

```
Redis的配置和管理
	1. 提示：
        为什么学习时需要自己去配置和管理Redis?
        因为学习时，没有运维工程师
        学习时，自己是前后端、产品经理、测试、运维程序员
	2. 配置
        配置文件位置：/etc/redis/redis.conf
        编辑配置文件：sudo vim /etc/redis/redis.conf
        建议修改项：
			注释掉bind：# bind 127.0.0.1
			关闭保护模式：protected-mode no
			后台运行：daemonize yes
		重启redis：
			查看进程pid：ps aux | grep redis-server
			杀掉进程：sudo kill -9 pid
			启动redis：sudo redis-server /etc/redis/redis.conf
	3. 管理
        必须先开启服务端：
			先查看服务端是否开启：ps aux | grep redis-server
			如果服务端已开启就不管
			如果没有开启就开启：sudo redis-server /etc/redis/redis.conf
		然后再使用redis-cli登录到redis-server
			使用默认的IP和端口访问：
				redis-cli
			使用真实IP访问：
				redis-cli -h ubuntu真实IP
```

```
Redis支持的数据结构
0. Redis的数据模型是：key-value

value可以是以下这些类型
1. String：字符串
2. hash：散列、hash表
3. list：列表
4. set：无序集合
5. zset：有序集合

1. String：字符串
	value ===> "n74y23847yshcb"
	"key": "n74y23847yshcb"
2. hash：散列、hash表
	value ===> field val
	value ===> "name" "zxc"
	"key": "name" "zxc"
3. list：列表
	value ===> "1" "2" "3"
	"key": "1" "2" "3"
4. set：无序集合
	vlaue ===> "1" "2" "3"
	"key": "1" "3" "2"
5. zset：有序集合
	vlaue ===> "1" score "2" score "3" score
	"key": "1" score "2" score "3" score
```

```
Redis也是支持  增删改查

String类型
	set：一次保存一个键值
		set key value
	mset：一次保存一个键值或者多个键值
		mset key1 value1 key2 value2 [key3 value3 ......]
	get：一次读取一个键值
		get key value
	mget：一次读取一个键值或者多个键值
		mget key1 key2 [key3 ......]
	setex：存储带有有效期的字符串
		setex key seconds value
		
键命令
	keys：获取当前库中所有的key
		keys pattern (keys *)(keys n*)(keys *n)(keys n*m)
	del：删除整条记录(很危险，慎用)
		del key1 key2 [key3 ......]
	expire：给已有的key追加过期时间的
		expire key seconds
	提示：所有的键命令都适用于所有的数据类型。

Hash类型：用于存储对象结构的数据，比如，存储一个用户的信息，包含用户名和密码
	hset：一次保存一个键值
		hset key field value
	hmset：一次保存多个键值
		hmset key field1 value1 field2 value2 [field3 value3 ......]
	hget：一次获取一个键值
		hget key field
	hmget：一次获取多个键值
		hmget key field1 field2 [field3 ......]
	hgetall：获取该记录所有的数据 {field1 value1 field2 value2 [field3 value3 ......]}
		hgetall key 
	hdel：删除field对应的value
		hdel key field1 field2 [field3 ......]
		
List类型
	提示：命令不要记，分析需求是重点，根据分析的结果得出要保存的数据的类型，最后再去选择命令。
	使用场景：对数据进行排序和存储时，或者如果希望最后添加的数据在最前（浏览记录），可以选择List类型
	lpush：从左向右压入数据的，数据加入的顺序正好保存的顺序是相反的
		lpush key value1 value2 [value3 ......]
	rpush：从右向左压入数据的，数据加入的顺序正好保存的顺序是相同的
		rpush key value1 value2 [value3 ......]
	lrange：根据索引读取列表数据的，0索引表示第一个(最开始的)，-1索引表示最后一个(最末尾的)
		索引可以为负数，如果为负数，表示从末尾往前查数据
		lrange key start stop
	lrem：删除指定的元素
    	lrem key count value
    	count > 0: 从头往尾移除
    	count < 0: 从尾往头移除
    	count = 0: 移除所有(添加数据前的去重)
    	A B A B B
    	移除最后两个B
    	lrem key -2 B
    	如果要移除所有的B
    	lrem key 0 B
 
Set集合(无序集合)
	说明：元素具有唯⼀性，不重复，自动去重(跟list不同)
	说明：对于集合没有修改操作，因为不知道怎么取到要改的数据(跟list不同)
	使用场景：如果遇到保存一列数据，没有顺序要求，不重复和不修改，可以选择使用无序集合
	sadd：添加元素，保存的顺序和添加的顺序可能会不同
		sadd key member1 member2 [member3 ......]
	smembers：获取元素
		smembers key 
		返回值：[member1 member2 member3 ......]
	srem：删除元素
		srem key member1 member2 [member3 ......]

Zset集合(有序集合：根据权重由小到大排序的)
	说明：元素具有唯⼀性，不重复，自动去重(跟list不同)
	说明：对于集合没有修改操作，因为不知道怎么取到要改的数据(跟list不同)
	使用场景：如果遇到保存一列数据，有顺序要求，不重复和不修改，可以选择使用有序集合
	zadd：添加元素
		zadd key score1 member1 [score2 member2 ......]
	zrange：根据角标获取元素
		zrange key start stop
	zrangebyscore：根据权重获取元素
		zrangebyscore key min max
	zrem：删除元素
		zrem key member1 [score2 member2 ......]
```

```
1. 以下关于NoSQL的描述正确的是：ACD（多选）
A：NoSQL使用Key-Value数据模型存取数据。
B：NoSQL可以使用关系型数据库的API。
C：NoSQL数据结构简单、易扩展，性能好。
D：Redis属于NoSQL的一种，具备NoSQL的特点。
```

```
2. 以下关于Redis的描述正确的是：ABCD（多选）
A：Redis中的数据会存储在内存中。
B：Redis使用Key-Value数据模型存取数据。
C：Redis可以用作数据库、缓存和消息中间件。
D：Redis读写性能极高。
```

```
3. 以下关于Redis的配置描述正确的是：ABCD（多选）
A：Redis默认端口号为6379。
B：Redis配置文件名为：redis.conf。
C：Redis以守护进程运⾏的配置方式为：daemonize yes。
D：Redis默认只有16个库。
```

```
4. 以下关于Redis操作String的命令中可以同时设置多个键值的命令是：C（单选）
A：set。
B：mget。
C：mset。
D：setex。
```

```
5. 以下关于Redis操作Hash的命令中可以同时设置多个键值的命令是：B（单选）
A：hset。
B：hmset。
C：hmget。
D：hvals。
```

```
6. 以下关于Redis操作List的命令中可以保证最后添加的数据在最前面的命令是：B（单选）
A：rpush。
B：lpush。
C：linsert。
D：lset。
```

```
7. 已知List数据：history [a b c d b c]
以下关于Redis操作List的命令中可以删除所有的b的命令是(其他数据依然保留)：ABC（多选）
A：lrem history 2 b。
B：lrem history -2 b。
C：lrem history 0 b。
D：lrange history 0 b。
```

```
8.以下关于Redis中的Set和Zset的描述正确的是：AB（多选）
A：Set和Zset中都可以自动去重。
B：Set和Zset中都没有修改操作。
C：Set和Zset中获取数据的命令都是smembers。
D：Set和Zset中都可以排序。
```

