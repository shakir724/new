import React from "react";
import image from "./m.jpg";
import "./About.css";
import "react-bootstrap";

class About extends React.Component {
  render() {
    return (
      <div className="AboutUsDiv">
        <div class="container-fluid ">
          <div class="row ab-r">
            <div class="col-md-6  ">
              <img src={image} className="Image" />
            </div>
            <div class=" col-md-6 card ab-us">
              <h2 id="ab-us-h">Memorable Marriage</h2>
              <p id="ab-us-p">
                The Paragraphs module allows content creators to choose which
                kinds of paragraphs they want to place on the page, and the
                order in which they want to place them. They can do all of this
                through the familiar node edit screen. There is no need to
                resort to code, the dreaded block placement config screen or
                Panelizer overrides. They just use node edit form where all
                content is available to them in one place.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default About;
