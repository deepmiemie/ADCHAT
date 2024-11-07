<template>
    <div style="overflow: hidden;">
        <el-card style="margin:0px auto 0px;width:80%;background-color: rgba(35, 36, 38, 0.421);">
            <div class="md">
                <span style="display: inline-block;font-size:20px;color: rgba(227, 227, 227, 0.777);
                margin-left:20px;margin-right:43px;">Username</span>
                <input type="text" :class="userInfo.username==='' ?'myinput':'normaled' " v-model="userInfo.username"
                @keyup.enter = "hdenter(0)" ref="input11"  />
            </div>

            <div style="margin-top:20px;" class="md">
                <span style="display: inline-block;font-size:20px;color: rgba(227, 227, 227, 0.777);
                margin-left:20px;margin-right:49px;">Password</span>
                <input type="password" :class="userInfo.password==='' ?'myinput':'normaled' " v-model="userInfo.password"
                @keyup.enter = "hdenter(1)" ref="input12"  />
            </div>

            <div style="margin-top:20px;" class="md">
                <span style="display: inline-block;font-size:20px;color: rgba(227, 227, 227, 0.777);
                margin-left:20px;margin-right:25px;">Repassword</span>
                <input type="password" :class="repassword==='' ?'myinput':'normaled' " v-model="repassword"
                @keyup.enter = "hdenter(2)" ref="input13"  />
            </div>
        </el-card>

        <div style="margin-left:200px;margin-top:20px;color:rgba(176, 176, 176, 0.768);
        height:300px;">
            <i :class="tostyle" style="font-size:60px;" @click="moved" ></i>
        </div>

    </div>
</template>
<script>
export default {
    name:"Log",
    data(){
        return {
            userInfo:{
                username:"dd",
                password:"ddd",
            },
            repassword:"",
            tostyle:"el-icon-s-promotion",
        }
    },
    methods: {
        hdenter(idx){
            this.inputList[idx+1].focus();
        },
        moved(){
            this.tostyle = "el-icon-s-promotion moved";
            
            setTimeout(()=>{
                // this.$router.push("./signup2");
            },2000)
        }
    },
    mounted() {
        this.inputList = [this.$refs.input11,this.$refs.input12,this.$refs.input13];
    },
}
</script>
<style lang="css">
    .md{
        position: relative;
    }
    .myinput{
        border:0px;
        border-bottom: 3px solid rgba(196, 200, 203, 0);
        background-color: rgba(240, 248, 255, 0);
        margin-left:-10px;
        font-size:20px;
        color:rgba(196, 200, 203, 0.725);
        width:20px;
        transition:width 0.3s ease-in-out;
    }
   .myinput:focus{
        outline: none;
        width: 200px;
        border-bottom: 3px solid rgba(196, 200, 203, 0.725);
   }
   .myinput:focus .md{
        background-color: aqua;
   }
   .normaled{
        border:0px;
        border-bottom: 3px solid rgba(196, 200, 203, 0.725);
        background-color: rgba(240, 248, 255, 0);
        margin-left:-10px;
        font-size:20px;
        color:rgba(196, 200, 203, 0.725);
        width:200px;
   }
   .normaled:focus{
        outline: none;
   }
   .moved{
    animation: mm 2s 1;
    animation-fill-mode: forwards;
   }
   @keyframes mm{
    100%{
        font-size:100px;
        transform: translate(500px,200px);
    }
   }
</style>