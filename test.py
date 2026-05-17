
import vk_api
import random
import time

from vk_api.longpoll import (
    VkLongPoll,
    VkEventType
)

from vk_api.keyboard import (
    VkKeyboard,
    VkKeyboardColor
)

# =========================================================
# CONFIG
# =========================================================

VK_TOKEN = "vk1.a.kloBTHojoIonWwjUfUctJS2y5GBJKRNnYXOtV2ZUfQUIpO9bVoNK_FODzfhyuZQm4z9K1VfKKDmC3xVIDGu6HCFzQ0k8oNC47yYEoRMIS_J0doTWg7213gb-MXrTB6Wvt9VOk0ENfvbX_SvlTdOaY-y5HI57c2-89gN5M6J1rSB1qNbMka7qEjghYaWJZN2dKilWMw7VJK0jeI8Lu-RnkA"

# =========================================================
# ADMINS
# =========================================================

ADMIN_IDS = [
    1350783137,
    1130643805
]

# =========================================================
# BRAND
# =========================================================

GROUP_LINK = "https://vk.com/club238794967"

MASTER_LINK = "https://vk.com/your_profile"

# =========================================================
# SERVICES
# =========================================================

SERVICES = {

    "classic": {
        "name": "💅 Классический маникюр",
        "price": "1500₽"
    },

    "gel": {
        "name": "✨ Маникюр + гель-лак",
        "price": "2500₽"
    },

    "design": {
        "name": "🎨 Дизайн ногтей",
        "price": "3000₽"
    }
}

# =========================================================
# VK INIT
# =========================================================

vk_session = vk_api.VkApi(
    token=VK_TOKEN
)

vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

# =========================================================
# SEND MESSAGE
# =========================================================

def send_message(
    user_id,
    text,
    keyboard=None,
    attachment=None
):

    vk.messages.send(

        user_id=user_id,

        message=text,

        random_id=random.randint(
            1,
            999999999
        ),

        keyboard=keyboard,

        attachment=attachment
    )

# =========================================================
# MAIN KEYBOARD
# =========================================================

def main_keyboard():

    keyboard = VkKeyboard(
        one_time=False
    )

    keyboard.add_button(
        "💅 Услуги",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_button(
        "💰 Прайс",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "🖼 Портфолио",
        color=VkKeyboardColor.POSITIVE
    )

    keyboard.add_button(
        "📞 Контакты",
        color=VkKeyboardColor.NEGATIVE
    )

    return keyboard.get_keyboard()

# =========================================================
# SERVICES KEYBOARD
# =========================================================

def services_keyboard():

    keyboard = VkKeyboard(
        one_time=False
    )

    keyboard.add_button(
        "💅 Классический",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "✨ Гель-лак",
        color=VkKeyboardColor.POSITIVE
    )

    keyboard.add_line()

    keyboard.add_button(
        "🎨 Дизайн ногтей",
        color=VkKeyboardColor.SECONDARY
    )

    return keyboard.get_keyboard()

# =========================================================
# START
# =========================================================

def start(user_id):

    text = (

        "💖 NAIL STUDIO\n\n"

        "Добро пожаловать "
        "в студию красивых ногтей ✨\n\n"

        "У нас вы можете:\n"
        "• сделать маникюр\n"
        "• покрытие гель-лаком\n"
        "• заказать nail design\n\n"

        "Выберите действие ниже 👇"
    )

    send_message(
        user_id,
        text,
        keyboard=main_keyboard()
    )

# =========================================================
# SERVICES
# =========================================================

def show_services(user_id):

    text = (

        "💅 Наши услуги\n\n"

        "✨ Классический маникюр\n"
        "✨ Маникюр + гель-лак\n"
        "✨ Дизайн ногтей\n\n"

        "Выберите услугу 👇"
    )

    send_message(
        user_id,
        text,
        keyboard=services_keyboard()
    )

# =========================================================
# PRICE
# =========================================================

def show_prices(user_id):

    text = (

        "💰 Прайс-лист\n\n"

        "💅 Классический маникюр — 1500₽\n\n"

        "✨ Маникюр + гель-лак — 2500₽\n\n"

        "🎨 Дизайн ногтей — 3000₽"
    )

    send_message(
        user_id,
        text
    )

# =========================================================
# PORTFOLIO
# =========================================================

def show_portfolio(user_id):

    text = (

        "🖼 Портфолио мастера\n\n"

        f"{GROUP_LINK}"
    )

    send_message(
        user_id,
        text
    )

# =========================================================
# CONTACTS
# =========================================================

def show_contacts(user_id):

    text = (

        "📞 Контакты\n\n"

        "📍 Москва\n\n"

        f"💌 Мастер:\n{MASTER_LINK}"
    )

    send_message(
        user_id,
        text
    )

# =========================================================
# BOOKING
# =========================================================

def create_booking(
    user_id,
    username,
    service_name,
    price
):

    # =====================================================
    # SEND TO ADMINS
    # =====================================================

    admin_text = (

        "🆕 НОВАЯ ЗАПИСЬ\n\n"

        f"👤 VK ID: {user_id}\n"

        f"📨 Username: {username}\n\n"

        f"💅 Услуга:\n"
        f"{service_name}\n\n"

        f"💰 Цена:\n"
        f"{price}"
    )

    for admin in ADMIN_IDS:

        try:

            send_message(
                admin,
                admin_text
            )

        except:
            pass

    # =====================================================
    # USER SUCCESS
    # =====================================================

    text = (

        "✅ Заявка отправлена!\n\n"

        "Мастер уже получила "
        "вашу заявку 💖"
    )

    send_message(
        user_id,
        text,
        keyboard=main_keyboard()
    )

# =========================================================
# MAIN LOOP
# =========================================================

print("VK BOT STARTED")

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            user_id = event.user_id

            text = event.text.lower()

            # =============================================
            # START
            # =============================================

            if text in [
                "start",
                "начать",
                "/start"
            ]:

                start(user_id)

            # =============================================
            # SERVICES
            # =============================================

            elif text == "💅 услуги":

                show_services(user_id)

            # =============================================
            # PRICE
            # =============================================

            elif text == "💰 прайс":

                show_prices(user_id)

            # =============================================
            # PORTFOLIO
            # =============================================

            elif text == "🖼 портфолио":

                show_portfolio(user_id)

            # =============================================
            # CONTACTS
            # =============================================

            elif text == "📞 контакты":

                show_contacts(user_id)

            # =============================================
            # CLASSIC
            # =============================================

            elif text == "💅 классический":

                service = SERVICES["classic"]

                text_message = (

                    f"{service['name']}\n\n"

                    f"💰 Стоимость: "
                    f"{service['price']}\n\n"

                    "Напишите мастеру "
                    "для записи 💖\n\n"

                    f"{MASTER_LINK}"
                )

                send_message(
                    user_id,
                    text_message
                )

                create_booking(
                    user_id,
                    "VK USER",
                    service["name"],
                    service["price"]
                )

            # =============================================
            # GEL
            # =============================================

            elif text == "✨ гель-лак":

                service = SERVICES["gel"]

                text_message = (

                    f"{service['name']}\n\n"

                    f"💰 Стоимость: "
                    f"{service['price']}\n\n"

                    "Напишите мастеру "
                    "для записи 💖\n\n"

                    f"{MASTER_LINK}"
                )

                send_message(
                    user_id,
                    text_message
                )

                create_booking(
                    user_id,
                    "VK USER",
                    service["name"],
                    service["price"]
                )

            # =============================================
            # DESIGN
            # =============================================

            elif text == "🎨 дизайн ногтей":

                service = SERVICES["design"]

                text_message = (

                    f"{service['name']}\n\n"

                    f"💰 Стоимость: "
                    f"{service['price']}\n\n"

                    "Напишите мастеру "
                    "для записи 💖\n\n"

                    f"{MASTER_LINK}"
                )

                send_message(
                    user_id,
                    text_message
                )

                create_booking(
                    user_id,
                    "VK USER",
                    service["name"],
                    service["price"]
                )
