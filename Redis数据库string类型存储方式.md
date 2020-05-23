## Redis数据库string类型存储方式

本文介绍的是Redis数据库中string类型的存储方式，核心内容为： **`SDS`**。

#### SDS介绍

**SDS** 表示 **简单动态字符串**，全称为：`Simple Dynamic String`。

它是Redis自己封装的一种数据结构，用来操作string类型数据，且是在Redis中被广泛使用的字符串结构。

#### SDS数据类型定义

在了解Redis如何存储字符串之前，我们先来看一下Redis是如何定义SDS数据结构的类型的。

在Redis源码的`src/sds.h`文件中定义了sds数据类型，源码如下：

```C
typedef char *sds;
```

通过sds数据类型定义方式我们可以知道：

```
sds指向的类型是 char *，是这一种C语言的字符串类型。也就是说SDS和传统的C语言字符串类型是兼容的。
```

```
但是，sds和char *也并不完全等同。因为C语言字符串只能存储文本数据，不能存储二进制数据。而sds是二进制安全的，所以sds即可以保存文本数据也可以保存二进制数据。
```

补充说明：为什么C语言字符串不能保存二进制数据？

```
在C语言中，字符串是以 '\0' 字符（NULL结束符）结尾的字符数组来存储的，通常表达为字符指针的形式（char *）。它不允许 字节0 出现在字符串中间，因此，它不能用来存储任意的二进制数据。

char name[] = "itcast";
```

那么接下来，我们再来看一下，为什么sds可以保存二进制数据。

```
sds在保存字符串时，也是需要去标识字符串的结束的。但是sds标识字符串结束的方式不是通过 '\0' 字符，而是通过记录字符串的长度来实现的。记录字符串长度的字段定义在SDS数据结构的header中。
```

那么接下来，我们再来看一下，SDS数据结构中定义的header。

#### SDS数据结构定义

在Redis源码的`src/sds.h`文件中定义了SDS数据结构，封装了多种不同的header，源码如下：

```c
struct __attribute__ ((__packed__)) sdshdr5 {
	// 存储静态的短字符串（长度小于32）
    unsigned char flags; /* 3 lsb of type, and 5 msb of string length */
    char buf[];
};
// __attribute__ 是为了增强编译器检查
// __packed__ 则是告诉编译器则可能少的分配内存
struct __attribute__ ((__packed__)) sdshdr8 {
    // 字符串的长度，即已经使用的buf长度
    uint8_t len; /* used */
    // 为buf分配的总长度
    uint8_t alloc; /* excluding the header and null terminator */
    // 新增属性，记录该结构体的实际类型，标志位仅二进制后3位，前5位仅对sdshdr5结构体有用
    unsigned char flags; /* 3 lsb of type, 5 unused bits */
    // 柔性数组，为结构体分配内存的时候顺带分配，作为字符串的实际存储内存
    // 由于buf不占内存，所以buf的地址就是结构体尾部的地址，也是字符串开始的地址
    char buf[];
};
struct __attribute__ ((__packed__)) sdshdr16 {
    uint16_t len; /* used */
    uint16_t alloc; /* excluding the header and null terminator */
    unsigned char flags; /* 3 lsb of type, 5 unused bits */
    char buf[];
};
struct __attribute__ ((__packed__)) sdshdr32 {
    uint32_t len; /* used */
    uint32_t alloc; /* excluding the header and null terminator */
    unsigned char flags; /* 3 lsb of type, 5 unused bits */
    char buf[];
};
struct __attribute__ ((__packed__)) sdshdr64 {
    uint64_t len; /* used */
    uint64_t alloc; /* excluding the header and null terminator */
    unsigned char flags; /* 3 lsb of type, 5 unused bits */
    char buf[];
};
```

sds一共有5种类型的header。多种类型的header是为了能让不同长度的字符串可以使用不同大小的header。这样，短字符串就能使用较小的header，从而节省内存。

```
长度在0和2^5-1之间，选用sdshdr5的header。
长度在2^5和2^8-1之间，选用sdshdr8的header。
长度在2^8和2^16-1之间，选用sdshdr16的header。
长度在2^16和2^32-1之间，选用sdshdr32的header。
长度大于2^32的，选用sdshdr64的header。能表示的最大长度为2^64-1。
```

一个sds字符串的完整结构，两部分组成：

```
1. 一个header：
	1.1 包含字符串的长度(len)、最大容量(alloc)、标志位(flags)。sdshdr5有所不同。
	
2. 一个字符数组buf：
	2.1 这个字符数组的长度等于最大容量+1。真正有效的字符串数据，其长度通常小于最大容量。
	2.2 在真正的字符串数据之后，是空余未用的字节（一般以字节0填充），允许在不重新分配内存的前提下让字符串数据向后做有限的扩展。
	2.3 在真正的字符串数据之后，还有一个NULL结束符，即ASCII码为0的’\0’字符。这是为了和传统C字符串兼容。
	2.4 之所以字符数组的长度比最大容量多1个字节，就是为了在字符串长度达到最大容量时仍然有1个字节存放NULL结束符。

3. header内容说明：
	3.1 len：表示字符串的真正长度（不包含NULL结束符在内）。
	3.2 alloc：表示字符串的最大容量（不包含最后多余的那个字节）。
	3.3 flags：总是占用一个字节。其中的最低3个bit用来表示header的类型。
		以下定义的常量对应每一种header类型
		#define SDS_TYPE_5 0
        #define SDS_TYPE_8 1
        #define SDS_TYPE_16 2
        #define SDS_TYPE_32 3
        #define SDS_TYPE_64 4
```

了解了SDS数据结构之后，我们最后来看一下Redis是如何使用SDS数据结构存储字符串 **"itcast"** 的。

#### 存储字符串 "itcast"

```bash
127.0.0.1:6379> SET str itcast
OK
127.0.0.1:6379> GET str
"itcast"
```

```
第一步：使用键名"str"存储字符串"itcast"
第二步：使用键名"str"读取字符串"itcast"
```

```
|0x06|0x08|0x01|'i'|'t'|'c'|'a'|'s'|'t'|'\0'|'\0'填充...|'\0'|
```

```
len：0x06，表示字符串数据长度为6。
alloc：0x08，表示字符数组最大容量为128。
flags：0x01，表示SDS类型为SDS_TYPE_8，即sdshdr8。
其余的是字符串数组buf中的内容。
```

#### SDS与C语言字符串对比：

| C语言字符串                    | SDS                                  |
| ------------------------------ | ------------------------------------ |
| 只能保存文本数据               | 既能保存文本又能保存二进制数据       |
| 获取字符串长度的复杂度为O(n)   | 获取字符串长度的复杂度为O(1)         |
| 可能会造成缓冲区溢出           | 杜绝了缓冲区溢出                     |
| 修改N次字符串内存会重新分配N次 | 减少了修改字符串时内存重新分配的次数 |

#### 对比结果说明：

```
1. 常数复杂度获取字符串长度
	1.1 获取C语言字符串的长度时，程序必须遍历整个字符串对遇到的每个字符进行计数，直到遇到代表字符串结尾的空字符串为止。这个操作的复杂度为O(n)。
	1.2 SDS数据结构中的字段len记录了字符串的长度，这个操作的复杂度为O(1)。
	1.3 通过使用SDS而不是C语言字符串，这确保了字符串长度的获取的工作不会影响Redis的性能。
2. 杜绝了缓冲区溢出
	2.1 由于C语言字符串自身不记录字符串的长度，所以容易造成缓冲区溢出。
	2.2 而当SDS API需要对字符串进行修改时，首先会检查SDS的空间是否满足修改所需的空间，因为SDS自身有对字符串长度记录的字段len和记录总空间的字段alloc，可以借助这两个字段进行检查。SDS空间分配政策完全杜绝了发生缓冲区溢出的可能性。
3. 减少了修改字符串时内存重新分配的次数
	3.1 C语言字符串不记录自身长度，每次增长或者缩短字符串长度时，程序都要对这个C字符串数组进行一次内存重新分配操作，不然容易造成内存益出。
	3.2 SDS内部实现了空间预分配策略。
		当拼接字符串时，程序不仅会为SDS字符串分配拼接所需要的空间，而且还会为SDS字符串分配额外的空间。
```

#### 参考文档

```
https://github.com/charpty/redis-source-reading/tree/master/src
```

