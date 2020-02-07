<template>
  <div>
    <table class="chunkytable" v-for="(ind) in chunk(datasets)" :key="ind.id">
      <tbody>
        <tr v-for="i in ind" :key="i.id">
          <td>
            <label>
              {{ i.year }}
            </label>
          </td>
          <td>
            <EditableCell
              :value="i.value"
              :objid="i.id"
              v-on:update:value="updateValue"
              />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import EditableCell from './EditableCell';

export default {
  name: 'ChunkyTable',
  components: {
    EditableCell,
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
    chunk: function(arr) {
      let chunkSize=10;
      let  R = [];
      for (let i=0,len=arr.length; i<len; i+=chunkSize) {
        R.push(arr.slice(i,i+chunkSize));
      }
      return R;
    },
    updateValue: function(patch) {
      this.$emit('update:datasets', patch);
    }
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
