from aiogram import types


async def build_keyboard(buttons: list[list[dict]]) -> types.InlineKeyboardMarkup: # noqa
    """
    Build an inline keyboard from a list of button dictionaries

    :param buttons: List of lists containing button dictionaries
    :return: InlineKeyboardMarkup object.

    buttons = [
        [{'text': 'Button 1', 'callback_data': 'callback_1'}],
        [{'text': 'Button 2', 'web_app': 'https://example.com'}]
    ]
    keyboard = await build_keyboard(buttons)
    """
    inline_keyboard = []
    for row in buttons:
        keyboard_row = []
        for button in row:
            if 'callback_data' in button:
                keyboard_row.append(
                    types.InlineKeyboardButton(
                        text=button['text'],
                        callback_data=button['callback_data']
                    )
                )
            elif 'web_app' in button:
                keyboard_row.append(
                    types.InlineKeyboardButton(
                        text=button['text'],
                        web_app=types.WebAppInfo(url=button['web_app'])
                    )
                )
        inline_keyboard.append(keyboard_row)

    return types.InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
