import React from "react";
// import $ from "jquery";
import "react-bootstrap";
import "./Dashboard.css";
class Dashboard extends React.Component {
  render() {
    return (
      <div>
        <div id="wrapper">
          <div className="overlay"></div>

          <nav
            className="navbar navbar-inverse fixed-top"
            id="sidebar-wrapper"
            role="navigation"
          >
            <ul className="nav sidebar-nav container">
              <div className="sidebar-header">
                <div className="sidebar-brand">
                  <a href="#">Brand</a>
                </div>
              </div>
              <li>
                <a href="#dashboardContent" className="dashboard">
                  Dashboard
                </a>
              </li>
              <li role="separator" className="Dashdivider"></li>
              <li>
                <a href="#guestList" className="guestList">
                  Guest List
                </a>
              </li>
              <li role="separator" className="Dashdivider"></li>
              <li>
                <a href="#registry" className="registry">
                  Registry
                </a>
              </li>
              <li role="separator" className="Dashdivider"></li>
              <li>
                <a href="#todolist" className="todo">
                  Todo List
                </a>
              </li>
              <li role="separator" className="Dashdivider"></li>
              {/* <li className="dropdown"> */}
              {/* <a href="#works" className="dropdown-toggle" data-toggle="dropdown">
                  Works <span className="caret"></span>
                </a> */}
              <li>
                <a href="#weddingContent" className="wedding">
                  Wedding
                </a>
              </li>
              {/* <ul className="dropdown-menu animated fadeInLeft" role="menu">
                  <div className="dropdown-header">Dropdown heading</div>
                  <li>
                    <a href="#pictures">Pictures</a>
                  </li>
                  <li>
                    <a href="#videos">Videeos</a>
                  </li>
                  <li>
                    <a href="#books">Books</a>
                  </li>
                  <li>
                    <a href="#art">Art</a>
                  </li>
                  <li>
                    <a href="#awards">Awards</a>
                  </li>
                </ul> */}
              {/* </li> */}
              <li role="separator" className="Dashdivider"></li>
              <li>
                <a href="#invitationcardContent" className="invitationCard">
                  Invitation Card
                </a>
              </li>
              {/* <li role="separator" className="Dashdivider"></li>
              <li>
                <a href="#" className="contact">
                  Contact
                </a>
              </li>
              <li role="separator" className="Dashdivider"></li>
              <li>
                <a href="#" className="followMe">
                  Follow me
                </a>
              </li> */}
            </ul>
          </nav>

          <div id="page-content-wrapper">
            {/* <button
              type="button"
              className="hamburger animated fadeInLeft is-closed"
              data-toggle="offcanvas"
            >
              <span className="hamb-top"></span>
              <span className="hamb-middle"></span>
              <span className="hamb-bottom"></span>
            </button> */}

            <div className="container contentContainer">
              <div className="row">
                <div className="col-lg-12 col-lg-offset-2">
                  <h1>Fancy Toggle Sidebar Navigation</h1>
                  <br />
                  <br />
                  <p id="dashboardContent">
                    <h4 className="contentHeading">This is Dashboard</h4>
                    <br />
                    <li role="separator" className="Dashdivider"></li>
                    vebtgg bgtLandjaeger chicken fatback pork loin doner sirloin
                    cow short ribs hamburger shoulder salami pastrami. Pork
                    swine beef ribs t-bone flank p steak biltong. Corned beef
                    pork loin cow pig short ribs boudin bacon pork belly chicken
                    andouille. Filet mignon flank turkey tongue. Turkey swine.
                    Hamburger drumstick turkey, shank rump biltong pork loin
                    jowl sausage chicken. Rump pork belly fatback ball tip swine
                    doner pi ball tip kielbasa pastrami flank tri-tip t-bone
                    kevin landj{" "}
                  </p>
                  <br />
                  <br />
                  <p id="guestList">
                    <h4 className="contentHeading">This is Guest List</h4>
                    <br />
                    <li role="separator" className="Dashdivider"></li>
                    <br />
                    Pig meatloaf
                    <br />
                    bresaola venison
                    <br /> short loin
                    <br /> rump pork
                    <br /> loin brisket <br />
                    pork loin
                    <br /> doner sirloin
                    <br /> pastramis filet
                    <br />
                    mignon
                    <br /> flank leberkas
                    <br />
                  </p>
                  <br />
                  <br />
                  <p id="registry">
                    <h4 className="contentHeading">This is Registry</h4>
                    <br />
                    <li role="separator" className="Dashdivider"></li>
                    <br />
                    Filet mignon brisket pancetta fatback short ribs short loin
                    prosciutto jowl turducken biltong kevin pork chop pork beef
                    ribs bresaola. Tongue beef ribs pastrami boudin. Chicken
                    bresaola kielbasa strip steak biltong. Corned beef pork loin
                    cow pig short ribs boudin bacon pork belly chicken
                    andouille. Filet mignon flank turkey tongue. Turkey ball tip
                    kielbasa pastrami flank tri-tip t-bone kevin landjaeger
                    capicola tail fatback pork loin beef jerky.
                  </p>
                  <br />
                  <br />
                  <p id="todolist">
                    <h4 className="contentHeading"> This is ToDo List</h4>
                    <br />
                    <li role="separator" className="Dashdivider"></li>
                    <br />
                    Chicken ham hock shankle, strip steak ground round meatball
                    pork belly jowl pancetta sausage spare ribs. Pork loin cow
                    salami pork belly. Tri-tip pork loin sausage jerky
                    prosciutto t-bone bresaola frankfurter sirloin pork chop
                    ribeye corned beef chuck. Short loin hamburger tenderloin,
                    landjaeger venison porchetta strip steak turducken pancetta
                    beef cow leberkas sausage beef ribs. Shoulder ham jerky
                    kielbasa. Pig doner short loin pork chop. Short ribs
                    frankfurter rump meatloaf.
                  </p>
                  <br />
                  <br />
                  <p id="weddingContent">
                    <h4 className="contentHeading">This is Wedding</h4>
                    <br />
                    <li role="separator" className="Dashdivider"></li>
                    <br />
                    Filet mignon biltong chuck pork belly, corned beef ground
                    round ribeye short loin rump swine. Hamburger drumstick
                    turkey, shank rumpb c nbd cb sgub sdb cb sg bcgdg msdcsugdu
                    sdmhcbs cegd wdgc dgcb cgugwwashn fsujbgj biltong pork loin
                    jowl sausage chicken. Rump pork belly fatback ball tip swine
                    doner pig. Salami jerky cow, boudin pork chop sausage tongue
                    andouille turkey.
                  </p>
                  <br /> <br />
                  <p id="invitationcardContent">
                    <h4 className="contentHeading">This is Invitation card</h4>
                    <br />
                    <li role="separator" className="Dashdivider"></li>
                    <br />
                    Filet mignon biltong chuck pork belly, corned beef ground
                    round ribeye short loin rump swine. Hamburger drumstick
                    turkey, shank rump biltong porkj loin jowl sausage chicken.
                    Rump pork belly fatback ball tip swine doner pig. Salami
                    jerky cow, boudin pork chop sausage tongue andouille turkey.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Dashboard;
