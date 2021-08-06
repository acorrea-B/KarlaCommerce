import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import store from '@/store'
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import("@/views/Login.vue")
    },
    {
      path: '/shop',
      name: 'ShoppingCart',
      component: () => import("@/views/ShoppingCart.vue")
    },
    {
      path: '/purchasepayment',
      name: 'PyamentConfirm',
      component: () => import("@/views/Purchase/PaymentConfirm.vue"),
      props:{default: true, 
        data: route => ({ purchase: route.query.purchase,
                     }),
        },
    },
    {
      path: '/purchases',
      name: 'PurchasesOperator',
      component: () => {
        if (store.getters.auth) {
          return import("@/views/Operator/Purchases.vue");
        } else {
          return import("@/views/Login.vue");
          
        }
      }
     
    },
    {
      path: '/purchase',
      name: 'PurchaseConfirm',
      component: () => {
        if (store.getters.purchase) {
          return import("@/views/Purchase/PurchaseConfirm.vue");
        } else {
          return import("@/views/ShoppingCart.vue");
        }
      }
    },
    {
      path: '/products',
      name: 'products',
      component: () => import("@/views/Products.vue")
    },
    {
      path: '/error-404',
      name: 'error-404',
      component: () => import('@/views/error/Error404.vue'),
      meta: {
        layout: 'full',
      },
    },
    {
      path: '*',
      redirect: 'error-404',
    },
  ],
})

export default router