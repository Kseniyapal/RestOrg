import React, { Children } from "react";
import "../Components/ComponentsStyles/OrderNumber.css"

const OrderNumber = ({children, ...props}) => {
    return (
        <div className="order__bg">
            <a {...props} className="order">{children}</a>
        </div>    
    
    )
}

export default OrderNumber;