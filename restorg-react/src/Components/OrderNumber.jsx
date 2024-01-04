import React, { Children, useEffect, useState } from "react";
import "../Components/ComponentsStyles/OrderNumber.css"
import { useNavigate } from "react-router";

const OrderNumber = ({children, elementId, ...props}) => {
    const nav = useNavigate()
    const [disabled, setDisabled] = useState("disabled")

    const redirectToOrder = () =>{
        nav("/order/" + elementId)
    }

    const enableSomeButtons = () => {
        const user = JSON.parse(localStorage.getItem("user"))
        if(user.role == "W"){
            if((props.element.waiter == null || props.element.waiter == user.id) && (props.element.status == "NA" || props.element.status == "DONE")){
                setDisabled("")
            }
        }
        else if(user.role == "B"){
            if(props.element.status == "IP" || props.element.status == "DDS"){
                if(props.element.menu_drinks.length != 0){
                    setDisabled("")
                }
            }
        }
        else if(user.role == "C"){
            if(props.element.status == "IP" || props.element.status == "DDK"){
                if(props.element.menu_dishes.length != 0){
                    setDisabled("")
                }
            }
        }
    }

    useEffect(() => {
        enableSomeButtons()
    }, [])
    return (
            <button disabled={disabled} onClick={redirectToOrder} className="order">
                <div className="order__bg">
                    {children}
                </div>    
            </button>
    )
}

export default OrderNumber;