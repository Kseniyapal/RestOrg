import React, { Children } from "react";
import "../../ComponentsStyles/AcceptButtonMini.css"

const AcceptButtonMini = ({children, ...props}) => {
    return (
        <a type="submit" {...props} >{children}</a>
    )
}

export default AcceptButtonMini;