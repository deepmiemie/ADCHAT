<template>
    <div style="overflow: hidden;">
        <div class="animate__animated animate__fadeInUpBig animate__delay-1s" style="margin-top:580px;">
            <router-link to="mychat/signup/" @click="toc"><span><Tr2 :fontconstent="'Sign up'" :x="-0.47" /></span></router-link>
            <span><Tr2 :fontconstent="'Login'" :x="-0.35" /></span>
        </div>
    </div>
</template>
<script>
import Tr2 from "./3d/Tr2.vue"
import 'animate.css'

export default {
    name:"Slbt",
    components:{Tr2,},
    data(){
        return{
            isshow:false
        }
    },
    mounted() {
        setTimeout(()=>{
            this.isshow = true;
        },1500)
    },
    methods: {
        toc(){
            console.log(11)
        }
    },
}
</script>
<style lang="css">
    
</style>