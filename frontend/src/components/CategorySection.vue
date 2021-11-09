<template>
  <section class="section category">
    <h2 class="title">Allow your style to match your ambition!</h2>
    <div class="category-center container">
      <div class="category-box">
        <img src="../assets/model3.jpg" alt="" />
        <div class="content">
          <h2>Shop for Man</h2>
          <!-- <span>155 Products</span> -->
          <router-link
            v-bind:to="{
              name: 'Search',
              query: { gender: 'Men' },
            }"
            class="navbar-item"
            >shop now</router-link
          >
        </div>
      </div>

      <div class="category-box">
        <img src="../assets/woman-2564660_1920.jpg" alt="" />
        <div class="content">
          <h2>Shop for Woman</h2>
          <!-- <span>155 Products</span> -->
          <router-link
            v-bind:to="{
              name: 'Search',
              query: { gender: 'Women' },
            }"
            class="navbar-item"
            >shop now</router-link
          >
          <!-- <a href="#">shop now</a> -->
        </div>
      </div>

      <div class="category-box">
        <img src="../assets/man-2425121_1920.jpg" alt="" />
        <div class="content">
          <h2>Shop for Man and Woman</h2>
          <!-- <span>155 Products</span> -->
          <router-link
            v-bind:to="{
              name: 'Search',
              query: { gender: 'Unisex' },
            }"
            class="navbar-item"
            >shop now</router-link
          >
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
/* ========= Category ========= */
.section {
  padding: 2.5rem 0;
}

.category .title {
  font-size: 1.3rem;
  font-weight: 500;
  text-align: center;
  margin-bottom: 1.5rem;
}

.category-center {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.category-box {
  position: relative;
  border-radius: 0.5rem;
  height: 15rem;
  overflow: hidden;
  z-index: 1;
}

.category-box::after {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-image: linear-gradient(
    to right,
    rgba(0, 0, 0, 0.4) 30%,
    transparent
  );
  z-index: 2;
}

.category-box img {
  object-fit: cover;
  height: 15rem;
  width: 100%;
  /* transform: scale(1); */
  transition: all 500ms linear;
}

.category-box:hover img {
  transform: scale(1.1);
}

.category-box .content {
  position: absolute;
  top: 30%;
  left: 5%;
  color: #fff;
  z-index: 4;
}

.category-box .content h2 {
  font-weight: 500;
  margin-bottom: 0.25rem;
  color: #fff;
}

.category-box .content span {
  display: block;
  margin-bottom: 0.5rem;
}

.category-box .content a {
  display: inline-block;
  color: #fff;
  text-transform: uppercase;
  padding: 0.2rem 0.7rem;
  border: 1px solid #fff;
  transition: all 300ms linear;
}

.category-box:hover a {
  border: 1px solid #222;
  background-color: #222;
}

@media only screen and (max-width: 1200px) {
  .category-box .content h2 {
    font-size: 1rem;
  }

  .category-box .content span {
    font-size: 0.75rem;
  }

  .category-box .content a {
    font-size: 0.75rem;
    padding: 0.5rem 1.1rem;
  }
}

@media only screen and (max-width: 996px) {
  .category-center {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media only screen and (max-width: 768px) {
  .category-box {
    height: 20rem;
  }
}

@media only screen and (max-width: 567px) {
  .category-center {
    grid-template-columns: 1fr;
  }

  .category-box {
    height: 20rem;
    max-width: 35rem;
    margin: 0 auto;
  }

  .category-box .content {
    top: 20%;
  }
}
</style>