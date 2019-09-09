import React, { Component } from "react";

class Login extends Component {
    render() {
        return (
            <div>
                <form>
                    <div>
                        <label htmlFor="email">Email:</label>
                        <input type="email" />
                    </div>

                    <div>
                        <label htmlFor="password">Password:</label>
                        <input type="password" />
                    </div>
                </form>
            </div>
        );
    }
}

export default Login;