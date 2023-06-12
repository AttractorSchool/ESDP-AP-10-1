## 🌍 Пароли и логины для входа и тестирования приложения


<table>
    <tr>
        <th>Вход для:</th>
        <th>Логин</th>
        <th>Пароль</th>
    </tr>
    <tr>
        <td>администратора(admin)</td>
        <td>root@root.com</td>
        <td>root</td>
    </tr>
    <tr>
        <td>обычный пользователь</td>
        <td>user</td>
        <td>1234</td>
    </tr>
</table>

## Запуск проекта

Для запуска проекта и создания образов используйте следующую команду:

`docker-compose up --build`

Для запуска проекта в фоновом режиме, используйте флаг `-d`:

`docker-compose up -d`


## Остановка проекта

Чтобы остановить работу всех сервисов, выполните следующую команду:

`docker-compose down`


## Миграции

Чтобы создать новые миграции, используйте команду `makemigrations`:

`docker-compose exec app python manage.py makemigrations`


Чтобы применить эти миграции, используйте команду `migrate`:

`docker-compose exec app python manage.py migrate`


