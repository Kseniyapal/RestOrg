import React, { Children, useState, useCallback, useEffect } from "react";
import "../Components/ComponentsStyles/PurchaseItem.css"

const OrderItem = ({...props}) => {
    const [buttonStyle, setButtonStyle] = useState({background: "#FFF"})

    const changeColor = () => {
        setButtonStyle({background: "#747474"})
    }

    const deleteButton = () => {
        if(props.deleteButton){
            return (<div className="purchase__delete">
                <button onClick={() => props.deleteFunction(props.element)}>Удалить</button>
            </div>
            )
        }
        else{
            return <div></div>
        }
    }

    return (
        <div className="purchase__flex">    
            <div className="purchase__img">
                    <img src={"/" + props.imgSource}alt={props.imgSource}></img>
            </div>
            <div className="purchase__name order__name">{props.name}</div>     
            {deleteButton()}        
    </div>                                
    )
}

export default OrderItem;