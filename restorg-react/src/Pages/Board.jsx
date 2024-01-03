import classes from "./PagesStyles/Board.css"
import Header from "../Components/Header";
import darkTriangle from "../Styles/icons/black_triangle.svg"
import lightTriangle from "../Styles/icons/light_triangle.svg"
import OrderNumber from "../Components/OrderNumber.jsx"
import { useEffect } from "react";


const Board = () => {
    const fetchOrders = () => {
        fetch("http://localhost:8088/api/orders/")
        .then(response => response.json())
        .then(data => console.log(data))
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
                            <OrderNumber href="/order">105</OrderNumber>

                            </div>
                        </div>

                        <div className="column2__flex">
                            <div className="board__orders">

                            </div>
                        </div>

                        <div className="column3__flex">
                            <div className="board__orders">

                            </div>
                        </div>

                    </div>

                </div>
                <div className="checkboxes">
                    <form>
                        <div className="checkboxes__button">
                            <button>показать заказы</button>
                        </div>
                        <div className="checkboxes__flex">
                            <div className="checkbox__flex">
                                <input type="radio" id="sort" name="waiter" />
                                <label for="scales">официант</label>
                            </div>
                            <div className="checkbox__flex">
                                <input type="radio" id="sort" name="cook" />
                                <label for="scales">повар</label>
                            </div>
                            <div className="checkbox__flex">
                                <input type="radio" id="sort" name="bartender" />
                                <label for="scales">бармен</label>
                            </div>
                        </div>
                   
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Board;