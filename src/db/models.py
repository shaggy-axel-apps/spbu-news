import sqlalchemy as sq

from settings.config import engine, Base


class Group(Base):
    """ Группы в универе, следующая пара с датой и временем """
    __tablename__ = 'group'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    group_alias = sq.Column(sq.String)
    next_lesson_at = sq.Column(sq.DateTime)
    # через {next_lesson_at} - {datetime.now()} пройдет {lesson.title} в аудитории {lesson.place}
    next_lesson_description = sq.Column(sq.String)


class Notification(Base):
    """ Уведомления о занятии группы """
    __tablename__ = 'notification'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    notify_for = sq.Column(sq.Integer)  # время в секундах за сколько надо уведомить


class User(Base):
    """ Пользователь telegram-бота """
    __tablename__ = 'user'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    telegram_id = sq.Column(sq.Integer, unique=True)
    group = sq.ForeignKey(Group, null=True)
    notification = sq.ForeignKey(Notification, null=True)
