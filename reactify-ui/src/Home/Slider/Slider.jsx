import React, { Component } from "react";

import "./Slider.css";

// section1 :s1
// component : com
//container : con
// p : part

class Slider extends Component {
  render() {
    return (
      <div className="section-1">
        {/*This section will be displayed in large screen and will hide in small screen */}
        <div className="section-1-p1">
          <div className="container-fluid">
            {/* This div has buttons and text */}
            <div className="s1-com xx">
              <h1 id="s1-h1">Wedding Made Easy </h1>
              <h4 id="s1-h4">One stop destination for your wedding</h4>
              <div className="s1-btn-con">
                <button id="sec-1-btn1">Sign up</button>
                <button id="sec-1-btn2">Sign in </button>
              </div>
            </div>
            {/* video background */}
            <div className="vid-el">
              <video autoplay="true" loop="true" muted="true" class="video">
                <source
                  type="video/mp4"
                  src="https://static.xoedge.com/xo-homepage/The_Knot_Homepage_2019.mp4"
                />
              </video>
            </div>
          </div>
        </div>

        {/* This section will be visible in mobile devices only and will be hidden rest of the time*/}
        <div className="section-1-p2">
          <div className="s1-p1">
            <h3 id="s1-h3">Wedding Made Easy</h3>
            <h5>One Stop Destination for wedding</h5>
          </div>
        </div>
        {/* ************************************************************************ */}
      </div>
    );
  }
}

export default Slider;
