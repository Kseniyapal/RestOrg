import React, { useEffect, useState } from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import UserField from "../Components/UI/Fields/UserField";
import "./PagesStyles/Register.css";
import { useNavigate } from "react-router";




const Register = () => {
    const nav = useNavigate()
    const [role, setSelect] = useState("W")
    const [name, setName] = useState("")
    const [surname, setSurname] = useState("")
    const [patronymic, setPatronymic] = useState("")
    const [email, setEmail] = useState("")
    const [login, setLogin] = useState("")
    const [pass, setPass] = useState("")
    const [message, setMessage] = useState("")
    const [messageStyle, setMessageStyle] = useState({})

    const registerUser = () => {
        const token = JSON.parse(localStorage.getItem("token")).auth_token
        const requestOptions = {
            method: "POST",
            headers: { "Authorization": "Token "+ token,
            'Content-Type': 'application/json'}, 
            body: JSON.stringify({
                email: email,
                first_name: name,
                last_name: surname,
                patronymic: patronymic,
                role: role,
                username: login,
                password: pass
            })
        }
        fetch("http://127.0.0.1:8088/api/users/", requestOptions)
        .then(response => {
            if(response.ok){
                setName("")
                setSurname("")
                setPatronymic("")
                setEmail("")
                setLogin("")
                setPass("")
                setMessage("Работник добавлен")
                setMessageStyle({color: "#92B76E"})
            }
            else{
                console.log(response)
                setMessage("Данные не верны")
                setMessageStyle({color: "#cc7575"})
            }
        })    
    }

    return (
        <Wrapper>
            <Header/>
            <Content>
                <div className="register__bg">
                    <Container>
                        <div className="window__center">    
                            <div className="register__window">
                                <div className="register__name__flex">
                                    <UserField value={name} onChange={e => setName(e.target.value)} name="имя"/>
                                    <UserField value={surname} onChange={e => setSurname(e.target.value)} name="фамилия"/>
                                </div>
                                <div className="register__fatherly">
                                    <UserField value={patronymic} onChange={e => setPatronymic(e.target.value)} name="отчество*"/>
                                </div>
                                <div className="register__main">
                                    <UserField value={email} onChange={e => setEmail(e.target.value)} name="почта"/>
                                    <UserField value={login} onChange={e => setLogin(e.target.value)} name="логин"/>
                                    <UserField value={pass} onChange={e => setPass(e.target.value)} name="пароль"/>
                                    <div className="register__role">роль</div>
                                    <select onChange={e =>  setSelect(e.target.value)} className="register__select">
                                        <option value="W" className="register__select__item">Официант</option>
                                        <option value="B" className="register__select__item">Бармен</option>
                                        <option value="C" className="register__select__item">Повар</option>
                                    </select>
                                </div>
                                <div style={messageStyle} className="register__message">{message}</div>            
                                <div className="register__continue__flex">
                                    <button onClick={registerUser} className="register__button">Зарегистрировать</button>
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