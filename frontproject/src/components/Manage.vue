<template>
    <div>
        <h1 style="text-align: center;" class="animate__animated animate__bounce animate__delay-1s">super-administrator system</h1>
        <h2>Superuser Name</h2>
        <el-input v-model="username"></el-input>
        <h2>Superuser Password</h2>
        <el-input v-model="password"></el-input>
        <el-button style="margin-top:20px;" @click="toEdit()">Edit</el-button>
        <hr style="margin:50px 0px 50px 0px;" />
        <div>
            <h3>Managing user requests</h3>
            <el-table
            :data="userlist"
            style="width: 100%">
            <el-table-column
              prop="id"
              label="id"
              width="180">
            </el-table-column>
            <el-table-column
              prop="username"
              label="username"
              width="180">
            </el-table-column>
            <el-table-column
              prop="email"
              label="email"
              width="180">
            </el-table-column>
            <el-table-column
            prop="country"
            label="country"
            width="180">
           </el-table-column>
           <el-table-column
           prop="phone"
           label="phone"
           width="180">
          </el-table-column>

          <el-table-column
          prop="organization"
          label="organization"
          width="180">
          </el-table-column>
          <el-table-column
          prop="organization"
          label="organization"
          width="180">
            <template slot-scope="scope">
                <el-button @click="toPass(scope.$index)">pass</el-button>
            </template>
          </el-table-column>
          </el-table>
        </div>

        <el-button @click="getData" style="margin-top:10px;">getdata</el-button>
        <hr style="margin:50px 0px 50px 0px;" />
        <h3>Already approved user applications</h3>
            <el-table
            :data="formuserlist"
            style="width: 100%">
            <el-table-column
            prop="id"
            label="id"
            width="180">
            </el-table-column>
            <el-table-column
            prop="username"
            label="username"
            width="180">
            </el-table-column>
            <el-table-column
            prop="email"
            label="email"
            width="180">
            </el-table-column>
            <el-table-column
            prop="country"
            label="country"
            width="180">
            </el-table-column>
            <el-table-column
            prop="phone"
            label="phone"
            width="180">
            </el-table-column>
            <el-table-column
            prop="organization"
            label="organization"
            width="180">
            </el-table-column>
            </el-table>
    </div>
</template>
<script>

import 'animate.css'
export default {
    name:"Manage",
    data(){
        return {
            username :"",
            password :"",
            isAdm :false,
            userlist :[],
            formuserlist:[],
        }
    },
    methods: {
        toEdit(){
            if(this.username === "Deepmiemie@gmail.com" && this.password === "!Liwenhan123"){
                this.isAdm = true;
            }
        },
        async toPass(idx){
            console.log(idx);
            const id = this.userlist[idx].id;
            // 删除gptuser中的数据
            await this.$ajax
            .delete(`test/gptuser/${id}`)
            .then(res=>{
                console.log(res.data)
            })
            .catch(err=>{
                console.log(err)
            })

            // 增加到gptformuser中
            await this.$ajax
            .post('test/gptformuser/',this.userlist[idx])
            .then(res=>{
                console.log(res.data)
            })
            .catch(err=>{
                console.log(err)
            })

            await this.getData()
        },

        async getData(){
            await this.$ajax
            .get("test/gptuser/")
            .then(res=>{
                this.userlist = res.data.data;
            })
            .catch(err=>{
                console.log(err);
            })

            await this.$ajax
            .get("test/gptformuser/")
            .then(res=>{
                this.formuserlist = res.data.data;
            })
            .catch(err=>{
                console.log(err);
            })


        }
    },
    beforeCreate() {
        this.$ajax
        .get("test/gptuser/")
        .then(res=>{
            this.userlist = res.data.data;
        })
        .catch(err=>{
            console.log(err);
        })

        this.$ajax
        .get("test/gptformuser/")
        .then(res=>{
            this.formuserlist = res.data.data;
        })
        .catch(err=>{
            console.log(err);
        })
    },
}
</script>
<style lang="css">
    
</style>