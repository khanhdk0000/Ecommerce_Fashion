<template>
  <!-- Grid -->
  <section class="gallary section">
    <figure class="gallary-item item-1" @click="handleClick('Accessories')">
      <img src="../assets/watch.jpg" alt="" class="gallary-img" />
      <div class="content">
        <h2>Accessories</h2>
      </div>
    </figure>

    <figure class="gallary-item item-2" @click="handleClick('Footwear')">
      <img src="../assets/shoe.jpg" alt="" class="gallary-img" />
      <div class="content">
        <h2>Shoes</h2>
      </div>
    </figure>

    <figure class="gallary-item item-3" @click="handleClick('Personal Care')">
      <img src="../assets/makeup.jpg" alt="" class="gallary-img" />
      <div class="content">
        <h2>Personal Care</h2>
      </div>
    </figure>

    <figure class="gallary-item item-4" @click="handleClick('Sporting Goods')">
      <img src="../assets/tennis-3554019_1920.jpg" alt="" class="gallary-img" />
      <div class="content">
        <h2>Sporting Goods</h2>
      </div>
    </figure>
  </section>
</template>

<script>
import { useRouter } from "vue-router";

export default {
  setup() {
    const router = useRouter();

    const handleClick = async (destination) => {
      router.push({ name: "Search", query: { category: destination } });
    };
    return { handleClick };
  },
};
</script>

<style lang="scss" scoped>
/* ======== Grid ======= */
.gallary {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: repeat(6, 4vw);
  gap: 1rem;
}

.gallary-item {
  overflow: hidden;
  position: relative;
}

.gallary-item::after {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
}

.gallary-img {
  object-fit: cover;
  height: 100%;
  width: 100%;
  transition: all 500ms linear;
}
.gallary-item:hover {
  cursor: pointer;
}

.gallary-item:hover .gallary-img {
  transform: scale(1.1);
}

.gallary-item .content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 10;
  color: #fff;
  width: 100%;
  text-align: center;
}

.gallary-item .content h2 {
  font-size: 1.4rem;
  font-weight: 500;
  color: #fff;
}

.gallary-item .content a {
  display: inline-block;
  padding: 0.5rem 1rem;
  border: 1px solid #fff;
  margin-top: 2rem;
  color: #fff;
}

.item-1 {
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 7;
}

.item-2 {
  grid-column-start: 3;
  grid-column-end: 5;
  grid-row-start: 1;
  grid-row-end: 4;
}
.item-3 {
  grid-column-start: 5;
  grid-column-end: 7;
  grid-row-start: 1;
  grid-row-end: 4;
}
.item-4 {
  grid-column-start: 3;
  grid-column-end: 7;
  grid-row-start: 4;
  grid-row-end: 7;
}

@media only screen and (max-width: 996px) {
  .gallary-item .content h2 {
    font-size: 1.6rem;
  }

  .gallary-item .content a {
    padding: 0.7rem 1.3rem;
    margin-top: 1.5rem;
  }
}

@media only screen and (max-width: 768px) {
  .gallary-item .content h2 {
    font-size: 1.4rem;
  }

  .gallary-item .content a {
    padding: 0.4rem 1rem;
    margin-top: 1rem;
  }
}

@media only screen and (max-width: 600px) {
  .gallary {
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(20, 4vw);
  }

  .item-1 {
    grid-column-start: 1;
    grid-column-end: 7;
    grid-row-start: 1;
    grid-row-end: 7;
  }

  .item-2 {
    grid-column-start: 1;
    grid-column-end: 7;
    grid-row-start: 7;
    grid-row-end: 11;
  }
  .item-3 {
    grid-column-start: 1;
    grid-column-end: 7;
    grid-row-start: 11;
    grid-row-end: 15;
  }
  .item-4 {
    grid-column-start: 1;
    grid-column-end: 7;
    grid-row-start: 15;
    grid-row-end: 19;
  }
}

.brands li img {
  width: 100%;
  object-fit: contain;
  height: 12rem;
}

@media only screen and (max-width: 567px) {
  .brands li img {
    height: 9rem;
  }
}
</style>