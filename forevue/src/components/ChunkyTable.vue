<template>
  <div>
    <table class="chunkytable" v-for="(ind,index) in chunk(datasets)" :key="index">
      <tbody>
        <tr v-for="i in ind" :key="i.id">
          <td>{{ i.year }}</td>
          <td>{{ i.value }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ChunkyTable',
  components: {
  },
  props: [
    'datasets',
    'name',
  ],
  data: function() {
    return {
    };
  },
  computed: {
  },
  methods: {
    chunk: function chunk(arr) {
      let chunkSize=10;
      let  R = [];
      for (let i=0,len=arr.length; i<len; i+=chunkSize) {
				R.push(arr.slice(i,i+chunkSize));
      }
      return R;
    },
  },
}
</script>

<style>
.chunkytable {
  margin-bottom: 2%;
  margin-right: 5%;
  display: inline-block;
  vertical-align: top;
}
.chunkytable tr td:first-child {
  font-weight: bold;
}
</style>
