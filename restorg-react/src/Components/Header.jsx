import React, { useState } from "react";
import Container from "./Container.jsx";
import "./ComponentsStyles/Header.css";
import logo from "../Styles/icons/logo.png";
import menuIco from "../Styles/icons/menu.svg";
import { useNavigate } from "react-router";
import { Link } from "react-router-dom";

const Header = () => {
    const nav = useNavigate()
    let [menuItems, setMenuItems] = useState([])
    const [menuImgStyle, setmenuImgStyle] = useState({})

    const logOut = () => {
        const token = JSON.parse(localStorage.getItem("token")).auth_token
        fetch("http://localhost:8088/api/auth/token/logout/", {
            method: "POST",
            headers: { "Authorization": "Token " + token,
            'Content-Type': 'application/json'} 
        })
        localStorage.setItem("token", JSON.stringify([]))
        localStorage.setItem("user", JSON.stringify([]))
        nav("/")
        setMenuItems([])
        setmenuImgStyle({})
    }

    const mouseEnter = () => {
        const user = JSON.parse(localStorage.getItem("user"))
        if(user == null || user.id == undefined){
            setmenuImgStyle({display: "none"})
            setMenuItems([
                {className:"menu__item__noRole", text:"войти как работник", click: () => nav("/sign")}])
        }
        else if(user.role == "A"){
            const email = JSON.parse(localStorage.getItem("user")).email 
            setmenuImgStyle({display: "none"})
            setMenuItems([
            {className:"menu__item__adminn", text:"профиль", click: () => {
                nav("/profile/" + user.id)
                window.location.reload(true)
            }},
            {className:"menu__item__adminn", text:"к заказам", click: () => nav("/board")},
            {className:"menu__item__adminn", text:"регистрация работника", click: () => nav("/register")},
            {className:"menu__item__adminn", text:"список работников", click: () => nav("/workers")},
            {className:"menu__item__adminn", text:"добавить блюдо", click: () => nav("/register_dish")},
            {className:"menu__item__adminn", text:"выйти", click: () => {
                logOut()
                window.location.reload(true)
            }}
            ])
        }
        else {
            setmenuImgStyle({display: "none"})
            setMenuItems([
                {className:"menu__item", text:"профиль", click: () => {
                    nav("/profile/" + user.id)
                    window.location.reload(true)
            }},
            {className:"menu__item", text:"к заказам", click: () => nav("/board")},
            {className:"menu__item", text:"список работников", click: () => nav("/workers")},
            {className:"menu__item", text:"выйти", click: () => {
                logOut()
                window.location.reload(true)
            }}
            ])
        }
    }

    const mouseLeave = () => {
        setMenuItems([])
        setmenuImgStyle({})
    }

    return (
        <div className="header__bg">
            <Container>
                <div className="header__flex">
                    <div className="header__nav__flex">
                        <div className="header__main"><Link to="/">На главную</Link></div>
                        {/* <div className="header__about"><a href="/#about">о сервисе</a></div> */}
                    </div>
                    <div className="header__logo">
                        <img src={logo}/>
                    </div>
                    <div onClick={mouseEnter} onMouseLeave={mouseLeave} className="header__menu">
                        <img style={menuImgStyle} src={menuIco} />
                        <div className="menu__flex">
                            {menuItems.map(el => 
                                <div key={el.text} onClick={el.click} className={el.className}>{el.text}</div>
                            )}
                        </div>
                    </div>
                </div>

            </Container>
        </div>
    )
}

export default Header;