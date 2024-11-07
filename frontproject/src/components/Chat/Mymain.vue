<template>
    <div style="margin:-10px;height:1000px;width:1690px;position: relative;">
        <div style="position: absolute;">

        </div>
        <div style="background-color: rgba(0, 0, 0, 0.87);margin-left: -2px;">
                <span style="vertical-align: middle;width: 85%;display: inline-block;">
                    <a href="#"><img src="../../assets/v1.png" width=85 style="padding:0px;margin:0px;margin-left:20px;padding:15px;vertical-align: middle;"/></a>
                    <!-- background-image: linear-gradient(20deg, rgb(213, 209, 210) 20%,rgba(113, 182, 191, 0.874) 50%, rgb(155, 169, 161) 100%); -->
                    <a href="#" style="text-decoration: none;">
                    <span style="display: inline-block;vertical-align: middle;
                    background-image: linear-gradient(20deg, rgb(213, 209, 210) 20%,rgba(113, 182, 191, 0.874) 50%, rgb(155, 169, 161) 100%);
                    -webkit-background-clip: text;font-weight: bold;color:transparent;"
                    >
                        <div style="font-size:50px;">ChatAD</div>
                        <div style="font-size:20px;margin-left:3px;">A Chat Model of AD</div>
                    </span>
                    </a>

                </span>
                <span style="vertical-align: middle;display: inline-block;">
                    <el-dropdown>
                        <span class="el-dropdown-link">
                            <el-avatar
                            :src="imgPath"
                            >user</el-avatar>
                        </span>

                        <template #dropdown>
                            <el-dropdown-menu>
                                <el-dropdown-item>
                                    <el-upload
                                    class="avatar-uploader"
                                    action="http://127.0.0.1:8000/test/upload/"
                                    :on-success = "handleSuccess"
                                    :show-file-list = false
                                  >
                                  <i class="el-icon-upload2"></i>Upload avatar
                                  </el-upload>
                                </el-dropdown-item>
                            </el-dropdown-menu>
                        </template>
                    </el-dropdown>
                </span>

        </div>

        <el-container style="height:1000px;margin: 0px;">
            <div
            style="background-color: black;position: absolute;left:0px;
            height:1000px;width: 250px;overflow: hidden;">
            </div>
            <div style="position: absolute;top:250px;">
                <button :class="style_list[0]" @click="change_style(0)">Basic Knowledge</button>
                <button :class="style_list[1]" @click="change_style(1)" >Operating Parameters</button>
                <button :class="style_list[2]" @click="change_style(2)" >Micro-Organisms</button>
                <button :class="style_list[3]" @click="change_style(3)" >Exogenous Additive<br />production</button>
                <button :class="style_list[4]" @click="change_style(4)" >Customized Literature<br />Library</button>
                
                <div style="position: relative;z-index: 90;width:250px;margin-top: -20px;">
                    <el-collapse>
                        <el-collapse-item title=" " name="1" >
                            <div style="white-space: nowrap;" v-if="endc===''">{{intro}}</div>
                            <div v-else>
                                <div v-for="value in fileList" style="margin-left:50px;">
                                    <i class="el-icon-s-order" style="margin-right:5px;"></i>
                                    {{value.name}}
                                </div>
                            </div>
                        </el-collapse-item>
                    </el-collapse>
                </div>
            </div>
            <el-main style="padding-right:10px;display: inline-block;margin-left:250px;height:1000px;overflow: hidden;">
                <span style="width:70%;display: inline-block;height:890px;vertical-align: top;">
                    <el-card style="height:840px;background-color: black;overflow: auto;" class="chat-card" ref="cl">
                        <div v-for="value,index in msgList" :key="value.id">
                            <div v-if="value.cls===0||value.cls===1||value.cls===2||value.cls===3" style="background-color: rgba(240, 248, 255, 0.507);margin: 0 auto 0;width:400px;text-align: center;
                            border-radius: 20px;margin-top:10px;padding:5px 0px 5px 0px;color:rgba(214, 215, 216, 0.889);margin-bottom:-80px;">
                                ChatAD suggests you choose the {{value.cls+1}} nd category
                            </div>

                            <div v-if="value.isUser" style="padding:20px;padding-bottom: 40px;transform: translate(0px,50px);">
                                <el-avatar :size="40" 
                                :src="imgPath" />
                                <span style="background-image: linear-gradient(20deg,rgba(123, 88, 106, 0.571) 10%,rgba(10, 10, 142, 0.407) 90%);display: block;transform: translate(50px,-10px);width:850px;
                                border-radius: 10px;padding:10px;"  class="usercontent" @click="tips(index)">
                                    <span style="margin-left:10px;color:rgba(255, 255, 255, 0.785);" v-html="value.userinfo"></span>
                                </span>
                            </div>

                            <div style="background-color: rgba(109, 87, 60, 0);padding:20px;padding-bottom: 40px;
                            " v-if="value.isgptshow">
                                <el-avatar :size="40" 
                                :src="`http://127.0.0.1:8000/media/uploads/v1.png`" 
                                fit = "fill"
                                />
                                <span></span>
                                <span style="background-color: #f3e4f14c;display: block;transform: translate(50px,-10px);width:850px;
                                border-radius: 10px;padding:10px;padding-top:0px;">
                                    <span style="margin-left:10px;color:rgb(255, 255, 255);line-height: 30px;letter-spacing: 1px;"
                                    >
                                        <span v-html="md.render(value.gptinfo)"></span>
                                    </span>
                                </span>

                            </div>
                        </div>

                    </el-card>
                    <div style="margin-top:10px;width:100%;">
                        <el-tooltip
                        class="box-item"
                        effect="light"
                        :content="tipsd"
                        raw-content
                        placement="top-start"
                        >
                        <textarea class="textareass" v-model="userMsg" @input="getclass" :readonly="!isLoading"></textarea>
                        </el-tooltip>
                    <!-- <div v-else>
                        <textarea class="textareass" v-model="userMsg" @input="getclass" :readonly="!isLoading"></textarea>
                    </div> -->

                        <button style="vertical-align: middle;width:17%;border:0px;display: inline-block;
                        height:120px;border-radius: 0px 5px 5px 0px;position: relative;z-index: 1;
                        font-size:20px;color:aliceblue;font-family: 'Times New Roman', Times, serif;
                        font-weight: bold;background-color: rgba(0, 0, 0, 0.67);"
                        @click="sendMsg">
                            <span style="vertical-align: middle;margin-right:10px;">send</span>
                            <i class="el-icon-s-promotion"></i>
                        </button>

                        <div style="position: absolute;transform: translate(750px,-100px);z-index: 100;position: relative;" class="dt">
                            <span style="background-color: rgba(141, 141, 141, 0.445);display: inline-block;vertical-align: middle;color:white;
                            transform: translate(-10px,-2px);position: absolute;right:989px;z-index:2020;height:40px;border-radius: 5px;" class="floatext" ref="floatext">
                            <i class="el-icon-picture" style="font-size:20px;margin-right:5px;padding:5px;margin-top:5px;" v-if="td"></i>
                            <el-upload action="http://127.0.0.1:8000/test/uploadpdf/" style="display: inline-block;" class="toupload" 
                             :show-file-list="false" multiple v-model="fileList" :on-change="handleFileChange" >
                            <i class="el-icon-plus" style="font-size:20px;margin-right:10px;padding:5px;" v-if="td"></i>
                            </el-upload>
                            <i class="el-icon-loading" style="font-size:20px;margin-right:10px;padding:5px;" v-if="geload" ></i>
                            <span v-else-if="generateLoading" style="font-size:10px;margin-right:10px;padding:5px;" >successful!</span>
                            </span>
                            <span class="el-icon-help showuploaded" style="vertical-align: middle;" ref="showuploaded"
                            @click="getoupload(0)" @blur="getoupload(0)" @mouseover="getoupload(1)" @mouseout="getoupload(2)"></span>
                        </div>

                    </div>
                </span>

                <span style="display: inline-block;background-color: rgba(0, 0, 0, 0.793);height:1200px;vertical-align: top;
                width:30%;" >
                    <span style="color:aliceblue;text-align: center;display: inline-block;width:100%;
                    height:50px;line-height: 50px;background-color: rgba(159, 166, 192, 0.371);font-size: 20px;font-weight: bold;">Reference</span>
                    <div style="overflow: auto;height: 830px;" class="pdflist" ref ="bibl">
                        <div v-for="value in pdfList" :key="value.id" :class="(ispdf+1 === value.num)?'pdf_highlight':'pdf_normal' ">
                            <el-card style="width:90%;margin:0 auto 0;height:600px;margin-top:20px;overflow: auto;overflow-x: auto;">
                                <div v-for="ipdf ,key in value.pdfinfo" style="margin-bottom: 20px;" :key="key">
                                    <div style="font-style: italic;font-family: 'Times New Roman', Times, serif;font-weight: bold;font-size:20px;">pdf:{{key}}</div>
                                    <div :style="`font-size:20px;font-weight:bold;background-color: rgba(84, 83, 83, 0.145);white-space: nowrap;width:${value.ml*7.2}px;display: inline-block;`">
                                        {{ipdf.title}}</div>
                                    <div style="font-size:15px;font-style: italic;white-space: nowrap;"><b>Auth:</b>{{ipdf.author}}</div>
                                    <div style="font-size:15px;font-style: italic;white-space: nowrap"><b>Date:</b>
                                        {{ipdf.modData.slice(2,6)}}/{{ipdf.modData.slice(6,8)}}/{{ipdf.modData.slice(8,10)}}
                                    </div>
                                    <div style="font-size:15px;font-style: italic;white-space: nowrap"><b>Kwds:</b>
                                        {{ipdf.keywords}}</div>
                                </div>
                            </el-card>
                        </div>
                        <div style="height:540px;"></div>
                    </div>

                </span>
            </el-main>

        </el-container>
    </div>
</template>

<script>
import {nanoid} from 'nanoid';
import axios from 'axios';
import Logo from './Logo.vue';
import MarkdownIt from 'markdown-it';

export default {
    name : "Mymain",
    data(){
        return {
            rtd:100,
            cls:100,
            isl:false,
            ispdf:100,
            style_list:["asidebutton","asidebutton","asidebutton","asidebutton","asidebutton",],
            userMsg:"",
            msgList:[
                {cls:100,rtd:100,isUser:false,id:nanoid(),userinfo:"",isgptshow:true,gptinfo:""},
            ],
            gptinfo:"",
            pdfList:[],
            num:1,
            showicon:false,
            isLoading:true,
            imgPath:"",
            imgid:0,
            tipsd:"In order to prevent problems such as multiple requests being sent at the same time, <br />please <b>refrain</b> from using chat boxes or other interruptions during the llama2 reply period.",
            isSend:true,
            isBt:true,
            td:false,
            fileList:[],
            endc:"",
            generateLoading:false,
            geload:false,
            md:undefined,
        }
    },
    methods: {
        create(){
            this.md = new MarkdownIt();
        },
        change_style(idx){
            console.log(111)
            this.style_list = ["asidebutton","asidebutton","asidebutton","asidebutton","asidebutton",];
            this.style_list[idx] = "asidebutton_act";
            this.cls = idx;
            if(idx===4){
                this.isSend=false;
            }else{
                this.isSend=true;
            }
        },
        async sendMsg(){
            if(this.initinterval !== undefined){
                clearInterval(this.initinterval);
            }
            if(this.userMsg !== ""){
                this.isUser = true;
                this.isLoading = false;
                this.msgList[this.num].isUser = true;
                this.msgList[this.num] = {...this.msgList[this.num],id:nanoid(),userinfo:this.userMsg,isgptshow:false,gptinfo:""};
                this.num += 1;
                await axios
                .get(`/test/getchat/?question=${this.userMsg}&class_type=${this.cls+1}&isinit=true`)
                .then(res=>{
                    console.log(res)
                    this.msgList[this.msgList.length-1].isgptshow = true;
                    // const pdfListmeta = {id:nanoid(),pdfinfo:res.data.data}
                    // let mtl = 0;
                    // for(let j=0;j<Object.values(pdfListmeta.pdfinfo).length;j++){
                    //     let mt = pdfListmeta.pdfinfo[j].title.length;
                    //     if(mt > mtl){mtl = mt};
                    // }
                    // const pdfListmetapp = {...pdfListmeta,ml:mtl,num:this.num};
                    // this.pdfList.push(pdfListmetapp);
                    // this.pdfList = pdfListmetapp;
                    this.pdfList.push(
                        {id:nanoid(), pdfinfo:Object.values(res.data.data), num:this.num}
                    )

                    console.log(this.pdfList)
                    this.interval = setInterval(async ()=>{
                        await axios
                        .get(`/test/getchat/?question=${this.userMsg}&class_type=${this.cls+1}&isinit=false`)
                        .then(res=>{
                            this.$set(this.msgList[this.msgList.length-1], 'gptinfo',this.msgList[this.msgList.length-1].gptinfo + res.data.data);
                            this.$forceUpdate();
                        })
                        .catch(err=>{
                            console.log(err);
                            clearInterval(this.interval);
                            setTimeout(()=>{
                                this.isLoading = true;
                            },100)
                            if(this.cls == 4){
                                this.isSend = false;
                                this.rtd = this.cls;
                                this.msgList[this.num]={cls:4,rtd:this.rtd,isUser:false}
                            }else{
                                this.isSend = false;
                                this.rtd = this.cls;
                                this.msgList[this.num]={cls:this.cls,rtd:this.rtd,isUser:false}
                            }
                        })
                    },50)
                })
                .catch(err=>{
                    console.log(err)
                })
            }else{
                this.tipsd = "Please enter a valid question, which usually cannot be empty";
            }


        },
        getclass(){
            this.$refs.cl.scrollTop = 500;
            console.log(this.$refs.cl.scrollTop)
            if(this.isLoading && this.isSend){
                axios
                .get(`/test/getclass/?question=${this.userMsg}`)
                .then(res=>{
                    this.rtd = res.data.data-1;
                    this.msgList[this.num]={cls:res.data.data-1,rtd:this.rtd,isUser:false}
                })
                .catch(err=>{
                    console.log(err);
                })
            }else{

            }
        },
        tips(idx){
            console.log(idx);
            this.$refs.bibl.scrollTop = 320*idx;
            this.ispdf = idx;
        },
        handleSuccess(res){
            console.log(res)
            if(this.imgid!=0){
            axios
            .delete(`/test/upload/${this.imgid}/`)
            }
            this.imgPath = res.data.file;
            this.imgid = res.data.id;
        },

        getoupload(type){
            if(type===0){
                if(this.isBt){
                    this.$refs.showuploaded.style.fontSize="35px";
                    this.$refs.showuploaded.style.color="rgba(240,248,255,0.412)";
                    this.isBt = !this.isBt;
                    this.$refs.floatext.style.width = "90px";
                    setTimeout(()=>{
                        this.td = true;
                    },200)
                }else{
                    this.$refs.showuploaded.style.fontSize="25px";
                    this.$refs.showuploaded.style.color="rgb(255,255,255)";
                    this.isBt = !this.isBt;
                    this.$refs.floatext.style.width = "0px"
                    this.td = false;
                }

            }else if(type===1){
                this.$refs.showuploaded.style.fontSize="35px";
                this.$refs.showuploaded.style.color="rgba(240,248,255,0.412)";
                this.$refs.floatext.style.width = "90px";
                this.isBt = !this.isBt;
                setTimeout(()=>{
                    this.td = true;
                },200)
            }else{
                this.isBt = !this.isBt;
            }
        },
        
        async handleFileChange(file,fileList){
            this.fileList = fileList;
            let intro = "";
            console.log(this.fileList);
            for(let i =0;i<this.fileList.length;i++){
                intro += `${this.fileList[i].name}         ${this.fileList[i].size} b`;
            }
            this.change_style(4);
            this.endc = intro;
            this.$refs.floatext.style.width = "120px";
            this.geload = true;
            setTimeout(async ()=>{
                await axios
                .get("test/generate/")
                .then(
                    res =>{
                        console.log(res)
                        this.geload = false;
                        this.$refs.floatext.style.width = "180px";
                        this.generateLoading = true;
                    }
                )
                .catch(
                    err =>{
                        console.log(err)
                    }
                )
            },1000)

        },


    },
    props:{Logo,},

    computed:{
        intro(){
            let pageText = ""
            if(this.cls===0){
                pageText = `
                Material addition effects of anaerobic digestion.
                There is a wide variety of materials added to anaerobic digestion studies that are designed to improve the waste degradation process, increase gas production, reduce waste treatment time, or improve environmental friendliness. Below are some examples of common added materials:
                Organic waste: This is one of the most common materials added, including food residues, agricultural waste, household waste, etc., and is used as the main carbon and energy source.
                Nitrogen source materials: Nitrogen sources such as urea, ammonia, plant and animal residues are added to maintain a proper carbon to nitrogen ratio and promote microbial growth.
                Microbial culture materials: including vitamins, minerals and microbial strains, used to increase microbial activity and population.
                Buffers and pH regulators: e.g. lime, bicarbonate, used to maintain a suitable pH range and prevent fluctuations in acidity.
                Inhibitors: used to inhibit the growth of specific microbial communities to minimize unwanted reactions, e.g., inhibitors of sulfate-reducing bacteria.
                Adsorbents: e.g. activated carbon, used to remove organic contaminants from waste and improve digestion efficiency.
                Moisture regulators: additive materials, such as moisture adsorbents or porous materials, used to regulate the moisture content within the reactor.
                Auxiliary carbon sources: e.g. acetic acid, whey, starch, etc., used to change the carbon to nitrogen ratio of the waste and improve methane production.
                Biological improvers: including specific strains of bacteria, biological stimulants, etc., used to improve microbial activity and waste decomposition.
                Fermentation agents: organic acids, pectinases, etc. to accelerate fermentation and degradation of waste.
                Surfactants: used to improve solubility and microbial adhesion of waste.
                Natural fillers: e.g. wood chips, straw, rice straw, etc., which can be used as structural support and degradation aids.
                Substrate additives: Specific substrates, such as lactic acid, whey slurry, and fatty acids, can be used to direct gas production pathways and improve gas production efficiency.
                The selection and quantitative addition of these materials depends on factors such as the nature of the waste, treatment goals, reactor type, and operating conditions. Researchers adapt and optimize the type and amount of added materials to specific project needs to achieve optimal anaerobic digestion.
                (ii)
                The addition of various materials during anaerobic digestion can significantly affect the waste treatment efficiency and the gas products produced. The following is a detailed analysis of the effect of quantitative addition of different materials on anaerobic digestion and their quantitative effects:
                1. Carbon source materials:
                Quantitative impact: Increasing the addition of a carbon source usually increases gas production, especially methane gas.
                Detailed analysis: Increasing the carbon source can provide more digestible organic material and promote the growth and activity of microorganisms, thus increasing the production of methane. However, adding too much carbon source may lead to over-acidic reaction and reduce the stability of the system.
                2. Nitrogen source material:
                Impact: Moderate amounts of nitrogen sources help maintain the carbon to nitrogen ratio and increase the rate of waste degradation.
                Quantitative impact: moderate addition of nitrogen source can increase methane production, but excessive addition may lead to ammonia and nitrogen accumulation.
                Detailed Analysis: Nitrogen is an essential component of microbial growth, and moderate additions of nitrogen can improve anaerobic digestion by promoting microbial growth and activity. Insufficient nitrogen source may limit the growth of microorganisms, while excessive nitrogen source may lead to excessive ammonia nitrogen or sulfate in the gas product, which may cause negative impact on the environment.
                3. microbial species:
                QUANTITATIVE IMPACT: The introduction of specific gas-producing microbial species can increase the production of specific gas products, such as methane.
                Detailed analysis: the addition of specific microbial species, such as methanogenic bacteria, can be directed to promote the production of specific gases. This is useful for specific targets in waste treatment and resource recovery. Note, however, that different microbial species may have different adaptations to environmental conditions and waste properties.
                4. Buffers and pH regulators:
                Impact: maintaining an appropriate pH range is critical for microbial activity. Lime: is used to maintain a neutral or alkaline environment in the reactor and helps stabilize the digestion process. Bicarbonate: can be used to adjust the pH of the reactor to prevent overly acidic or alkaline conditions from occurring.
                Quantitative effects: Addition in the right amount helps stabilize the pH, but over-addition may lead to alkaline conditions.
                Detailed Analysis: Maintaining an appropriate pH range is critical for microbial growth and waste decomposition. Lack of buffers may result in a drop in pH, creating acidic conditions that inhibit microbial activity. Excessive buffers, on the other hand, may lead to alkaline conditions.
                5. Microbial culture substances:
                Impact: Vitamins, minerals and microbial strains can increase microbial activity and numbers.
                Quantitative impact: moderate addition can increase microbial activity, but excessive amounts may lead to microbial community imbalance.
                Detailed analysis: microbial culture substances to supplement the nutrition required by microorganisms, but should be added carefully to avoid unnecessary costs and excessive microbial communities.
                6. reactor design:
                Quantitative impact: the choice of reactor type and size has a significant impact on the efficiency and gas production of anaerobic digestion.
                DETAILED ANALYSIS: The type of reactor (e.g., complete mixed reactor or fixed bed reactor) can influence the microbial distribution and gas yield in the reactor. Quantitative selection of reactor size should take into account waste volume and treatment rate.
                7. Additives and auxiliary materials:
                Quantitative impact: the addition of microbial nutrients and adsorbents can affect the growth of microorganisms and the removal efficiency of pollutants in the waste.
                Detailed analysis: The addition of microbial nutrients in the right amount can improve the activity of microorganisms, thus accelerating the decomposition of waste. The addition of adsorbents can improve the pollutant removal efficiency, but excessive use may reduce gas production.
                8, organic waste:
                Impact: organic waste is a major carbon and energy source and is critical to the anaerobic digestion process.
                Quantitative impact: increasing the addition of organic waste usually increases methane gas production, but overdosing may lead to reactor oversaturation.
                Detailed analysis: Organic wastes provide the carbon source needed by microorganisms to promote microbial growth and waste decomposition. The amount added should be adjusted according to the nature of the waste and the capacity of the reactor to avoid over- or under-addition.
                9. Inhibitors:
                Impact: Inhibitors reduce unwanted microbial activity.
                Quantitative impact: Moderate use can control specific microbial communities, but excessive amounts may reduce overall waste treatment efficiency.
                DETAILED ANALYSIS: Inhibitors can be used to control unwanted microorganisms, but should be used carefully to avoid adverse effects on beneficial microorganisms.
                10. Adsorbents:
                IMPACT: Adsorbents may improve the removal efficiency of organic contaminants.
                QUANTITATIVE IMPACT: Moderate use may improve removal efficiency, but excessive use may reduce gas production.
                Detailed analysis: adsorbents can be used to improve the removal efficiency of pollutants, but the amount added should be balanced between maximizing the removal effect and gas production.
                11, moisture regulator:
                Impact: regulating moisture content can affect the performance and stability of the reactor.
                Quantitative impact: moderate use can maintain suitable moisture conditions, but overuse may lead to dilution effect of the reactor.
                DETAILED ANALYSIS: Moisture regulators can be used to control moisture in the reactor, but should be dosed according to the characteristics of the waste.
                In summary, dosing different materials needs to be carefully balanced to achieve optimum anaerobic digestion. This takes into account the nature of the waste, the treatment objectives and the environmental conditions to ensure that the process is stable, efficient and environmentally friendly. Quantitative analysis can help optimize anaerobic digestion systems to meet specific waste treatment needs.
                `
            }else if(this.cls===1){
                pageText = `
                Microbial effects of anaerobic digestion
                The impact of various types of microorganisms in anaerobic digestion studies is an important topic regarding microbial diversity, functions and interactions. Different types of microorganisms play key roles in the anaerobic digestion process. The following is a detailed description of some common microbial types and their effects, including specific microbial names:
                1, Methanogenic bacteria (Methanogens):
                Specific microbial names: Methanogenic bacteria such as Methanobacterium, Methanococcus, Methanosarcina, etc.
                Impact: Methanogens are the most important microorganisms in anaerobic digestion, they convert organic matter into methane gas.
                Detailed analysis: These microorganisms are responsible for methane production in the final stage of anaerobic digestion, and their activity and diversity can directly affect the production and quality of methane gas. Different species of methanogenic bacteria may differ in the rate of gas production and the stability of methane production. Therefore, it is very important to quantitatively regulate different species of methanogenic bacteria in anaerobic digestion system.
                2、Acidogenic bacteria (Acidogens):
                Specific microbial name: Acidogenic bacteria such as Clostridium, Bacillus, Propionibacterium, etc.
                Impact: acidifying bacteria will be complex organic waste decomposition into organic acids.
                Detailed analysis: These microorganisms play a role in the early stages of anaerobic digestion, the waste degradation into more digestible intermediate products, to create conditions for the subsequent gas production stage.
                3, acetic acid bacteria (Acetogens):
                Specific microbial name: Acetic acid producing bacteria such as Acetobacterium, Syntrophobacter and so on.
                Impact: Acetic acid bacteria will convert organic acids into acetic acid. Acetic acid-producing bacteria contribute to the production of acetic acid in anaerobic digestion, which is a precursor to methane production.
                Detailed analysis: They participate in the oxidation of organic matter, producing acetic acid and hydrogen, which provide substrates for subsequent methane production. Appropriate amount of acetic acid generating bacteria help to maintain the appropriate ratio of acetic acid and methane, and promote methane production.
                4, Sulfate Reducing Bacteria (Sulfate Reducers):
                Specific microorganism name: such as Desulfovibrio, etc.
                Impact: Sulfate Reducers can competitively consume hydrogen and organic matter, reducing methane production.
                Detailed analysis: Their presence can inhibit methane generation and adversely affect waste treatment efficiency. Therefore, it is necessary to quantitatively control their number in the system to maximize methane production.
                5, Nitrite Reducing Bacteria (Nitrate Reducers):
                Specific microbial name: such as Paracoccus, Pseudomonas, etc..
                Impact: Nitrate Reducers competitively consume hydrogen and organic matter to reduce methane production.
                Detailed analysis: their presence can lead to the production of nitrogen gas in the waste treatment process, rather than methane.
                6. Denitrifying bacteria (Denitrifiers):
                Specific microbial name: such as Rhodobacter, Thiobacillus, etc..
                Impact: denitrifying bacteria can utilize nitrates and nitrites in the waste, reducing the efficiency of nitrogen removal.
                Detailed analysis: They are usually not desired microorganisms as they reduce methane production and may lead to incomplete waste treatment.
                7. Aromatic Dehydrogenase Microbes (Aromatic Dehydrogenase Microbes):
                Specific microbial names: e.g. Syntrophus, Smithella, etc.
                Impact: These microorganisms can degrade organic substances that are difficult to degrade, such as aromatic compounds.
                Detailed analysis: They play an important role in the treatment of anaerobic systems containing difficult-to-biodegrade wastes, improving the digestion of organic matter.
                8, cellulose degrading bacteria (Cellulolytic Bacteria):
                Specific microbial name: Cellulolytic bacteria such as Clostridium thermocellum and Ruminococcus.
                Quantitative impact: These microorganisms help to break down difficult to degrade wastes such as cellulose and increase digestible organic matter.
                Detailed analysis: Moderate amounts of cellulose-degrading bacteria can increase the rate of waste decomposition, but quantitative control is needed to avoid excessive waste decomposition and extrusion gas production steps. By quantitatively monitoring the presence and number of these bacteria, their contribution to the rate of cellulose degradation can be determined.
                9, Nitrite-Oxidizing Bacteria (Nitrite-Oxidizing Bacteria):
                Specific microbial name: Nitrite-oxidizing bacteria such as Nitrospira.
                Quantitative impact: Nitrite-oxidizing bacteria can oxidize nitrite to nitrate, reducing ammonia and nitrite.
                Detailed analysis: the presence of nitrite oxidizing bacteria can reduce nitrite concentration, the presence of the right amount of nitrite oxidizing bacteria to help maintain the appropriate level of ammonia and nitrite to support methane production.
                10, nitrifying bacteria (Nitrifying Bacteria):
                Specific microbial name: Nitrifying bacteria such as Nitrosomonas and Nitrobacter.
                Quantitative impact: Nitrifying bacteria may lead to nitrification and nitrosation of ammonia nitrogen, reducing ammonia nitrogen can be used for methane generation.
                Detailed analysis: By quantitatively controlling the number of nitrifying bacteria, the loss of ammonia nitrogen can be reduced and the utilization of ammonia nitrogen can be improved.
                11, yeast:
                Specific microorganism name: Yeast (Yeast)
                Quantitative impact: Yeast may be involved in the fermentation and acetic acid production of organic waste.
                Detailed analysis: The presence of yeast can influence the fermentation process, but its quantity needs to be adjusted according to the type of waste and treatment objectives.
                Different types of microorganisms interact in anaerobic digestion systems, and their presence and activity can directly affect the degradation efficiency, type of gas production and gas yield of the waste. Therefore, understanding and managing the microbial community is key to optimizing the anaerobic digestion process. Researchers have adapted microbial community composition and operating conditions to achieve specific waste treatment and resource recovery goals.
                `
            }else if(this.cls===2){
                pageText = `
                Analysis of anaerobic digestion systems
                Anaerobic digestion is a type of biological reaction system used for waste treatment and bioenergy generation that has a variety of important properties and characteristics. The following is an introduction to the analysis of the properties of anaerobic digestion system:
                1, anaerobic environment:
                INTRODUCTION: Anaerobic digestion is a biological reaction process that occurs under anaerobic conditions, where microorganisms degrade organic wastes in an anoxic or anaerobic environment. One of the distinguishing features of anaerobic digestion system is its anaerobic environment.
                ANALYSIS: Anaerobic digestion systems under anaerobic conditions are usually better suited than aerobic systems for treating high-level organic wastes because they do not depend on oxygen and do not result in complete oxidation of the waste. In this environment, microorganisms degrade organic waste in the absence of oxygen. This environment helps in the production of useful gases such as methane, but it needs to be carefully controlled to prevent the production of harmful gases such as sulfides.
                2.Organic matter degradation:
                Anaerobic digestion systems are effective in degrading a wide range of organic matter, including food residues, agricultural wastes, sludge, and so on. Microorganisms decompose these organic materials under anaerobic conditions, converting them into gases such as methane and carbon dioxide, reducing the volume of waste and pollution.
                3, gas production characteristics:
                Properties: a significant feature is that in anaerobic digestion system mainly produces methane gas, while a small amount of carbon dioxide and other gases can also be produced. Anaerobic digestion system produces combustible gases such as methane, which can be used as a source of energy.
                ANALYSIS: Methane is an important biogas that can be used for electricity, heating and fuel. The gas-producing properties of anaerobic digestion systems make them an important means of bioenergy recovery and have potential economic value in waste treatment and resource recovery.
                4, Microbial diversity:
                Introduction: anaerobic digestion relies on a variety of microbial communities, including methanogenic bacteria, sulfate-reducing bacteria, acetic acid-producing bacteria, etc.
                ANALYSIS: The balance of microbial activity and community is critical to the stability and performance of the system. Quantitative monitoring of microbial species and numbers helps optimize system operation.
                5, pH regulation:
                INTRODUCTION: Maintaining an appropriate pH range is critical to the stability of anaerobic digestion systems. Anaerobic digestion systems need to maintain a suitable pH range, usually between neutral and slightly alkaline.
                ANALYSIS: Changes in pH can directly affect microbial activity and waste degradation rates. Therefore, the addition of a buffer is often required to control the pH. The pH range should typically be controlled between 6.5 and 8.0 to ensure microbial growth and activity. Buffers and pH adjusters are used to maintain suitable pH conditions.
                6.Reactor design:
                The nature of anaerobic digestion systems is influenced by reactor type and design. Common reactor types include complete mixed reactors, fixed bed reactors, and temperature controlled reactors. Reactor selection and design affects gas production, waste treatment rates, and energy efficiency. Different types of reactors have different characteristics and are suitable for different types and sizes of waste treatment projects. The choice of reactor type affects the performance and efficiency of the system.
                7. Diversity of waste sources:
                INTRODUCTION: Anaerobic digestion can be used to treat a wide range of organic wastes, including agricultural wastes, food residues, sludge, animal and plant residues, etc. Anaerobic digestion systems are suitable for a wide range of waste sources, including municipal wastewater treatment plants, farms, and food processing plants.
                Analysis: Different types of wastes have different chemical compositions and degradation difficulties, so it is necessary to adjust the operating parameters and additives of the system according to the type of waste.
                8. Biodegradability:
                Nature: anaerobic digestion system relies on the activity and diversity of microbial communities, which can effectively degrade a variety of organic wastes, including food residues, agricultural wastes and sewage sludge.
                ANALYSIS: The microbial communities in anaerobic digestion systems include methanogenic bacteria, sulfate-reducing bacteria, and acetic acid-producing bacteria, which work synergistically to break down organic waste into products such as methane and carbon dioxide. This biodegradability allows waste to be effectively converted into energy.
                9, waste reduction:
                Nature: anaerobic digestion system can significantly reduce the volume and weight of organic waste.
                Analysis: By converting organic waste into gas and sediment, anaerobic digestion systems can reduce the volume of waste and lower the cost of landfill or waste disposal.
                10. Waste Stability:
                PROPERTY: The anaerobic digestion process improves waste stability and reduces the presence of harmful microorganisms and pathogens.
                Analysis: Under anaerobic conditions, the methane gas produced and the acidic environment have an inhibitory effect on harmful microorganisms, thus improving the health and safety of waste.
                11、Wide range of application:
                Nature: The anaerobic digestion system is applicable to a wide range of waste types, including organic solid waste, sewage sludge, and agricultural waste.
                Analysis: Because of its wide applicability, anaerobic digestion system plays an important role in urban and rural waste treatment, energy recovery and environmental protection.
                12. Environmental friendliness:
                Nature: Anaerobic digestion systems help reduce greenhouse gas emissions and have a low carbon footprint.
                ANALYSIS: By effectively controlling the degradation process of waste, anaerobic digestion systems help to reduce the release of greenhouse gases such as methane, which is beneficial to environmental protection and sustainable development.
                13. Operation and maintenance requirements:
                PROPERTY: Anaerobic digestion systems usually require stringent operation and maintenance, including control of parameters such as temperature, pH, and stirring speed.
                ANALYSIS: In order to keep the system running efficiently, regular monitoring and maintenance is required to ensure the health and stability of the microbial community.
                14. Temperature control:
                INTRODUCTION: Temperature is a key factor in microbial activity and is vital to the operation of anaerobic digestion systems.
                Analysis: Usually, the temperature should be between 35°C and 55°C. Different microbial communities have different adaptability to temperature, so the temperature needs to be controlled according to the specific situation.
                15. Reaction time:
                INTRODUCTION: Reaction time is the amount of time the waste remains in the anaerobic digestion system and affects the degradation rate and gas production of the waste.
                Analysis: reaction time adjustment can be used to optimize the rate of gas production and waste treatment efficiency, long residence time can improve the waste degradation rate.
                16、Added substances:
                Introduction: Carbon source, nitrogen source, microbial culture material, buffer, etc. are often added in anaerobic digestion.
                Analysis: Adequate addition of different substances can adjust the waste treatment process, improve gas production and degradation efficiency.
                In conclusion, anaerobic digestion system is a versatile waste treatment technology with important properties such as biodegradability, gas production characteristics, waste minimization and environmental friendliness. Understanding these properties can help to better understand and optimize the performance of anaerobic digestion systems.            
                `
            }else if(this.cls===3){
                pageText = `
                Impact of anaerobic digestion on biogas production
                Anaerobic digestion is an important waste treatment and biogas generation process with a variety of factors affecting gas output. The following is a detailed description of the factors and influences that affect gas production from anaerobic digestion, listed in points:
                1, the type of waste:
                Impact: different types of waste have different chemical composition and degradation difficulty, which directly affects the gas output.
                Analysis: the carbon, nitrogen, sulfur content of organic waste, solid content and the degradation difficulty of the waste is the main factor of gas production. Easily degradable organics in the waste usually produce more gas. Easily degradable organic wastes, such as food residues, usually produce more gas, while difficult to degrade wastes, such as lignocellulose, have less gas output.
                2. Organic loading rate:
                Impact: the organic loading rate indicates the mass of organic matter entering the reactor per unit of time, which has a direct impact on gas output.
                Analysis: higher organic loading rate usually leads to higher gas output, but in the loading rate is too high may trigger system instability.
                3. Temperature:
                IMPACT: Temperature is a key factor in microbial activity and has a significant effect on gas output rates.
                ANALYSIS: Higher temperatures usually promote microbial activity and increase gas output rates. However, too high a temperature may lead to microbial inhibition or death, typical temperature range between 35 ° C and 55 ° C.
                4. pH:
                Impact: The appropriate pH range is critical for microbial growth, activity and gas production performance.
                ANALYSIS: The pH of anaerobic digestion systems should normally be controlled in the neutral to slightly alkaline range to maintain microbial activity. pH deviations from the desired range may inhibit microbial activity and affect gas production. Typically the pH range should be between 6.5 and 8.0.
                5. Microbial population:
                IMPACT: Different species of microorganisms have different metabolic pathways and activities in anaerobic digestion and have different gas production capabilities.
                ANALYSIS: By adjusting the species and number of microbial communities, the degradation rate and gas output of waste can be influenced. Optimizing the structure and number of microbial communities is the key to improving gas production efficiency. The presence of methane-producing and acetic acid-producing bacteria is very important for gas production.
                6. Mixing degree and agitation:
                IMPACT: Mixing and agitation improves the contact between the waste and microorganisms and increases the efficiency of gas production. Good waste mixing helps maintain uniform temperature and pH conditions and promotes gas production.
                ANALYSIS: The right amount of mixing and agitation helps to disperse the waste uniformly, promotes microbial degradation, and increases the rate of gas production. Insufficient mixing may result in localized anaerobic waste and reduced gas output.
                7. Substrate concentration:
                Impact: substrate concentration refers to the concentration of organic matter in the waste, affecting the rate of gas output.
                Analysis: Higher substrate concentration usually leads to more gas output, but too high a concentration may lead to inhibition in the gas production pathway.
                8. Nitrogen source and carbon to nitrogen ratio:
                IMPACT: The addition of a nitrogen source can affect gas production and waste degradation. An appropriate carbon to nitrogen ratio can promote gas production, but an inappropriate ratio may inhibit gas production.
                ANALYSIS: An appropriate amount of nitrogen source helps to maintain an appropriate carbon to nitrogen ratio example and promotes methane production. An appropriate carbon to nitrogen ratio helps maintain microbial growth and waste decomposition, but an inappropriate ratio may lead to ammonia and nitrogen accumulation or excessive carbonization.
                9. Reactor design:
                IMPACT: Different types of anaerobic digestion reactors (e.g., complete mixed, fixed bed, etc.) have different gas yield efficiencies.
                ANALYSIS: Reactor types include completely mixed, fixed bed, and high solid phase reactors, etc. Their selection affects waste residence time and gas production rates. Selection of the appropriate reactor type depends on the nature of the waste and gas production requirements.
                10. Fermenters and additives:
                Impact: The addition of specific fermenters or additives can facilitate gas production or waste degradation. Additives such as microbial culture substances, buffers, etc. can affect microbial activity and waste decomposition.
                Analysis: Different additives can affect the efficiency of waste treatment and the rate of gas production, and the appropriate additives should be selected according to the needs. The use of the right amount of additives can improve the efficiency of gas production, but need to carefully control the amount of additives to avoid unnecessary costs and impact.
                11, moisture content:
                Impact: Moisture content affects the fluidity of waste and the growth of microorganisms. The right amount of moisture helps to maintain the proper dilute concentration of the waste and promotes gas production.
                ANALYSIS: Excessive or insufficient moisture may reduce the efficiency of gas output and moderate control of moisture content is required. Moisture should be controlled appropriately depending on the waste type and reactor type.
                12. Operating conditions:
                IMPACT: Operating conditions include residence time, temperature, and pH control.
                ANALYSIS: Adjustment of these operating conditions can optimize the rate of gas production and waste treatment efficiency, but should be adjusted on a case-by-case basis.
                In summary, the gas output of anaerobic digestion systems is affected by a variety of factors, including the nature of the waste, operating parameters, and microbial activity. Optimizing these factors can help improve system efficiency, reduce environmental impacts, and better achieve the goals of organic waste treatment and energy recovery.            
                `
            }else if(this.cls===4){
                pageText = this.endc;
            }
            return pageText
        },
        invLoading(){
            return !this.isLoading;
        },

    },
    watch:{
        rtd(){
            this.change_style(this.rtd)
        },
        userMsg(){
            this.tipsd = "In order to prevent problems such as multiple requests being sent at the same time, <br />please <b>refrain</b> from using chat boxes or other interruptions during the llama2 reply period."
        },
        cls(){
            console.log(111);
            if(this.cls === 4){
                this.isSend = false;
                this.rtd = this.cls;
                this.msgList[this.num]={cls:4,rtd:this.rtd,isUser:false}
            }else{
                this.isSend = true;
            }
        }
    },
    mounted(){
        this.create()
        axios
        .delete("http://127.0.0.1:8000/test/uploadpdf/")
        .then(res=>{
            console.log("have finished")
        })
        .catch(err=>{
            console.log(err)
        })
        let gptallcontent = 
        `Hello, I am ChatAD anaerobic digestion expert large language models! I can answer any questions you may have about your knowledge in the field of anaerobic digestion and give you literature sources.
        Now You can enter your own questions for Q&A and the model will automatically match your questions to the corresponding databases, or you can manually match knowledge bases after entering your questions. 
        In addition, the model also supports automatic uploading of literature for the Q&A function. 
        Come and interact with ChatAD!`
        // gptallcontent = this.md.render(gptallcontent);
        let idx = 0
        this.initinterval = setInterval(()=>{
            this.$set(this.msgList[this.msgList.length-1], 'gptinfo',this.msgList[this.msgList.length-1].gptinfo + gptallcontent[idx++]);
            this.$forceUpdate();
            if(idx >= gptallcontent.length){
                clearInterval(this.initinterval);
            }
        },50)
    }


}



</script>

<style lang="css">
.el-upload-dragger {
    border : 0px;
    margin:0px !important;
    background-color: rgba(0, 0, 0, 0.336) !important;
    width:250px !important;
}
.el-card__body{
    padding:0px !important;
}
.el-collapse-item__header{
    background-color: rgba(240, 248, 255, 0.355) !important;
    border:0px !important;
    outline: none !important;
    box-shadow: 0px 0px 0px 0px;
}

.el-collapse-item__content{
    background-color: rgba(61, 61, 61, 0.662) !important;
    height:300px;
    overflow-x: auto;
}

.el-avatar{
    background-color: #4e4d4e63 !important;
    border: 1px solid white !important;
}

</style>

<style lang="css" scoped>
.asidebutton{
    width:250px;
    height:80px;
    display: block;
    font-size:20px;
    margin-bottom: 20px;
    white-space: nowrap;
    color: white;
    font-style: italic;
    border:0px;
    background-color: rgba(184, 202, 202, 0.322);
    transition: background-color 0.5s,width 0.5s,font-size 0.5s;
    position: relative;
    z-index: 100;
}
.asidebutton:hover{
    font-size:25px;
    width:300px;
    background-color: aliceblue;
    color:rgba(0, 0, 0, 0.616);
    font-weight: bold;
}
.asidebutton_act{
    width:300px;
    height:80px;
    font-style: italic;
    margin-bottom: 20px;
    border:0px;
    font-size:25px;
    background-color: aliceblue;
    color:rgba(0, 0, 0, 0.616);
    font-weight: bold;
}

.el-textarea__inner:focus{
    box-shadow: 0 0 0 1px rgb(253, 166, 166) inset  !important;
}
.textareass{
    resize:none;
    font-size:20px;
    border:0px;
    border-radius:5px 0px 0px 5px;
    background-color: rgba(0, 0, 0, 0.67);
    color: aliceblue;
    padding:10px;
    vertical-align: middle;
    display: inline-block;
    width: 80%;
    height:100px;
}
.textareass::-webkit-scrollbar{
    display: none;
}
.textareass:focus{
    outline: none;
    box-shadow: 0px 0px 10px -2px rgb(1, 98, 184) ;
}
.chat-card::-webkit-scrollbar{
    display: none;
}
.pdflist::-webkit-scrollbar{
    display: none;
}
.pdf_highlight{
    background-color: rgba(183, 245, 245, 0.445);
}
.pdf_normal{
    background-color: rgba(240, 248, 255, 0);
}

.usercontent{
    background-color: rgba(210, 254, 255, 0.153);
    padding:20px;
    padding-bottom: 40px;
}

.usercontent:hover{
    background-color: rgba(54, 255, 228, 0.29);
}

.usercontent:active{
    background-color:  rgba(210, 254, 255, 0.153);
}

.showuploaded{
    font-size:25px;
    transition: font-size 0.3s;
    color:rgb(255, 255, 255);
}


.floatext{
    width:0px;
    font-size:0px;
    transition: width 0.5s;
}

.el-icon-plus:hover{
    color:rgba(255, 255, 255, 0.785);
    cursor: pointer;
    transform: scale(1.2);
    transition: transform 0.3s,color 0.3s;
}
.toupload:active{
    cursor: pointer;
}
</style>

