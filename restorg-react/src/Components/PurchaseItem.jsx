import React, { Children, useState, useCallback, useEffect } from "react";
import "../Components/ComponentsStyles/PurchaseItem.css"


const PurchaseItem = ({...props}) => {

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

    useEffect(() => {
        console.log(props.imgSource)
    }, [])

    return (
        <div className="purchase__flex">    
            <div className="purchase__img">
                    <img src={"/" + props.imgSource} alt="картинка не загрузилась("></img>
            </div>
            <div className="purchase__name">{props.name}</div>
            <div className="purchase__counter__flex">
                <div className="purchase__minus"><button onClick={()=>decrement()}>-</button></div>
                <div className="purchase__number">{count}</div>    
                <div className="purchase__plus"><button onClick={()=>increment()}>+</button></div>
            </div>
    </div>                                
    )
}

export default PurchaseItem;

