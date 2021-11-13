<template>
  <footer id="footer" class="section footer">
    <div class="container">
      <div class="footer-container">
        <div class="footer-center">
          <h3>EXTRAS</h3>
          <a href="#">Brands</a>
          <a href="#">Gift Certificates</a>
          <a href="#">Affiliate</a>
          <a href="#">Specials</a>
          <a href="#">Site Map</a>
        </div>
        <div class="footer-center">
          <h3>INFORMATION</h3>
          <a href="#">About Us</a>
          <a href="#">Privacy Policy</a>
          <a href="#">Terms & Conditions</a>
          <a href="#">Contact Us</a>
          <a href="#">Site Map</a>
        </div>
        <div class="footer-center">
          <h3>MY ACCOUNT</h3>
          <a href="#">My Account</a>
          <a href="#">Order History</a>
          <a href="#">Wish List</a>
          <a href="#">blogletter</a>
          <a href="#">Returns</a>
        </div>
        <div class="footer-center">
          <h3>CONTACT US</h3>
          <div>
            <span>
              <i class="fas fa-map-marker-alt"></i>
            </span>
            HCM
          </div>
          <div>
            <span>
              <i class="far fa-envelope"></i>
            </span>
            company@gmail.com
          </div>
          <div>
            <span>
              <i class="fas fa-phone"></i>
            </span>
            123456789
          </div>
          <div>
            <span>
              <i class="far fa-paper-plane"></i>
            </span>
            VN
          </div>
        </div>
      </div>
    </div>
  </footer>
  <!-- End Footer -->
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
/* ========= Footer ======== */
.footer {
  margin-top: 25px;
  background-color:#222;
  padding: 3rem 0.5rem;
  line-height: 1.5rem;
}

.footer-center span {
  margin-right: 0.5rem;
}

.footer-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  color: #fff;
}

.footer-center a:link,
.footer-center a:visited {
  display: block;
  color: #959595;
  font-size: 0.7rem;
  transition: 0.6s;
}

.footer-center a:hover {
  color: #f60091;
}

.footer-center div {
  color:#959595;
  font-size: 0.7rem;
}

.footer-center h3 {
  font-size: 0.9rem;
  font-weight: 400;
  margin-bottom: 0.5rem;
}

@media only screen and (max-width: 998px) {
  .footer-container {
    grid-template-columns: repeat(2, 1fr);
    row-gap: 1rem;
  }
}

@media only screen and (max-width: 768px) {
  .footer-container {
    grid-template-columns: 1fr;
    row-gap: 1rem;
  }
}


</style>