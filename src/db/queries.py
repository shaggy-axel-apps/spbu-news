from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.orm import sessionmaker, Session

from db import User
from settings import load_config

config = load_config()
_session = sessionmaker(config.db)

def save_user(telegram_id: int) -> bool:
    """ Регистрация пользователя """
    session: Session = _session()
    try:
        users = session.query(User).filter(User.telegram_id == telegram_id)
        if not users.first():
            session.add(User(telegram_id=telegram_id))
            session.commit()
        else:
            return False
    except (IntegrityError, InvalidRequestError):
        return False
    return True
