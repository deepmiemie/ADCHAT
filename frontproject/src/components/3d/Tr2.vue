<template>
    <div ref="threecontent"  style="display: inline-block;" @mouseover="cht(1)" @mouseout="cht(0)" >
    </div>
</template>
<script>
import * as THREE from 'three'
import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';
import { FontLoader } from 'three/addons/loaders/FontLoader.js';
/// <reference path="node_modules/@types/three/src/Three.d.ts" />
/// <reference path="node_modules/@types/three/src/constants.d.ts" />
/// <reference path="node_modules/@types/three/src/Three.Legacy.d.ts" />
/// <reference path="node_modules/@types/three/src/utils.d.ts" />
export default {
    name:"Tr2",
    data(){
        return {
            scene:new THREE.Scene(), //创建场景
            camera:new THREE.PerspectiveCamera(75,window.innerWidth / window.innerHeight,0.1,1000), //创建相机
            renderer:new THREE.WebGLRenderer({alpha:true}), //创建渲染器
            fsize:0.2,
        }
    },
    methods: {

        cht(type){
            // console.log(this.cube_p.children[2].geometry)
            if(type==1){
                this.inverval = setInterval(() => {
                    this.fsize += 0.005;
                    this.scene.remove(this.cube_p);
                    this.createBox(this.fontconstent)
                    if(this.fsize >= 0.25){
                        clearInterval(this.inverval);
                    }
                }, 10);

            }else{
                this.fsize = 0.2;
                this.scene.remove(this.cube_p);
                this.createBox(this.fontconstent)
            }


        },
        createBox(fontcontent){
            const gl = new THREE.BoxGeometry(1.3, 0.1, 0.8 ); // 定义几何体类型

            const ml = new THREE.LineBasicMaterial({
                transparent:true,
                opacity:0.8,
                color:"#2C425E"

            }); //定义线条材质

            // 给出立方体
            const cube = new THREE.Mesh(gl,ml);

            // 添加边框
            const edges = new THREE.EdgesGeometry(gl);
            const ll = new THREE.LineBasicMaterial({ color: '#36ABA7', linewidth: 10 });  // black color for the edges
            const ls = new THREE.LineSegments(edges, ll);

                        
            this.cube_p = new THREE.Object3D();
            this.cube_p.add(cube);
            this.cube_p.add(ls);

            // 添加字体
            const loader = new FontLoader();
            loader.load( 'http://127.0.0.1:8000/media/fonts/helvetiker_bold.typeface.json', (font)=>{
                const tx = new TextGeometry( `${fontcontent}`, {
                        font: font,
                        size: this.fsize,
                        height: 0.03
                    } );
                    let tm = new THREE.MeshBasicMaterial({ color: "#C0C1C3" });
                    const txm = new THREE.Mesh(tx,tm);
                    txm.position.set(this.x,0.15,0.08);
                    txm.rotation.x=80;
                    this.cube_p.add(txm);
                } );
            
            this.scene.add(this.cube_p)

        },
        createLine(){
            const points = [];
            points.push(new THREE.Vector3(0,0,0));
            points.push(new THREE.Vector3(0,2,0));
            points.push(new THREE.Vector3(1,2,0));
            const gl = new THREE.BufferGeometry().setFromPoints(points); // 定义几何体类型
            const ml = new THREE.LineBasicMaterial({color:0x0000ff}); //定义线条材质

            // 给出线条
            this.line = new THREE.Line(gl,ml);
            this.scene.add(this.line);
        },
        
        creatFont(){

        },


        animate(){
            requestAnimationFrame(this.animate);
            // this.controls.update(); // 启动阻尼时
            // 设置动画
            if(this.cube_p.rotation.x <= 0.2 && this.isl == 1){
                this.cube_p.rotation.x += 0.001;
            }else if(this.isl != 2){
                this.isl = 2;
            }

            if(this.cube_p.rotation.x > -0.2 && this.isl == 2){
                this.cube_p.rotation.x -= 0.001;
            }else if(this.isl != 1){
                this.isl = 1;
            }

            // 渲染器对场景和摄像头进行渲染
            this.renderer.render(this.scene,this.camera);
        },
    },
    props:["fontconstent","x"],
    mounted() {

        
        // this.renderer.setSize(window.innerWidth,window.innerHeight);
        this.renderer.setSize(400,200)

        this.camera.position.set(0,1,0);
        this.camera.lookAt(0,0,0);

        this.$refs.threecontent.appendChild(this.renderer.domElement);

        this.createBox(this.fontconstent);

        this.isl = 1
        this.cube_p.rotation.x = 0;
        this.cube_p.rotation.y = 0;

        // 实现循环动画
        this.animate();
    },
}
</script>
<style lang="css">
    
</style>