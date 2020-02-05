<template>
  <div id="app">
    <div v-for="item in jsondata.CountryYearIndicators" :key="item.code">
      <h2>{{ item.name }}</h2>
      <div v-for="ind in item.indicators" :key="ind.code" class="trendyblock">
        <h4>{{ ind.name }}</h4>
        <TrendyChart :datasets="[ind.chartdata]" />
      </div>
      <table class="trendytable">
        <tbody>
          <tr v-for="i in item.indicators" :key="i.code">
            <td>
              <h3>{{ i.name }}</h3>
              <tr v-for="ind in i.data" :key="ind.year">
                <td>
                  {{ ind.year }}
                </td>
                <td>
                  {{ ind.value }}
                </td>
              </tr>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import TrendyChart from './components/TrendyChart';

export default {
  name: 'app',
  components: {
    TrendyChart,
  },
  data: function () {
    return {
      jsondata: '',
      currentLegend : null,
    };
  },
  computed: {
    legend: function() {
      return {
        year: this.currentLegend ? this.currentLegend.year : '',
        value: this.currentLegend ? this.currentLegend.value : '',
      };
    }
  },
  mounted() {
    axios.get('/display_data/?country=PER').then(res => {
       this.jsondata = res.data;
      });
  },
  methods: {
    onMouseMove(params) {
      if (!params) {
        return;
      }
      this.currentLegend = {
        year: params.data[0].year,
        value: params.data[0].value,
      };
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
  margin: 60px 10%;
}
.trendyblock {
  width: 45%;
  margin: auto;
  margin-right: 5%;
  display: inline-block;
}
.trendytable {
  /*
  margin-left: 5%;
  width: 45%;
  display: inline-block;
  */
}
</style>
