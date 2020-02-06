<template>
  <div id="app">
    <div v-for="country in jsondata.CountryYearIndicators" :key="country.id">
      <CountryStats :country="country"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import CountryStats from './components/CountryStats';

export default {
  name: 'app',
  components: {
    CountryStats,
  },
  data: function () {
    return {
      jsondata: '',
    };
  },
  computed: {
  },
  methods: {
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
