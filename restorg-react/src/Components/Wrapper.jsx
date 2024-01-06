import React from "react";
import "./ComponentsStyles/Wrapper.css"

const Content = ({children, ...props}) => {
    return (
        <div className="Wrapper">
            {children}
        </div>
    )
}

export default Content;