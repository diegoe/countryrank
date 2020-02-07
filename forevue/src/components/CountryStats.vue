<template>
  <div>
    <h2>{{ country.name }}</h2>
    <div v-for="ind in country.indicators" :key="ind.code" class="trendyblock">
      <div v-if="ind.data.length > 1">
        <h3>{{ ind.name }} ({{ yearRange(ind.data).from }} – {{ yearRange(ind.data).to }}) </h3>
        <TrendyChart
          :datasets="ind"
          :name="ind.name"
          :decimals="formats[ind.code]"
          />
        <ChunkyTable
          :datasets="ind.data"
          :name="ind.name"
          v-on:update:datasets="updateDatasets"
          />
      </div>
    </div>
  </div>
</template>

<script>
import TrendyChart from './TrendyChart';
import ChunkyTable from './ChunkyTable';

export default {
  name: 'app',
  components: {
    TrendyChart,
    ChunkyTable,
  },
  props: [
    'country',
  ],
  data: function () {
    return {
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
      if (!dataset ||
          dataset.length < 1 ||
          !dataset[0].hasOwnProperty('year')) {
        return { from: 0, to: 0 };
      } else {
        return {
          from: dataset[0].year,
          to: dataset[dataset.length - 1].year,
        };
      }
    },
    updateDatasets: function(patch) {
      let el = 0;
      for(let i in this.country.indicators) {
        let tmp = this.country.indicators[i].data.find(x => x.id == patch.id);
        if (tmp)
          el = tmp;
      }

      el.value = patch.value;
    }
  },
  mounted() {
  },
}
</script>

<style>
.trendyblock {
  margin: auto;
  margin-right: 5%;
}
</style>

