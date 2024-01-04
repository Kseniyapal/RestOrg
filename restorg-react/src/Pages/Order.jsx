import React, { useState } from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import MenuItem from "../Components/MenuItem";
import WindowC from "../Components/UI/WindowC";
import AcceptButton from "../Components/UI/Buttons/AcceptButton"
import UserField from "../Components/UI/Fields/UserField";
import "./PagesStyles/Order.css";
import AroowIco from "../Styles/icons/arrow_left.svg"
import {useNavigate} from "react-router"
import {Link} from "react-router-dom"
import {useParams} from "react-router-dom"
import Image from "../Components/Image";
import { useEffect } from "react";
import PurchaseItem from "../Components/PurchaseItem";
import OrderItem from "../Components/OrderItem";

const Order = () => {
    const nav = useNavigate()
    const params = useParams()
    const [descriptionStyle, setDescriptionStyle] = useState({background: "#92B76E"})
    const [orders, setOrders] = useState([])
    const [dishes, setDishes] = useState([])
    const [drinks, setDrinks] = useState([])
    const [description, setDescription] = useState("Ожидsssает принятия в работу")
    let [order, setOrder] = useState({})
    let [waiterName, setWaiterName] = useState("")

    const fetchOrder = () => { 
        const token = JSON.parse(localStorage.getItem("token")).auth_token
        fetch("http://localhost:8088/api/orders/" + params.id + "/",{
            method: "GET",
            headers: { "Authorization": "Token "+ token,
            'Content-Type': 'application/json'} 
        })
        .then(response => response.json())
        .then(data => {
            setOrder(data)
        })        
    } 
    
    const fetchDishes = () => {
        fetch("http://localhost:8088/api/dishes/")
        .then(response => response.json())
        .then(data => {
            setDishes(data)
        })   
    }

    const fetchDrinks = () => {
        fetch("http://localhost:8088/api/drinks/")
        .then(response => response.json())
        .then(data => {
            setDrinks(data)
        }) 

    }


    const fetchUser = () => {
        const token = JSON.parse(localStorage.getItem("token")).auth_token
        fetch("http://localhost:8088/api/users/" + order.waiter + "/",{
            method: "GET",
            headers: { "Authorization": "Token "+ token,
            'Content-Type': 'application/json'} 
        })
        .then(response => response.json())
        .then(data => {
            setWaiterName(data.first_name +" "+ data.last_name)
        })   
    }

    useEffect(() => {
        fetchOrder()
    }, []) 

    useEffect(() => {
        seeDishes()
    }, [order])

    useEffect(() => {
        seeDrinks()
    }, [order])

    useEffect(() => {
        seeWaiter()
        changeDescription()
        changeDescriptionColor()
       
    }, [order])



    const addOrdersDrinks = () => {
        order.drinks.forEach(el => {
            drinks.forEach(drink => {
                if(drink.id == el){
                    orders.push(drink)
                    setOrders(orders)
                    console.log(orders)

                }
            }) 
        })
    }
 
    const addOrdersDishes = () => {
        
        order.dishes.forEach(el => {
            dishes.forEach(dish => {    
                if(dish.id == el){                    
                    orders.push(dish)
                    setOrders(orders)
                    console.log(orders)

                }
            })  
        })        
    }

    useEffect(() => {
        if( drinks != [] && dishes != [] && order.id != undefined){
            addOrdersDishes()
        }
    }, [dishes])

    useEffect(() => {
        if( drinks != [] && dishes != [] && order.id != undefined){
            addOrdersDrinks()
        }
        
    }, [drinks])

    const seeWaiter = () => {
        if(order.waiter == null){
            setWaiterName("Заказ ничей")
        }      
        else{
            fetchUser()
        }
    }

    const seeDishes = () => {
        if(order.dishes!=undefined)
            if(order.dishes.lenght != 0){
                fetchDishes()
            }      
    }

    const seeDrinks = () => {
        if(order.drinks!=undefined)
            if(order.drinks.lenght != 0){
                fetchDrinks()
            }      
    }

    const setOrderWorked = () => {
        const token = JSON.parse(localStorage.getItem("token")).auth_token
        const user = JSON.parse(localStorage.getItem("user"))
        let newStatus = ""

        if(user.role == "W" || user.role == "A"){
            if(order.status == "NA"){
                newStatus = "IP"
            }
            else if(order.status == "IP"|| order.status == "DDS" || order.status == "DDK"){
                newStatus = "DONE"
            }
            else{
                nav("/board") //удаление с серва
                return
            }
            
            fetch("http://localhost:8088/api/orders/" + params.id + "/",{
                    method: "PATCH",
                    headers: { "Authorization": "Token "+ token,
                    'Content-Type': 'application/json'}, 
                    body: JSON.stringify({
                        waiter: user.id,
                        status: newStatus
                    }) 
                })
            nav("/board")
        }

        else if(user.role == "C"){
            if(order.status == "IP"){
                newStatus = "DDS"
            }
            else{
                newStatus = "DONE"
            }
            fetch("http://localhost:8088/api/orders/" + params.id + "/",{
                    method: "PATCH",
                    headers: { "Authorization": "Token "+ token,
                    'Content-Type': 'application/json'}, 
                    body: JSON.stringify({
                        status: newStatus
                    }) 
                })
            nav("/board")

        }

        else if(user.role == "B"){
            if(order.status == "IP"){
                newStatus = "DDK"
            }
            else{
                newStatus = "DONE"
            }
            fetch("http://localhost:8088/api/orders/" + params.id + "/",{
                    method: "PATCH",
                    headers: { "Authorization": "Token "+ token,
                    'Content-Type': 'application/json'}, 
                    body: JSON.stringify({
                        status: newStatus
                    }) 
                })
            nav("/board")

        }


    }

    const changeDescription = () => {
        if(order.status == "NA"){
            setDescription("Ожидает принятия в работу")
        }
        else if(order.status == "IP" || order.status == "DDS" || order.status == "DDK"){
            setDescription("Ожидает приготовления")
        }
        else if(order.status == "DONE"){
            setDescription("Ожидает доставки")
        }
    }

    const changeDescriptionColor = () => {
        if(order.status == "IP" || order.status == "DDS" || order.status == "DDK"){
            setDescriptionStyle({background: "#BBC175"})
        }
        else if(order.status == "DONE"){
            setDescriptionStyle({background: "#C17575"})

        }
    }

    return (
        <Wrapper> 
            <div className="order__page__bg">
                <Container>
                    <Content>    
                            <div className="order__flex__column">
                                <div className="order__back__flex">
                                    <div className="back__button">
                                        <Link onClick={() => nav(-1)}><img src={AroowIco} className="arrow__icon"></img></Link>
                                    </div>
                                    <div className="back__info">
                                        Назад к Таблице
                                    </div>
                                </div>
                                <div className="order__info__flex">
                                    <div className="order__header__flex">
                                        <div className="number__info__flex">
                                            <div className="oreder__number">
                                                205
                                            </div>
                                            <div className="table__info">
                                                номер стола <span className="table__number">{order.table_number}</span>
                                            </div>
                                        </div>
                                        <div className="role__info__flex">
                                            <div className="waiter__info">
                                                Официант:<br/> {waiterName}
                                            </div>
                                            <div style={descriptionStyle} className="order__status">
                                                {description}
                                            </div>
                                            {/* <div className="order__time">
                                                20:31
                                            </div> */}
                                        </div>
                                    </div>
                                    <div className="order__application">
                                        <div className="application__title">{order.comment == "" ? "" : "Примечание:"}</div>
                                        <div className="application__info">
                                            {order.comment == "" ? "" : order.comment}
                                        </div>
                                    </div>
                                    <div className="order__done__button">
                                        <button onClick={setOrderWorked}>Заказ Отработан</button>
                                    </div>
                                    <div className="orders__list__grid">
                                        {orders.map(el => 
                                                <OrderItem key={el.id + el.name} name={el.name} imgSource={el.image}></OrderItem>
                                        )}
                                    </div>          
                                </div>
                            </div>
                    </Content>
                </Container>
            </div>
        </Wrapper>
    );
}

export default Order;