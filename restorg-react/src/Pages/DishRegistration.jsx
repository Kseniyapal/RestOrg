import React, { useState } from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import UserField from "../Components/UI/Fields/UserField";
import "./PagesStyles/Register.css";


const DishRegistration = () => {
    const [dishType, setSelect] = useState("dish")
    const [name, setName] = useState("")
    const [mass, setMass] = useState("")
    const [price, setPrice] = useState("")
    const [image, setImage] = useState("")
    const [message, setMessage] = useState("")
    const [messageStyle, setMessageStyle] = useState({})

    const registerDish = () => {
        const token = JSON.parse(localStorage.getItem("token"))?.auth_token
        if(token){
            const requestOptions = {
                method: "POST",
                headers: { "Authorization": "Token "+ token,
                'Content-Type': 'application/json'}, 
                body: JSON.stringify({
                    name: name,
                    weight: mass,
                    price: price,
                    image: "images/" + image
                })
            }
            fetch("http://127.0.0.1:8088/api/dishes/ ", requestOptions)
            .then(response => {
                if(response.ok){
                    setName("")
                    setMass("")
                    setPrice("")
                    setImage("")
                    setMessage("Блюдо добавлено")
                    setMessageStyle({color: "#92B76E"})
                }
                else{
                    setMessage("Данные не верны")
                    setMessageStyle({color: "#cc7575"})
                }
            })
        }
    }

    const registerDrink = () => {
        const token = JSON.parse(localStorage.getItem("token"))?.auth_token
        if(token){
            const requestOptions = {
                method: "POST",
                headers: { "Authorization": "Token "+ token,
                'Content-Type': 'application/json'}, 
                body: JSON.stringify({
                    name: name,
                    volume: mass,
                    price: price,
                    image: "images/" + image
                })
            }
            fetch("http://127.0.0.1:8088/api/drinks/ ", requestOptions)
            .then(response => {
                if(response.ok){
                    setName("")
                    setMass("")
                    setPrice("")
                    setImage("")
                    setMessage("Напиток добавлен")
                    setMessageStyle({color: "#92B76E"})
                }
                else{
                    setMessage("Данные не верны")
                    setMessageStyle({color: "#cc7575"})
                }
            })
        }
    }

    const registration = () => {
        if(dishType == "dish"){
            registerDish()
        }
        else if(dishType == "drink"){
            registerDrink()
        }
    }
    
    return (
        <Wrapper>
            <Header/>
            <Content>
                <div className="register__bg">
                    <Container>
                        <div className="window__center">    
                            <div className="register__window">
                                <div className="register__main">
                                    <UserField value={name} onChange={e => setName(e.target.value)} name="название"/>
                                    <UserField value={mass} onChange={e => setMass(e.target.value)} name="вес/обьем"/>
                                    <UserField value={price} onChange={e => setPrice(e.target.value)} name="цена"/>
                                    <UserField style={{width: "170%"}} value={image} onChange={e => setImage(e.target.value)} name="название картинки"/>
                                    <select onChange={e =>  setSelect(e.target.value)} className="register__select">
                                        <option value="dish" className="register__select__item">Блюдо</option>
                                        <option value="drink" className="register__select__item">Напиток</option>
                                    </select>
                                </div>

                                <div style={messageStyle} className="register__message">{message}</div>            
                                <div className="register__continue__flex">
                                    <button style={{height: "50px", width: "200px"}} onClick={registration} className="register__button">Добавить</button>
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

export default DishRegistration;