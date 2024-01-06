import React from "react";

const priceAmount = ({...props}) => {
    if(props.amount!=0){
        return (
            <div className={props.className}>
                Итого к оплате: {props.amount}₽
            </div>
        )
    }
    else {
        return (
            <div></div>
        )
    }

}

export default priceAmount;