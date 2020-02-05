<template>
  <div class="trendychart">
    <p class="trendyp">
      <strong>{{ legend.year }}</strong><br/>
      {{ legend.value }}
    </p>
    <TrendChart :datasets="datasets" :interactive="true" :min="0" @mouse-move="onMouseMove">
    </TrendChart>
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
  ],
  data: function() {
    return {
      currentLegend : null,
    };
  },
  computed: {
    legend: function() {
      return {
        year: this.currentLegend ? this.currentLegend.year : '',
        value: this.currentLegend ? this.currentLegend.value : '',
      };
    },
    yearRange: function() {
      return {
        from: 0,
        to: 0,
      }
    },
  },
  methods: {
    onMouseMove(params) {
      if (!params) {
        this.currentLegend = null;
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
</style>
