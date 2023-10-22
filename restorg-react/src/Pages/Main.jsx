import React from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import "./PagesStyles/Main.css";
import background from "../Styles/image/3321789.png";
import WindowC from "../Components/UI/WindowC";
import bigLogo from "../Styles/image/bigLogo.png"

const Main = () => {
    return (
        <div>
        <Wrapper>
            <Header/>
            <Content>
                <div className="main__bg">
                    <Container>
                        
                        <img  src={bigLogo} className="main__logo"></img>
                            
                        <WindowC>
                            
                        </WindowC>
                    </Container>
                </div>
            </Content>
            <Footer/>
        </Wrapper>
        </div>
        
    );
}

export default Main;