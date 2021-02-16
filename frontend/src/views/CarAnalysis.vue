<template>
  <div class="animated fadeIn" style="padding 10px 10px 10px 10px">
    <h1>車輛數據分析</h1>
    <CNav variant="pills">
      <CSelect
        style="height: 10%; width: 20%; display: inline-block"
        prepend="車牌："
        :options="car_plates"
        :value.sync="select_car_plate_options"
      />
      <CInput
        style="height: 10%; width: 20%; display: inline-block"
        prepend="開始時間："
        v-model="start_date"
        type="date"
      />
      <CInput
        style="height: 10%; width: 20%; display: inline-block"
        prepend="結束時間："
        v-model="end_date"
        type="date"
      />
      <CButton
        style="height: 10%; width: 5%; display: inline-block"
        color="success"
        @click="searchAnalysis()"
        >搜尋</CButton
      >
    </CNav>
    <div>
      <CRow>
        <CCol lg="6">
          <CCard>
            <CCardBody>
              <CChartBar
                style="height: 300px"
                :datasets="[
                  {
                    data: [10, 22, 34, 46, 58, 70, 46, 23, 45, 78, 34, 12],
                    backgroundColor: '#E55353',
                    label: 'Sales',
                  },
                ]"
                labels="months"
                :options="{ maintainAspectRatio: false }"
              />
            </CCardBody>
          </CCard>
        </CCol>

        <CCol lg="6">
          <CCard>
            <CCardBody>
              <CChartRadar
                style="height: 300px"
                :datasets="[
                  {
                    data: [10, 22, 34, 46, 58, 70, 46, 23, 45, 78, 34, 12],
                    backgroundColor: '#E55353',
                    label: 'Sales',
                  },
                ]"
                labels="months"
                :options="{ maintainAspectRatio: false }"
              />
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
      <CRow>
        <CCol lg="6">
          <CCard>
            <CCardBody>
              <CChartPie
                style="height: 300px"
                :datasets="[
                  {
                    data: [10, 22, 34, 46, 58, 70, 46, 23, 45, 78, 34, 12],
                    backgroundColor: '#E55353',
                    label: 'Sales',
                  },
                ]"
                labels="months"
                :options="{ maintainAspectRatio: false }"
              />
            </CCardBody>
          </CCard>
        </CCol>

        <CCol lg="6">
          <CCard>
            <CCardBody>
              <CChartLine
                style="height: 300px"
                :datasets="[
                  {
                    data: [10, 22, 34, 46, 58, 70, 46, 23, 45, 78, 34, 12],
                    backgroundColor: '#E55353',
                    label: 'Sales',
                  },
                ]"
                labels="months"
                :options="{ maintainAspectRatio: false }"
              />
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
    </div>
  </div>
</template>
<script>
import { freeSet } from "@coreui/icons";
export default {
  name: "CarAnalysis",
  freeSet,
  data() {
    return {
      car_plates: [],
    };
  },
};
</script>
