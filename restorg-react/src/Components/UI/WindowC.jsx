import React from "react";
import classes from  "../ComponentsStyles/WindowC.module.css"

const WindowC = ({children, ...props}) => {
    return (
        <div className={classes.WindowC}>
            {children}
        </div>
    )
}

export default WindowC;