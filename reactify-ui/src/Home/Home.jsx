import React, { Component } from "react";

// import "./Home.css";
// import "react-bootstrap";
import Slider from "./Slider/Slider.jsx";
import Service from "./Services/Service.jsx";
import About from "./About/About.jsx";

import Footer from "../Footer/Footer.jsx";
import NavBar from "../NavBar/NavBar.jsx";

class Home extends Component {
  render() {
    return (
      <div>
        {/* <NavBar /> */}
        <Slider />
        <Service />
        <About />
        <Footer />
      </div>
    );
  }
}

export default Home;
