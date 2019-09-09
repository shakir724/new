import React, {Component} from 'react';
import {fetch} from 'whatwg-fetch';
import cookie from 'react-cookies';


class Dashboard extends Component {
    state = {
        user: []
    }

    render() {
        return (
            <div>
                <h1>Dashboard of {this.state.user.map(element => {return element.firstName})}</h1>
            </div>
        );    
    }

    componentDidMount = () => {
        this.get()
    }

    get = () => {
        const url = "http://localhost:8000/api/Accounts/";
        const settings = {
            method: "GET",
            timeout: 0,
            headers: {
                'Authorization':'Basic dGVzdDFAZ21haWwuY29tOnRlc3Q=',
                'X-CSRF-TOKEN':cookie.load('csrftoken'),
            },
            // credentials: "include"
        }
        const thisComp = this;

        fetch(url, settings)
        .then(function(response) {
            return response.json()
        }).then(function(json) {
            console.log(json);
            thisComp.setState({
                user: json
            });
            console.log(thisComp.state);
        }).catch(function(ex) {
            console.log(ex)
        })

        return thisComp.state;
    }
}

export default Dashboard;