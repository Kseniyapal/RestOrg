import React, { Children } from "react";
import "../../ComponentsStyles/AcceptButtonMini.css"
import { Link } from "react-router-dom";

const AcceptButtonMini = ({children, ...props}) => {
    return (
        <Link type="submit" {...props}  >{children}</Link>
    )
}

export default AcceptButtonMini;