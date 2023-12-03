import React from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import WindowC from "../Components/UI/WindowC";
import AcceptButton from "../Components/UI/Buttons/AcceptButton"
import UserField from "../Components/UI/Fields/UserField";
import "./PagesStyles/Register.css";




const Register = () => {
    return (
        <Wrapper>
            <Header/>
            <Content>
                <div className="register__bg">
                    <Container>
                        <div className="window__center">    
                            <div className="register__window">

                                <div className="register__name__flex">
                                    <UserField name="имя"/>
                                    <UserField name="фамилия"/>
                                </div>

                                <div className="register__fatherly">
                                    <UserField name="отчество*"/>
                                </div>

                                <div className="register__main">
                                    <UserField name="почта"/>
                                    <UserField name="логин"/>
                                    <UserField type="password" name="пароль"/>
                                </div>
                                            
                                <div className="register__continue__flex">
                                    <button className="register__button">Зарегистрироваться</button>
                                    <a href="/" className="a__back">Назад</a>
                                </div>
                                
                            </div>
                            
                        </div> 
                    
                    </Container>
                </div>
            </Content>

            <Footer/>
        </Wrapper>
        
        
    );
}

export default Register;