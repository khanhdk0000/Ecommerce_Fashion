<template>
  <div>
    <section class="hero">
      <div class="glide glide1" id="glide1">
        <div class="glide__track" data-glide-el="track">
          <ul class="glide__slides glide__hero">
            <li class="glide__slide">
              <div class="banner">
                <div class="banner-content">
                  <span>New Inspiration 2021</span>
                  <h1>CLOTHING MADE FOR YOU!</h1>
                  <h3>Trending style collection</h3>
                  <div class="buttons-group">
                    <router-link
                      v-bind:to="{
                        name: 'Search',
                        
                      }"
                      ><button class="custom-button">
                        shop now
                      </button></router-link
                    >
                  </div>
                </div>
                <img src="../assets/model2.png" class="special_01" alt="" />
              </div>
            </li>
          </ul>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
// Required Core Stylesheet
@import "node_modules/@glidejs/glide/src/assets/sass/glide.core";

/* Hero Area */
.hero,
.glide__hero,
.banner {
  position: relative;
  height: 550px;
  width: 100%;
  background-color: #dfe7fd;
}

.banner img {
  position: absolute;
  bottom: 0;
}

.banner img.special_01 {
  width: 42rem;
  right: -5%;
}

.banner-content {
  position: absolute;
  top: 50%;
  transform: translate(25%, -50%);
}

.banner-content span {
  display: inline-block;
  font-size: 0.85rem;
  color: #444;
  margin-bottom: 0.5rem;
}

.banner-content h1 {
  font-size: 2rem;
  font-weight: 500;
  margin-bottom: 0.5rem;
  color: black;
}

.banner-content h3 {
  font-weight: 400;
  color: #444;
  margin-bottom: 1rem;
}

.buttons-group button {
  display: inline-block;
  background-color: transparent;
  border: 1px solid #444;
  outline: none;
  margin: 5px;
  padding: 0.6rem 1.5rem;
  font-size: 1rem;
  text-transform: uppercase;
  font-weight: 500;
  cursor: pointer;
  transition: all 300ms ease-in-out;
}

.custom-button {
  background-color: #222;
  color: #fff;
}

.custom-button:hover {
  background-color: transparent;
  color: #222;
}

.buttons-group button:first-child {
  background-color: #222;
  color: #fff;
}

.buttons-group button:first-child:hover {
  background-color: transparent;
  color: #222;
}

.buttons-group button:last-child:hover {
  background-color: #222;
  color: #fff;
}

.glide__arrows {
  /* position: absolute; */
  top: 50%;
}

.glide__arrow {
  position: absolute;
  top: 50%;
  background-color: #555;
  border: 1px solid #222;
  outline: none;
  padding: 1.3rem 1.5rem;
  border-radius: 50%;
  font-size: 1.6rem;
  color: #fff;
  visibility: hidden;
  opacity: 0;
  cursor: pointer;
  transition: all 300ms ease-in-out;
}

.glide:hover .glide__arrow {
  visibility: visible;
  opacity: 1;
}

.glide__arrow:hover {
  color: #222;
  background-color: transparent;
}

.glide__arrow--left {
  left: 5%;
}

.glide__arrow--right {
  right: 5%;
}
</style>