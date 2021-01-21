<template>
  <div class="animated fadeIn" style="padding 10px 10px 10px 10px">
    <CButton
      class="py-0"
      style="width: auto"
      v-if="car_plates.length > 0"
      @click="showColumnFilter = !showColumnFilter"
    >
      <CIcon :content="$options.freeSet.cilFilter" />
    </CButton>

    <CDataTable
      style="margin-top: 10px"
      border
      striped
      hover
      pagination
      :items="car_plates"
      :fields="fields"
      :column-filter="showColumnFilter"
      :items-per-page="10"
      :sorter="true"
    >
      <template #user_id="{ item }">
        <td align="center">{{ item.car_plate }}</td>
      </template>
      <template #start_date="{ item }">
        <td align="center">{{ item.start_date }}</td>
      </template>
      <template #end_date="{ item }">
        <td align="center">{{ item.end_date }}</td>
      </template>
    </CDataTable>
  </div>
</template>

<script>
import { freeSet } from "@coreui/icons";
import * as moment from "moment/moment";
export default {
  name: "CarPlate",
  freeSet,
  data() {
    return {
      showColumnFilter: false,

      // Register Car
      car_plate: "",
      start_date: "",
      end_date: "",
      car_plates: [],

      fields: [
        {
          key: "car_plate",
          label: "車牌",
          _style: "width: 10%",
        },
        {
          key: "start_date",
          label: "開始時間",
          _style: "width: 10%",
        },
        {
          key: "end_date",
          label: "結束時間",
          _style: "width: 10%",
        },
      ],
    };
  },

  created() {
    this.getCarPlates();
  },

  methods: {
    getCarPlates() {
      this.$http.get("http://localhost:8000/api/carPlate").then((res) => {
        this.car_plates = res.data;
      });
    },
  },
};
</script>