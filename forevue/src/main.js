import Vue from 'vue'
import App from './App.vue'
import TrendChart from 'vue-trend-chart';

Vue.use(TrendChart);
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
