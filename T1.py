token = "" #подставить свой access_token
'''
Чтоб получить access_token нужно:
- перейти по этой ссылке https://vk.com/apps?act=manage с авторизованным аккаунтом
- нажать на кнопку "Создать приложение"
- дать любое название вашему приложению и выбрать тип "Standalone-приложение"
- нажать "Подключить приложение"
- подтвердить свой аккаунт
- взять ID приложения в "Настройках" (в меню слева)
- перейти по адресу https://oauth.vk.com/authorize передав параметри client_id, redirect_uri
display, scope, response_type. Подробнее можно узнать перейдя по ссылке https://vk.com/dev/implicit_flow_user
Для этой программы нужны права "messages"
'''
import requests #нужен для связи з вк
from time import sleep #нужен для приостановки времени
delet = ''
st = ''
def asd(w):
    global delet
    qwe=requests.get("https://api.vk.com/method/messages.getById", params={'message_ids':w,'access_token':token}).json() #получаем сообщения по id
    try:
        qwe = qwe['response']
        for a in range(1,len(qwe)):
                try:
                    print(qwe[a].get('body'))
                except UnicodeEncodeError: # если в сообщении есть смайл
                    for a in qwe[a].get('body'):
                        try:
                            print(a, end='')
                        except:
                            pass
                        
    except KeyError: # если отправлено слишком много запросов и вк молчит
        print('Error\nsleep')
        sleep(3)
        qwe=requests.get("https://api.vk.com/method/messages.getById", params={'message_ids':w,'access_token':token}).json()
        qwe = qwe['response']
        for a in range(1,len(qwe)):
                print(qwe[a].get('body'))
f = requests.get("https://api.vk.com/method/messages.get", params={'count':1,'access_token':token}).json()
print("Max:", f['response'][1]['mid'])
start = int(input('Показать сообщения от(int) > '))
end   = int(input('До(int) > '))
if( end > f['response'][1]['mid'] ):
    end = f['response'][1]['mid']
for i in range(start, end):
    if(i%100==0):
        if(st!=''):
            asd(st)
        st = str(i)
    else:
        st = st+', '+str(i)
    if((i-start)%2000==1999):
        print('wait...')
        sleep(3)
        print('Countrie')
st = st+', '+str(i+1)
asd(st)
print(delet)
input( 'Нажмите Enter' )
