<template>
  <div>
    <div v-show="edit == false">
      <label @dblclick="editing">
        {{ backvalue }}
      </label>
    </div>
    <input type="text"
      ref="cellinput"
      class="editablecell"
      v-bind:size="backvalue.length"
      v-show="edit == true"
      v-model="backvalue"
      v-on:focus="focused"
      v-on:blur="blurred"
      v-on:keyup.enter="edit = false"/>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'EditableCell',
  components: {
  },
  props: [
    'value',
    'objid',
  ],
  data: function() {
    return {
      edit: false,
      changedValue: undefined,
    };
  },
  computed: {
    jsonpath: function() {
      // TODO: This drops the ball on being reusable
      return "/Indicators/" + this.objid + "/value";
    },
    backvalue: {
      get: function() {
        return this.changedValue ? this.changedValue : this.value.toString();
      },
      set: function(changed) {
        this.$emit('input', changed);
        this.changedValue = changed;
      },
    },
  },
  methods: {
    editing: function() {
      this.edit = true;
      this.$nextTick(() => this.$refs.cellinput.focus());
    },
    focused: function() {
      return true;
    },
    blurred: function() {
      this.edit = false;
      let patch = {
        'op': 'replace',
        'path': this.jsonpath,
        'value': this.backvalue,
      };

      window.console.log(patch);
      axios.patch('/display_data/', patch).then(res => {
        window.console.log(res.data);
      });
    },
  },
}
</script>

<style>
.editablecell {
  font-size: 100%;
}
</style>
