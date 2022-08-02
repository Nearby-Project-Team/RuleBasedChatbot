from exceptions.storage_exception import StoreException
from dto.notification_type import NotificationType
from .storage_repository import StorageRepositoryEntity
from datetime import datetime as dt
from cron_converter import Cron
from pytz import timezone

'''
Date의 경우, 다음과 같으s Format으로만 들어온다고 가정한다.
YYYY-MM-DD HH:MM
'''
TZ = timezone('Asia/Seoul')

class CalandarRepository(StorageRepositoryEntity):
    
    def dateQueryBuilder(self, elderly_id: str, sdate: str, edate: str, notificationType: NotificationType):
        selectedColumns = ""
        if notificationType:
            selectedColumns += "content, ScheduleDate"
        else :
            selectedColumns += "content, ScheduleDate, notificationType"
        
        if (not sdate) and (not edate) and (notificationType == NotificationType.ONEOFF):
            raise StoreException("Invalid Date Format for QueryBuilder!")
        
        query = ''
        if notificationType == NotificationType.ONEOFF:
            dateCondition = "ScheduleDate"
            if sdate:
                dateCondition = "'{}' <= ".format(sdate) + dateCondition
            if edate:
                dateCondition = dateCondition + " <= '{}'".format(edate) 
            query = 'SELECT {} FROM Calandar WHERE elderly_id={} AND {} AND notificationType=ONEOFF'.format(selectedColumns, elderly_id, dateCondition)
        elif notificationType == NotificationType.REPEAT:
            query = 'SELECT {} FROM Calandar WHERE elderly_id={} AND notificationType=REPEATATION'.format(selectedColumns, elderly_id)
        else :
            query = 'SELECT {} FROM Calandar WHERE elderly_id={}'.format(selectedColumns, elderly_id)
        return query
    
    def getIsNextInTime(self, regex: str, sdate: str, edate: str):
        s = TZ.localize(dt.strptime(sdate, "%Y-%m-%d %H:%M")) 
        e = TZ.localize(dt.strptime(edate, "%Y-%m-%d %H:%M"))
        cron = Cron(regex)
        schedule = cron.schedule(start_date=s)
        nSchedule = schedule.next()
        if e < nSchedule:
            return False
        else :
            return nSchedule
    
    def getOneSideCalandarInfo(self, elderly_id: str, sdate: str, edate: str, notificationType: NotificationType):
        try:
            c = self.conn.cursor()
            c.execute(self.dateQueryBuilder(elderly_id=elderly_id, sdate=sdate, edate=edate, notificationType=notificationType))
            calandarList = c.fetchall()
            repeat = []
            if notificationType == NotificationType.REPEAT:
                for content, date in calandarList:
                    nSche = self.getIsNextInTime(date, sdate, edate)
                    if nSche:
                        repeat.append((content, nSche))
            return repeat
        except Exception as e:
            raise StoreException("Error in reading {} user's calandar data".format(elderly_id))
    
    def getBothSideCalandarInfo(self, elderly_id: str, sdate: str, edate: str):
        try:
            c = self.conn.cursor()
            c.execute(self.dateQueryBuilder(elderly_id=elderly_id, sdate=sdate, edate=edate, notificationType=None))
            calandarList = c.fetchall()
            one_off = []
            repeat = []
            for content, date, noti_type in calandarList:
                if noti_type == NotificationType.ONEOFF:
                    one_off.append((content, date))
                elif noti_type == NotificationType.REPEAT:
                    nSche = self.getIsNextInTime(date, sdate, edate)
                    if nSche:
                        repeat.append((content, nSche))
                else :
                    raise StoreException("Invalid Date Format for QueryBuilder!")
            return one_off, repeat
        except Exception as e:
            raise StoreException("Error in reading {} user's calandar data".format(elderly_id))