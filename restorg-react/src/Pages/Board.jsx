import classes from "./PagesStyles/Board.css"
import Header from "../Components/Header";
import darkTriangle from "../Styles/icons/black_triangle.svg"
import lightTriangle from "../Styles/icons/light_triangle.svg"
import OrderNumber from "../Components/OrderNumber.jsx"
import { useEffect, useState } from "react";


const Board = () => {
    let [NADishes, setNADishes] = useState([])
    let [IPDishes, setIPDishes] = useState([])
    let [DoneDishes, setDoneDishes] = useState([])

    const fetchOrders = () => {
        if(JSON.parse(localStorage.getItem("token")) != null){
            const token = JSON.parse(localStorage.getItem("token")).auth_token
            fetch("http://localhost:8088/api/orders/",{
                method: "GET",
                headers: { "Authorization": "Token "+ token,
                'Content-Type': 'application/json'} 
            })
            .then(response => response.json())
            .then(data => {
                if(data.detail == undefined){
                    splitDishes(data)
                }
                else{
                    return
                }
            })
        }
    }  


    const splitDishes = (dishes) => {
        dishes.forEach(element => {
            if(element.status == "NA"){
                NADishes.push(element)
                setNADishes([...NADishes])
            }
            else if(element.status == "IP" || element.status == "DDS" || element.status == "DDR"){
                IPDishes.push(element)
                setIPDishes([...IPDishes])            
            }
            else{
                DoneDishes.push(element)
                setDoneDishes([...DoneDishes])
            }
        });
    }

    useEffect(() => {
        fetchOrders()
    }, [])


    return (
        <div className="board">
            <Header></Header> 

            <img src={darkTriangle} className="dark__triangle1"></img>
            <img src={lightTriangle} className="light__triangle1"></img>

            <img src={darkTriangle} className="dark__triangle2"></img>
            <img src={lightTriangle} className="light__triangle2"></img>

            <div className="board__bg">
                <div className="board__container">
                
                    <div className="columns__flex">

                        <div className="column1__flex">
                            <div className="board__orders">
                                {NADishes.map((el) => 
                                    <OrderNumber element={el} colorStyle="column1__flex" key={el.id}  elementId={el.id}>{el.id}</OrderNumber>
                                )}
                            </div>
                        </div>

                        <div className="column2__flex">
                            <div className="board__orders">
                                {IPDishes.map((el) => 
                                    <OrderNumber element={el} colorStyle="column2__flex" key={el.id} elementId={el.id} >{el.id}</OrderNumber>
                                )}
                            </div>
                        </div>
   
                        <div className="column3__flex">
                            <div className="board__orders">
                                {DoneDishes.map(el => 
                                    <OrderNumber element={el} colorStyle="column3__flex" key={el.id} elementId={el.id} >{el.id}</OrderNumber>
                                )}
                            </div>
                        </div>

                    </div>

                </div>
                <div className="checkboxes">    
                    {/* <form>
                        <div className="checkboxes__button">
                            <button>показать заказы</button>
                        </div>
                        <div className="checkboxes__flex">
                            <div className="checkbox__flex">
                                <input type="radio" id="sort" name="waiter" />
                                <label form="scales">официант</label>
                            </div>
                            <div className="checkbox__flex">
                                <input type="radio" id="sort" name="cook" />
                                <label form="scales">повар</label>
                            </div>
                            <div className="checkbox__flex">
                                <input type="radio" id="sort" name="bartender" />
                                <label form="scales">бармен</label>
                            </div>
                        </div>
                   
                    </form> */}
                </div>
            </div>
        </div>
    );
}

export default Board;