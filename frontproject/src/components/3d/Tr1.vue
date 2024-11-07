<template>
    <div ref="threecontent">
    </div>
</template>
<script>
import * as THREE from 'three'

/// <reference path="node_modules/@types/three/src/Three.d.ts" />
/// <reference path="node_modules/@types/three/src/constants.d.ts" />
/// <reference path="node_modules/@types/three/src/Three.Legacy.d.ts" />
/// <reference path="node_modules/@types/three/src/utils.d.ts" />
export default {
    name:"Tr1",
    data(){
        return {
            scene:new THREE.Scene(), //创建场景
            camera:new THREE.PerspectiveCamera(75,window.innerWidth / window.innerHeight,0.1,1000), //创建相机
            renderer:new THREE.WebGLRenderer(), //创建渲染器
        }
    },
    methods: {
        createBox(){
            const gl = new THREE.BoxGeometry( 1, 1, 1 ); // 定义几何体类型
            const ml = new THREE.LineBasicMaterial({color:0x0000ff}); //定义线条材质

            // 给出立方体
            this.cube = new THREE.Mesh(gl,ml);
            this.scene.add(this.cube);
            this.camera.position.z = 5;
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
        
        createStar(){
            const stargeo = new THREE.BufferGeometry() //定义几何体类型为点状
            const starmat = new THREE.PointsMaterial({
                color:0xFFFF,
                size:0.05,
                transparent:true,
                opacity:0.7,
                blending:THREE.AdditiveBlending
            }) //定义星星类型

            // 定义星星位置
            const vertices = [];
            for (let i = 0; i < 5000; i++) {
                const x = (Math.random() - 0.5) * 15;
                const y = (Math.random() - 0.5) * 15;
                const z = (Math.random() - 0.5) * 15;
                vertices.push(x, y, z);
            }
            stargeo.setAttribute('position',new THREE.Float32BufferAttribute(vertices,3));

            this.star = new THREE.Points(stargeo,starmat);
            this.scene.add(this.star);
            
        },

        animate(){
            requestAnimationFrame(this.animate);

            // 设置几何体动画
            this.star.rotation.x += 0.0003;
            this.star.rotation.y += 0.0003;
            this.star.rotation.z += 0.0003;

            // this.controls.update(); // 启动阻尼时

            // 渲染器对场景和摄像头进行渲染
            this.renderer.render(this.scene,this.camera);
        },
    },
    mounted() {
        // this.renderer.setSize(window.innerWidth,window.innerHeight);
        this.renderer.setSize(1690,1000)
        this.camera.position.set( 0, 0, 0 );
        this.$refs.threecontent.appendChild(this.renderer.domElement);

        this.createStar();
        // 实现循环动画
        this.animate();
    },
}
</script>
<style lang="css">
    
</style>