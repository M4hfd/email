import smtplib
from dotenv import load_dotenv
import os


load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)

text =("""
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.

""")
friend_name = "СТЕПАН"
my_name = "Игорь"
site = "https://dvmn.org/referrals/XLCaM42NxT03w3z0cxvrKZ6Q0nOnUOG53TdNCpNe/"
text = text.replace('%website%', site)
text = text.replace('%friend_name%',friend_name)
text = text.replace("%my_name%", my_name)
email_from = "kazimirkorneplod@yandex.ru"
email_to = "sklu7zi@gmail.com"
subject = "Приглашение мяяв"
letter = """\
From: {0}
To: {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8";
{3}
""".format(email_from, email_to ,subject , text)
letter = letter.encode("UTF-8")


server.sendmail(email_from, email_to, letter)
server.quit()
