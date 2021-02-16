import Vue from 'vue'
import Router from 'vue-router'

// Containers
const TheContainer = () => import('@/containers/TheContainer')

// Views
const Dashboard = () => import('@/views/Dashboard')
const Driver = () => import('@/views/Driver')
const Car = () => import('@/views/Car')
const Tracking = () => import('@/views/Tracking')
const CarAnalysis = () => import('@/views/CarAnalysis')
const DriverAnalysis = () => import('@/views/DriverAnalysis')
const CarPlate = () => import('@/views/CarPlate')



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
      redirect: '/dashboard',
      component: TheContainer,
      children: [
        {
          path: '/',
          redirect: 'dashboard',
          component: {
            render(c) {
              return c('router-view')
            },
          },
          children: [
            {
              path: 'dashboard',
              component: Dashboard
            },
            {
              path: 'driver',
              component: Driver
            },
            {
              path: 'car',
              component: Car
            },
            {
              path: 'carPlate',
              component: CarPlate
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