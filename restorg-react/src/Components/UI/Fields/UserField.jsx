import React, { Children } from "react";
import "../../ComponentsStyles/UserField.css"

const UserField = ({children, name, ...props}) => {
    return (
        <div className="input">
            <div className="input__name">{name}</div>
            <input {...props} >{children}</input>
        </div>
    )
}

export default UserField;