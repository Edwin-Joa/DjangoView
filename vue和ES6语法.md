## Vue.js

用于开发前端页面

jQuery和vue一样都是用于开发前端

不同点：

* jQuery面向过程多一些，即使jQuery里面也有对象
  * 操作标签属性：先获取标签，再操作属性；
  * 操作内容：先获取标签，在准备内容，最后写入到html
* Vue.js面向封装多一些
  * 将数据直接绑定到页面，控制数据从而刷新页面
  * 组件，即对标签的封装，提高复用性

---

***遵循MVVM设计模式***



---

1. Vue基本使用：

   * 导包：

     ```html
     方法1. 本地导入
     <script src='vue.js'></script>
    
     方法2.远程导入
     ```
  <script src='导入地址'></script>
     ```

   * 创建vue对象：
   
     ```html
     window.onload = function (){
     	var vm = new Vue(){
     		// 绑定操作对象
     		el: '#app',
     		data:{
     			'content':'Python37期'
     ```

    		}
     	}
    };
     ```

   * 创建容器与对象进行关联
   
     ```html
     
     ```
  <div id='app'>
     	<img src='' alt='图片'>
     </div>
     ```

   


   如：vue操作数据

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Vue的使用</title>
       <script src="./js/vue.js"></script>
       <script>
           window.onload= function(){
               var vm = new Vue({
                   el:'.box',
                   data: {
                       content:'vue的基本使用'
                   }
               })
           }
       </script>
   </head>
   <body>
       <div class='box'>{{content}}</div>
   </body>
   </html>
   ```

   

---

2. Vue基本语法：
   * 增加标签数据：
   
     > {{变量名}}
   
     ```html
     <script>
     	window.onload=function(){
             var vm = new Vue({
                 el:'#box',
                 data:{
                     content:'vue操作数据',
                     linkdata:'百度连接',
                     url:'http://www.baidu.com'
                 }
             })
         }
     </script>
     
     
     <body>
         <div id='box'>
             <a v-bind:href='url'>{{linkdata}}</a>
             <p>
                 {{content}}
             </p>
         </div>
     </body>
     ```
   
     
   
   * 修改标签属性
   
     > <标签 v-bind:属性='属性值'></标签>
   
     如：
   
     ```html
      <a v-bind:href='url'>{{linkdata}}</a>
     ```
   
     
   
   * 给标签增加方法
   
     > 语法：<标签 v-on:事件名='调用的函数名'></标签>
     >
     > 简写：<标签 @事件名='调用的函数名'></标签>
   
     如：
   
     ```html
     <script>
     	window.onload=function(){
             var vm2=new Vue({
                     el:'#meth',
                     data:{
                         count:1
                     },
                     methods:{
                         fnclickbutton:function(){
                             this.count +=1
                         }
                     }
                 })
         }
     </script>
     
     <div id='meth'>
         <p>-{{count}}s</p>
         <button @click='fnclickbutton'>+1s</button>
     </div>
     ```
   
     

---



3. 条件渲染：

   * v-if=

     > v-if='' 
     >
     > v-if='true/false', 如果为true，则标签内容会被渲染，否则不会渲染

     如：

     ```html
     check:function(count){
                             if (this.count>=10){
                                 return true
                             } else {
                                 return false
                             }
                         }
     
     <p v-if='check(this.count)'>
             <img src="/home/ubuntu/Desktop/Opencv/vuecode/下载.jpeg" alt="">
             <img src="/home/ubuntu/Desktop/Opencv/vuecode/1f434.png" alt="">
             <img src="/home/ubuntu/Desktop/Opencv/vuecode/$.png">
             <img src="/home/ubuntu/Desktop/Opencv/vuecode/下载 (1).jpeg" alt="">
     </p>
     ```

   * v-else

     > v-else必须跟在v-if或v-else-if后面，否则将不会被识别

     如：

     ```html
     <div v-if="Math.random() > 0.5">
       Now you see me
     </div>
     <div v-else>
       Now you don't
     </div>
     ```

   * v-else-if

     > v-else-if同v-else一样，必须紧跟v-if或v-else_if之后，否则不会被识别

     如：

     ```html
     <p v-if='type=="A"'>
         A
     </p>
     <p v-else-if='type=="B"'>
         B
     </p>
     <p v-else>
         not A, B
     </p>
     ```

   * v-show

     > 其用法同v-if
     >
     > v-show 和 v-if
     >
     > 区别：
     >
     > 1. v-if 是“真正”的条件渲染，因为它会确保在切换过程中条件块内的事件监听器和子组件适当地被销毁和重建。
     >
     > 2. v-if 也是惰性的：如果在初始渲染时条件为假，则什么也不做——直到条件第一次变为真时，才会开始渲染条件块。
     >
     > 3. 相比之下，v-show 就简单得多——不管初始条件是什么，元素总是会被渲染，并且只是简单地基于 CSS 进行切换。
     >
     > 一般来说，v-if 有更高的切换开销，而 v-show 有更高的初始渲染开销。因此，如果需要非常频繁地切换，则使用 v-show 较好；如果在运行时条件很少改变，则使用 v-if 较好。

---



4. 列表渲染：v-for=''
   * 列表渲染

     * 普通列表

       > itemlist = [1,2,3,4,5]
       >
       > <li v-for='i in itemlist'>{{i}}</li>

     * 获取下标和列表元素

       > indexlist:['a','b','c','d']
       >
       > <li v-for='(item,index) in indexlist'>下标：{{index}}==>数值：{{item}}</li>

   * 字典渲染

     > <li v-for='i in objdata'>{{i}}</li> 
     >
     > <li v-for='(value,key) in objdata'>属性值：{{value}}==>属性名：{{key}}</li>
     >
     > <li v-for='obj in objlist'>属性值1:{{obj.name}}==属性值2:{{obj.age}}</li>

---



5. 双向绑定数据： v-model=''

   * 单行文本框绑定

     ```html
     var vm5 = new Vue({
                     el:'#bind',
                     data:{
                         message:''
                     }
                 })
     
     <div id="bind">
         <input type="text" v-model="message">
     <p>单行内容为：{{message }}</p>
     </div>
     ```

     

   * 多行文本框绑定

     > 同单行绑定

   * 单选框绑定

     ```html
     var vm5 = new Vue({
                     el:'#bind',
                     data:{
                         message:'',
                         textarea:'',
                         gender:''
                     }
                 })
     
     <input type="radio" name="sex" id="" value="男" v-model='gender'>男
         <input type="radio" name="sex" id="" value="女" v-model='gender'>女
         <p>性别为：{{gender}}</p>
     ```

     

   * 多选框绑定

     ```html
     var vm5 = new Vue({
                     el:'#bind',
                     data:{
                         message:'',
                         textarea:'',
                         gender:'',
                         hobby:[]
                     }
                 })
     
         <input type="checkbox" name="hobby" value="唱歌" v-model='hobby'>唱歌
         <input type="checkbox" name="hobby" value="跳舞" v-model='hobby'>跳舞
         <input type="checkbox" name="hobby" value="Rap" v-model='hobby'>Rap
         <input type="checkbox" name="hobby" value="篮球" v-model='hobby'>篮球
         <p>爱好有：{{hobby}}</p>
     ```

     

   * 下拉菜单绑定

     ```html
     var vm5 = new Vue({
                     el:'#bind',
                     data:{
                         message:'',
                         textarea:'',
                         gender:'',
                         hobby:[],
                         city:''
                     }
                 })
     
         <select name="addr" id="" v-model='city'>City
             <option value="Beijing">Beijing</option>
             <option value="Shanghai">Shanghai</option>
             <option value="Guangzhou">Guangzhou</option>
             <option value="Shenzhen">Shenzhen</option>
             
         </select>
     <p>所选城市：{{city}}</p>
     ```

     

---

6. 前后端交互案例

   * 前端代码

     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>英雄查询</title>
         <script src="./js/vue.js"></script>
         <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
         <script>
             window.onload= function(){
                 var vm = new Vue({
                     // delimiters:['[[',']]'],
                     el:'.box',
                     data:{
                         q:'',
                         results:[]
                     },
                     methods:{
                         query_func:function(){
                             axios.get(
                                 url='http://127.0.0.1:8000/search?q='+this.q
                             ).then(response=>(
                                 this.results = response.data.results
                             )
                             ).catch(error=>{
                                 alert(error.response.data.message)
                             })
                         }
                     }
                 })
             }
         </script>
     </head>
     <body>
         <div class="box">
             <input type="text" name="query_con" v-model='q'>
             <button @click='query_func'>查询</button>
             <li v-for='r in results'>姓名：{{r.name}}  性别：{{r.gender}}</li>
         </div>
     </body>
     </html>
     ```

     

   * 后端

     > 另外还要pip安装django-cors-headers，配置解决跨域请求问题
     >
     > 配置路由

     ```python
     from django.shortcuts import render
     from django.http import JsonResponse
     from django.views import View
     from .models import HeroInfo
     # Create your views here.
     
     
     class QueryHero(View):
         def get(self,request):
             q_con = request.GET.get('q')
             if not q_con:
                 return render(request,'front_end_request.html')
             q_data = HeroInfo.objects.filter(hname__contains=q_con)
             # print('查询结果',q_data)
     
             if not q_data.exists():
                 return JsonResponse({'message':'查无此人'},status=404)
     
             data = []
             for h in q_data:
                 if h.hgender == 0:
                     h.hgender='女'
                 elif h.hgender == 1:
                     h.hgender='男'
                 data.append({'name':h.hname,'gender':h.hgender})
             return JsonResponse({'results':data,'message':'ok'})
     ```

     

---

### ES6语法

1. 变量声明
   * ES5只有var
   * let 和 const 是ES6新增的声明变量的关键字
   * var let const 三者的区别：
     * var: 声明的是变量，有预解析功能，可以修改
     * let: 声明的是变量，没有预解析功能，可以修改
     * const: 声明的是常量，没有预解析功能，一旦赋值，不能再更改
2. ES6中对象的简写
   * 当对象的属性名和变量名一致，那么可以简写，将属性名和变量名合在一起，写一个
3. ES6箭头函数
   * 箭头函数解决的问题：
     * 函数中有多层作用域的嵌套时，this的指向不明确，this的指向会发生变化



---

### Vue实例生命周期





