import React, { Children, useState, useCallback, useEffect } from "react";
import "../Components/ComponentsStyles/PurchaseItem.css"
import PlusIco from "../Styles/icons/plus.svg"
import Menu from "../Pages/Menu";

const OrderItem = ({...props}) => {
    const [buttonStyle, setButtonStyle] = useState({background: "#FFF"})

    const changeColor = () => {
        setButtonStyle({background: "#747474"})
    }
    return (
        <div className="purchase__flex">    
            <div className="purchase__img">
                    <img src={props.imgSource}alt={props.imgSource}></img>
            </div>
            <div className="purchase__name order__name">{props.name}</div>
            {/* <div  className="purchase__worked"><button onClick={changeColor} style={buttonStyle} >отработано</button></div> */}
            
    </div>                                
    )
}

export default OrderItem;