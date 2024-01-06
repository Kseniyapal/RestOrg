import React, { Children, useState, useCallback, useEffect } from "react";
import "../Components/ComponentsStyles/PaymentItem.css"
import PlusIco from "../Styles/icons/plus_square.svg"
import MinusIco from "../Styles/icons/minus_square.svg"

const PaymentItem = ({...props}) => {

    const [count, setCount] = useState(props.count)

    const increment = () => {
        setCount(count + 1)
        props.purchase = {...props.purchase, count : count + 1}
        props.change(props.purchase)
    }

    const decrement = () => {
        if(count == 1){
            props.delete(props.purchase)
        }
        else {
            setCount(count - 1)
            props.purchase = {...props.purchase, count : count - 1}
            props.change(props.purchase)
        }
    }

    return (
        <div className="payment__item">    
            <div className="payment__item__name">{props.name}</div>
            <div className="payment__item__numbers__flex">
                <div className="payment__item__count__flex">
                    <button className="payment__item__minus"><img src={MinusIco} onClick={()=>decrement()}></img></button>
                    <div className="payment__item__count">{props.count}</div>
                    <button className="payment__item__minus"><img src={PlusIco} onClick={()=>increment()}></img></button>
                </div>
                <div className="payment__item__price">{props.price} ₽</div>
            </div>
        </div>              
    )
}

export default PaymentItem;
