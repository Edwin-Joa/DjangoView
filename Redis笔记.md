### 计算机的存储

- 永久存储 —— 磁盘 —— 断电不会丢失数据，IO慢(数据读写慢)
- 缓存 —— 内存条 —— 断电丢失数据，IO快(读写很快)

### 数据库存储

- 永久存储库：Mysql.....
- 缓存库：Redis缓存数据(用它来做缓存，该数据库也可以永久保存数据)

缓存的时候场景：

1、打车软件的坐标数据，使用的就是缓存！凡事无需永久存储的时候，且该数据频繁被添加和读取；

2、给永久存储数据库，架设缓存层，来提高数据的读取的效率；



### Redis安装！

#### 1、使用包管理工具安装

ubuntu里`apt-get`就是包管理工具，官网提供的快速安装应用的工具；

Mac里`brew`;

RedHat里`yum `;

```shell
sudo apt-get install redis-server

# 1、默认配置文件路径
/etc/redis/redis.conf
# 2、包管理工具默认可执行程序存储的路径有些应用安装路径是在/usr/bin/
/usr/local/bin/redis-server
/usr/local/bin/redis-cli
```

#### 2、自定义线下安装（安装包安装）

```shell
# 1、下载安装包(选择3.0.6版本)：http://download.redis.io/releases/
# 2、把安装包压缩文件拷贝到ubuntu虚拟机桌面目录下并解压解压安装包
cd ~/Desktop
tar -zxvf redis-3.0.6.tar.gz
# 3、进入解压后的安转包目录
cd redis-3.0.6
# 4、自己阅读安装目录下的README和INSTALL文件(一般的安装包都提供该文件，用于说明安装和使用步骤的)
# 5、编译c/c++语言源码
sudo make
# 6、把编译之后的可执行文件放入指定标准安装目录中
sudo make install
# 7、把默认提供的配置文件，拷贝到标准目录中
sudo cp ./redis.conf /etc/redis/

# 补充：redis线下安装的源码和编译获取的可执行程序，都在src目录中；
```

### redis基本操作

```python
# 指定配置文件启动redis
sudo redis-server /etc/redis/redis.conf
# 关闭redis服务器
redis-cli -h 127.0.0.1 -p 6379 shutdown
```

### redis指令操作

#### 1、字符串类型

```shell
# 设置键值对
set <key> <value>
# 获取一个key的值
get <key>

# 设置键值对的同时指定有效期
setex <key> <有效期,秒> <value>

# 一次设置多个键值对
mset <key1> <value1> <key2> <value2> .... <keyN> <valueN>
# 一次获取多个键的值
mget <key1> <key2> ... <keyN>

# 查看当前库有哪些key
# 此处正则只支持“*”、“[]”和“?”三种；
# “*”匹配任意字符
# “[]”匹配指定字符
# “?”匹配任意一个字符
keys <正则表达式>
```

#### 2、hash类型数据操作

```python
# 新建只有一个属性的哈希
hset <key> <field> <value>
# 新建有多个属性的哈希
hmset <key> <field1> <value1> <field2> <value2> ...

# 获取一个哈希的所有键
hkeys <key>
# 获取一个哈希的一个属性值
hget <key> <field>
# 获取一个哈希的多个属性值
hmget <key> <field1> <field2>...
# 删除一个哈希中的属性
hdel <key> <field1> <field2>...
# 注意：如果使用"del <key>"命令会把整个哈希删除
```

#### 3、list列表类型数据操作

```python
# 列表左侧插入
lpush <key> <value1> <value2>...
# 列表右侧插入
rpush <key> <value1> <value2>...
# 列表指定位置插入(在xxx之前插入)
linsert <key> before <xxx> <value>
# 列表指定位置插入(在xxx之后插入)
linsert <key> after <xxx> <value>

# 列表成员获取
# 整数代表下表，和python列表下标类似
# 索引从左侧开始，第⼀个元素为0
# 索引可以是负数，表示从尾部开始计数，如-1表示最后⼀个元素
lrange <key> 0 -1 # [0,-1]获取所有
lrange <key> 0 2 # [0,2]获取下标0,1,2三个值

# 修改指定下标位置的值
lset <key> <index> <新值>

# 删除列表中的一个成员
# 1、其中count为0，代表删除所有相同的值
# 2、其中count为n(正整数),代表从左到右遍历删除相同的值
# 3、其中count为-n(负整数),代表从右到左遍历删除相同的值
lrem <key> <count> <value>

# 列表的截取
# 截取下标[start,end]范围类的数据
# 注意：直接操作原列表；
ltrim <key> <start> <end>
```

#### 4、set集合类型

特征：

- 成员无序
- 值的类型为string
- 成员不能重复，具备唯一性
- 集合成员没有修改操作

```python
# 添加集合成员
sadd <key> <member1> <member2> <member3>...
# 查看集合中的所有成员
smembers <key>
# 删除指定成员
srem <key> <member>
```

#### 5、zset有序集合

所谓有序集合，就是在原有集合set基础上，给每一个成员添加一个**分值/权重值**来记录每个成员的顺序！

- 使用分值/权重值记录顺序，故有序
- 成员数据类型为string
- 成员唯一
- **分值/权重值**是一个浮点数

```python
# 添加成员
zadd <key> <score1> <member1> <score2> <member2> ...

# 根据下标获取有续集成员
# 默认有序集合顺序是按照分值生序排列
# 以下，获取[start, stop]下标范围内的成员
# 索引从左侧开始，第⼀个元素为0
# 索引可以是负数，表示从尾部开始计数，如-1表示最后⼀个元素
zrange <key> <start> <stop>

# 返回分值范围内的成员： min_scoer <= 分值 <= max_score
zrangebyscore <key> <min_score> <max_score>

# 删除指定成员
zrem <key> <member1> <member2> ...
# 删除指定分值范围内的成员
zremrangebyscore <key> <min_score> <max_score>
```

### Redis的python客户端的使用

```python
from redis.client import StrictRedis

# 1、新建客户端链接对象
conn = StrictRedis(
	host='127.0.0.1',
  port=6379
)

# 2、通过客户端对象中的实例方法对redis进行增删改查操作
# set name weiwei
conn.set("name", "weiwei")
# get name
conn.get("name")
# zadd book_count 99 西游记 88 红楼梦 77 三国演义
# 注意：在较新的redis客户端版本中，有续集的新增操作中，成员及分值是以python字典形式传入函数中 —— 成员为key，分值为value
conn.zadd("book_count", {"西游记":99, "红楼梦":88, "三国演义":77})
```





