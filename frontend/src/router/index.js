import Vue from 'vue'
import Router from 'vue-router'

// Containers
const TheContainer = () => import('@/containers/TheContainer')

// Views
const Driver = () => import('@/views/Driver')
const Car = () => import('@/views/Car')
const Tracking = () => import('@/views/Tracking')
const CarAnalysis = () => import('@/views/CarAnalysis')
const DriverAnalysis = () => import('@/views/DriverAnalysis')



Vue.use(Router)

export default new Router({
  mode: 'hash', // https://router.vuejs.org/api/#mode
  linkActiveClass: 'active',
  scrollBehavior: () => ({ y: 0 }),
  routes: configRoutes()
})

function configRoutes () {
  return [
    {
      path: '/',
      redirect: '/driver',
      component: TheContainer,
      children: [
        {
          path: '/',
          redirect: 'driver',
          component: {
            render(c) {
              return c('router-view')
            },
          },
          children: [
            {
              path: 'driver',
              component: Driver
            },
            {
              path: 'car',
              component: Car
            },
            {
              path: 'tracking',
              component: Tracking
            },
            {
              path: 'carAnalysis',
              component: CarAnalysis
            },
            {
              path: 'driverAnalysis',
              component: DriverAnalysis
            }
          ]
        }
      ]
    }
  ]
}