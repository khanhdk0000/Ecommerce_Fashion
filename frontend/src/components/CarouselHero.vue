<template>
  <Carousel>
    <Slide v-for="item in items" :key="item">
      <div class="carousel__item">
        <figure class="image">
          <div class="crop">
            <img :src="item.url" />
          </div>
        </figure>
      </div>
    </Slide>

    <template #addons>
      <Navigation class="pagination" />
    </template>
  </Carousel>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Navigation, Pagination, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data() {
    return {
      items: [],
    };
  },
  mounted() {
    this.items = [
      {
        url: require('../assets/wristwatch-1149669.jpg'),
      },
      {
        url: require('../assets/woman-3377839.jpg'),
      },
      {
        url: require('../assets/tie-690084.jpg'),
      },
    ];
  },
});
</script>

<style>
.carousel__item {
  min-height: 400px;
  width: 100%;
  background-color: white;
  color: white;
  font-size: 20px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel__slide {
  padding: 10px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 5px solid white;
}
.pagination {
  background-color: #4040a1;
}

.crop {
  width: 100%;
  height: 400px;
  overflow: cover;
  transform: translateY(-30%);
}
</style>