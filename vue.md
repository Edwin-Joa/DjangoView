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
     <script src='vue.js'></script>
     ```

   * 创建vue对象：

     ```html
     window.onload = function (){
     	var vm = new Vue(){
     		// 绑定操作对象
     		el: '#app',
     		data:{
     
     		}
     	}
     };
     ```

   * 创建容器与对象进行关联

     ```html
     <div id='app'>
     	<img src='' alt='图片'>
     </div>
     ```

     

---

2. Vue基本语法：
   * 增加标签数据：data: {}
   * 修改标签属性： v-bind:
   * 给标签增加方法： v-on:      简写：@
3. 条件渲染：v-if:
4. 列表渲染：v-for:
   * 列表渲染
   * 字典渲染
5. 双向绑定数据： v-model: