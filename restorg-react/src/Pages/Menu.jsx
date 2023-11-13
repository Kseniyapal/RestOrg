import React from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import WindowC from "../Components/UI/WindowC";
import AcceptButton from "../Components/UI/Buttons/AcceptButton"
import UserField from "../Components/UI/Fields/UserField";
import "./PagesStyles/Menu.css";
import SearchIco from "../Styles/icons/search_ico.svg"
import WaterIco from "../Styles/icons/Water.png"
import HotIco from "../Styles/icons/Hot.png"





const Register = () => {
    return (
        <Wrapper>
            <Header/>
            <Content>
                <div className="menu__bg">
                    <Container>
                        <div className="menu__window__center">    
                            <div className="menu__window__flex">

                                <div className="menu__search">
                                    <img src={SearchIco}></img>
                                    <input placeholder="Поиск по названию..."></input>
                                </div>

                                <div className="menu__list">

                                    <div className="menu__water">
                                        <div className="menu__head">
                                            <img src={WaterIco}></img>
                                            <span>Напитки</span>
                                        </div>
                                        
                                        <hr></hr>

                                        <div className="menu__grid">
                                            <div className="grid__item">

                                            </div>
                                        </div>
                                        
                                    </div>

                                    <div className="menu__water">
                                        <div className="menu__head">
                                            <img src={HotIco}></img>
                                            <span>Горячее</span>
                                        </div>
                                        
                                        <hr></hr>

                                        <div className="menu__grid">
                                            <div className="grid__item">

                                            </div>
                                        </div>
                                        
                                    </div>
                                    
                                </div>




                                
                            </div>
                            
                        </div>
                
                    </Container>
                </div>
                <div className="menu__order">
                            
                </div>
                
            </Content>


            <Footer/>
        </Wrapper>
        
        
    );
}

export default Register;