<template>
  <div class="animated fadeIn" style="padding: 10px 10px 10px 10px">
    <CButton
      class="py-0"
      style="width: auto"
      v-if="users.length > 0"
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

    <div v-if="users.length > 0">
      <CDataTable
        style="margin-top: 10px"
        border
        striped
        hover
        pagination
        :items="users"
        :fields="fields"
        :column-filter="showColumnFilter"
        :items-per-page="10"
        :sorter="true"
      >
        <template #operations="{ item }">
          <td align="right">
            <CButton
              color="primary"
              variant="outline"
              class="py-0"
              @click="
                clickUpdateUser(
                  item.pk,
                  item.idnumber,
                  item.username,
                  item.sex,
                  item.addr,
                  item.email,
                  item.phone
                )
              "
            >
              <CIcon :content="$options.freeSet.cilPencil" />
            </CButton>
            <br />
            <CButton
              color="danger"
              variant="outline"
              class="py-0"
              @click="deleteUser(item.pk, item.username)"
            >
              <CIcon :content="$options.freeSet.cilTrash" />
            </CButton>
          </td>
        </template>

        <template #idnumber="{ item }">
          <td align="center">{{ item.idnumber }}</td>
        </template>

        <template #username="{ item }">
          <td align="center">{{ item.username }}</td>
        </template>

        <template #sex="{ item }">
          <td align="center">{{ item.sex }}</td>
        </template>

        <template #addr="{ item }">
          <td align="left">{{ item.addr }}</td>
        </template>

        <template #email="{ item }">
          <td align="right">{{ item.email }}</td>
        </template>

        <template #phone="{ item }">
          <td align="right">{{ item.phone }}</td>
        </template>

        <template #user_id="{ item }">
          <td align="right">{{ item.user_id }}</td>
        </template>
      </CDataTable>
    </div>

    <!-- 新增使用者 -->
    <CModal :show.sync="showCreateModal" color="dark">
      <template v-slot:header>
        新增使用者
        <CButtonClose @click="showCreateModal = false" style="width: auto" />
      </template>

      <CInput v-model="idnumber" prepend="身分證字號" />
      <CInput v-model="username" prepend="姓名" />
      <CSelect
        prepend="性別"
        :options="sex_options"
        :value.sync="select_sex_options"
      />
      <CInput v-model="addr" prepend="地址" />
      <CInput v-model="email" prepend="電子郵件" />
      <CInput v-model="phone" prepend="手機號碼" />

      <template v-slot:footer>
        <p class="text-danger">{{ error_msg }}</p>
        <CButton
          size="sm"
          color="success"
          @click="insertUser()"
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

    <!-- 修改使用者 -->
    <CModal :show.sync="showModifyModeal" color="dark">
      <template v-slot:header>
        修改個人資料
        <CButtonClose @click="showModifyModeal = false" style="width: auto" />
      </template>

      <CInput v-model="idnumber" prepend="身分證字號" disabled />
      <CInput v-model="username" prepend="姓名" disabled />
      <CSelect
        prepend="性別"
        :options="sex_options"
        :value.sync="select_sex_options"
        disabled
      />
      <CInput v-model="addr" prepend="地址" />
      <CInput v-model="email" prepend="電子郵件" />
      <CInput v-model="phone" prepend="手機號碼" />

      <template v-slot:footer>
        <p class="text-danger">{{ error_msg }}</p>
        <CButton
          size="sm"
          color="success"
          @click="updateUser()"
          class="modal_footer_btn"
          >確認</CButton
        >
        <CButton
          size="sm"
          color="secondary"
          @click="showModifyModeal = false"
          class="modal_footer_btn"
          >取消</CButton
        >
      </template>
    </CModal>
  </div>
</template>

<script>
import { freeSet } from "@coreui/icons";
export default {
  name: "Driver",
  freeSet,

  data() {
    return {
      showColumnFilter: false,
      showCreateModal: false,
      showModifyModeal: false,

      // Register User
      idnumber: "",
      username: "",
      sex: "",
      addr: "",
      email: "",
      phone: "",
      user_id: "",
      error_msg: "",

      sex_options: ["男", "女"],
      select_sex_options: "男",
      users: [],
      fields: [
        {
          key: "idnumber",
          label: "身分證字號",
          _style: "width: 10%",
        },
        {
          key: "username",
          label: "姓名",
          _style: "width: 10%",
        },
        {
          key: "sex",
          label: "性別",
          _style: "width: 10%",
        },
        {
          key: "addr",
          label: "地址",
        },
        {
          key: "email",
          label: "電子郵件",
        },
        {
          key: "phone",
          label: "手機號碼",
        },
        {
          key: "user_id",
          label: "使用者編號",
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
    this.getUsers();
  },

  methods: {
    getUsers() {
      this.$http.get("http://localhost:8000/api/user").then((res) => {
        this.users = res.data;
      });
    },

    insertUser() {
      this.idnumber = this.idnumber.trim();
      this.username = this.username.trim();
      this.addr = this.addr.trim();
      this.email = this.email.trim();
      this.phone = this.phone.trim();
      if (this.idnumber == "") {
        this.error_msg = "身分證字號未填寫";
        return;
      }
      if (this.username == "") {
        this.error_msg = "姓名未填寫";
        return;
      }
      if (this.addr == "") {
        this.error_msg = "地址未填寫";
        return;
      }
      if (this.email == "") {
        this.error_msg = "電子郵件未填寫";
        return;
      }
      if (this.phone == "") {
        this.error_msg = "手機號碼未填寫";
        return;
      }
      if (this.select_sex_options === "男") {
        this.sex = "男";
      } else if (this.select_sex_options === "女") {
        this.sex = "女";
      }
      let param = {
        idnumber: this.idnumber,
        username: this.username,
        sex: this.sex,
        addr: this.addr,
        email: this.email,
        phone: this.phone,
      };
      this.$http
        .post("http://localhost:8000/api/user", param)
        .then((res) => {
          // console.log(res);
          this.showCreateModal = false;
          this.getUsers();
        })
        .catch((error) => {
          // console.log(error.response.data.detail);
          this.error_msg = error.response.data.detail;
        });
    },

    clickUpdateUser(pk, idnumber, username, sex, addr, email, phone) {
      this.showModifyModeal = true;
      this.pk = pk;
      this.idnumber = idnumber.trim();
      this.username = username.trim();
      this.sex = sex.trim();
      this.addr = addr.trim();
      this.email = email.trim();
      this.phone = phone.trim();
    },

    updateUser() {
      let param = {
        addr: this.addr,
        email: this.email,
        phone: this.phone,
      };
      this.$http
        .put(`http://localhost:8000/api/user/${this.pk}`, param)
        .then((res) => {
          this.showModifyModeal = false;
          this.getUsers();
        })
        .catch((error) => {
          this.getUsers();
        });
    },

    deleteUser(pk, username) {
      if (confirm(`確定刪除 '${username}'?`))
        this.$http
          .delete(`http://localhost:8000/api/user/${pk}`)
          .then((res) => {
            this.getUsers();
          })
          .catch((error) => {
            this.getUsers();
          });
    },
  },
};
</script>