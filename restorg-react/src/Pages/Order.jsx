import React, { useState } from "react";
import  Container  from "../Components/Container";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import "./PagesStyles/Order.css";
import AroowIco from "../Styles/icons/arrow_left.svg"
import {useNavigate} from "react-router"
import {Link} from "react-router-dom"
import {useParams} from "react-router-dom"
import { useEffect } from "react";
import OrderItem from "../Components/OrderItem";

const Order = () => {
    const nav = useNavigate()
    const params = useParams()
    const [descriptionStyle, setDescriptionStyle] = useState({background: "#92B76E"})
    const [orders, setOrders] = useState([])
    const [description, setDescription] = useState("Ожидает принятия в работу")
    let [order, setOrder] = useState({})
    let [waiterName, setWaiterName] = useState("")

    const fetchOrder = () => { 
        let token = JSON.parse(localStorage.getItem("token"))
        if(token != null && token != undefined && token != ""){
            token = JSON.parse(localStorage.getItem("token")).auth_token
            fetch("http://localhost:8088/api/orders/" + params.id + "/",{
                method: "GET",
                headers: { "Authorization": "Token "+ token,
                'Content-Type': 'application/json'} 
            })
            .then(response => response.json())
            .then(data => {
                if(data.detail == "Not found."){
                    nav("not found")
                    return
                }
                if(data.drinks == undefined){
                    fetchDishes(data)
                }
                else if(data.dishes == undefined){
                    fetchDrinks(data)
                }
                else {
                    fetchDishesAndDrinks(data)
                }
                setOrder(data)
                console.log(data)
            })  
        }   
        else{
            nav("/notFound")
        }   
    } 
    
    const fetchDishes = (orderData) => {
        fetch("http://localhost:8088/api/dishes/")
        .then(response => response.json())
        .then(data => {
            const newDishes = []
            orderData.dishes.forEach(dishId => {
                data.forEach(dish => {
                    if(dish.id == dishId){
                        newDishes.push(dish)
                    }
                })
            });
            setOrders([...orders, ...newDishes])
        })   
    }

    const fetchDrinks = (orderData) => {
        fetch("http://localhost:8088/api/drinks/")
        .then(response => response.json())
        .then(data => {
            const newDrinks = []
            orderData.drinks.forEach(drinkId => {
                data.forEach(drink => {
                    if(drink.id == drinkId){
                        newDrinks.push(drink)
                    }
                })
            });
            setOrders([...orders, ...newDrinks])
        })  
    }

    const fetchDishesAndDrinks = (orderData) => {
        fetch("http://localhost:8088/api/dishes/")
        .then(response => response.json())
        .then(data => {
            const newDishes = []
            orderData.dishes.forEach(dishId => {
                data.forEach(dish => {
                    if(dish.id == dishId){
                        newDishes.push(dish)
                    }
                })
            });
            
            fetch("http://localhost:8088/api/drinks/")
            .then(response => response.json())
            .then(data => {
                const newDrinks = []
                orderData.drinks.forEach(drinkId => {
                    data.forEach(drink => {
                        if(drink.id == drinkId){
                            newDrinks.push(drink)
                        }
                    })
                });
                setOrders([...orders, ...newDrinks, ...newDishes])
            })  
        })   
    }


    const fetchUser = () => {
        if(JSON.parse(localStorage.getItem("token")) != null){
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
    }

    useEffect(() => {
        fetchOrder()
    }, []) 

    useEffect(() => {
        seeWaiter()
        changeDescription() 
        changeDescriptionColor()
    }, [order])

    const seeWaiter = () => {
        if(order.waiter == null){
            setWaiterName("")
        }      
        else{
            fetchUser()
        }
    }

    const setOrderWorked = () => {
        const token = JSON.parse(localStorage.getItem("token")).auth_token
        const user = JSON.parse(localStorage.getItem("user"))
        let newStatus = ""
        if(user.role == "W"){
            if(order.status == "NA"){
                if(order.dishes == undefined){
                    newStatus = "DDS" 
                }
                else if(order.drinks == undefined){
                    newStatus = "DDR"
                }
                else{
                    newStatus = "IP" 
                }
            }
            else if(order.status == "IP"|| order.status == "DDS" || order.status == "DDR"){
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
            else if(order.status == "DDS"){
                newStatus = "DDS"
            }
            else{
                newStatus = "DDS"
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
                newStatus = "DDR"
            }
            else if(order.status == "DDR"){
                newStatus = "DDR"
            }
            else if(order.status == "DDS"){
                newStatus = "DDR"

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
        else if(user.role == "A"){
            if(order.status == "NA"){
                newStatus = "IP"
            }
            else if(order.status == "IP"){
                newStatus = "DDS"
            }
            else if(order.status == "DDS"){
                newStatus = "DDR"
            }
            else if(order.status == "DDR"){
                newStatus = "DDS"
            }
            fetch("http://localhost:8088/api/orders/" + params.id + "/",{
                    method: "PATCH",
                    headers: { "Authorization": "Token "+ token,
                    'Content-Type': 'application/json'}, 
                    body: JSON.stringify({
                        status: newStatus,
                        waiter: 3
                    }) 
                })
            nav("/board")
        }
    }

    const changeDescription = () => {
        if(order.status == "NA"){
            setDescription("Ожидает принятия в работу")
        }
        else if(order.status == "IP" || order.status == "DDS" || order.status == "DDR"){
            setDescription("Ожидает приготовления")
        }
        else if(order.status == "DONE"){
            setDescription("Ожидает доставки")
        }
    }

    const changeDescriptionColor = () => {
        if(order.status == "IP" || order.status == "DDS" || order.status == "DDR"){
            setDescriptionStyle({background: "#BBC175"})
        }
        else if(order.status == "DONE"){
            setDescriptionStyle({background: "#C17575"})
        }
    }

    const adminEditButton = () => {
        const user = JSON.parse(localStorage.getItem("user"))
        if(user != null && user.role == "A"){
            return (
                <div className="order__edit">
                    <button onClick={() => nav("/order_edit/" + order.id)}>Редактировать заказ</button>
                </div>
            )
        }
        else{
            return <div></div>
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
                                        <Link to="/board"><img src={AroowIco} className="arrow__icon"></img></Link>
                                    </div>
                                    <div className="back__info">
                                        Назад к Таблице
                                    </div>
                                </div>
                                <div className="order__info__flex">
                                    <div className="order__header__flex">
                                        <div className="number__info__flex">
                                            <div className="oreder__number">
                                                {order.id}
                                            </div>
                                            <div className="table__info">
                                                номер стола <span className="table__number">{order.table_number}</span>
                                            </div>
                                        </div>
                                        <div className="role__info__flex">
                                            <div className="waiter__info">
                                                {order.waiter==null? "":"Официант:"}<br/> {waiterName}
                                            </div>
                                            <div style={descriptionStyle} className="order__status">
                                                {description}
                                            </div>
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
                                    {adminEditButton()}    
                                </div>
                            </div>
                    </Content>
                </Container>
            </div>
        </Wrapper>
    );
}

export default Order;