<template>
    <div>
        <div>
            <span class="showt">One moment please</span>
            <span class="showt">{{sl}}</span>
        </div>
        <div class="showt">We're sending an email to your inbox now!</div>

        <div style="width:610px;overflow-x:hidden;margin-left: -20px ;">
            <video src="http://127.0.0.1:8000/media/uploads/1.mp4" height="570px;" class="vd"
            autoplay loop style="opacity:0.3;margin-left:-100px;"></video>
        </div>
    </div>
</template>
<script>
import 'animate.css'

export default {
    name:"Sup2",
    data(){
        return{
            sl:"",
        }
    },
    mounted() {
        this.interval = setInterval(()=>{
            if(this.sl.length <= 6){
                this.sl += ".";
            }else{
                this.sl = "";
            }
        },200)

        this.toLog();
    },
    methods: {
        toLog(){
            setTimeout(()=>{
                this.$router.push("./signup3");
                this.$store.state.signupidx = 2;
            },5000)
        }
    },
}
</script>
<style lang="css" scoped>
    .showt{
        font-size:30px;
        color:rgba(232, 239, 242, 0.773);
        font-weight: bold;
        font-family: 'Times New Roman', Times, serif;
    }
</style>