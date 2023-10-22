import React from "react";
import "../ComponentsStyles/WindowC.css"

const WindowC = ({children, ...props}) => {
    return (
        <div className="WindowC">
            {children}
        </div>
    )
}

export default WindowC;