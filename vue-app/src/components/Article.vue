<template>
    <div class="home">
      <el-row display="margin-top:10px">
        <el-input v-model="input" aria-placeholder="请输入文章标题" style="display: inline-table; width: 30%;float: left"></el-input>
        <el-button type="primary" @click="addArticle()" style="float: left; margin: 2px">新增文章</el-button>
      </el-row>

      <el-row>
        <el-table :data="articleList" style="width: 100%" border>
          <el-table-column prop="id" label="序号" min-width="100">
            <template scope="scope">{{ scope.row.pk}}</template>
          </el-table-column>

          <el-table-column prop="title" label="标题" min-width="100">
            <template scope="scope">{{scope.row.fields.title}}</template>
          </el-table-column>

          <el-table-column prop="create_date" label="添加时间" min-width="100">
            <template scope="scope">{{scope.row.fields.create_date}}</template>
          </el-table-column>
        </el-table>
      </el-row>
    </div>
</template>

<script>
    export default {
        name: "Article",
        data(){
          return{
            input:'',
            articleList:[]
          }
        },

      mounted() {
          this.showArticle()
      },

      methods:{
          addArticle(){
            this.$http.get('http://127.0.0.1:8000/blog/addArticle?title='+this.input)
            .then((response)=>{
              var res = JSON.parse(response.bodyText)
              if(res.error_num===0){
                this.showArticle()
              }else{
                this.$message.error("新增文章失败,请重试")
                console.log(res['msg'])
              }
            })
          },

          showArticle(){
            this.$http.get('http://127.0.0.1:8000/blog/showArticles')
            .then((response)=>{
                var res = JSON.parse(response.bodyText)
                console.log(res)
                if (res.error_num === 0) {
                  this.articleList = res['list']
                } else {
                  this.$message.error('博客列表获取失败')
                  console.log(res['msg'])
                }
              }
            )

          }
      }


    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
