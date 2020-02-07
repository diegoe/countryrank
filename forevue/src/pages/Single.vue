<template>
  <div id="single">
    <div v-for="country in jsondata.CountryYearIndicators" :key="country.id">
      <CountryStats :country="country"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import CountryStats from '../components/CountryStats';

export default {
  name: 'Single',
  components: {
    CountryStats,
  },
  props: [
    'code',
  ],
  data: function () {
    return {
      jsondata: '',
    };
  },
  computed: {
  },
  methods: {
    getJsonData: function() {
      if (this.code) {
        axios.get('/display_data/?country=' + this.code).then(res => {
           this.jsondata = res.data;
        });
      } else {
        axios.get('/display_data/?country=USA').then(res => {
           this.jsondata = res.data;
        });
      }
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
#single {
  margin-top: 60px;
  margin: 60px 10%;
}
.trendyblock {
  margin: auto;
  margin-right: 5%;
}
</style>
