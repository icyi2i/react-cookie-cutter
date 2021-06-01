import React from "react"
import helpers from "../helpers"

import "../styles/App.css"

const App = () => {

    return (
        <div>
            <h1>Hello react!</h1>
            <p>Time : { helpers.getTimestamp() }</p>
        </div>
    )
}

export default App
