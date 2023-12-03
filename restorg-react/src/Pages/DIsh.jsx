import React from "react";
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
import DishImg from "../Styles/image/dish_img.jpeg"






const Dish = () => {
    return (
        <Wrapper> 
            <div className="dish__page__bg">
                <Container>
                    <Content>
                        
                        <div className="dish__flex__column">
                            <div className="order__back__flex">
                                <div className="back__button">
                                    <a href="javascript:history.back()"><img src={AroowIco} className="arrow__icon"></img></a>
                                </div>
                                <div className="back__info">
                                    Назад к Меню
                                </div>
                            </div>

                            <div className="dish__info">
                                <div className="dish__info__flex">
                                    <div className="dish__image">
                                        <img src={DishImg}></img>
                                    </div>

                                    <div className="dish__add__flex">
                                        <div className="dish__name">
                                            Название
                                        </div>

                                        <div className="dish__add__row__flex">
                                            <div className="dish__cost">

                                                    Масса:<br></br>
                                                    350 гр.

                                            </div>

                                            <div className="dish__mass">
                                                    Цена:<br></br>
                                                    700 ₽

                                            </div>
                                        </div>

                                        <div className="dish__add__button">
                                            <button>Добавить к заказу</button>

                                        </div>

                                    </div>

                                </div>
                            


                                <div className="dish__compound__flex">
                                    <div className="compound__title">Состав:</div>
                                    <div className="compound__text">
                                        Сайт рыбатекст поможет дизайнеру, верстальщику, вебмастеру сгенерировать несколько абзацев
                                        более менее осмысленного текста рыбы на русском языке, а начинающему оратору отточить 
                                        навык публичных выступлений в домашних условиях. При создании генератора мы использовали
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