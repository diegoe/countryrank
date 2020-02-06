import Vue from 'vue'
import VueRouter from 'vue-router';

import TrendChart from 'vue-trend-chart';

import Home from './pages/Home';

Vue.use(VueRouter);
Vue.use(TrendChart);

Vue.config.productionTip = false

const routes = [
  { path: '/', component: Home },
];

const router = new VueRouter({
  routes: routes,
});

new Vue({
  router: router,
  render: (h) => h('router-view'),
}).$mount('#app')
