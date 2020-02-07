<template>
  <div id="overview">
    <h1>countryrank:<br/>World Overview</h1>
    <p class="herotext">
      <em>countryrank</em> is a simple aggregator and visualization of
      CSV data from some specific sources from data.worldbank.org. It's
      built specifically as a demo project of quick full stack
      development divided into a toy backend and an editable frontend.
    </p>
    <div class="filterarea">
      <input type="text" class="filterfield" placeholder="Search your country" />
    </div>
    <span v-for="country in jsondata.CountryYearIndicators" :key="country.id">
      <h2>
        <router-link
          :to="{ name: 'country', params: { code: country.code }}">
          {{ country.name }}
        </router-link>
      </h2>
      <div class="indicators-flex">
        <p class="indicator" v-for="ind in country.indicators" :key="ind.id">
            <strong>{{ ind.name }} {{ latestData(ind.data).year || "" }}</strong><br/>
            {{ latestData(ind.data).value || "No data available." }}
        </p>
        <p class="countrylink">
        <router-link
          :to="{ name: 'country', params: { code: country.code }}">
          Complete statistics about {{ country.name }} ➜
        </router-link>
        </p>
      </div>
    </span>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  components: {
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
      axios.get('/display_data/?limit=1').then(res => {
         this.jsondata = res.data;
      });
    },
    latestData: function(arr) {
      let val = arr[arr.length -1];
      if (val && val.hasOwnProperty('year')) {
        return val;
      } else {
        return {
          year: '',
          value: '',
        }
      }
    }
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
#overview {
  margin-top: 60px;
  margin: 60px 10%;
}
.indicator,
.countrylink {
  width: 40%;
  margin: 1% 3%;
}
.countrylink {
  text-align: right;
}
.countrylink a {
  margin: 10%;
  display: inline-block;
}
.indicators-flex {
  display: flex;
  flex-flow: row wrap;
}
.filterfield {
  width: 60%;
  padding: 1rem;
  border: 2px solid #eee;
  font-size: 120%;
  text-align: center;
}
.filterarea {
  text-align: center;
}
.herotext {
  margin: 3% 5%;
}
</style>
