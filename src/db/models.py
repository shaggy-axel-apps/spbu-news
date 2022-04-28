import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base

from settings.config import load_config


config = load_config()
Base = declarative_base()


class Group(Base):
    """ Группы в универе, следующая пара с датой и временем """
    __tablename__ = 'spb_group'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    group_alias = sq.Column(sq.String, unique=True)
    next_lesson_at = sq.Column(sq.DateTime)
    # через {next_lesson_at} - {datetime.now()} пройдет {lesson.title} в аудитории {lesson.place}
    next_lesson_description = sq.Column(sq.String)


class Notification(Base):
    """ Уведомления о занятии группы """
    __tablename__ = 'spb_notification'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    notify_for = sq.Column(sq.Integer)  # время в секундах за сколько надо уведомить


class User(Base):
    """ Пользователь telegram-бота """
    __tablename__ = 'spb_user'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    telegram_id = sq.Column(sq.Integer, unique=True)
    group = sq.Column(sq.Integer, sq.ForeignKey(
        'spb_group.id', ondelete='SET NULL'), nullable=True)
    notification = sq.Column(sq.Integer, sq.ForeignKey(
        'spb_notification.id', ondelete='SET NULL'), nullable=True)


def migrate(**options):
    Base.metadata.create_all(config.db)


if __name__ == '__main__':
    migrate()
