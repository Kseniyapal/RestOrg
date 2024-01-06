import React, { Children } from "react";
import "../../ComponentsStyles/AcceptButton.css"

const AcceptButton = ({children, ...props}) => {
    return (
    
            <a {...props}>{children}</a>
    
    )
}

export default AcceptButton;