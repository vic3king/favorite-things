<template>
  <div id="app">
    <Navbar />
    <div>
      <router-view />
    </div>
  </div>
</template>
<script>
import Navbar from "@/components/Navbar";
export default {
  name: "app",
  components: {
    Navbar
  }
};
</script>

<style>
* {
  font-family: "poppins";
  border-radius: 0px !important;
}
body {
  background-color: #f5f3ef;
}
</style>
