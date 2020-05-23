```
20200417-Python-就业班-直播课

黑马Python就业3期（20200417）-5月18日-晚自习

授课资料网盘地址：
百度盘：链接:https://pan.baidu.com/s/1FX74k3t7C7gRuIvkvXMLzA  密码:cqve
360盘：https://yunpan.360.cn/surl_yYdmCGwuJuX (提取码:c6fe)

git django redis vue 美多商城网站
vue 只需要能够听懂页面效果，和认识代码即可
vue 用于开发美多商城网站的前端页面
```

### 1. Vue.js 的概述

```
1. 作用：
	类似jQuery.js，用于开发前端的一种框架
2. 概念：
	Vue.js 是一个构建数据驱动的 web 界面的渐进式框架
	Vue.js 的目标是通过尽可能简单的 API 实现响应的数据绑定和组合的视图组件
	核心：是一个响应的数据绑定系统
3. 模式：
	遵守MVVM设计模式
	M：数据层，处理数据的
	V：视图层，处理数据渲染的
	VM：视图数据层，处理视图和数据的关联的
4. Vue的包
	https://cn.vuejs.org/v2/guide/installation.html#%E7%9B%B4%E6%8E%A5%E7%94%A8-lt-script-gt-%E5%BC%95%E5%85%A5
```

### 2. Vue的基本使用

```
1. 声明式渲染
	官网说明：
        https://cn.vuejs.org/v2/guide/#%E5%A3%B0%E6%98%8E%E5%BC%8F%E6%B8%B2%E6%9F%93

2. 使用步骤
	2.1 编写HTML
	2.2 准备<div>盒子标签
	2.3 导入Vue.js
	2.4 创建Vue对象，绑定页面，声明变量
	2.5 变量渲染HTML
	
3. 提示：
	我们现在不再和 HTML 直接交互了。
	一个 Vue 应用会将其挂载到一个 DOM 元素上 (对于这个例子是 #app) 然后对其进行完全控制。
```

```html
<body>
    <!-- 2. 定义盒子容器 -->
    <div id="app">
        <!-- 1. 编写HTML -->
        <!-- <h1>姓名</h1>
        <h1>年龄</h1> -->

        <!-- 5. 变量渲染HTML -->
        <h1>{{ username }}</h1>
        <h1>{{ age }}</h1>
    </div>

    <!-- 4. 创建Vue对象，绑定页面，声明变量 -->
    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                username: '张小厨',
                age: 18
            }
        });
    </script>
</body>
```

### 3. Vue 的基本语法

```
提示：Vue的基本语法中的指令带有前缀 v-，以表示它们是 Vue 提供的特殊 attribute。
1. 绑定属性：v-bind
2. 事件监听器：v-on
3. 条件与循环：v-if、v-for
4. 双向绑定：v-model
5. 控制标签是否展示：v-show
```

#### 3.1 绑定属性：v-bind

```
以下案例：
	<img v-bind:src="image_url" alt="图片">
	该指令的意思是：“Vue实例的 image_url 成员赋值给这个元素节点的 src 属性”。
```

```html
<body>
    <div id="app">
        <!-- <img src="" alt="图片"> -->
        <!-- <img v-bind:src="image_url" alt="图片"> -->
        <!-- v-bind的简写 -->
        <img :src="image_url" alt="图片">
    </div>

    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                image_url: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590080240482&di=38b055b891d82f734177ac5dbef579e2&imgtype=0&src=http%3A%2F%2Fimg0.imgtn.bdimg.com%2Fit%2Fu%3D3155134890%2C954358724%26fm%3D214%26gp%3D0.jpg'
            }
        });
    </script>
</body>
```

#### 3.2 事件监听器 v-on

```
为了让用户和你的应用进行交互，我们可以用 v-on 指令添加一个事件监听器。
通过它可以调用在 Vue 实例中定义的方法。
官网说明：
https://cn.vuejs.org/v2/guide/#%E5%A4%84%E7%90%86%E7%94%A8%E6%88%B7%E8%BE%93%E5%85%A5
```

```html
<body>
    <div id="app">
        <!-- <button v-on:click="btnClick">咬我呀</button> -->
        <!-- v-on的简写 -->
        <button @click="btnClick">咬我呀</button>
    </div>

    <script>
        var vm = new Vue({
            el: '#app',
            methods: {
                btnClick:function() {
                    alert("哈哈，咬不到！！！")
                }
            }
        });
    </script>
</body>
```

#### 3.3 条件与循环 v-if、v-for

```
官网说明：
	https://cn.vuejs.org/v2/guide/#%E6%9D%A1%E4%BB%B6%E4%B8%8E%E5%BE%AA%E7%8E%AF
```

```html
<!-- 条件 -->
<body>
    <div id="app">
        <div v-if="seen">现在你看到我了</div>
        <div v-else>现在你看到的是我了</div>
    </div>

    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                seen: true,
            }
        });
    </script>
</body>
```

```html
<!-- 循环 -->
<body>
    <div id="app">
        <ul>
            <li v-for="subject in subjects">{{ subject }}</li>
        </ul>
    </div>

    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                subjects: [
                    'python',
                    'java',
                    '前端'
                ]
            }
        });
    </script>
```

#### 3.4 双向绑定 v-model

```
为了保证用户交互产生的数据，可以传递到vue的数据层
官网说明：
	https://cn.vuejs.org/v2/guide/forms.html
可以用 v-model 指令在表单 <input> , <textarea> , <select> 元素上创建双向数据绑定。
```

```html
<body>
    <div id="app">
        <input type="text" v-model="username" placeholder="请输入...">
        <div>你输入的是：{{ username }}</div>
    </div>

    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                username: "",
            }
        });
    </script>
</body>
```

#### 3.5 是否展示 v-show

```
可以使用 v-show 根据具体的条件去控制当前标签是否展示
```

```html
<body>
    <div id="app">
        <input type="text" v-model="username" v-on:blur="check_username" placeholder="请输入...">
        <!-- <div>你输入的是：{{ username }}</div> -->
        <span v-show="username_error">用户名位数不够</span>
    </div>

    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                username: "",
                // 默认不展示错误信息
                username_error: false,
            },
            methods: {
                check_username:function() {
                    if (this.username.length >= 5) {
                        // 满足条件隐藏错误信息
                        this.username_error = false;
                    } else {
                        // 不满足条件展示错误信息
                        this.username_error = true;
                    }
                }
            }
        });
    </script>
</body>
```

### 4. to do list案例

```html
<body>
	<div id="app">
		<h2>To do list</h2>
		<input v-model="inputContent" type="text" id="txt1" class="inputtxt">
		<input v-on:click="fnAdd" type="button" id="btn1" class="inputbtn" value="增加">
		
		<ul id="list" class="list">
			<li v-for="(item,index) in data_list">
				<span>{{ item }}</span>
				<a @click="fnUp(index)" href="javascript:;" class="up"> ↑ </a>
				<a @click="fnDown(index)" href="javascript:;" class="down"> ↓ </a>
				<a @click="fnDel(index)" href="javascript:;" class="del">删除</a>
			</li>
		</ul>
	</div>

	<script>
		var vm = new Vue({
			el:'#app',
			data:{
				inputContent:"",
				data_list:['学习html','学习js','学习vue']
			},
			methods: {
				// 1.增加
				fnAdd:function (){
					if (!this.inputContent) {
						alert('内容不允许为空')
						return;
					}
					// 在数组末尾添加新元素
					this.data_list.push(this.inputContent);
					// 清空输入框
					this.inputContent = "";
				},
				// 2.删除
				fnDel:function (index){
					// splice(下标,个数,插入的内容)
					this.data_list.splice(index, 1)
				},

				// 3.上排序
				fnUp:function (index){
					// 根据下标获取对应的数据
					oldData = this.data_list[index]
					// 删除对应位置的数据
					this.data_list.splice(index, 1)
					// 在上一个位置插入
					this.data_list.splice(index -1, 0, oldData)
				},

				// 4.下排序
				fnDown:function (index){
					// 根据下标获取对应的数据
					oldData = this.data_list[index]
					// 删除对应位置的数据
					this.data_list.splice(index, 1)
					// 在下一个位置 插入
					this.data_list.splice(index +1, 0, oldData)
				},
			},	
		});
	</script>
</body>
```

### 5. ES6 语法

```html
提示：
	ES6 是 JavaScript 语言的新版本
	ES5 相较于 ES6 在它的基础上增加了一些语法
	在 vue 组件开发中会使用很多的 ES6 的语法，所以掌握这些常用的 ES6 语法是必须的
1. 变量声明
2. ES6 中对象的简写
3. ES6 箭头函数
```

#### 5.1 变量声明

```html
1. 提示：
	let 和 const 是ES6新增的声明变量的关键字

2. var、let、const的区别
	var：声明的是变量，有预解析功能，可以修改
	let：声明的是变量，没有预解析功能，可以修改
	const：声明的是常量，没有预解析功能，一旦赋值，不能再更改
```

```js
<script>
    /* 定义变量 */
    // var
    alert(name); // var有预解析
    var name = "zxc";
    name = "zxj";   // var可以修改
    alert(name);

    // let
    // alert(age); // let没有预解析
    let age = 18;
    age = 20;      // let可以修改
    alert(age);

    // const
    // alert(sex); // const没有预解析
    const sex = "男";
    // sex = "女";    // const不能修改
    alert(sex); 
</script>
```

#### 5.2 ES6 中对象的简写

```
提示：
	当对象中的属性和变量名一致时，对象可以使用简写的写法
```

```js
<script>
    /* 对象的简写 */
    var username = "zxc";
    var password = "123";

    // var User = {
    //     username:username,
    //     password:password
    // };
    // alert(User.username)

    // 对象的简写
    var User = {
        username,
        password
    };
    alert(User.username)
</script>
```

#### 5.3 ES6 箭头函数

```js
<script>
    /* 函数简写和箭头函数 */
    // ES5及旧版的JS函数
    function fnTest1(params) {
    	alert(params);
	}
    fnTest1("fnTest1");

    // ES6及新版的JS函数
    var fnTest2 = (params)=>{
        alert(params);
    }
    fnTest2("fnTest2");
</script>
```

```js
<script>
    /* 箭头函数和this指向 */
    // ES5及旧版的JS函数
    // var obj1 = {
    //     name: "zxc",
    //     fnTest1: function () {
    //         // 指向的是obj1
    //         alert(this);

    //         setTimeout(function () {
    //         	   // 指向的是window
    //             alert(this);
    //         }, 2000);
    //     }
    // }
    // obj1.fnTest1();

    // ES6及新版的JS函数
    var obj2 = {
        name: "zxj",
        fnTest2: function () {
            // 指向的是obj2
            alert(this);

            setTimeout(() => {
                // 指向的依然是obj2
                alert(this);
            }, 2000);
        }
    }
	obj2.fnTest2();
</script>
```

### 6. Vue实例生命周期

```
每个 Vue 实例在被创建时都要经过一系列的初始化过程——例如，需要设置数据监听、编译模板、将实例挂载到 DOM 并在数据变化时更新 DOM 等。同时在这个过程中也会运行一些叫做生命周期钩子的函数，这给了用户在不同阶段添加自己的代码的机会。

官网说明：
https://cn.vuejs.org/v2/guide/instance.html#%E5%AE%9E%E4%BE%8B%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E9%92%A9%E5%AD%90
```

```html
<body>
    <div id="app">
        <h1>{{ num }}</h1>

        <button @click="btnClick">点我吧</button>
    </div>
    
    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                num: 100
            },
            methods: {
                btnClick:function() {
                    this.num += 1;
                },
            },
            beforeCreate(){
                console.log('beforeCreate');
            },
            created(){
                console.log('created');
            },
            beforeMount(){
                console.log('beforeMount');
            },
            mounted(){
                console.log('mounted');
            },
            beforeUpdate(){
                console.log('beforeUpdate');
            },
            updated(){
                console.log('updated');
            },
            beforeDestroy(){
                // 看不到效果，因为它是在销毁
                console.log('beforeDestroy');
            },
            destroyed(){
                // 看不到效果，因为它是在销毁
                console.log('destroyed');
            }
        });
    </script>
</body>
```

### 7. Ajax-axios

```
局部刷新
官网说明：
	https://cn.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html
```

```js
<script>
    var vm = new Vue({
        el: '#app',
        data: {
        },
        mounted(){
            // 官方提供的测试地址
            var url = 'https://api.coindesk.com/v1/bpi/currentprice.json';
            axios.get(url, {})
                .then((response) => {
                	console.log(response.data);
            })
                .catch((error) => {
                	console.log(error);
            })
        },
    });
</script>
```

