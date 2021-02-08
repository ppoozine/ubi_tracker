<template>
  <div class="animated fadeIn" style="padding 10px 10px 10px 10px">
    <CRow>
      <CCol sm="3">
        <CCard>
          <CCardHeader>選擇駕駛及時間</CCardHeader>
          <CCardBody>
            <div>
              駕駛：
              <CSelect :options="usernames" :value.sync="select_username_options" />
              開始時間:
              <CInput v-model="start_date" type="date" />
              結束時間:
              <CInput v-model="end_date" type="date" />
              <CButton block color="success" @click="searchTrip()">確認</CButton>
            </div>
          </CCardBody>
        </CCard>

        <CCard>
          <CCardHeader>軌跡總覽</CCardHeader>
          <CCardBody style="height: 400px; overflow-y: scroll">
            <div class="trips" v-for="trip in trips" :key="trip.date">
              <CCard>
                <CCardBody borderColor="primary">
                  <div style="float: left">
                    日期：{{ trip.trip_date }}
                    <br />
                    ID：{{ trip.trip_id }}
                  </div>
                  <div style="float: right">
                    <CButton
                      color="primary"
                      variant="outline"
                      border
                      @click="drawTrip(trip.tracker_id, trip.trip_date, trip.trip_id)"
                      >Show</CButton
                    >
                  </div>
                </CCardBody>
              </CCard>
            </div>
          </CCardBody>
        </CCard>
      </CCol>
      <CCol sm="9">
        <CCard 旅行軌跡>
          <div class="google-map" id="map"></div>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>
<script>
import { freeSet } from "@coreui/icons";
export default {
  name: "Tracking",
  data() {
    return {
      username: "",
      usernames: [],
      select_username_options: "",
      start_date: "",
      end_date: "",

      trips: [],
      coordinates: [],
      lineCoordinates: [],

      map: null,
      line: null,
      // 預設為目前所有點的中心
      center: {
        lat: 24.91697,
        lng: 121.21245,
      },
    };
  },

  created() {
    this.getUsername();
  },

  mounted() {
    this.initMap();
  },

  methods: {
    getUsername() {
      this.$http.get("http://localhost:8000/api/username").then((res) => {
        for (var i = 0; i < res.data.length; i++) {
          this.usernames.push(res.data[i].username);
        }
        this.select_username_options = this.usernames[0];
      });
    },

    searchTrip() {
      this.username = this.select_username_options;
      this.start_date = this.start_date;
      this.end_date = this.end_date;
      this.$http
        .get(
          `http://localhost:8000/api/carTrip/${this.start_date}/${this.end_date}/${this.username}`
        )
        .then((res) => {
          this.trips = res.data;
        });
    },

    // 建立地圖
    initMap() {
      // 透過 Map 物件建構子建立新地圖 map 物件實例，並將地圖呈現在 id 為 map 的元素中
      this.map = new google.maps.Map(document.getElementById("map"), {
        // 設定地圖的中心點經緯度位置
        center: this.center,
        // 設定地圖縮放比例 0-20
        zoom: 10,
        // 限制使用者能縮放地圖的最大比例
        maxZoom: 20,
        // 限制使用者能縮放地圖的最小比例
        minZoom: 3,
        // 設定是否呈現右下角街景小人
        streetViewControl: false,
        // 設定是否讓使用者可以切換地圖樣式：一般、衛星圖等
        mapTypeControl: false,
      });
    },

    drawTrip(tracker_id, trip_date, trip_id) {
      this.initMap();
      console.log("追蹤器：" + tracker_id);
      console.log("日期：" + trip_date);
      console.log("ID：" + trip_id);

      this.$http
        .get(
          `http://localhost:8000/api/carTracking/${tracker_id}/${trip_date}/${trip_id}`
        )
        .then((res) => {
          this.coordinates = res.data;
          this.drawLine(this.coordinates);
          this.mapFitZoom(this.coordinates);
        });
    },

    drawLine(coordinates) {
      this.lineCoordinates = [];
      for (var i = 0; i < coordinates.length; i++) {
        this.lineCoordinates.push(
          new google.maps.LatLng(coordinates[i].latitude, coordinates[i].longitude)
        );
      }

      console.log(this.lineCoordinates);

      var lineSymbol = {
        path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW,
        strokeColor: "#393",
      };

      this.line = new google.maps.Polyline({
        path: this.lineCoordinates,
        icons: [
          {
            icon: lineSymbol,
            offset: "0%",
          },
          {
            icon: lineSymbol,
            offset: "25%",
          },
          {
            icon: lineSymbol,
            offset: "50%",
          },
          {
            icon: lineSymbol,
            offset: "75%",
          },
          {
            icon: lineSymbol,
            offset: "100%",
          },
        ],
        map: this.map,
      });
    },

    mapFitZoom(coordinates) {
      var bounds = new google.maps.LatLngBounds();
      for (var i = 0; i < coordinates.length; i++) {
        bounds.extend(
          new google.maps.LatLng(coordinates[i].latitude, coordinates[i].longitude)
        );
      }
      this.map.fitBounds(bounds);
    },
  },
};
</script>

<style scoped>
.google-map {
  width: 100%;
  height: 850px;
}
</style>
