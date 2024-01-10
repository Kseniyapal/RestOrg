import React, { useEffect, useState } from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import "./PagesStyles/Profile.css";
import { useNavigate, useParams } from "react-router";

const Register = () => {
    const nav = useNavigate()
    const params = useParams()
    const [user, setUser] = useState({})
    const [buttons, setButtons] = useState([
        {text: "К заказам", click: () => nav("/board")},
        {text: "Список работников", click: () => nav("/workers")},
        ])

    const fetchUser = () => {
        const token = JSON.parse(localStorage.getItem("token"))?.auth_token
        if(token){
            fetch("http://localhost:8088/api/users/" + params.id + "/",{
                method: "GET",
                headers: { "Authorization": "Token "+ token,
                'Content-Type': 'application/json'} 
            })
            .then(response => response.json())
            .then(data => {
                if(data.detail != "Not found."){
                    setUser(data)
                    setAdminButtons()
                }
                else{
                    nav("/notFound")
                }
            })   
        }
        else{
            nav("/notFound")
        }
    }

    const userRole = () => {
        if(user.role == "C"){
            return "повар"
        }
        else if(user.role == "B"){
            return "бармен"
        }
        else if(user.role == "W"){
            return "официант"
        }
        else{
            return "админ"
        }
    }

    const setAdminButtons = () => {
        if(JSON.parse(localStorage.getItem("user")).role == "A"){
            setButtons([
                {text: "К заказам", click: () => nav("/board")},
                {text: "Зарегистрировать работника", click: () => nav("/register")},
                {text: "Добавить блюдо", click: () => nav("/register_dish")},
                {text: "Список работников", click: () => nav("/workers")},
            ])
        }
    }

    useEffect(() => {
        fetchUser()
    }, [])

    if(user.role != undefined){
        return (
            <Wrapper>
                <Header/>
                <Content>
                    <div className="profile__bg">
                        <Container>
                            <div className="profile__info__flex">
                                <div className="profile__info__role">
                                    {user.role}
                                </div>
                                <div className="profile__info__text">
                                    <div className="profile__field">Имя: {user.first_name}</div>
                                    <hr/>
                                    <div className="profile__field">Фамилия: {user.last_name}</div>
                                    <hr/>
                                    <div className="profile__field">Почта: {user.email}</div>
                                    <hr/>
                                    <div className="profile__field">Номер: {user.id}</div>
                                    <hr/>
                                    <div className="profile__field">Роль: {userRole()}</div>
                                    <hr/>
                                </div>
                            </div>
                            <div className="profile__buttons">
                                {buttons.map(el => 
                                        <button onClick={el.click} key={el.text}>{el.text}</button>
                                    )}
                            </div>
                        </Container>
                    </div>
                </Content>
                <Footer/>
            </Wrapper>   
        );
    }
    else{
        return <div></div>
    }
}

export default Register;