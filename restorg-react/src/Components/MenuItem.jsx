import React, { Children } from "react";
import "../Components/ComponentsStyles/MennuItem.css"
import PlusIco from "../Styles/icons/plus.svg"

const MenuItem = ({children, ...props}) => {
    return (
        <div className="menuItem">
        <a href={props.link} spellcheck="false">
            <div className="grid__item">
                
                <div className="item__flex">
                    <div  className="item__img">
                        <img src={props.imgSource}></img>
                    </div>

                    
                    <div className="item__info__flex">
                        <div className="item__name"> {props.name} </div>
                        <div className="item__mass"> {props.mass} </div>
                        <div className="item__describtion"> {props.time} </div>
                        <div className="item__cost"> {props.cost} </div>
                    </div>


                    <div className="item__add">
                        <button><img src={PlusIco}/></button>
                    </div>
                </div>

            </div>  
        </a>     
        </div>                                      
    )
}

export default MenuItem;


