<template>
  <div id="overview">
    <table>
      <tr v-for="country in jsondata.CountryYearIndicators" :key="country.id">
        <td>
          <h2>
            <router-link
              :to="{ name: 'country', params: { code: country.code }}">
              {{ country.name }}
            </router-link>
          </h2>
        </td>
        <td>
          <div class="indicator" v-for="ind in country.indicators" :key="ind.id">
            <strong>{{ ind.name}}<br/>
            {{ latestData(ind.data).year }}</strong><br/>
            {{ latestData(ind.data).value }}
          </div>
        </td>
      </tr>
    </table>
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
.indicator {
  display: inline-block;
  width: 15%;
  margin: 3% 3%;
}
</style>
