<template>
  <div class="navbar-item has-dropdown is-hoverable is-mega">
    <div class="navbar-link">Categories</div>
    <div id="blogDropdown" class="navbar-dropdown">
      <div class="container is-fluid">
        <div class="columns">
          <div class="column" v-for="col in menu" :key="col">
            <router-link
              :to="{
                name: 'Search',
                query: { category: col.category },
              }"
              class="navbar-item title is-6 is-mega-menu-title"
            >
              {{ col.category }}</router-link
            >
            <router-link
              :to="{
                name: 'Search',
                query: { subcategory: row },
              }"
              class="navbar-item"
              v-for="row in col.subcategory"
              :key="row"
            >
              <div class="navbar-content">
                <p>{{ row }}</p>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menu: [
        {
          category: "Apparel",
          subcategory: [
            "Topwear",
            "Bottomwear",
            "Socks",
            "Innerwear",
            "Dress",
            "Loungewear",
            "Saree",
            "Apparel Set",
          ],
        },
        {
          category: "Accessories",
          subcategory: [
            "Watches",
            "Socks",
            "Belts",
            "Bags",
            "Shoe Accessories",
            "Jewellery",
            "Eyewear",
            "Scarves",
            "Wallets",
            "Headwear",
            "Mufflers",
            "Ties",
            "Perfume",
          ],
        },
        {
          category: "Footwear",
          subcategory: ["Shoes", "Flip Flops", "Sandal"],
        },
        {
          category: "Personal Care",
          subcategory: [
            "Fragrance",
            "Lips",
            "Skin Care",
            "Makeup",
            "Nails",
            "Beauty Accessories",
            "Skin",
            "Eyes",
            "Bath and Body",
            "Hair",
            "Perfume",
          ],
        },
        {
          category: "Sporting Goods",
          subcategory: ["Sports Equipment", "Wristbands"],
        },
      ],
    };
  },
};
</script>

<style>
</style>
