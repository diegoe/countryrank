<template>
  <div id="app">
    <div v-for="item in jsondata.CountryYearIndicators" :key="item.id">
      <h2>{{ item.name }}</h2>
      <div v-for="ind in item.indicators" :key="ind.code" class="trendyblock">
        <h3>{{ ind.name }} ({{ yearRange(ind.data).from }} – {{ yearRange(ind.data).to }}) </h3>
        <TrendyChart :datasets="ind" :name="ind.name" :decimals="formats[ind.code]"/>
        <ChunkyTable :datasets="ind.data" :name="ind.name" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import TrendyChart from './components/TrendyChart';
import ChunkyTable from './components/ChunkyTable';

export default {
  name: 'app',
  components: {
    TrendyChart,
    ChunkyTable,
  },
  data: function () {
    return {
      jsondata: '',
      /*
       TODO: Ideally we could abstract this in the Indicator model on
       the backend, or we could simply have a bunch of purely visual
       components that inherit from Chunky and Trendy.
       */
      formats: {
        'EN.ATM.CO2E.PC': 5,
        'IP.PAT.RESD': 0,
        'SP.DYN.LE00.IN': 3,
        'IP.PAT.NRES': 0,
        'NY.GDP.MKTP.CD': 5,
        'SP.POP.TOTL': 0,
        'TX.VAL.TECH.MF.ZS': 5,
      },
    };
  },
  computed: {
  },
  methods: {
    yearRange: function(dataset) {
      if (!dataset) {
        return { from: 0, to: 0 };
      } else {
        return {
          from: dataset[0].year,
          to: dataset[dataset.length - 1].year,
        };
      }
    },
    getJsonData: function() {
      axios.get('/display_data/?country=PER').then(res => {
         this.jsondata = res.data;
      });
    },
  },
  mounted() {
    this.getJsonData();
  },
}
</script>

<style>
* {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#app {
  margin-top: 60px;
  margin: 60px 10%;
}
.trendyblock {
  margin: auto;
  margin-right: 5%;
}
</style>
