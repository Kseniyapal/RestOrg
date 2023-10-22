import React from "react";
import Container from "./Container.jsx";
import "./ComponentsStyles/Header.css";
import logo from "../Styles/icons/logo.png";
import menuIco from "../Styles/icons/menu.svg";

const Header = () => {
    return (
        <div className="header__bg">
            <Container>
                <div className="header__flex">
                    <div className="header__nav__flex">
                        <div className="header__main"><a href="/main">на главную</a></div>
                        <div className="header__about"><a href="/main">о сервисе</a></div>
                    </div>
                    <div className="header__logo">
                        <img src={logo}/>
                    </div>
                    <div className="header__menu">
                        <img src={menuIco} />
                    </div>
                    
                </div>
            </Container>
        </div>
    )
}

export default Header;