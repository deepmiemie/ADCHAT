import VueRouter from 'vue-router'
import Vue from 'vue'
import Manage from "../components/Manage"
import Home from '../components/Home'
import Login from '../components/Login'
import Signup from '../components/Signup'
import Test from '../components/Test'
import Mychat from '../components/Mychat'
import Mymain from "../components/Chat/Mymain"

import Sup from "../components/SL/Sup"
import Sup1 from "../components/SL/SL_C/Sup1"
import Sup2 from "../components/SL/SL_C/Sup2"
import Sup3 from "../components/SL/SL_C/Sup3"

import Slbt from "../components/Slbt"
import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path:"/admin",
    name:"admin",
    component:Manage,
  },
  {
    path:"/mymain",
    name:"mymain",
    component:Mymain,
  },
  {
    path:"/mychat",
    name:"mychat",
    component:Mychat,
    children:[
      {
        path:"/",
        name:"slbt",
        component:Slbt
      },
      {
        path:"signup",
        name:"signup",
        component:Sup,
        children:[
          {
            path:"/",
            name:"signup1",
            component:Sup1,
          },
          {
            path:"signup2",
            name:"signup2",
            component:Sup2,
          },
          {
            path:"signup3",
            name:"signup3",
            component:Sup3,
          },
        ]
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to,from,next)=>{
  // console.log(to)
  if((to.name!=='mychat' || to.name!=='signup') && (to.meta.needLogin) ){
    console.log('对不起您需要登录...')
    if(store.state.isLogined){
      next()
    }else{
      next('/login')
    }
  }else{
    next()
  }
})

router

export default router
