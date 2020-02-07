<template>
  <div class="trendychart">
    <p class="trendyp">
      <strong>{{ legend.year }}</strong><br/>
      {{ legend.value }}
    </p>
    <TrendChart :datasets="formattedDataset" :interactive="true" :min="0" @mouse-move="onMouseMove"/>
  </div>
</template>

<script>
import TrendChart from 'vue-trend-chart';

export default {
  name: 'TrendyChart',
  components: {
    TrendChart,
  },
  props: [
    'datasets',
    'name',
    'decimals',
  ],
  data: function() {
    return {
      currentLegend: null,
    };
  },
  computed: {
    legend: function() {
      return {
        year: this.currentLegend ? this.currentLegend.year : '',
        value: this.currentLegend ? this.currentLegend.value : '',
      };
    },
    formattedDataset: function() {
      let raw = this.datasets.data;
      let formatted = raw.map(x => {
        x.value = Number(x.value).toFixed(this.decimals);
        return x;
      });
      return [{
        data: formatted,
        fill: true,
        className: this.datasets.code.split('.').join(''),
      }];
    },
  },
  methods: {
    onMouseMove(params) {
      if (!params) {
        this.currentLegend = null;
        return;
      } else {
        this.currentLegend = {
          year: params.data[0].year,
          value: params.data[0].value,
        };
      }
    }
  },
}
</script>

<style>
.trendychart {
  /*
  width: 45%;
  display: inline-block;
  vertical-align: top;
  margin-right: 5%;
  */
}
.trendyp {
  height: 40px;
  display: block;
}
.ENATMCO2EPC,
.IPPATRESD,
.SPDYNLE00IN,
.IPPATNRES,
.NYGDPMKTPCD,
.SPPOPTOTL,
.TXVALTECHMFZS {
  /* Optional chart styling */
}
</style>
