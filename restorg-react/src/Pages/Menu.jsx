import React, { useEffect, useState } from "react";
import { useLocation, useParams } from "react-router"
import { useNavigate } from "react-router"
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import MenuItem from "../Components/MenuItem";
import PurchaseItem from "../Components/PurchaseItem"
import "./PagesStyles/Menu.css";
import WaterIco from "../Styles/icons/Water.png"
import HotIco from "../Styles/icons/Hot.png"
import PriceAmount from "../Components/PriceAmount";

const Menu = () => {
    const params = useParams()
    const [purchases, setPurchases] = useState(() => {
        if (localStorage.getItem("purchases") == null || localStorage.getItem("purchases") == ""){
            return []
        }
        const saved = localStorage.getItem("purchases")
        const initialValue = JSON.parse(saved)
        return initialValue
    })
    const [drinks, setDrinks] = useState([])
    const [dishes, setDishes] = useState([])
    const [priceAmount, setPriceAmount] = useState(0)
    const [orderButton, setOrderButton] = useState("disabled")

    const fetchDishes = () => {
        fetch("http://localhost:8088/api/dishes/")
        .then(response => response.json())
        .then(data => setDishes(data))
    }  

    const fetchDrinks = () => {
        fetch("http://localhost:8088/api/drinks/")
        .then(response => response.json())
        .then(data => setDrinks(data))
    }  

    const deletePurchase = (purchase) => {
        const index = purchases.indexOf(purchase)
        purchases.splice(index, 1)
        setPurchases([...purchases])
        return index
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

    const addPurchase = (purchase) => {
        if(purchases.filter(el => el.id == purchase.id && el.type == purchase.type).length == 0){
            setPurchases([...purchases, purchase])
        }
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

    useEffect(() => {
        if(params.drinks == undefined || params.drinks == "drinks"){
            fetchDishes()
            fetchDrinks()
        }
        else{
            nav("/notFound")
        }
        localStorage.setItem("purchases", JSON.stringify([]))

    }, [])

    const menuDIsh = () => {
        if(params.drinks == "drinks"){
            return <div></div>
        }
        else{
            return (
            <div className="menu__hot">
                <div className="menu__head">
                    <img src={HotIco}></img>
                    <span >Блюда</span>
                </div>
                <hr id="dishes"></hr>
                <div className="menu__grid">
                    {dishes.map((dish) => 
                        <MenuItem type={"dish"} addPurch={addPurchase} key={dish.id} id={dish.id} name={dish.name} imgSource={dish.image} mass={dish.weight + "г"} price={dish.price + "₽"}></MenuItem>
                    )}
                </div>                                  
            </div>
            )
        }
    }

    useEffect(() => {
        localStorage.setItem("purchases", JSON.stringify(purchases))
        countAmountOfPrice()
        setOrderButtonActive(purchases)
    }, [purchases])

    const nav = useNavigate()
    const location = useLocation()    
    return (
        <Wrapper> 
            <Header/>
            <Content>
                <div className="menu__bg">
                    <Container>
                        <div className="menu__window__flex">
                            <div className="menu__search">
                                <a href={location.pathname + "#dishes"} className="search__drink">
                                    <img src={HotIco}></img>
                                    <span>Блюда</span>
                                </a>
                                <a href={location.pathname + "#drinks"} className="search__drink">
                                    <img src={WaterIco}></img>
                                    <span>Напитки</span>
                                </a>
                            </div>
                            <div className="menu__list__flex">
                                {menuDIsh()}
                                <div  className="menu__water">
                                    <div className="menu__head">
                                        <img src={WaterIco}></img>
                                        <span>Напитки</span>
                                    </div>               
                                    <hr id="drinks" ></hr>
                                    <div className="menu__grid">
                                        {drinks.map((dish) => 
                                            <MenuItem type={"drink"} volume={dish.volume + "мл."} addPurch={addPurchase} key={dish.id} id={dish.id} name={dish.name} imgSource={dish.image} price={dish.price + "₽"}></MenuItem>
                                        )}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </Container>
                </div>
                <div className="menu__order">
                    <Container>
                        <div className="order__flex">
                            <div className="order__list__flex">
                                {purchases.map((purchase) => 
                                      <PurchaseItem count={purchase.count} name={purchase.name} id={purchase.id} purchase={purchase} change={changePurchaseById} delete={deletePurchase} key={purchase.type + purchase.id} imgSource={purchase.image}/>
                                )}
                            </div>
                            <div className="order__button">
                                <button onClick={() => {
                                    nav("/payment")
                                }} disabled={orderButton}>Оформить заказ</button>                                     
                                <PriceAmount className="order__price" amount={priceAmount}></PriceAmount>          
                            </div>
                        </div>
                    </Container>
                </div>
            </Content>
        </Wrapper>
        
        
    );
}

export default Menu;