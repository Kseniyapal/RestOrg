import React from "react";
import "./ComponentsStyles/Container.css"

const Container = ({children, ...props}) => {
    return (
        <div className="Container">
            {children}
        </div>
    )
}

export default Container;