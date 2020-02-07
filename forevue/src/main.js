import Vue from 'vue'
import VueRouter from 'vue-router';

import TrendChart from 'vue-trend-chart';

import Single from './pages/Single';
import Overview from './pages/Overview';

Vue.use(VueRouter);
Vue.use(TrendChart);

Vue.config.productionTip = false

const routes = [
  { path: '/', component: Overview },
  { path: '/country/:code', component: Single, props: true, name: 'country' },
];

const router = new VueRouter({
  routes: routes,
});

new Vue({
  router: router,
  render: (h) => h('router-view'),
}).$mount('#app')
