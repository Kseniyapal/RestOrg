import React from "react";

const Image = ({imgSource, ...props}) => {
    return (
        <div>
            <img src={"/" + imgSource} alt={props.alt}></img>
        </div>
    )
}

export default Image;