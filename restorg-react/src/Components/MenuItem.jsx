import React, { Children } from "react";
import "../Components/ComponentsStyles/MennuItem.css"
import PlusIco from "../Styles/icons/plus.svg"

const MenuItem = ({children, ...props}) => {
    return (
        <div className="menuItem">
        
            <div className="grid__item">
            
                <div className="item__flex">
                        <div  className="item__img">
                            <a href={props.link} className="item__link">
                                <img src={props.imgSource}></img>
                            </a> 
                        </div>

                        <div className="item__info__flex">
                            <a href={props.link} className="item__link">
                                <div className="item__name"> {props.name} </div>
                                <div className="item__mass"> {props.mass} </div>
                                <div className="item__describtion"> {props.time} </div>
                                <div className="item__cost"> {props.cost} </div>
                            </a>
                        </div>
                    


                        <div className="item__add">
                            <button><img src={PlusIco}/></button>
                        </div>
                    </div>

                </div>  
            
        </div>                                      
    )
}

export default MenuItem;


