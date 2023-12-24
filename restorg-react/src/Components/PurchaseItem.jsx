import React, { Children, useState, useCallback } from "react";
import "../Components/ComponentsStyles/PurchaseItem.css"
import PlusIco from "../Styles/icons/plus.svg"
import Menu from "../Pages/Menu";

const PurchaseItem = ({...props}) => {

    const [count, setCount] = useState(1)

    const increment = () => {
        setCount(count + 1)
    }

    const decrement = () => {
        if(count == 1){
            props.delete(props.purchase)
        }
        else setCount(count - 1)
    }

    return (
        <div className="purchase__flex">    
            <div className="purchase__img">
                    <img src={props.imgSource}alt="картинка не загрузилась("></img>
            </div>
        <div className="purchase__counter__flex">
            <div className="purchase__minus"><button onClick={()=>decrement()}>-</button></div>
            <div className="purchase__cnumber">{count}</div>
            <div className="purchase__plus"><button onClick={()=>increment()}>+</button></div>
        </div>
    </div>                                
    )
}

export default PurchaseItem;

