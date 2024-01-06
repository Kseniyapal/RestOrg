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
    let [tableNumber, setTableNumber] = useState("")
    const [additionalMessage, setAdditionalMessage] = useState("")
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
        const user = JSON.parse(localStorage.getItem("user"))
        if(user != ""){
            nav("/board")
        }
        else{
            nav("/")
        }
    }

    useEffect(() => {
        localStorage.setItem("purchases", JSON.stringify(purchases))
        countAmountOfPrice()
        console.log(localStorage.getItem("purchases"))

        setOrderButtonActive(purchases)
    }, [purchases])

    const postOrder = () => {
        const user = JSON.parse(localStorage.getItem("user"))
        let waiter = null
        const purchases = JSON.parse(localStorage.getItem("purchases"))
        const dishesList = []
        const drinksList = []
        console.log(JSON.parse(localStorage.getItem("purchases")))
        purchases.forEach(el => {
            if(el.type == "dish"){
                let count = el.count
                while(count > 0){
                    count -= 1
                    dishesList.push(el.id)
                    console.log(dishesList)
                }         
            }
            else{
                let count = el.count
                while(count > 0){
                    count -= 1
                    drinksList.push(el.id)
                }   
            }
        })
        if(user != "" && user.role == "W"){
            waiter = user.id
        }
        if(tableNumber == ""){
            tableNumber=1
        }
        const requestOptions = {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                waiter: waiter,
                number: 1,
                menu_dishes: dishesList,
                menu_drinks: drinksList,
                status: "NA",
                comment: addCountToAdditionalMessage(),
                number: tableNumber
                
            })
        }
        fetch("http://127.0.0.1:8088/api/orders/", requestOptions)
            .then(data => console.log(data))
    }

    const addCountToAdditionalMessage = () => {
        let additionalInfo = ""
        purchases.forEach(el => {
            additionalInfo += el.name +" - в количестве "+ el.count + " штук." + "\n"
        })
        return (additionalInfo + "\n") + additionalMessage
    }

    useEffect(() => {
        addCountToAdditionalMessage()
    }, [])

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
                                <textarea onChange={e => setAdditionalMessage(e.target.value)} maxLength={450} className="payment__additiopnal"></textarea>
                            </div>
                            <div className="payment__pricelist__flex">
                                <div className="payment__purchase">Ваш Заказ:</div>
                                {purchases.map(purchase => 
                                    <PaymentItem purchase={purchase} name={purchase.name} price={purchase.price} count={purchase.count} key={purchase.id + purchase.type} change={changePurchaseById} delete={deletePurchase}></PaymentItem>
                                )}
                                <input value={tableNumber} onChange={e => {
                                    if(e.target.value.slice(-1).match(/[0-9]/)|| e.target.value == ""){
                                        setTableNumber(e.target.value)
                                    }
                                    }} placeholder="Номер столика" className="payment__table"></input>
                                <PriceAmount className="order__price" amount={priceAmount}></PriceAmount>
                                <div className="payment__button">
                                    <button disabled={orderButton} onClick={() => {
                                        payPurchase()
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