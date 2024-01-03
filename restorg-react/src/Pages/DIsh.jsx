import React, { useEffect, useState } from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import MenuItem from "../Components/MenuItem";
import WindowC from "../Components/UI/WindowC";
import AcceptButton from "../Components/UI/Buttons/AcceptButton"
import UserField from "../Components/UI/Fields/UserField";
import "./PagesStyles/Dish.css";
import AroowIco from "../Styles/icons/arrow_left.svg"
import {useNavigate} from "react-router"
import {Link} from "react-router-dom"
import {useParams} from "react-router-dom"
import Image from "../Components/Image"
import cal from "../Styles/image/dish_img.jpeg"

const Dish = () => {
    let [dish, setDish] = useState({})
    let nav = useNavigate()
    let params = useParams()

    const fetchDish = () => { 
        fetch("http://localhost:8088/api/dishes/" + params.id + "/")
        .then(response => response.json())
        .then(data => {
            data.type = "dish"
            setDish(data)
        })        
    }  

    const fetchDrink = () => { 
        fetch("http://localhost:8088/api/drinks/" + params.id + "/")
        .then(response => response.json())
        .then(data => {
            data.type = "drink"
            setDish(data)
        })        
    }  

    const addPurchase = (dish) => {
        let purchaseList = JSON.parse(localStorage.getItem("purchases"))
        if(purchaseList.filter(el => el.id == dish.id && el.type == dish.type).length == 0){
            dish.count = 1
            purchaseList.push(dish)
            localStorage.setItem("purchases", JSON.stringify(purchaseList))
        }
        nav(-1)
    }

    useEffect(() => {
        if(params.type == "dish"){
            fetchDish()
        }
        else{
            fetchDrink()
        }
    }, [])


    return (
        <Wrapper> 
            <div className="dish__page__bg">
                <Container>
                    <Content>
                        <div className="dish__flex__column">
                            <div className="order__back__flex">
                                <div className="back__button">
                                <Link onClick={() => nav(-1)}><img src={AroowIco} className="arrow__icon"></img></Link>
                                </div>
                                <div className="back__info">
                                    Назад к Меню
                                </div>
                            </div>
                            <div className="dish__info">
                                <div className="dish__info__flex">
                                    <div className="dish__image">
                                        <Image imgSource={dish.image} alt={dish.image}></Image>
                                    </div>
                                    <div className="dish__add__flex">
                                        <div className="dish__name">
                                            {dish.name}
                                        </div>
                                        <div className="dish__add__row__flex">
                                            <div className="dish__cost">
                                                    Масса:<br></br>
                                                    {dish.weight} гр.
                                            </div>
                                            <div className="dish__mass">
                                                    Цена:<br></br>
                                                    {dish.price} ₽
                                            </div>
                                        </div>
                                        <div className="dish__add__button">
                                            <button onClick={() => addPurchase(dish)}>Добавить к заказу</button>
                                        </div>
                                    </div>
                                </div>
                                <div className="dish__compound__flex">
                                    <div className="compound__title">Описание:</div>
                                    <div className="compound__text">
                                        Пример - как бы выглядело описание. При создании генератора мы использовали
                                        небезизвестный универсальный код речей. Текст генерируется абзацами случайным образом от 
                                        двух до десяти предложений в абзаце, что позволяет сделать текст более привлекательным и живым.
                                    </div>
                                </div>
                            </div>
                        </div>      
                    </Content>
                </Container>
            </div>
        </Wrapper>
    );
}

export default Dish;