import React from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import "./PagesStyles/Main.css";
import WindowC from "../Components/UI/WindowC";
import menuLogo from "../Styles/icons/Group 28.png"
import userLogo from "../Styles/icons/User.png"
import bigLogo from "../Styles/image/bigLogo.png"
import AcceptButton from "../Components/UI/Buttons/AcceptButton"
import AcceptButtonMini from "../Components/UI/Buttons/AcceptButtomMini"


const Main = () => {
    return (
        <div className="main">
        <Wrapper>
            
            <Header className="main__header"/>
            
            <Content>
                <div className="main__bg">
                    <Container>
                        
                        <img  src={bigLogo} className="main__logo"></img>
        
                        <WindowC>   
                            <AcceptButton href='/menu' className="AcceptButton" >Заказ Блюд</AcceptButton>
                            <AcceptButton href='/menu' className="AcceptButton">Заказ На Баре</AcceptButton>                      
                        </WindowC>
                        
                        <AcceptButtonMini href='/board' className='AcceptButtonMini'>
                            <img src={menuLogo} className="buttonImg"></img>
                            Таблица<br/> Заказов
                        </AcceptButtonMini>
                    
                        <AcceptButtonMini href='/sign' className='AcceptButtonMini'>
                            <img src={userLogo} className="buttonImg"></img>
                            Войти как<br/> работник
                        </AcceptButtonMini>
                    
                    </Container>
                </div>
            </Content>
            <div className="info__bg" id="about">
                <Container>

                    <div className="info__flex">
                    
                        <div className="info__line">
                            <hr></hr>
                        </div>

                        <div className="main__info">

                            <div className="info__about__flex">
                                <div className="info__about__text">
                                    <span> О Сервисе</span>
                                    <div>
                                    Сайт рыбатекст поможет дизайнеру, верстальщику, вебмастеру сгенерировать
                                    несколько абзацев более менее осмысленного текста рыбы на русском языке,а начинающему оратору отточить навык публичных выступлений в домашних условиях. 
                                    При создании генератора мы использовали небезизвестный универсальный код речей. 
                                    Текст генерируется абзацами случайным образом от двух до десяти предложений в абзаце, что позволяет сделать текст более привлекательным и живым для визуально-слухового восприятия.
                                    </div>
                                </div>
                                
                            </div>

                            <div className="info__admin_flex">
                        
                                <div className="info__about__text"> 
                                    <span> Администратор </span>
                                    По своей сути рыбатекст является альтернативой традиционному 
                                    lorem ipsum, который вызывает у некторых людей недоумение при попытках прочитать рыбу текст. В отличии от lorem ipsum, текст 
                                    рыба на русском языке наполнит любой макет непонятнымсмыслом и придаст неповторимый колорит советских времен.
                                </div>

                            </div>
                        </div>

                        <div className="info__line">
                            <hr></hr>
                        </div>
                    </div>
                </Container>
            </div>
            <Footer/>
        </Wrapper>
        
        </div>
    );
}

export default Main;