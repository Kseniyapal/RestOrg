import React, { useEffect, useState } from "react";
import  Container  from "../Components/Container";
import Header from "../Components/Header";
import Footer from "../Components/Footer";
import Content from "../Components/Content";
import Wrapper from "../Components/Wrapper";
import "./PagesStyles/Workers.css";
import WorkerItem from "../Components/WorkerItem";
import { useNavigate } from "react-router";

const Workers = () => {
    const nav = useNavigate()
    const [waiters, setWaiters] = useState([])
    const [coocks, setCoocks] = useState([])
    const [bartenders, setBartenders] = useState([])

    const RequestUsers = () => {
        let token = JSON.parse(localStorage.getItem("token"))
        if(token != null && token != undefined && token != ""){
            token = JSON.parse(localStorage.getItem("token")).auth_token
            const requestOptions = {
                method: "GET",
                headers: { "Authorization": "Token "+ token,
                'Content-Type': 'application/json'}, 
            }
            fetch("http://127.0.0.1:8088/api/users/", requestOptions)
            .then(response => response.json())
            .then(data => {
                const newWaiters = []
                const newCoocks = []
                const newBartenders = []

                data.forEach(worker => {
                    if(worker.role == "W"){
                        newWaiters.push(worker)
                    }
                    else if(worker.role == "C"){
                        newCoocks.push(worker)
                    }
                    else if(worker.role == "B"){
                        newBartenders.push(worker)
                    }
                })
                setWaiters(newWaiters)
                setCoocks(newCoocks)
                setBartenders(newBartenders)
            })
        }
        else{
            nav("/notFound")
        }
    }


    useEffect(() => {
        RequestUsers()
    }, [])

    return (
        <Wrapper>
            <Header/>
            <Content>
                <div className="workers__bg">
                    <Container>
                        <div className="workers__label">Список сотрудников</div>
                        <div className="workers__role__list">
                            <div className="workers__role__label">Бармены</div>
                            <div className="workers__list__flex">
                                {bartenders.map(element => 
                                    <WorkerItem key={element.id} worker={element}/>
                                )}
                            </div>
                        </div>
                        <div className="workers__role__list">
                            <div className="workers__role__label">Официанты</div>
                            <div className="workers__list__flex">
                                {waiters.map(element => 
                                    <WorkerItem key={element.id} worker={element}/>
                                )}
                            </div>
                        </div>
                        <div className="workers__role__list">
                            <div className="workers__role__label">Повара</div>
                            <div className="workers__list__flex">
                                {coocks.map(element => 
                                    <WorkerItem key={element.id} worker={element}/>
                                )}
                            </div>
                        </div>
                    </Container>
                </div>
            </Content>
            <Footer/>
        </Wrapper>   
    );
}

export default Workers;