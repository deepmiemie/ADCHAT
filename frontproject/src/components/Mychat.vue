<template>
    <div >
        <div style="position: absolute;top:0px;left:0px;">
            <Tr1 />
        </div>


        <div :style="`position: absolute;right: 0px;top:0px;background-color: aliceblue;width: ${$store.state.divWid}px;height:1000px;z-index: 100;
        background-color: rgba(167, 167, 167, 0.605);transition:width 0.3s ease-in-out`" class="animate__animated animate__fadeInRight">
            <router-view></router-view>
        </div>

        <div style="transform: translate(0px,300px);color:white">
            <div>
                <span class="title_style">{{intro}}</span>
                <span style="width:20px;height:50px;background-color: rgb(255, 255, 255);
                display: inline-block;" :class="cursor" v-if="!isShow"></span>
            </div>
            <div>
                <span class="title_style">{{intro2}}</span>
                <span style="width:20px;height:50px;background-color: rgb(255, 255, 255);
                display: inline-block;" class="animate__animated animate__flash animate__infinite" v-if="isShow"></span>
            </div>
        </div>


    </div>
</template>
<script>
import 'animate.css'
import Tr1 from "./3d/Tr1.vue"

export default {
    name : "Mychat",
    data(){
        return {
            intro:"",
            intro2:"",
            all_content:"Welcome to use ChatAD",
            all_content2:"AI Expert in Anaerobic Digestion",
            num:0,
            cursor:"",
            isShow:false,
        }
    },
    methods: {
        show(){
            return new Promise((resolve,reject)=>{
                this.interval = setInterval(()=>{
                    this.cursor = "animate__animated animate__flash animate__infinite"
                    if (this.num > this.all_content.length){
                        clearInterval(this.interval);
                        setTimeout(()=>{
                            resolve();
                        },1000)
                    }
                    this.intro += this.all_content.slice(this.num,this.num+1);
                    this.num += 1;
                },200)
            })
        },
        show2(){
            this.num = 0;
            return new Promise((resolve,reject)=>{
                this.interval = setInterval(()=>{
                    this.cursor = "animate__animated animate__flash animate__infinite move2"
                    if (this.num > this.all_content2.length){
                        clearInterval(this.interval);
                        setTimeout(()=>{
                            resolve();
                        },1000)
                    }
                    this.intro2 += this.all_content2.slice(this.num,this.num+1);
                    this.num += 1;
                },200)
            })

        },
        async oprmove(idx){
            if(idx === 1){
                this.cursor += " move";
            }else if(idx === 2){
                this.cursor = "animate__animated animate__flash animate__infinite move2";
            }
        },
        signup(){
            this.$router.push("./mychat/signup");
        }
    },
    components:{Tr1,},
    async mounted() {
        await this.show();
        await this.oprmove(1);
        setTimeout(()=>{
            this.oprmove(2);
            setTimeout(()=>{
                this.isShow = true;
                this.show2();
            },1500)
        },1500)
    },
}
</script>
<style lang="css" scoped>
    .title_style{
        font-size:60px;
        font-weight:bold;
        display: inline-block;
    }
    .move{
        animation: m 1s 1;
        animation-fill-mode: forwards;
    }
    .move2{
        transform: translate(-702px,66px);
    }
    @keyframes m{
        100%{
            transform: translate(-702px,66px);
        }
    }

</style>