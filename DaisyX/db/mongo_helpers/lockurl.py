from DaisyX.services.mongo import mongodb as db_x

lockurl = db_x["LOCKURL"]


def add_chat_i(chat_id):
    sta = lockurl.find_one({"chat_id": chat_id})
    if sta:
        return False
    else:
        lockurl.insert_one({"chat_id": chat_id})
        return True


def remove_chat_i(chat_id):
    sta = lockurl.find_one({"chat_id": chat_id})
    if not sta:
        return False
    else:
        lockurl.delete_one({"chat_id": chat_id})
        return True


def get_all_chats_i():
    r = list(lockurl.find())
    if r:
        return r
    else:
        return False


def get_session_i(chat_id):
    stark = lockurl.find_one({"chat_id": chat_id})
    if not sta:
        return False
    else:
        return sta
