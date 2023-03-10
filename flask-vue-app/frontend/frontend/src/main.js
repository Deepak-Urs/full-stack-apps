import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css";
import BootStrapVue from "bootstrap-vue";

Vue.config.productionTip = false;
Vue.use(BootStrapVue);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
