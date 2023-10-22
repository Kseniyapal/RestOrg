import React from "react";
import "./ComponentsStyles/Content.css"
import Container from "./Container";

const Content = ({children, ...props}) => {
    return (
        <div className="Content">
            
            {children}
            
        </div>
    )
}

export default Content;