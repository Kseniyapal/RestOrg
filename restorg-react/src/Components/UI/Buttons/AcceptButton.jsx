import React, { Children } from "react";
import "../../ComponentsStyles/AcceptButton.css"
import { Link } from "react-router-dom";

const AcceptButton = ({children, ...props}) => {
    return (
    
            <Link {...props}>{children}</Link>
    
    )
}

export default AcceptButton;