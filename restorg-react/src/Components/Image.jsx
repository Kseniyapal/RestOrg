import React from "react";

const Image = ({...props}) => {
    return (
        <div>
            <img src={props.imgSource}></img>
        </div>
    )
}

export default Image;