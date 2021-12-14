# Отчёт


### 1.    Придумать свою предметную область и продумать схему БД для неё.

В качестве предметной области мы выбрали хранение данных о киентах, филиалах, услугах и данных о выполнении услуг. Первая таблица включает в себя ID книги, имя и фамилию клиента а также телефонный номер и количество денег, которое клиент заплатил за услуги. Вторая таблица состоит из четырех столбцов: ID филиала, название, адресс и телефонный номер. Третья таблица состоит из четырех столбцов: ID, название услуги, её тип и стоимость. Четвертая таблица также состоит из четырех столбцов: ID филиала, ID услуги, ID покупателя и дату выполнения услуги.




### 2.    Выделить функциональные требования.

### 3.    Реализовать реляционную БД для своей предметной области (все таблицы должны быть не менее чем в третьей нормальной форме)

### 4.    Критерии к БД:
[1]     БД должна быть в третьей нормальной форме или выше;

[2]     Минимальное количество таблиц – 4;

[3]     Все подключения из GUI должны осуществляться выделенным, не root, пользователем;

[4]     Должен существовать как минимум один индекс, созданный вами по выбранному текстовому не ключевому полю;

[5]     В одной из таблиц должно присутствовать поле, заполняемое/изменяемое только триггером (например, «общая стоимость бронирования» в таблице «бронирования», которое автоматически высчитывается при добавлении/изменении/удалении билетов, входящих в это бронирование)

### 5.    Реализовать программу GUI со следующим функционалом:

[1]     Создание базы данных (важно(!) именно create database, а не только create table)

[2]     Удаление базы данных

[3]     Вывод содержимого таблиц

[4]     Очистка(частичная - одной, и полная - всех) таблиц

[5]     Добавление новых данных

[6]     Поиск по заранее выбранному (вами) текстовому не ключевому полю

[7]     Обновление кортежа

[8]     Удаление по заранее выбранному текстовому не ключевому полю

[9]     Удаление конкретной записи, выбранной пользователем

[10]     Все функции должны быть реализованы как хранимые процедуры.

- Из GUI вызываются только хранимые функции.


