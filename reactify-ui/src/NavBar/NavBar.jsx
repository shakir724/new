import React from "react";
import { Navbar, Nav } from "react-bootstrap";
import "./NavBar.css";

class NavBar extends React.Component {
  render() {
    return (
      <Navbar
        collapseOnSelect
        expand="lg"
        variant="light"
        className="Navigation navbar-fixed-top "
      >
        <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbar-toggle iconColor responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="ml-auto NavText">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="NavText" href="#">
                  Planning Tools
                </a>
              </li>
              <li role="separator" className="divider"></li>

              <li className="nav-item">
                <a className="NavText" href="#">
                  Local Vendors
                </a>
              </li>
              <li role="separator" className="divider"></li>

              <li className="nav-item">
                <a className="NavText" href="#">
                  Wedding Websites
                </a>
              </li>
              <li role="separator" className="divider"></li>
              <li className="nav-item">
                <a className="NavText" href="#">
                  Registry
                </a>
              </li>
              <li role="separator" className="divider"></li>

              <li className="nav-item">
                <a className="NavText" href="#">
                  Rings + Dresses
                </a>
              </li>
              <li role="separator" className="divider"></li>
              <li className="nav-item">
                <a className="NavText" href="#">
                  Photos
                </a>
              </li>
              <li role="separator" className="divider"></li>
              <li className="nav-item">
                <a className="NavText" href="#">
                  Ideas & Advice
                </a>
              </li>
              <li role="separator" className="divider"></li>
              <li className="nav-item">
                <a className="NavText" href="#">
                  Shop
                </a>
              </li>
              <li role="separator" className="divider"></li>

              <li className="nav-item">
                <a className="NavText" href="#">
                  Sign up
                </a>
              </li>
              <li role="separator" className="divider"></li>

              <li className="nav-item">
                <a className="NavText" href="#">
                  Sign in
                </a>
              </li>
            </ul>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

export default NavBar;
