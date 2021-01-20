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
        tracker_id = '';
        car_plate = '';
        create_date = today();
        error_msg = '';
        showCreateModal = true;
      "
    >
      <CIcon :content="$options.freeSet.cilPlus" />
      新增車輛
    </CButton>

    <CDataTable
      style="margin-top: 10px"
      border
      striped
      hover
      pagination
      :items="cars"
      :fields="fields"
      :column-filter="showColumnFilter"
      :items-per-page="10"
      :sorter="true"
    >
      <template #operations="{ item }">
        <td align="right">
          <CButton
            color="danger"
            variant="outline"
            class="py-0"
            @click="deleteCar(item.pk, item.car_plate)"
          >
            <CIcon :content="$options.freeSet.cilTrash" />
          </CButton>
        </td>
      </template>
      <template #user_id="{ item }">
        <td align="left">{{ item.user_id }}</td>
      </template>
      <template #tracker_id="{ item }">
        <td align="left">{{ item.tracker_id }}</td>
      </template>
      <template #car_plate="{ item }">
        <td align="center">{{ item.car_plate }}</td>
      </template>
      <template #create_date="{ item }">
        <td align="center">{{ item.create_date }}</td>
      </template>
      <template #active="{ item }">
        <td align="center">
          <CSwitch
            style="padding-top: 3px"
            color="info"
            shape="pill"
            :checked="item.active"
            v-bind="{ labelOn: 'Y', labelOff: 'N' }"
            @update:checked="
              item.active = !item.active;
              updateActive(item.pk, item.active);
            "
          />
        </td>
      </template>
    </CDataTable>

    <CModal :show.sync="showCreateModal" color="dark">
      <template v-slot:header>
        新增車輛
        <CButtonClose @click="showCreateModal = false" style="width: auto" />
      </template>

      <CSelect
        prepend="姓名"
        :options="usernames"
        :value.sync="select_username_options"
      />
      <CInput v-model="tracker_id" prepend="追蹤器編號" />
      <CInput v-model="car_plate" prepend="車牌" />
      <CInput v-model="create_date" prepend="創建時間" type="date" />
      <CSelect
        prepend="狀態"
        :options="active_options"
        :value.sync="select_active_options"
      />

      <template v-slot:footer>
        <p class="text-danger">{{ error_msg }}</p>
        <CButton
          size="sm"
          color="success"
          @click="createCar()"
          class="modal_footer_btn"
          >確認</CButton
        >
        <CButton
          size="sm"
          color="secondary"
          @click="showCreateModal = false"
          class="modal_footer_btn"
          >取消</CButton
        >
      </template>
    </CModal>
  </div>
</template>

<script>
import { freeSet } from "@coreui/icons";
import * as moment from "moment/moment";
export default {
  name: "Car",
  freeSet,
  data() {
    return {
      showColumnFilter: false,
      showCreateModal: false,
      showModifyModal: false,

      // Register Car
      username: "",
      tracker_id: "",
      car_plate: "",
      create_date: "",
      active: "",
      error_msg: "",

      active_options: ["啟用", "尚未啟用"],
      select_active_options: "啟用",
      cars: [],
      usernames: [],
      select_username_options: "",
      fields: [
        {
          key: "user_id",
          label: "使用者編號",
          _style: "width: 10%",
        },
        {
          key: "tracker_id",
          label: "追蹤器編號",
          _style: "width: 10%",
        },
        {
          key: "car_plate",
          label: "車牌",
          _style: "width: 10%",
        },
        {
          key: "create_date",
          label: "創建時間",
          _style: "width: 10%",
        },
        {
          key: "active",
          label: "狀態",
          _style: "width: 5%",
        },
        {
          key: "operations",
          label: "",
          filter: false,
          sorter: false,
          _style: "width: 1%",
        },
      ],
    };
  },

  created() {
    this.getCars();
    this.getUsername();
  },

  methods: {
    today() {
      return moment().format("YYYY-MM-DD");
    },

    getUsername() {
      this.$http.get("http://localhost:8000/api/username").then((res) => {
        for (var i = 0; i < res.data.length; i++) {
          this.usernames.push(res.data[i].username);
        }
        this.select_username_options = this.usernames[0];
      });
    },

    getCars() {
      this.$http.get("http://localhost:8000/api/car").then((res) => {
        this.cars = res.data;
      });
    },

    createCar() {
      this.username = this.select_username_options;
      console.log("car:" + this.username);
      this.tracker_id = this.tracker_id.trim();
      this.car_plate = this.car_plate.trim();

      if (this.username == "") {
        this.error_msg = "姓名未填寫";
        return;
      }
      if (this.tracker_id == "") {
        this.error_msg = "追蹤器編號未填寫";
        return;
      }
      if (this.car_plate == "") {
        this.error_msg = "車牌未填寫";
        return;
      }

      if (this.select_active_options === "啟用") {
        this.active = true;
      } else if (this.select_active_options === "尚未啟用") {
        this.active = false;
      }

      let param = {
        username: this.username,
        tracker_id: this.tracker_id,
        car_plate: this.car_plate,
        create_date: this.create_date,
        active: this.active,
      };

      this.$http
        .post("http://localhost:8000/api/car", param)
        .then((res) => {
          this.showCreateModal = false;
          this.getCars();
        })
        .catch((error) => {
          this.error_msg = error.response.data.detail;
        });
    },

    deleteCar(pk, car_plate) {
      if (confirm(`確定刪除 '${car_plate}'?`))
        this.$http
          .delete(`http://localhost:8000/api/car/${pk}`)
          .then((res) => {
            this.getCars();
          })
          .catch((error) => {
            this.getCars();
          });
    },

    updateActive(pk, active) {
      let param = {
        active: active,
      };
      this.$http
        .put(`http://localhost:8000/api/car/${pk}`, param)
        .then((res) => {
          this.getCars();
        });
    },
  },
};
</script>