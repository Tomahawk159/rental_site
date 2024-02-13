from telegram.config_data.config import config


CONTACTS = {
                'map': """https://api-maps.yandex.ru/services/constructor/1.0/js/"""
                       """?um=constructor%3Aa03517d51003a0715d9961b836a889ed9a54f443201b1b23f20ceefbd47c2bdd&amp;"""
                       """width=348&amp;height=297&amp;lang=en_FR&amp;scroll=true""",
                'city': 'г.Пермь',
                'phone': '+7-999-11-11111',
                'email': 'perm@mail.ru',
                'adress': 'ул. Ленина 10'
            }

URL_TG_API = f'https://api.telegram.org/bot{config.tg_bot.token}/sendMessage'

TG_CHAT_ID = 1730221801
