Данный скрипт предназначен для перевода субтитров в окне браюзера

Подключается переправление трафика через расширение chrome
Requestly: Redirect Url, Modify Headers etc

Далее скрипт работает в качестве прозрачного прокси с выводом переведённой информации

# Создание перенаправления портов
sudo iptables -t nat -I PREROUTING -p tcp --dport 443 -j REDIRECT --to-ports 8080
sudo iptables -t nat -I OUTPUT -p tcp -o lo --dport 443 -j REDIRECT --to-ports 8080

# -----------------------
Использовать версию пакета
pip install googletrans==4.0.0-rc1