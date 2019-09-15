import React from "react";
import "./Footer.css";

import { MDBIcon, MDBContainer } from "mdbreact";

class Footer extends React.Component {
  render() {
    return (
      <div>
        <footer class="mainfooter" role="contentinfo">
          <div class="footer-middle">
            <div class="container-fluid">
              <div class="row">
                <div class="col-md-3 col-sm-6">
                  <div class="footer-pad">
                    <ul class="list-unstyled">
                      <li>
                        <a href="#"></a>
                      </li>
                      <li>
                        <a href="#">Wedding Websites</a>
                      </li>
                      <li>
                        <a href="#">Registry</a>
                      </li>
                      <li>
                        <a href="#">Marketplace</a>
                      </li>
                      <li>
                        <a href="#">Community</a>
                      </li>
                      <li>
                        <a href="#">Real Wedding Photos</a>
                      </li>
                    </ul>
                  </div>
                </div>
                <div class="col-md-3 col-sm-6">
                  <div class="footer-pad">
                    <ul class="list-unstyled">
                      <li>
                        <a href="#">About Us</a>
                      </li>
                      <li>
                        <a href="#">Advertise with us</a>
                      </li>
                      <li>
                        <a href="#">Career</a>
                      </li>
                      <li>
                        <a href="#">International</a>
                      </li>
                      <li>
                        <a href="#">Press</a>
                      </li>
                    </ul>
                  </div>
                </div>
                <div class="col-md-3 col-sm-6">
                  <div class="footer-pad">
                    <ul class="list-unstyled">
                      <li>
                        <a href="#">Privacy Policy</a>
                      </li>
                      <li>
                        <a href="#">Terms of Use</a>
                      </li>
                      <li>
                        <a href="#">Send Feedback</a>
                      </li>
                      <li>
                        <a href="#">Customer Service (FAQ)</a>
                      </li>

                      <li>
                        <a href="#"></a>
                      </li>
                    </ul>
                  </div>
                </div>

                <div class="col-md-3">
                  <h4>Follow Us</h4>

                  <MDBContainer>
                    <a href="#!" className="fb-ic mr-3">
                      <MDBIcon
                        fab
                        icon="facebook-f"
                        className="FooterFbColor"
                        size="2x"
                      />
                    </a>
                    <a href="#!" className="tw-ic mr-3">
                      <MDBIcon
                        fab
                        icon="twitter"
                        className="FooterTwitterColor"
                        size="2x"
                      />
                    </a>
                    <a href="#!" className="li-ic mr-3">
                      <MDBIcon
                        fab
                        icon="linkedin-in"
                        className="FooterLinkedInColor"
                        size="2x"
                      />
                    </a>
                    <a href="#!" className="ins-ic mr-3">
                      <MDBIcon
                        fab
                        icon="instagram"
                        size="2x"
                        className="FooterInstaColor"
                      />
                    </a>
                  </MDBContainer>
                </div>
              </div>
              <div class="row">
                <div class="col-md-12 copy">
                  <p class="text-center">
                    &copy; Copyright 2019 - Memorable Marraige. All rights
                    reserved.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </footer>
      </div>
    );
  }
}
export default Footer;
