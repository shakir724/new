import React, { Component } from "react";
import "./Service.css";
import website from "./Icons/website.svg";
import shop from "./Icons/shop.svg";
import todo from "./Icons/todo.svg";
import wedregistry from "./Icons/wed-registry.svg";

class Service extends Component {
  render() {
    return (
      <div className="section-2">
        <div className="container-fluid">
          <div className="row">
            {/* ----------------first row ----------------------------------------------- */}
            {/* First service element */}
            <div className="s2-c col-sm-6 col-md-3">
              <div className=" c-hov">
                <div className="s2-c-0">
                  <img id="web" src={website} alt="" />
                  <h4>Page Builder</h4>
                  <h6 id="s2-h6">Create your wedding website for free</h6>
                </div>
              </div>
            </div>

            {/* Second service element */}
            <div className="s2-c col-sm-6 col-md-3">
              <div className=" c-hov">
                <div className="s2-c-1">
                  <img id="web" src={todo} alt="" />
                  <h4>To-do list</h4>
                  <h6 id="s2-h6">Write down all the things needed wedding</h6>
                </div>
              </div>
            </div>
            {/* </div> */}
            {/* -------------------second row----------------------------------------------------- */}

            {/*Third service element */}
            <div className="s2-c col-sm-6 col-md-3">
              <div className=" c-hov">
                <div>
                  <center>
                    <img id="web" src={shop} alt="" />
                    <h4>Shop Gifts</h4>
                    <h6 id="s2-h6">Buy gifts and products for your wedding</h6>
                  </center>
                </div>
              </div>
            </div>

            {/* Fourth service element  */}
            <div className="s2-c col-sm-6 col-md-3">
              <div className=" c-hov">
                <div>
                  <center>
                    <img id="web" src={wedregistry} alt="" />
                    <h4>Registy</h4>
                    <h6 id="s2-h6">Register your marriage hassle free</h6>
                  </center>
                </div>
              </div>
            </div>
            {/* </div> */}
            {/* ------------------------------------------------------------------------------------- */}
          </div>
        </div>
      </div>
    );
  }
}

export default Service;
