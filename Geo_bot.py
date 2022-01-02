# -*- coding: utf-8 -*-
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from telegram import ReplyKeyboardMarkup

TOKEN = '1778541116:AAGb-rG-9D-QVa7NrlPVlDP0XqZQQO4yZBo'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

global k
k = 'central'


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Добро пожаловать в GeoBot!")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Здесь вы можете почитать про географию России")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Введите /lst чтобы увидеть список доступных для ознакомления регионов")
    test(update, context)


def test(update, context):
        reply_keyboard = [['/lst']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def next(update, context):
    lst(update, context)


def main(update, context):
    global k
    with open("{}/main.txt".format(k), "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)



def lst(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Выберите Федеральный округ:')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Северо-Западный - /North_West')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Центральный - /Central')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Южный - /Southern')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Северо-Кавказский - /North_Caucasian')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Уральский - /Ural')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Сибирский - /Siberian')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Приволжский - /Volga')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Дальневосточный - /Far_Eastern')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Города федерального значения - /Cities')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Для вызова меню нажмите кнопку в правой нижней части экрана")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="или введите /next")


def cities(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Москва - /Moscow')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Санкт-Петербург - /Saint_Petersburg')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Севастополь - /Sevastopol')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Возврат в меню - /next')

def North_West(update, context):
    global k
    k = 'North_West'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Чтобы узнать общую информацию про регон введите /main')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Выберите регион')
    A = ['Архангельская область', 'Вологодская область', 'Калининградская область', 'Республика Карелия', 'Республикуа Коми',
         'Ленинградская область', 'Мурманская область',  'Новгородская область', 'Псковская область', 'Возврат в меню']
    B = ['/Arhangelsk', '/Vologda', '/Kaliningrad', '/Karelia', '/Komi', '/Leningrad', '/Murmansk', '/Novgorod', '/Pskov', '/next']
    for i in range(len(A)):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='{} - {}'.format(A[i], B[i]))


def Central(update, context):
    global k
    k = 'central'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Чтобы узнать общую информацию про регон введите /main')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Выберите регион')
    A = ['1. Белгородская область', '2. Брянская область', '3. Владимирская область',
         '4. Воронежская область', '5. Ивановская область', '6. Калужская область',
         '7. Костромская область', '8. Курская область', '9. Липецкая область', '10. Московская область', '11. Орловская область',
         '12. Рязанская область', '13. Смоленская область', '14. Тамбовская область', '15. Тверская область',
         '16. Тульская область', '17. Ярославская область', 'Возврат в меню']
    B = ['/Belgorod ', '/Bryansk ', '/Vladimir ', '/Voronezh ', '/Ivanovo ', '/Kaluga ', '/Kostroma ', '/Kursk ',
         '/Lipetsk ', '/Moscow_Oblast ', '/Oryol', '/Ryazan', '/Smolensk ', '/Tambov ', '/Tver ', '/Tula ', '/Yaroslavl ', '/next']
    for i in range(len(A)):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='{} - {}'.format(A[i], B[i]))


def Far_Eastern(update, context):
    global k
    k = 'Far_Eastern'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Чтобы узнать общую информацию про регон введите /main')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Выберите регион')
    A = ['1. Республика Саха (Якутия)', '2. Камчатский край', '3. Приморский край', '4. Хабаровский край', '5. Амурская область',
         '6. Магаданская область', '7. Сахалинская область', '8. Еврейская автономная область', '9. Чукотский автономный округ',
         '10. Республика Бурятия', '11. Забайкальский край', 'Возврат в меню']
    B = ['/Yakutia ', '/Kamchatka ', '/Primorsky ', '/Khabarovsk ', '/Amur ', '/Magadan', '/Sakhalin ', '/Jewish_Autonomous', '/Chukotka',
         '/Buryatia', '/Zabaykalsk', '/next']
    for i in range(len(A)):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='{} - {}'.format(A[i], B[i]))


def Southern(update, context):
    global k
    k = 'Southern'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Чтобы узнать общую информацию про регон введите /main')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Выберите регион')
    A = ['1. Республика Адыгея', '2. Республика Калмыкия', '3. Краснодарский край',
         '4. Астраханская область', '5. Волгоградская область', '6. Ростовская область', '7. Республика Крым', 'Возврат в меню']
    B = ['/Adygea ', '/Kalmykia ', '/Krasnodar ', '/Astrakhan ', '/Volgograd ', '/Rostov ', '/Crimea ', '/next']
    for i in range(len(A)):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='{} - {}'.format(A[i], B[i]))


def Siberian(update, context):
    global k
    k = 'Siberian'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Чтобы узнать общую информацию про регон введите /main')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Выберите регион')
    A = ['1. Республика Алтай', '2. Республика Тыва', '3. Республика Хакасия', '4. Алтайский край',
         '5. Красноярский край', '6. Иркутская область', '7. Кемеровская область',
         '8. Новосибирская область', '9. Омская область', '10. Томская область', 'Возврат в меню']
    B = ['/Altai ', '/Tuva ', '/Khakassia ', '/Altai_Krai ', '/Krasnoyarsk ', '/Irkutsk ',
         '/Kemerovo ', '/Novosibirsk ', '/Omsk ', '/Tomsk ', '/next']
    for i in range(len(A)):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='{} - {}'.format(A[i], B[i]))


def Ural(update, context):
    global k
    k = 'Ural'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Чтобы узнать общую информацию про регон введите /main')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Выберите регион')
    A = ['1. Курганская область', '2. Свердловская область', '3. Тюменская область', '4. Челябинская область', 'Возврат в меню']
    B = ['/Kurgan ', '/Sverdlovsk ', '/Tyumen ', '/Chelyabinsk ', '/next']
    for i in range(len(A)):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='{} - {}'.format(A[i], B[i]))


def Volga(update, context):
    global k
    k = 'Volga'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Чтобы узнать общую информацию про регон введите /main')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Выберите регион')
    A = ['1. Республика Башкортостан', '2. Республика Марий Эл', '3. Республика Мордовия', '4. Республика Татарстан',
         '5. Удмуртская Республика', '6. Чувашская Республика', '7. Кировская область', '8. Нижегородская область',
         '9. Оренбургская область', '10. Пензенская область', '11. Пермский край', '12. Самарская область',
         '13. Саратовская область', '14. Ульяновская область', 'Возврат в меню']
    B = ['/Bashkortostan ', '/Mari_El ', '/Mordovia ', '/Nizhny_Novgorod  ', '/Orenburg ', '/Penza ', '/Perm ', '/Samara ',
         '/Saratov ', '/Tatarstan ', '/Udmurtia ', '/Ulyanovsk ', '/Chuvashia ', '/Kirov ', '/next']
    for i in range(len(A)):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='{} - {}'.format(A[i], B[i]))


def North_Caucasian(update, context):
    global k
    k = 'North_Caucasian'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Чтобы узнать общую информацию про регон введите /main')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Выберите регион')
    A = ['1. Республика Дагестан', '2. Республика Ингушетия', '3. Кабардино-Балкарская Республика',
         '4. Карачаево-Черкесская Республика', '5. Республика Северная Осетия', '6. Чеченская Республика', '7. Ставропольский край', 'Возврат в меню']
    B = ['/Dagestan ', '/Ingushetia ', '/Kabardino_Balkaria ', '/Karachay_Cherkessia ', '/North_Ossetia ', '/Chechen ', '/Stavropol ', '/next']
    for i in range(len(A)):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='{} - {}'.format(A[i], B[i]))



def Saint_Petersburg(update, context):
    with open('Saint_Petersburg.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
        txt = txt.split(';')
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Moscow(update, context):
    with open('Moscow.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
        txt = txt.split(';')
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)

def Sevastopol(update, context):
    with open('Sevastopol.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
        txt = txt.split(';')
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Arhangelsk(update, context):
    with open("North_West/Arhangelsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)

def Vologda(update, context):
    with open("North_West/Vologda.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)

def Kaliningrad(update, context):
    with open("North_West/Kaliningrad.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)

def Karelia(update, context):
    with open("North_West/Karelia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)

def Komi(update, context):
    with open("North_West/Komi.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)

def Leningrad(update, context):
    with open("North_West/Leningrad.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)

def Murmansk(update, context):
    with open("North_West/Murmansk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)

def Yoshkar_Ola(update, context):
    with open("North_West/Yoshkar_Ol.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)

def Novgorod(update, context):
    with open("North_West/Novgorod.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)

def Pskov(update, context):
    with open("North_West/Pskov.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Belgorod(update, context):
    with open("central/Belgorod.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Bryansk(update, context):
    with open("central/Bryansk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Vladimir(update, context):
    with open("central/Vladimir.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Voronezh(update, context):
    with open("central/Voronezh.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Ivanovo(update, context):
    with open("central/Ivanovo.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Kaluga(update, context):
    with open("central/Kaluga.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Kostroma(update, context):
    with open("central/Kostroma.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Kursk(update, context):
    with open("central/Kursk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Lipetsk(update, context):
    with open("central/Lipetsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Moscow_Oblast(update, context):
    with open("central/Moscow_oblast.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Oryol(update, context):
    with open("central/Oryol.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Ryazan(update, context):
    with open("central/Ryazan.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Smolensk(update, context):
    with open("central/Smolensk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Tambov(update, context):
    with open("central/Tambov.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Tver(update, context):
    with open("central/Tver.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Tula(update, context):
    with open("central/Tula.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Yaroslavl(update, context):
    with open("central/Yaroslavl.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Adygea(update, context):
    with open("Southern/Adygea.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Astrakhan(update, context):
    with open("Southern/Astrakhan.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Volgograd(update, context):
    with open("Southern/Volgograd.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Kalmykia(update, context):
    with open("Southern/Kalmykia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Krasnodar(update, context):
    with open("Southern/Krasnodar.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Rostov(update, context):
    with open("Southern/Rostov.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Crimea(update, context):
    with open("Southern/Crimea.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)



def Amur(update, context):
    with open("Far_Eastern/Amur.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Zabaykalsk(update, context):
    with open("Far_Eastern/Zabaykalsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Buryatia(update, context):
    with open("Far_Eastern/Buryatia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Jewish_Autonomous(update, context):
    with open("Far_Eastern/Jewish_Autonomous.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Kamchatka(update, context):
    with open("Far_Eastern/Kamchatka.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Magadan(update, context):
    with open("Far_Eastern/Magadan.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Primorsk(update, context):
    with open("Far_Eastern/Primorsky.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Yakutia(update, context):
    with open("Far_Eastern/Yakutia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Sakhalin(update, context):
    with open("Far_Eastern/Sakhalin.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Khabarovsk(update, context):
    with open("Far_Eastern/Khabarovsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Chukotka(update, context):
    with open("Far_Eastern/Chukotka.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Altai(update, context):
    with open("Siberian/Altai.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Altai_Krai(update, context):
    with open("Siberian/Altai_Krai.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Irkutsk(update, context):
    with open("Siberian/Irkutsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Kemerovo(update, context):
    with open("Siberian/Kemerovo.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Krasnoyarsk(update, context):
    with open("Siberian/Krasnoyarsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Novosibirsk(update, context):
    with open("Siberian/Novosibirsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Omsk(update, context):
    with open("Siberian/Omsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Tomsk(update, context):
    with open("Siberian/Tomsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Tuva(update, context):
    with open("Siberian/Tuva.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Khakassia(update, context):
    with open("Siberian/Khakassia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)



def Kurgan(update, context):
    with open("Ural/Kurgan.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Sverdlovsk(update, context):
    with open("Ural/Sverdlovsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Tyumen(update, context):
    with open("Ural/Tyumen.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Chelyabinsk(update, context):
    with open("Ural/Chelyabinsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Bashkortostan(update, context):
    with open("Volga/Bashkortostan.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Kirov(update, context):
    with open("Volga/Kirov.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Mari_El(update, context):
    with open("Volga/Mari_El.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Mordovia(update, context):
    with open("Volga/Mordovia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Nizhny_Novgorod(update, context):
    with open("Volga/Nizhny_Novgorod.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Orenburg(update, context):
    with open("Volga/Orenburg.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Penza(update, context):
    with open("Volga/Penza.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Perm(update, context):
    with open("Volga/Perm.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Samara(update, context):
    with open("Volga/Samara.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Saratov(update, context):
    with open("Volga/Saratov.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Tatarstan(update, context):
    with open("Volga/Tatarstan.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Udmurtia(update, context):
    with open("Volga/Udmurtia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Ulyanovsk(update, context):
    with open("Volga/Ulyanovsk.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Chuvashia(update, context):
    with open("Volga/Chuvashia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Dagestan(update, context):
    with open("North_Caucasian/Dagestan.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Ingushetia(update, context):
    with open("North_Caucasian/Ingushetia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Kabardino_Balkaria(update, context):
    with open("North_Caucasian/Kabardino_Balkaria.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Karachay_Cherkessia(update, context):
    with open("North_Caucasian/Karachay-Cherkessia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def North_Ossetia(update, context):
    with open("North_Caucasian/North_Ossetia.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Stavropol(update, context):
    with open("North_Caucasian/Stavropol.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def Chechen(update, context):
    with open("North_Caucasian/Chechen.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.split(";")
        for i in txt:
            context.bot.send_message(chat_id=update.effective_chat.id, text=i)



start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('next', next)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), Moscow)
dispatcher.add_handler(echo_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), Saint_Petersburg)
dispatcher.add_handler(echo_handler)
save_handler = CommandHandler('Sevastopol', Sevastopol)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler('cities', cities)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler('North_West', North_West)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler('Moscow', Moscow)
dispatcher.add_handler(save_handler)
next_handler = CommandHandler('lst', lst)
dispatcher.add_handler(next_handler)
next_handler = CommandHandler('Saint_Petersburg', Saint_Petersburg)
dispatcher.add_handler(next_handler)
save_handler = CommandHandler("Belgorod", Belgorod)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Bryansk", Bryansk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Vladimir", Vladimir)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Voronezh", Voronezh)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Ivanovo", Ivanovo)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Kaluga", Kaluga)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Kostroma", Kostroma)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Kursk", Kursk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Lipetsk", Lipetsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Moscow", Moscow)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Moscow_Oblast", Moscow_Oblast)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Oryol", Oryol)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Ryazan", Ryazan)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Smolensk", Smolensk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Tambov", Tambov)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Tver", Tver)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Tula", Tula)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Yaroslavl", Yaroslavl)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Adygea", Adygea)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Astrakhan", Astrakhan)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Volgograd", Volgograd)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Kalmykia", Kalmykia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Krasnodar", Krasnodar)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Rostov", Rostov)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Amur", Amur)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Jewish_Autonomous", Jewish_Autonomous)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Kamchatka", Kamchatka)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Crimea", Crimea)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Magadan", Magadan)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Primorsk", Primorsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Yakutia", Yakutia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Sakhalin", Sakhalin)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Khabarovsk", Khabarovsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Chukotka", Chukotka)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Altai", Altai)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Altai_Krai", Altai_Krai)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Irkutsk", Irkutsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Kemerovo", Kemerovo)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Krasnoyarsk", Krasnoyarsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Novosibirsk", Novosibirsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Omsk", Omsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Tomsk", Tomsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Tuva", Tuva)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Khakassia", Khakassia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Kurgan", Kurgan)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Sverdlovsk", Sverdlovsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Tyumen", Tyumen)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Zabaykalsk", Zabaykalsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Buryatia", Buryatia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Chelyabinsk", Chelyabinsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Bashkortostan", Bashkortostan)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Kirov", Kirov)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Mari_El", Mari_El)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Mordovia", Mordovia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Nizhny_Novgorod", Nizhny_Novgorod)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Orenburg", Orenburg)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Penza", Penza)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Perm", Perm)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Samara", Samara)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Saratov", Saratov)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Tatarstan", Tatarstan)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Udmurtia", Udmurtia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Ulyanovsk", Ulyanovsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Chuvashia", Chuvashia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Dagestan", Dagestan)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Ingushetia", Ingushetia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Kabardino_Balkaria", Kabardino_Balkaria)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Karachay_Cherkessia", Karachay_Cherkessia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("North_Ossetia", North_Ossetia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Stavropol", Stavropol)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Chechen", Chechen)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Southern", Southern)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Far_Eastern", Far_Eastern)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Siberian", Siberian)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Ural", Ural)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Volga", Volga)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("North_Caucasian", North_Caucasian)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Central", Central)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Arhangelsk", Arhangelsk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Vologda", Vologda)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Kaliningrad", Kaliningrad)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Karelia", Karelia)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Komi", Komi)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Leningrad", Leningrad)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Murmansk", Murmansk)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Novgorod", Novgorod)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("Pskov", Pskov)
dispatcher.add_handler(save_handler)
save_handler = CommandHandler("main", main)
dispatcher.add_handler(save_handler)

updater.start_polling()
updater.idle()