import React, { useEffect, useRef, useState } from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import MenuItem from "../Components/MenuItem";
import PurchaseItem from "../Components/PurchaseItem"
import WindowC from "../Components/UI/WindowC";
import AcceptButton from "../Components/UI/Buttons/AcceptButton"
import UserField from "../Components/UI/Fields/UserField";
import "./PagesStyles/Menu.css";
import SearchIco from "../Styles/icons/search_ico.svg"
import WaterIco from "../Styles/icons/Water.png"
import HotIco from "../Styles/icons/Hot.png"
// import ImgSource from "../../public/images/1644909112_9-fikiwiki-com-p-kartinki-yaichnitsa-glazunya-10.jpg"

const Menu = () => {
    const [purchases, setPurchases] = useState([])
    const [drinks, setDrinks] = useState([])
    const [dishes, setDishes] = useState([])

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

    const deleteItem = (purchase) => {
        const index = purchases.indexOf(purchase)
        purchases.splice(index, 1)
        setPurchases([...purchases])
    } 
    
    useEffect(() => {
        fetchDishes()
        fetchDrinks()
    }, [])

    const addPurchase = (purchase) => {
        if(purchases.filter(el => el.id == purchase.id).length == 0)
        setPurchases([...purchases, purchase])
    }
    
    return (
        <Wrapper> 
            <Header/>
            <Content>
                <div className="menu__bg">
                    <Container>
                        <div className="menu__window__flex">

                            <div className="menu__search">
                                <img src={SearchIco}></img>
                                <input placeholder="Поиск по названию..."></input>
                            </div>

                            <div className="menu__list__flex">
                                <div className="menu__hot">
                                    <div className="menu__head">
                                        <img src={HotIco}></img>
                                        <span>Блюда</span>
                                    </div>
                                    
                                    <hr></hr>

                                    <div className="menu__grid">
                                        {dishes.map((dish) => 
                                            <MenuItem addPurch={() =>addPurchase(dish)} key={dish.id} link="/menu_position" name={dish.name} imgSource={dish.image} mass={dish.weight + "г"} cost={dish.price + "₽"}></MenuItem>
                                        )}
                                    </div>
                                    
                                </div>


                                <div className="menu__water">
                                    <div className="menu__head">
                                        <img src={WaterIco}></img>
                                        <span>Напитки</span>
                                    </div>
                                    
                                    <hr></hr>

                                    <div className="menu__grid">
                                        {drinks.map((dish) => 
                                            <MenuItem addPurch={addPurchase} key={dish.id} id={dish.id} link="/menu_position" name={dish.name} imgSource={dish.image} cost={dish.price + "₽"}></MenuItem>
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
                                    <PurchaseItem id={purchase.id} purchase={purchase} delete={deleteItem} key={purchase.id} imgSource={purchase.image}/>
                                )}

                            </div>

                            <div className="order__button">
                                <button>Оформить заказ</button>
                            </div>

                        </div>
                        
                    </Container>
                </div>
                
            </Content>


            <Footer/>
        </Wrapper>
        
        
    );
}

export default Menu;