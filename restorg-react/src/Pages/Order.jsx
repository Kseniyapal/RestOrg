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
import "./PagesStyles/Order.css";
import AroowIco from "../Styles/icons/arrow_left.svg"






const Order = () => {
    return (
        <Wrapper> 
            <div className="order__page__bg">
                <Container>
                    <Content>
                        
                            
                            <div className="order__flex__column">
                                <div className="order__back__flex">
                                    <div className="back__button">
                                        <a href="javascript:history.back()"><img src={AroowIco} className="arrow__icon"></img></a>
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
                                                номер стола <span className="table__number">19</span>
                                            </div>

                                        </div>

                                        <div className="role__info__flex">
                                            <div className="waiter__info">
                                                Официант: Имя
                                            </div>
                                            <div className="order__status">
                                                ожидает принятия в работу
                                            </div>
                                            <div className="order__time">
                                                20:31
                                            </div>

                                        </div>

                                    </div>

                                    <div className="order__application">
                                        <div className="application__title">Примечание:</div>

                                        <div className="application__info">
                                            При создании генератора мы использовали небезизвестный универсальный код речей.
                                            Текст генерируется абзацами случайным образом от двух до десяти предложений в абзаце,
                                            что позволяет сделать текст более привлекательным и живым.
                                        </div>
                                    </div>

                                    <div className="order__done__button">
                                        <button>Заказ Отработан</button>
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