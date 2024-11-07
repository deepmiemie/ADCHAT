<template>
    <div style="height:640px;overflow:hidden">
        <div style="margin-top:20px;height:50px" class="md">
            <span style="display: inline-block;font-size:20px;color: #D5EDED;
            margin-left:20px;margin-right:20px;">Username</span>
            <input type="text" :class="userInfo.username==='' ?'myinput':'normaled' " v-model="userInfo.username"
            @keyup.enter = "hdenter(0)" ref="input1"  @blur="test('username')" @mouseover="tofocus(0)" @mouseout="nofocus(0)" />
            <div style="margin-left:130px;margin-top:10px;" class="err">{{userErr.username}}</div>
        </div>

        <div style="margin-top:30px;height:50px;">
            <span style="display: inline-block;font-size:20px;color: #D5EDED;
            margin-left:20px;margin-right:20px;">Password</span>
            <input type="password" style="margin-left:-5px;" @keyup.enter="hdenter(1)"
            :class="userInfo.password==='' ?'myinput':'normaled' " v-model="userInfo.password" ref="input2" @blur="test('password')" 
            @mouseover="tofocus(1)" @mouseout="nofocus(1)" />
            <div style="margin-left:130px;margin-top:10px;" class="err">{{userErr.password}}</div>
        </div>

        <div style="margin-top:30px;height: 50px;">
            <span style="display: inline-block;font-size:20px;color: #D5EDED;
            margin-left:20px;margin-right:20px;">Email</span>
            <input type="text" style="margin-left:32px;" @mouseover="tofocus(2)" @mouseout="nofocus(2)" @blur="test('email')"
             :class="emailc ==='' ?'myinput':'normaled' " v-model="emailc" ref="input3" />
            <span :style="`font-size:20px;opacity:${Number(!(emailc === ''))};transition:opacity 0.3s ease-in-out`" >
                <span style="color:aliceblue;">@</span>
                <el-dropdown @command="handlecom">
                    <span class="el-dropdown-link" style="color:aliceblue;font-size:20px;">
                      {{drop}}<i class="el-icon-arrow-down el-icon--right"></i>
                    </span>
                    <el-dropdown-menu slot="dropdown">
                      <el-dropdown-item command="126.com">126.com</el-dropdown-item>
                      <el-dropdown-item command="163.com">163.com</el-dropdown-item>
                      <el-dropdown-item command="gmail.com">gmail.com</el-dropdown-item>
                      <el-dropdown-item command="qq.com">qq.com</el-dropdown-item>
                    </el-dropdown-menu>
                  </el-dropdown>
            </span>
            <div style="margin-left:130px;margin-top:10px;" class="err">{{userErr.email}}</div>
        </div>

        <div style="margin-top:30px;height:50px;">
            <span style="display: inline-block;font-size:20px;color: #D5EDED;
            margin-left:20px;margin-right:20px;">Country</span>
            <el-dropdown @command="handlecom2" trigger="click">
                <el-button style="color:#D5EDED;font-size:20px;background-color: rgba(240, 248, 255, 0);"
                @click="userErr.country=''">
                    {{this.userInfo.country}}<i class="el-icon-arrow-down el-icon--right"></i>
                </el-button>
                <el-dropdown-menu slot="dropdown" style="background-color: rgba(0, 255, 255, 0);width: 125px;">
                    <el-dropdown-item command="China"  class="eit">China</el-dropdown-item>
                    <el-dropdown-item command="English" class="eit">English</el-dropdown-item>
                    <el-dropdown-item command="American" class="eit">American</el-dropdown-item>
                    <el-dropdown-item command="Canada" class="eit">Canada</el-dropdown-item>
                    <el-dropdown-item command="Australia" class="eit">Australia</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
            <span style="display: inline-block;font-size:20px;color: #D5EDED;
            margin-left:20px;margin-right:20px;">Org</span>
            <!-- <input type="text" class="pinput" style="width:155px;"/> -->
            <el-autocomplete
             v-model="userInfo.organization" @blur="userErr.organization=''"
            :fetch-suggestions="querySearch"></el-autocomplete>
            <div style="margin-left:125px;margin-top:10px;" class="err">
                <span>{{userErr.country}}</span>
                <span style="margin-left:115px;">{{userErr.organization}}</span>
            </div>
        </div>

        <div style="margin-top:50px;height:50px;">
            <span style="display: inline-block;font-size:20px;color: #D5EDED;
            margin-left:20px;margin-right:20px;">Phone</span>
            <span>
            <input type="text" class="pinput" style="width:40px;" v-model="p_f" />
            <span style="font-size:30px;color:#D5EDED;margin:0px 10px 0px 10px;">/</span>
            <input type="text" class="pinput" style="width: 285px;" v-model="p_b" />
            </span>
            <div style="margin-left:200px;margin-top:10px;" class="err">{{userErr.phone}}</div>
        </div>
        <div style="margin-left:200px;margin-top:50px;
        height:300px;">
            <a style="text-decoration: none;color:rgba(176, 176, 176, 0.768);">
                <i :class="tostyle" style="font-size:60px;" @click="moved" ></i>
            </a>
        </div>
    </div>
</template>
<script>
export default {
    name:"Sup1",
    data(){
        return{
            userInfo:{
                username:"deepmiemie",
                password:"!Liwenhan123",
                email:"Deepmiemie@gmail.com",
                country:"China",
                phone:"808-13012658299",
                organization:"Cht",
            },
            userErr:{
                username:"",
                password:"",
                email:"",
                country:"",
                phone:"",
                organization:"",
            },
            drop:"gmail.com",
            emailc:"",
            tostyle:"el-icon-s-promotion",
            p_f:"",
            p_b:"",
        }
    },
    methods: {
        handlecom(type){
            this.drop = type;
            this.userInfo.email = `${this.emailc}@${this.drop}`;
        },
        handlecom2(type){
            this.userInfo.country = type;
        },
        hdenter(idx){
            this.inputList[idx+1].focus();
        },
        querySearch(queryString, cb) {
            let restaurants = this.restaurants;
            let results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants;
            // 调用 callback 返回建议列表的数据
            cb(results);
        },
        createFilter(queryString) {
            return (restaurant) => {
            return (restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
            };
        },
        loadAll() {
            let loadarray = [];
            this.$ajax
            .get("media/load/value-key.json")
            .then(res=>{
                for(let i=0;i<Object.keys(res.data).length;i++){
                    loadarray.push(res.data[`${i}`]);
                }
            })
            .catch(err=>{
                console.log(err);
            })
            return loadarray;
        },
        moved(){
            const keylist = Object.keys(this.userInfo);
            let isl = 1;
            for(let i=0;i <keylist.length;i++){
                if(this.userInfo[keylist[i]] === ""){
                    this.userErr[keylist[i]] = "This field is required";
                    isl = 0;
                }
                if(this.p_b==="" || this.p_f===""){
                    this.userErr.phone = "This field is required";
                }
            }
            if(isl === 1){
                this.$ajax
                .post("test/gptuser/",this.userInfo)
                .then(res=>{
                    console.log(res);
                    setTimeout(()=>{
                        this.$router.push("./signup2");
                        this.$store.state.signupidx = 1;
                    },2000)
                    this.tostyle = "el-icon-s-promotion moved";
                })
                .catch(err=>{
                    console.log(err);
                })

            }
        },
        async test(type){
            if(type==="username"){
                const lenLimit = /^[a-zA-Z0-9_]{4,16}$/;
                if((lenLimit.test(this.userInfo.username) === false) && this.userInfo.username !== ""){
                    this.userErr.username = "The length of your username should be between 4 and 16";
                }else{
                    await this.$ajax
                    .get(`test/check/?field=${this.userInfo.username}`)
                    .then(res=>{
                        console.log(res);
                        const result = res.data.data;
                        if(result === 'true'){
                            console.log(111)
                            this.userErr.username = "The username already exists."
                        }else{
                            this.userErr.username = "";
                        }
                    })
                    .catch(err=>{
                        console.log(err);
                    })

                }
            }else if(type==="password"){
                const typeLimit = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).+$/;
                if((typeLimit.test(this.userInfo.password) === false) && this.userInfo.password !== ""){
                    this.userErr.password = `Your password should consist of both special characters,
                                         upper and lower case letters, and numbers`;
                }else{
                    this.userErr.password = "";
                }
            }else if(type==='email'){
                this.userErr.email = "";
                await this.$ajax
                .get(`test/check/?field=${this.userInfo.email}`)
                .then(res=>{
                    console.log(res);
                    const result = res.data.data;
                    if(result === 'true'){
                        console.log(111)
                        this.userErr.email = "The mailbox already exists."
                    }else{
                        this.userErr.username = "";
                    }
                })
                .catch(err=>{
                    console.log(err);
                })
            }
        },
        tofocus(idx){
            if(idx===0){
                this.$refs.input1.focus();
            }else if(idx===1){
                this.$refs.input2.focus();
            }else if(idx===2){
                this.$refs.input3.focus();
            }
        },
        nofocus(idx){
            if(idx===0){
                this.$refs.input1.blur();
            }else if(idx===1){
                this.$refs.input2.blur();
            }else if(idx===2){
                this.$refs.input3.blur();
            }
        }
    },
    mounted() {
        this.inputList = [this.$refs.input1,this.$refs.input2,this.$refs.input3];
        this.restaurants = this.loadAll();
    },
    watch: {
        emailc(){
            this.userInfo.email = `${this.emailc}@${this.drop}`;

        },
        p_f(){
            const numberLimit = /^\d+$/;
            if((numberLimit.test(this.p_f)===false) && this.p_f!==""){
                this.userErr.phone = "Please enter a valid phone number";
            }else{
                this.userErr.phone = "";
            }
            this.userInfo.phone = `${this.p_f}-${this.p_b}`;
        },
        p_b(){
            const numberLimit = /^\d+$/;
            if((numberLimit.test(this.p_b)===false) && this.p_b!==""){
                this.userErr.phone = "Please enter a valid phone number";
            }else{
                this.userErr.phone = "";
            }
            this.userInfo.phone = `${this.p_f}-${this.p_b}`;
        }
        
    }

}
</script>
<style lang="css" scoped>
    .md{
        position: relative;
    }
   .myinput{
    border:0px;
    border-bottom: 3px solid rgba(196, 200, 203, 0);
    background-color: rgba(240, 248, 255, 0);
    margin-left:-10px;
    font-size:20px;
    color:#D5EDED;
    width:20px;
    transition:width 0.3s ease-in-out;
   }
   .myinput:focus{
        outline: none;
        width: 200px;
        border-bottom: 3px solid #D5EDED;
   }
   .myinput:focus .md{
        background-color: aqua;
   }
   .normaled{
        border:0px;
        border-bottom: 3px solid #D5EDED;
        background-color: rgba(240, 248, 255, 0);
        margin-left:-10px;
        font-size:20px;
        color:#D5EDED;
        width:200px;
   }
   .normaled:focus{
        outline: none;
   }
   .pinput{
    height:40px;
    transform: translate(0px,-3px);
    width:50px;
    border:1px solid white;
    border-radius: 5px;
    background-color: rgba(240, 248, 255, 0);
    font-size:20px;
    color:#D5EDED;
   }
   .pinput:focus{
    outline: none;
   }
   .eit{
    color:#D5EDED;
    font-size:20px;
   }
   .eit:hover{
    background-color: rgba(0, 0, 0, 0.526);
    color:rgba(208, 221, 231, 0.666)
   }
   .moved{
    animation: mm 2s 1;
    animation-fill-mode: forwards;
   }
   .err{
    color:red;
    font-weight: lighter;
   }
   @keyframes mm{
    100%{
        font-size:100px;
        transform: translate(500px,200px);
    }
   }
</style>