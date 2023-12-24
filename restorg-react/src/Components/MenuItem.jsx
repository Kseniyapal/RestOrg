import React, { Children } from "react";
import "../Components/ComponentsStyles/MennuItem.css"
import PlusIco from "../Styles/icons/plus.svg"

const MenuItem = ({children, imgSource, addPurch, ...props}) => {
    return (
        <div className="menuItem">
        
            <div className="grid__item">
            
                <div className="item__flex">
                        <div  className="item__img">
                            <a href={props.link} className="item__link">
                                <img src={imgSource} alt = "Здесь должна быть картинка, но она не загрузилась)"></img>
                            </a> 
                        </div>

                        <div className="item__column__flex">
                           
                            <a href={props.link} className="item__info__flex">
                                <div className="item__name"> {props.name} </div>
                                <div className="item__numbers">
                                    <div className="item__mass"> {props.mass} </div>
                                    <div className="item__cost"> {props.cost} </div>
                                </div>
                            </a>
                        
                            <div className="item__add">
                                <button onClick={() => addPurch({name : props.name,
                                     image : imgSource,
                                      id : props.id, cost : props.cost})}><img src={PlusIco}/></button>
                            </div>
                        </div>
                    </div>

                </div>  
            
        </div>                                      
    )
}

export default MenuItem;


