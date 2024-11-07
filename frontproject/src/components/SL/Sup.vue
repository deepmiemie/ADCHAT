<template>
    <div style="margin-top:180px;margin-left:0px;">
        <el-container>
            <el-header style="font-size:30px;font-weight: bold;color:#D5EDED;">
                Please enter your real information!
            </el-header>

            <el-main style="padding:0px;">
                <div style="margin-left:80px;margin-bottom: 60px;">
                    <el-steps :space="300" :active="$store.state.signupidx" finish-status="success">
                        <el-step title="step1"></el-step>
                        <el-step title="step2"></el-step>
                        <el-step title="step3"></el-step>
                    </el-steps>
                </div>

                <div>
                    <router-view></router-view>
                </div>


            </el-main>
        </el-container>
    </div>
</template>
<script>
import store from "../../store"
import "animate.css"

export default {
    name:"Sup",
    beforeRouteEnter(to,from,next){
        store.state.divWid = 590;
        next();
    },
    data(){
        return {
            step:0,
        }
    }

}
</script>
<style lang="css" scoped>

</style>

<style>
   .el-input__inner{
    background-color: rgba(129, 164, 195, 0) !important;
    height:45px !important;
    color: rgba(227, 227, 227, 0.777) !important;
    font-size:20px !important;
    width:155px !important;
   }
   .el-autocomplete-suggestion{
    background-color: rgba(137, 94, 39, 0) !important;
    width:200px !important;
   }
   .el-autocomplete-suggestion li{
    font-size:20px !important;
    color:rgba(227, 227, 227, 0.777) !important;
   }
</style>