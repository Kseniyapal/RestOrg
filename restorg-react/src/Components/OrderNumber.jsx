import React, { Children } from "react";
import "../Components/ComponentsStyles/OrderNumber.css"

const OrderNumber = ({children, ...props}) => {
    return (
            <a {...props} className="order">
                <div className="order__bg">
                    {children}
                </div>    
            </a>
    )
}

export default OrderNumber;