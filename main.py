# Импорт всего нужного
import telebot
import random
from telebot import types

# Токен и привязка программы к боту
Token = '6168844788:AAGQ_QvmoskiEylmRq32QmsPZ1yEBL06O2I'
bot = telebot.TeleBot(Token)

# Моральная помощь
Moralsupport = {
    1: 'У тебя все получится',
    2: "Не сдавайся",
    3: 'Все будет хорошо',
    4: 'Я верю в тебя',
    5: 'Ты все сможешь',
}

# Все анекдоты
jokes = {
    1: 'Изя, два миллиона ливанцев вышли на протест против коррупции.Как ты думаешь, возможно такое в России?\n'
       '- Сёма, подумай сам, ну откуда в России два миллиона ливанцев?',
    2: 'У старого Мойше спросили:\n'
    '— Вы верите в приметы?\n'
    '— Смотря какие.\n'
    '— Ну, например, вы проснулись утром, и встали не с той ноги?\n'
    '— Милочка, в моем возрасте проснуться утром – это уже хорошая примета!\n',
    3: 'Два еврея зашли в христианский храм и поспорили, кто из них пожертвует меньше денег.\n'
       'Когда мимо проходил служитель, первый еврей положил копейку и победоносно посмотрел на товарища.\n'
       '- За двоих, - скромно сказал второй\n',
    4: 'На приёме у кардиолога.\n'
       '— Рабинович, сколько водки в день вы выпиваете? — спрашивает врач.\n'
       '—Триста граммов, — отвечает пациент.\n'
       '— Как триста?! Я же только сто пятьдесят разрешил!\n'
       '— Ещё сто пятьдесят разрешил терапевт.\n',
    5: 'Семидесятые годы. С Рабиновичем беседуют в ОБХСС:\n'
       '— У вас есть дача!\n'
       '— Так разве это плохо?\n'
       '—У вас есть машина!\n'
       '— Так разве это плохо?\n'
       '—У вашей жены - норковая шуба!\n'
       '—Так разве это плохо?\n'
       '— Но ваша зарплата - всего сто пятьдесят рублей!\n'
       '— Так разве это хорошо?\n',
    6: 'Моисей сказал:  - Всё от Бога.\n'
       'Соломон сказал:  - Всё от ума.\n'
       'Иисус сказал:  - Всё от сердца.\n'
       'Маркс сказал:  - Всё от потребностей.\n'
       'Фрейд сказал:  - Всё от секса.\n'
       'Эйнштейн сказал:  - Всё относительно...\n'
       'Сколько евреев — столько и мнений\n',
    7: 'В Одесской филармонии на фортепьянном концерте карманник Фима смотрит на пианиста и бормочет:\n'
       '— Такие великолепные пальцы — и такой ерундой занимаются!\n',
    8: 'К раввину вбегает мужчина:\n'
       '— Ребе, выслушайте меня, пожалуйста, это очень важно!\n'
       'Раввин откладывает Талмуд:\n'
       '— Что случилось?\n'
       '— Ребе, моя жена хочет меня отравить!\n'
       '— Этого не может быть. С чего ты взял?\n'
       '— Ребе, это точно. Я видел, как она что-то подсыпает в мою еду. И вкус у пищи изменился.\n'
       'Раввин думает, потом говорит:\n'
       '— Вот что надо сделать. Я поговорю с твоей женой и пойму в чем дело.\n'
       'Завтра приходи в синагогу, я скажу тебе свое мнение.\n'
       'На следующий день тот опять приходит в синагогу, видит — у раввина борода всклокочена,\n'
       'руки трясутся, глаза разъехались.Раввин:— Я только что говорил с твоей женой.\n'
       'Я говорил с ней три часа по телефону. Три часа. Хочешь мой совет?\n'
       '— Конечно, ребе!\n'
       '— Прими яд\n',
    9: 'Собрался еврейский конгресс с повесткой дня: «Почему евреи отвечают вопросом на вопрос?»\n'
       'Конгресс вынес резолюцию: «Ну и что?»\n',
    10: '- Скажите, Рабинович, правда ли, что вы открыли шикарный ресторан?\n'
        '- Таки да.\n'
        '- И у вас действительно подают котлеты из рябчика?\n'
        '- Почему нет?\n'
        '- Но это же очень разорительно!\n'
        '- Ну… мы добавляем туда немножко конины.\n'
        '- В какой пропорции?\n'
        '- Все по-честному, один к одному. Один рябчик – один конь.\n',
    11: 'Старый Абрам умирает у себя в кабинете на рабочем месте.\n'
        'Начальство решает отправить Изю, оповестить о случившемся его жену.\n'
        'Перед отъездом дают ему последние наставления:\n'
        '- Ты уж там как-нибудь поделикатнее с ней.\n'
        'Изя всё внимательно выслушал и отправился к дому усопшего. Прибывает на место, стучит в дверь.\n'
        'Дверь открывает жена умершего - Сара.\n'
        '- Здравствуйте, простите, вдова Абрама здесь живёт?\n'
        '- Да, но я не вдова.\n'
        '- Поспорим?\n',
    12: '- Абрам, и де вы шили свой красивый костюм?\n'
        '- В Париже.\n'
        '- Да? А это далеко от Жмеринки?\n'
        '- Очень далеко.\n'
        '- Ты смотри! Такая глушь, а как шьют.\n',
    13: '— Изя, шо ви таки будете делать, если к вам придут воры и будут искать деньги?\n'
        '— Абрам, я вас умоляю. Сначала посмеюсь, а потом буду искать вместе с ними.\n',
    14: 'Умер старый еврей. Вскрыли его завещание, читают:\n'
        '«Дочке моей, Сарочке, оставляю 100 тысяч долларов и дом.\n'
        'Внучке моей, Ривочке, оставляю 200 тысяч долларов и дачу.\n'
        'Зять мой Шмулик просил меня упомянуть его в завещании. Упоминаю: Привет тебе, Шмулик!»\n',
    15: 'Письмо из Тель-Авива в Одессу: «Сынок, высылaем тебе 20 доллaров, кaк ты и просил...\n'
        'Но хотим нaпомнить, что 20 доллaров пишется не с тремя нулями, a с одним!»\n',
    16: 'Слева - магазин Фимы, вывеска: «Самые низкие цены».\n'
        'Справа - магазин Цили, вывеска: «Самые качественные товары».\n'
        'Рувим Маркович, чей магазин в центре, посмотрел на соседей и повесил: «Главный вход».\n',
    17: 'Собрался один еврей-одессит в Италию ехать, ну, ему говорят, что мол у них там на базаре можно (нужно) цену, сбивать...\n'
        'хоть вдвое, вот. Ну, приехал туда значит, пошел на базар выбрал какую-то безделушку, спрашивает:\n'
        '— Сколько?\n'
        'Торговец:\n'
        '— 1000 лир.\n'
        '— 500!!!\n'
        '— 800...\n'
        '— 400!!!\n'
        '— Ты откуда такой?!\n'
        '— Я из Одессы!!!\n'
        '— О-о-о!!! В знак дружбы наших стран, забирай бесплатно!!!\n'
        '— Тогда давай две!!!\n',
    18: '— Рабинович, если бы у вас был миллион, на что бы вы его потратили?\n'
        '— А почему тратить, почему сразу тратить?!\n',
    19: 'Одесса. Университет. На экзамене по философии профессор задал лишь один вопрос студентам:\n'
        '"Почему?"\n'
        'Высший бал получил студент, давший ответ:\n'
        '"А почему бы и нет?"\n',
    20: 'Столетний одессит каждый день ходил в синагогу и молился.\n'
        'И вдруг, на следующий день после того, как ему исполнился 101 год, он не пришел.\n'
        'Встревоженный ребе немедленно после молитвы зашел к нему, чтобы узнать, здоров ли он,\n'
        'и увидел его здоровым, веселым и жизнерадостным.\n'
        'На вопрос о том, почему тот не пришел, старик ответил так:\n'
        '— Когда мне исполнилось 81, я понял, что скоро умру, и стал молиться, чтобы дожить до 90.\n'
        'В 90 я молился уже по привычке. Но когда мне исполнилось 101,'
        'я понял, что Бог слишком занят, чтобы заниматься моими просьбами, и, видимо, обо мне забыл.\n'
        'Taк что если я не буду о себе напоминать, проживу дольше.\n',
    21: '"Новый еврейский банк"\n'
        '— Мне сказали, шо вы даете кредиты под честное слово. Это хохма?\n'
        '— Нет, действительно даём, всё правда.\n'
        '— И вы не боитесь? А вдруг я вам деньги не верну? Шо тогда?\n'
        '— Ну-у, тогда вам будет очень стыдно, когда предстанете перед Всевышним\n'
        '— Ха! Это когда еще будет?!\n'
        '— Шо значит, когда? На пять дней просрочите, на шестой и предстанете.\n',
    22: 'Еврей перед казнью.\n'
        '— Ваше последнее желание?\n'
        '— Хочу черешни.\n'
        '— Но сейчас же январь!\n'
        '— Я подожду.\n',
    23: 'Один еврейский мальчик очень любил читать.'
        'Он читал всё, что попадалось ему под руку, и обожал ходить в свой любимый книжный магазин.'
        'Однажды он понял, что прочёл уже всё, что там продавалось.'
        'Мальчик спросил хозяина, есть ли в магазине что-нибудь, чего он никогда не видел.'
        'Хозяин сказал, что есть, и достал книгу под названием "Смерть".'
        'Он охотно продал её со скидкой, всего за 10 шекелей.'
        'Однако он предупредил мальчика, чтобы тот никогда не открывал первую страницу.'
        'Мальчик вернулся домой, прочитал книгу и остался доволен.'
        'Но ему всегда хотелось узнать, что же там, на первой странице.'
        'Однажды искушение стало слишком сильным, и он пролистал книгу к самому началу, и уронил её в УЖАСЕ.\n'
        'На первой странице было написано: "Рекомендуемая цена - 5 шекелей".',
    24: '— Здравствуйте, господин Кац! У вас с балкона лыжная гонка на Олимпиаде будет видна?\n'
        '— Да, будет участочек виден.\n'
        '— Тогда с вас 500 рублей за билет.\n',
    25: 'Раньше я относился к людям хорошо, а теперь – взаимно\n'
        '— Изя, меня укусила ваша собака! Я требую компенсации!\n'
        '— Да ради Бога! Я ее сейчас подержу, а вы кусайте!\n',
    26: '— Сема, давай быстрей, семеро одного не ждут!\n'
        '— Ждут, ждут — если у него деньги!\n',
    27: 'Рабиновича распознать легко в двух случаях.\n'
        'По искрометному юмору, когда он что-то продает,\n'
        'и по невосполнимой утрате в глазах, когда он что-то покупает.\n',
    28: '— Помоги мне, Господи! Есть таки нечего, жить не на что, ни рубля в кармане...\n'
        'Голос с неба:\n'
        '— Не ври, Изя!\n'
        '— Шо, доллары менять?!\n',
    29: '— Мойша, я слышал, твой дядя сошёл с ума и подарил тебе 10 тысяч долларов?\n'
        '— Бывает и такое, иначе как ещё это объяснить.\n'
        '— Одолжи тогда мне на месяц тысячу.\n'
        '— Изя, у тебя что-то со слухом? С ума сошёл мой дядя, а не я!\n',
    30: '— Соломон Маркович, шо такое зрелый возраст?\n'
        '— Это период между концом иллюзий молодости и началом галлюцинаций старости...\n'
}


# Стартовое окно
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    item1 = types.KeyboardButton("Еврейский анекдот")
    item2 = types.KeyboardButton("/start")
    item3 = types.KeyboardButton("/help")
    markup.add(btn1, item1, item2, item3)
    bot.send_message(
        message.chat.id,
        '👋 Приветствую, Я могу показать курс валют\n' +
        'Для этого отправьте /exchange в чат.\n' +
        'Для помощи отправьте /help в чат.\n'
        'Также есть команды: /history, /dota2, /curse, /moral_support\n'
        'подробнее о них написано во вкладке /help',
        reply_markup=markup
    )


# Список функцию собъяснением их действия
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        '1) Для перезапуска бота отправьте /start  в чат.\n' +
        '2) Для вызова оена помощи отправьте /help  в чат.\n' +
        '3) Для вызова окна истории бота отправьте /history в чат.\n' +
        '4) Для вызова окна актуальной информации про доту2 отправьте /dota2 в чат.\n' +
        '5) Бот может морально поддержать вас, для этого отправьте /moral_support в чат.\n' +
        '6) Бот может рассказать анекдот про евреев, для этого нажмите соответствующую кнопку.\n' +
        '7) Также бот может показать курс валют для этого отправьте /curse в чат.\n',
    )


# Моральная помощь
@bot.message_handler(commands=['moral_support'])
def moral_support(message):
    bot.send_message(
        message.chat.id,
        Moralsupport[random.randint(1, 5)])


# Информация про dota2
@bot.message_handler(commands=['dota2'])
def dota2_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='https://dota2.ru/news/updates/'
        )
    )
    bot.send_message(
        message.chat.id,
        'Здесь актуальная информация про доту2.\n',
        reply_markup=keyboard
    )


# Расскажет о проэкте
@bot.message_handler(commands=['history'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='http://127.0.0.1:8080'
        )
    )
    # Работает только для web версии или для программы на компьютер
    f = open('about_us.txt')
    bot.send_message(
        message.chat.id,
        f.read(),
        reply_markup=keyboard
    )


# Курс обмена
@bot.message_handler(commands=['exchange'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Dota2 new updates', url='https://dota2.ru/news/updates/'
        )
    )
    bot.send_message(
        message.chat.id,
        'Курса не будет. Иди в Доту играй\n',
        reply_markup=keyboard
    )


# Курс обмена
@bot.message_handler(commands=['curse'])
def curse_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'cbr.ru', url='https://www.cbr.ru/currency_base/daily/'
        )
    )
    bot.send_message(
        message.chat.id,
        'Вот пожалуйста\n',
        reply_markup=keyboard
    )


# Работа с кнопками
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    a = random.randint(1, 30)

    if message.text == 'Еврейский анекдот':
        bot.send_message(
            message.chat.id,
            jokes[a])

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Как научиться играть в Доту 2?')
        btn2 = types.KeyboardButton('Чем заняться в свободное время?')
        btn3 = types.KeyboardButton('Я хочу увидеть число пи')
        item1 = types.KeyboardButton("/start")
        item2 = types.KeyboardButton("/help")
        markup.add(btn1, btn2, btn3, item1, item2)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup)

    elif message.text == 'Как научиться играть в Доту 2?':
        bot.send_message(
            message.from_user.id,
            'Дота 2 - это увлекательная соревновательная онлайн игра, только зайдя в которую,'
            'Вас затянет в неё с головой. Но есть одна проблема. Дота - очень тяжёлая игра и чтобы '
            'победить, Вам необходимо разобраться в основных механиках, пройти обучение и посмотреть '
            'огромное количество гайдов или же Вы можете просто перейти по ' +
            '[ссылке](https://www.twitch.tv/stray228?lang=ru)',
            parse_mode='Markdown')

    elif message.text == 'Чем заняться в свободное время?':
        bot.send_message(
            message.from_user.id,
            'Существует множество способов убить время, но мы рекомендуем Вам убить своё свободное время'
            'бороздя просторы Доты 2, которую Вы можете скачать по ' +
            '[ссылке](https://store.steampowered.com/app/570/Dota_2/)',
            parse_mode='Markdown')

    elif message.text == 'Я хочу увидеть число пи':
        bot.send_message(
            message.from_user.id,
            'Исполнить ваше желание можно, перейдя по ' +
            '[ссылке](https://sanstv.ru/pi?ysclid=lgrvr1vgh0777419908)',
            parse_mode='Markdown')


# Чтобы бот работал все время
bot.polling(none_stop=True)
