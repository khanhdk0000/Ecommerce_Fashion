<template>
  <li class="accordion__item">
    <div
      class="accordion__trigger"
      :class="{ accordion__trigger_active: visible }"
      @click="open"
    >
      <!-- This slot will handle the title/header of the accordion and is the part you click on -->
      <!-- <slot name="accordion-trigger"></slot>     -->
      <div :class="{ accordion__trigger_active: visible }" class="subtitle is-5 ">
        {{ trigger }}
      </div>

      <span class="icon">
        <i
          v-bind:class="{ spinning: visible }"
          class="fas fa-chevron-right"
        ></i>
      </span>
    </div>

    <transition
      name="accordion"
      @enter="start"
      @after-enter="end"
      @before-leave="start"
      @after-leave="end"
    >
      <div class="accordion__content" v-show="visible">
        <ul>
          <!-- This slot will handle all the content that is passed to the accordion -->
          <!-- <slot name="accordion-content"></slot> -->
          <!-- {{
            content
          }} -->
          <div class="column">
            <div v-for="content in contents" :key="content">
              <a class="navbar-item" href="#">
                <div class="navbar-content">
                  <p>{{ content }}</p>
                </div>
              </a>
            </div>
          </div>
        </ul>
      </div>
    </transition>
  </li>
</template>


<script>
export default {
  props: ["trigger", "contents"],
  inject: ["Accordion"],
  data() {
    return {
      index: null,
    };
  },
  computed: {
    visible() {
      return this.index == this.Accordion.active;
    },
  },
  methods: {
    open() {
      if (this.visible) {
        this.Accordion.active = null;
      } else {
        this.Accordion.active = this.index;
      }
    },
    start(el) {
      el.style.height = el.scrollHeight + "px";
    },
    end(el) {
      el.style.height = "";
    },
  },
  created() {
    this.index = this.Accordion.count++;
  },
};
</script>

<style lang="scss" scoped>
.accordion__item {
  cursor: pointer;
  padding: 10px 0 10px 0;
  // border-bottom: 1px solid #ebebeb;
  position: relative;
}

.accordion__trigger {
  display: flex;
  justify-content: space-between;
}

.accordion__trigger_active {
  color: #5246c8;
}

.accordion-enter-active,
.accordion-leave-active {
  will-change: height, opacity;
  transition: height 0.3s ease, opacity 0.3s ease;
  overflow: hidden;
}

.accordion-enter,
.accordion-leave-to {
  height: 0 !important;
  opacity: 0;
}

.accordion__content {
  padding: 10px 0 10px 0px;
  font-family: Raleway;
  font-weight: 400;
  color: #72757e;
  // margin: 0 16px 0 0;
}

.spinning {
  transform: rotate(90deg);
  transition: all 0.1s linear;
}
</style>
