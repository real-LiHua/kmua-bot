from telegram import Chat, Message, User

from kmua.logger import logger


def get_message_common_link(message: Message) -> str | None:
    logger.debug(f"Get message common link for {message.link}")
    try:
        chat = message.chat
        link = f"https://t.me/c/{str(chat.id).removeprefix('-100')}/{message.id}"
        return link
    except Exception as e:
        logger.error(f"{e.__class__.__name__}: {e}")
        return None


def parse_message_link(link: str) -> tuple[int, int]:
    logger.debug(f"Parse message link for {link}")
    split_link = link.split("/")
    try:
        chat_id = int("-100" + split_link[-2])
        message_id = int(split_link[-1])
    except ValueError:
        logger.error(f"无法解析链接: {link}")
        return None, None
    return chat_id, message_id


def get_message_origin(message: Message) -> User | Chat | None:
    if origin := message.forward_origin:
        match origin.type:
            case origin.USER:
                return origin.sender_user
            case origin.CHANNEL:
                return origin.chat
            case origin.CHAT:
                return origin.sender_chat
    return message.sender_chat or message.from_user
