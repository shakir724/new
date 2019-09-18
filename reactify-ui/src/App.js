import React, { Component } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import Login from "./Accounts/Login.jsx";
import Dashboard from "./Dashboard/Dashboard.jsx";
import NoMatch from "./Others/NoMatch.jsx";
import Home from "./Home/Home.jsx";


class App extends Component {
  render() {
    return (
      <div>
        <BrowserRouter>
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/login/" component={Login} />
            <Route path="/dashboard/" component={Dashboard} />
            <Route component={NoMatch} />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
