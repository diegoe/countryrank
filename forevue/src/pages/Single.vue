<template>
  <div id="single">
    <h1>
      countryrank:
      <br/>
      {{ country.name }}
    </h1>
    <p class="herotext">
      Feel free to correct any incorrect value by double-clicking any
      number next to its corresponding year.
      <br/><br/>
      Statistics might be incomplete due to lack of reporting or missing
      records at the World Bank. Only the available information is
      presented.
      <br/><br/>
      <router-link
        :to="{ name: 'overview' }">
        ←  Back to World Overview
      </router-link>
    </p>
    <CountryStats :country="country"/>
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
      country: '',
    };
  },
  computed: {
  },
  methods: {
    getJsonData: function() {
      if (this.code) {
        axios.get('/display_data/?country=' + this.code).then(res => {
           this.jsondata = res.data;
           this.country = this.jsondata.CountryYearIndicators[this.code];
        });
      } else {
        axios.get('/display_data/?country=USA').then(res => {
           this.jsondata = res.data;
           this.country = res.data.CountryYearIndicators['USA'];
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
#single .herotext {
  margin: 3% 5%;
  margin-right: 10%;
}
</style>
