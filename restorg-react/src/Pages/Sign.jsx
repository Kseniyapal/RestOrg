import React, { useState } from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import WindowC from "../Components/UI/WindowC";
import AcceptButton from "../Components/UI/Buttons/AcceptButton"
import UserField from "../Components/UI/Fields/UserField";
import "./PagesStyles/Sign.css";
import { useNavigate } from "react-router";

const Sign = () => {
    const [email, setEmail] = useState()
    const [pass, setPass] = useState()
    const nav = useNavigate()

    const loadUser = (token) => {
        fetch("http://127.0.0.1:8088/api/users/", {
            method: "GET",
            headers: { "Authorization": "Token "+ token,
            'Content-Type': 'application/json'} 
        })
            .then(response => response.json())
            .then(data => localStorage.setItem("user", JSON.stringify(data.filter(el => el.email == email)[0])))  
    }
    const signIn = () => {
        const requestOptions = {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                password: pass,
                email: email,
            }) 
        }
        fetch("http://127.0.0.1:8088/api/auth/token/login", requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log(data.auth_token)
                const token = data.auth_token
                localStorage.setItem("token", JSON.stringify(data))
                loadUser(token)
            })
            nav("/")   
    }

    return (
        <Wrapper>
            <Header/>
            <Content>
                <div className="sign__bg">
                    <Container>
                        <div className="window__center__sign">    
                            <div className="sign__window">
                                <UserField 
                                    type="text"
                                    name="mail"
                                    value={email}
                                    onChange={e => setEmail(e.target.value)}
                                />
                                <UserField 
                                type="password" 
                                name="password"
                                value={pass} 
                                onChange={e => setPass(e.target.value)}
                                />
                                <div className="sign__continue__flex">
                                    <button onClick={signIn} className="sign__button">Войти</button>
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