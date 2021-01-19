<template>
  <div class="animated fadeIn" style="padding 10px 10px 10px 10px">
    <CButton
      class="py-0"
      style="width: auto"
      v-if="cars.length > 0"
      @click="showColumnFilter = !showColumnFilter"
    >
      <CIcon :content="$options.freeSet.cilFilter" />
    </CButton>
    <CButton
      shape="pill"
      variant="outline"
      color="dark"
      class="py-0"
      style="width: auto"
      @click="
        idnumber = '';
        username = '';
        sex = '';
        addr = '';
        email = '';
        phone = '';
        user_id = '';
        showCreateModal = true;
      "
    >
      <CIcon :content="$options.freeSet.cilPlus" />
      新增使用者
    </CButton>
  </div>
</template>

<script>
import { freeSet } from '@coreui/icons';
export default {
};
</script>