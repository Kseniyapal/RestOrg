import React from "react";
import  Container  from "../Components/Container";
import Content from "../Components/Content";
import { useState, useEffect } from "react";
import Wrapper from "../Components/Wrapper";
import "./PagesStyles/Payment.css";
import { useNavigate } from "react-router";
import { Link } from "react-router-dom";
import AroowIco from "../Styles/icons/arrow_left.svg"
import bigLogo from "../Styles/image/bigLogo.png"
import PaymentItem from "../Components/PaymentItem";
import PriceAmount from "../Components/PriceAmount"



const Payment = () => {
    const nav = useNavigate()
    const [purchases, setPurchases] = useState(() => {
        if (localStorage.getItem("purchases") == ""){
            return []
        }
        const saved = localStorage.getItem("purchases")
        const initialValue = JSON.parse(saved)
        return initialValue
    })
    const [priceAmount, setPriceAmount] = useState(0)
    const [orderButton, setOrderButton] = useState("disabled")

    const deletePurchase = (purchase) => {
        const index = purchases.indexOf(purchase)
        purchases.splice(index, 1)
        setPurchases([...purchases])
        return index
    } 

    const countAmountOfPrice = () => {
        let amount = 0
        JSON.parse(localStorage.getItem("purchases")).forEach(element => {
            const price = element.price
            const count = element.count
            amount += price * count
        });
        setPriceAmount(amount)
    } 

    const setOrderButtonActive = (purchases) => {
        if (purchases.length > 0){
            setOrderButton("")
        }
        else{
            setOrderButton("disabled")
        }
    }

    const insertPurchase = (index, purchase) => {
        purchases.splice(index, 0, purchase)
        setPurchases([...purchases])
    }

    const changePurchaseById = (purchase) => {
        const oldPurchase = purchases.filter(el => el.id == purchase.id && el.type == purchase.type)[0]
        const index = deletePurchase(oldPurchase)
        insertPurchase(index, purchase)
    }

    const payPurchase = () => {
        postOrder()
        localStorage.setItem("purchases", JSON.stringify([]))
    }

    useEffect(() => {
        localStorage.setItem("purchases", JSON.stringify(purchases))
        countAmountOfPrice()
        console.log(localStorage.getItem("purchases"))

        setOrderButtonActive(purchases)
    }, [purchases])

    const postOrder = () => {
        const requestOptions = {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                id: 1,
                waiter: null,
                number: 1,
                menu_dishes: [1],
                menu_drinks: [1],
                status: "NA",
            })
        }
        fetch("http://127.0.0.1:8088/api/orders/", requestOptions)
            .then(data => console.log(data))
    }

    return (
        <Wrapper>
            <Content>
                <div className="payment__bg">
                    <Container>
                        <div className="order__back__flex">
                            <div className="back__button">
                                <Link onClick={() => nav(-1)}><img src={AroowIco} className="arrow__icon"></img></Link>
                            </div>
                            <div className="back__info">
                                Назад к Меню
                            </div>
                        </div>
                        <div className="payment__flex">
                            <div className="payment__additionat__column">
                                <img  src={bigLogo} className="payment__logo"></img>
                                <div className="payment__additiopnal__label">Примечание к заказу:</div>
                                <textarea maxLength={450} className="payment__additiopnal"></textarea>
                            </div>
                            <div className="payment__pricelist__flex">
                                <div className="payment__purchase">Ваш Заказ:</div>
                                {purchases.map(purchase => 
                                    <PaymentItem purchase={purchase} name={purchase.name} price={purchase.price} count={purchase.count} key={purchase.id + purchase.type} change={changePurchaseById} delete={deletePurchase}></PaymentItem>
                                )}
                                <PriceAmount className="order__price" amount={priceAmount}></PriceAmount>
                                <div className="payment__button">
                                    <button disabled={orderButton} onClick={() => {
                                        payPurchase()
                                        nav("/board")
                                    }}>Оплатить</button>
                                </div>
                            </div>
                        </div>
                        

                    </Container>
                </div>
            </Content>

        </Wrapper>
        
        
    );
}

export default Payment;