from exceptions.storage_exception import StoreException
from dto.notification_type import NotificationType
from .storage_repository import StorageRepositoryEntity
from uuid import uuid4

class JokeRepository(StorageRepositoryEntity):
    
    def createTable(self):
        try:
            c = self.conn.cursor()
            c.execute('CREATE TABLE Joke(uuid varchar(100) not null primary key \
                                         joke TEXT not null);')
        except Exception as e:
            raise StoreException("Cannot create table")
    
    def insertJoke(self, statement):
        try:
            c = self.conn.cursor()
            joke_id = uuid4().hex
            c.execute('INSERT INTO Joke(uuid, joke) VALUES("{}", "{}")'.format(joke_id, statement))
        except Exception as e:
            raise StoreException("Cannot insert data into the Joke Table")
    
    def listAllJoke(self):
        try:
            c = self.conn.cursor()
            c.execute('SELECT * FROM Joke;')
            return c.fetchall()
        except Exception as e:
            raise StoreException("Cannot fetch data from the DB")
    
class FortuneRepository(StorageRepositoryEntity):
    
    def createTable(self):
        try:
            c = self.conn.cursor()
            c.execute('CREATE TABLE Fortune(uuid varchar(100) not null primary key \
                                            fortune TEXT not null);')
        except Exception as e:
            raise StoreException("Cannot create table")
    
    def insertFortune(self, statement):
        try:
            c = self.conn.cursor()
            fortune_id = uuid4().hex
            c.execute('INSERT INTO Fortune(uuid, fortune) VALUES("{}", "{}")'.format(fortune_id, statement))
        except Exception as e:
            raise StoreException("Cannot insert data into the Fortune Table")
    
    def listAllFortune(self):
        try:
            c = self.conn.cursor()
            c.execute('SELECT * FROM Joke;')
            return c.fetchall()
        except Exception as e:
            raise StoreException("Cannot fetch data from the DB")
    
class AlarmRepository(StorageRepositoryEntity):
    
    def createTable(self):
        try:
            c = self.conn.cursor()
            c.execute('CREATE TABLE Alarm(uuid varchar(100) not null primary key \
                                          alarm TEXT not null \
                                          alarm_type varchar(255) not null)')
        except Exception as e:
            raise StoreException("Cannot create table")
    
    def insertAlarm(self, statement, alert_type):
        try:
            c = self.conn.cursor()
            alarm_id = uuid4().hex
            c.execute('INSERT INTO Alarm(uuid, alarm, alarm_type) VALUES("{}", "{}", "{}")'.format(alarm_id, statement, alert_type))
        except Exception as e:
            raise StoreException("Cannot insert data into the Alarm Table")
    
    def listAllAlarm(self):
        try:
            c = self.conn.cursor()
            c.execute('SELECT * FROM Joke;')
            return c.fetchall()
        except Exception as e:
            raise StoreException("Cannot fetch data from the DB")