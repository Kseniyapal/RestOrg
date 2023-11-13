import React from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import WindowC from "../Components/UI/WindowC";
import AcceptButton from "../Components/UI/Buttons/AcceptButton"
import UserField from "../Components/UI/Fields/UserField";
import "./PagesStyles/Sign.css";




const Sign = () => {
    return (
        <Wrapper>
            <Header/>
            <Content>
                <div className="sign__bg">
                    <Container>
                        <div className="window__center">    
                            <div className="sign__window">
                                <UserField name="почта"/>
                                <UserField type="password" name="пароль"/>
                                
                                
                                <div className="sign__continue__flex">
                                    <button className="sign__button">Войти</button>
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

export default Sign;