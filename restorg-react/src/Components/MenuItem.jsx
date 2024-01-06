import React, { Children } from "react";
import "../Components/ComponentsStyles/MennuItem.css"
import PlusIco from "../Styles/icons/plus.svg"
import { Link } from "react-router-dom";
import { useNavigate } from "react-router"


const MenuItem = ({children, imgSource, addPurch, ...props}) => {
    return (
        <div className="menuItem">
            <div className="grid__item">
                <div className="item__flex">
                        <div  className="item__img">
                            <Link to={"/menu_position/" + props.id + "/" + props.type} className="item__link">
                                <img src={"/" + imgSource} alt = "Здесь должна быть картинка, но она не загрузилась)"></img>
                            </Link> 
                        </div>
                        <div className="item__column__flex">
                            <Link to={"/menu_position/" + props.id + "/" + props.type} className="item__info__flex">
                                <div className="item__name"> {props.name} </div>
                                <div className="item__numbers">
                                    <div className="item__mass"> {props.mass}{props.volume} </div>
                                    <div className="item__cost"> {props.price} </div>
                                </div>
                            </Link>
                            <div className="item__add">
                                <button onClick={() => addPurch({
                                        name : props.name,
                                        image : imgSource,
                                        id : props.id,
                                        price :  parseInt(props.price.slice(0,-1)),
                                        type : props.type,
                                        count : 1
                                       })}><img src={PlusIco}/></button>
                            </div>
                        </div>
                    </div>
                </div>  
        </div>                                      
    )
}

export default MenuItem;


