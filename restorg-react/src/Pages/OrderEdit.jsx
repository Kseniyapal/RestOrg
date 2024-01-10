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

const OrderEdit = () => {
    const nav = useNavigate()
    const params = useParams()
    const [descriptionStyle, setDescriptionStyle] = useState({background: "#92B76E"})
    const [orders, setOrders] = useState([])
    const [description, setDescription] = useState("Ожидает принятия в работу")
    const [order, setOrder] = useState({})
    const [waiterId, setWaiterId] = useState(3)
    const [message, setMessage] = useState("")
    const [comment, setComment] = useState("")
    const [tableNumber, setTableNumber] = useState("")
    const [waiters, setWaiters] = useState([])
    const [dishes, setDishes] = useState([])
    const [drinks, setDrinks] = useState([])

    let newDishes = []
    let newDrinks = []

    const fetchOrder = () => { 
        const token = JSON.parse(localStorage.getItem("token"))?.auth_token
        if(token){
            fetch("http://localhost:8088/api/orders/" + params.id + "/",{
                method: "GET",
                headers: { "Authorization": "Token "+ token,
                'Content-Type': 'application/json'} 
            })
            .then(response => response.json())
            .then(data => {
                if(data.detail == "Not found."){
                    nav("/notFound")
                    return
                }
                else if(JSON.parse(localStorage.getItem("user")).role != "A"){
                    nav("/notFound")
                    return
                }


                fetchDishesAndDrinks(data)

                setOrder(data)
                console.log(data)
                setComment(data.comment)
                setTableNumber(data.table_number)
                if(data.waiter == null){
                    setWaiterId(3)
                }
                else{
                    setWaiterId(data.waiter)
                }
                
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
                orderData.drinks.forEach(drinkId => {
                    data.forEach(drink => {
                        if(drink.id == drinkId){
                            newDrinks.push(drink)
                        }
                    })
                });
                setOrders([...orders, ...newDrinks, ...newDishes])
                setDishes(newDishes)
                setDrinks(newDrinks)
            })  
        })   
    }

    const fetchUsers = () => {
        const token = JSON.parse(localStorage.getItem("token"))?.auth_token
        if(token){
            fetch("http://localhost:8088/api/users/",{
                method: "GET",
                headers: { "Authorization": "Token "+ token,
                'Content-Type': 'application/json'} 
            })
            .then(response => response.json())
            .then(data => {
                const newWaiters = []
                data.forEach(worker => {
                    if(worker.role == "W"){
                        newWaiters.push(worker)
                    }
                })
                setWaiters(newWaiters)
            })  
        }
        else{
            nav("/notFound")
        }
    }
    
    const patchOrder = () => { 
        const token = JSON.parse(localStorage.getItem("token"))?.auth_token; 
        if (token) { 
            const dishesId = dishes.map(el => el.id)
            const drinksId = drinks.map(el => el.id)

            const requestBody = { 
                waiter: Number.parseInt(waiterId), 
                comment: comment, 
                number: tableNumber, 
                menu_dishes: dishesId,
                menu_drinks: drinksId
            }; 
     
            fetch("http://localhost:8088/api/orders/" + params.id + "/", { 
            method: "PATCH", 
            headers: { 
                "Authorization": "Token " + token, 
                'Content-Type': 'application/json' 
            }, 
            body: JSON.stringify(requestBody) 
            }) 
            .then(response => { 
                if (response.ok) { 
                    nav("/order/" + params.id + "/"); 
                } else { 
                    setMessage("Данные не верны"); 
                } 
            }) 
            .catch(error => { 
                console.error('Error editing order:', error); 
            }); 
        } 
    };

    useEffect(() => {
        fetchOrder()
        fetchUsers()
    }, []) 

    useEffect(() => {
        changeDescription() 
        changeDescriptionColor()
    }, [order])


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

    const deleteItem = (dish) => {
        if(orders.length > 1){
        if(dish.weight == undefined){
            newDrinks = drinks
            newDrinks = newDrinks.filter(el => el.id != dish.id)
            setOrders([...newDrinks, ...dishes])
            setDrinks(newDrinks)
        }
        else{
            newDishes = dishes
            newDishes = newDishes.filter(el => el.id != dish.id)
            setOrders([...newDishes, ...drinks])
            setDishes(newDishes)
        }
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
                                        <Link to={"/order/" + order.id}><img src={AroowIco} className="arrow__icon"></img></Link>
                                    </div>
                                    <div className="back__info">
                                        Отмена редактирования
                                    </div>
                                </div>
                                <div className="order__info__flex">
                                    <div className="order__header__flex">
                                        <div className="number__info__flex">
                                            <div className="oreder__number">
                                                {order.id}
                                            </div>
                                            <div className="table__info">
                                                номер стола <span className="table__number"><input value={tableNumber} onChange={e => {
                                                if(e.target.value.slice(-1).match(/[0-9]/)|| e.target.value == ""){
                                                    setTableNumber(e.target.value)
                                                }
                                                }} maxLength={3} >
                                                </input>
                                                </span>
                                            </div>
                                        </div>
                                        <div className="role__info__flex">
                                            <div className="waiter__info">
                                                <select value={waiterId} onChange={e => setWaiterId(e.target.value)}>
                                                    {waiters.map(waiter => 
                                                        <option key={waiter.id} value={waiter.id}>{waiter.id}.{waiter.first_name} {waiter.last_name}</option>    
                                                    )}
                                                </select>
                                            </div>
                                            <div style={descriptionStyle} className="order__status">
                                                {description}
                                            </div>
                                        </div>
                                    </div>
                                    <div className="order__application">
                                        <div className="application__title">{order.comment == "" ? "" : "Примечание:"}</div>
                                        <div className="application__info">
                                            <textarea onChange={e => setComment(e.target.value)} value={comment}></textarea>
                                        </div>
                                    </div>
                                    <div className="order__done__button">
                                        <button onClick={patchOrder}>Принять изменения</button>
                                    </div>
                                    <div className="orders__list__grid">
                                        {orders.map(el => 
                                                <OrderItem element={el} deleteFunction={deleteItem} deleteButton={true} key={el.id + el.name} name={el.name} imgSource={el.image}></OrderItem>
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

export default OrderEdit;