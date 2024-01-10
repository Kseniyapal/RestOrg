import React from "react";
import Container from "./Container";
import "./ComponentsStyles/Footer.css";

const Footer = () => {
    return (
        <div className="footer__bg">
            <Container>
                <div className="footer__flex">
                    <div className="footer__list1">
                        <div className="footer__title">RestORG</div>
                        <div className="footer_description">Организация работы персонала</div>
                    </div>
                    <div className="footer__list2">
                        <ul>
                            <div className="list__description">Если возникла проблема с сервисом:</div>
                            <li><a  className="aFooter" href="https://github.com/D0kshin/restorg-react">GitHub</a></li>
                            <li><a href="https://www.google.com/">Support</a></li>
                        </ul>
                    </div>

                </div>
            </Container>
        </div>
    )
}

export default Footer;