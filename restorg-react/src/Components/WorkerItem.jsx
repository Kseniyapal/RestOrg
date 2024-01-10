import React, { useEffect } from "react";
import "./ComponentsStyles/WorkerItem.css"
import { useState } from "react";
import { useNavigate } from "react-router";


const Content = ({worker}) => {
    const nav = useNavigate()
    const [buttonDisable, setButtonsDisable] = useState("")

    const activateButtonsForAdmin = () =>{
        const user = JSON.parse(localStorage.getItem("user"))
        if(user == null || user.role != "A"){
            setButtonsDisable("disable")
        }
        else{
            setButtonsDisable("")
        }
    } 

    useEffect(() => {
        activateButtonsForAdmin()
    }, [])

    return (
        <div className="worker">
            <button disabled={buttonDisable} onClick={() => nav("/profile/" + worker.id)} className="worker__button">
                <div className="worker__info__flex">
                    <div className="worker__name">{worker.id} {worker.first_name} {worker.last_name}</div>
                    <div>{worker.email}</div>
                </div>
            </button>
            <hr/>
        </div>
    )
}

export default Content;