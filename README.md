# RestOrg



## Веб-сервис для автоматизации работы кухни и зала в ресторане
## Заказ
 - Заказ содержит в себе информацию об официанте, который обслуживает, комментрий, статусе, номер столика и, собственно, сам заказ
 - Как только готовы и блюда, и напитки, то статус заказа автоматически статовится "Ожидает доставки"

## Статус заказа
 - Ожидает принятия в работу
 - Ожидает приготовления
 - Ожидает доставки

## Роли пользователей
 - Гость(неавторизированный)
 - Официант
 - Бармен
 - Повар
 - Администратор

Все пользователи могут создавать заказ

## Все авторизированные пользователи
 - Просмотр списка пользователей
 - Просмотр списка заказов (в зависимости от роли)
 - Просмотр конкретного заказа (в зависимости от роли)

## Возможности администратора
 - Создание аккаунтов сотрудников
 - Редактирование заказов
 - Просмотр личного кабинета любого сотрудника
 - Создание пунктов меню

## Возможности официанта
 - Передача заказа "в разработку"
 - Нет прав на просмотр заказа, обслуживающегося другим официантом
 - Взятие в работу любого свободного заказа

## Возможности повара
 - Выставление статуса заказа "Готовы блюда"
 - Просмотр заказа, который содержит хотя бы одно блюдо
 - Просмотр только блюд в заказе

## Возможности бармена
 - Выставление статуса заказа "Готовы напитки"
 - Просмотр заказа, который содержит хотя бы один напиток
 - Просмотр только напитков в заказе

## Страницы приложения
 - Стартовая страница
 - Страница со списком зазказов
 - Страница конкретного заказа
 - Страница редактирования заказа
 - Страница списка пользователей
 - Страница конкретного пользователя
 - Страница с меню
 - Страница регистрации пользователей
 - Страница добавления пунктов меню

## Docker
 ### Образы
 - docker pull d0kshin/restorg_react
 - docker pull kseniyapal/restorg_backend
 - docker pull kseniyapal/restorg_nginx

 ### Как запустить?
 - Загрузить себе образы командами выше
 - В терминале в директории проекта прописать команду docker compose up
 - Выполнить ряд следующих команд:

       docker compose -f docker-compose.yml exec backend python manage.py migrate

       docker compose -f docker-compose.yml exec backend python manage.py load_users
       
       docker compose -f docker-compose.yml exec backend python manage.py load_dishes
       
       docker compose -f docker-compose.yml exec backend python manage.py load_drinks
 - Перейти в браузере на http://localhost:3000/
 
## Authors

- [@Kseniyapal](https://github.com/Kseniyapal)
- [@KoroleffGeorge](https://github.com/KoroleffGeorge)
- [@D0kshin](https://github.com/D0kshin)