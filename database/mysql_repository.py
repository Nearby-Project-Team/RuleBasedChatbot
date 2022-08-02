from storage_repository import StorageRepositoryEntity
from exceptions.storage_exception import StoreException
from dto.notificationType import NotificationType
import cronex

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
                dateCondition = "{} <= ".format(sdate) + dateCondition
            if edate:
                dateCondition = dateCondition + " <= {}".format(edate) 
            query = 'SELECT {} FROM Calandar WHERE elderly_id={} AND {} AND notificationType=ONEOFF'.format(selectedColumns, elderly_id, dateCondition)
        elif notificationType == NotificationType.REPEAT:
            query = 'SELECT {} FROM Calandar WHERE elderly_id={} AND notificationType=REPEATATION'.format(selectedColumns, elderly_id)
        else :
            query = 'SELECT {} FROM Calandar WHERE elderly_id={}'.format(selectedColumns, elderly_id)
        return query
    
    def getDateRegex2NowTime(self, regex):
        
        pass
    
    def getOneSideCalandarInfo(self, elderly_id: str, sdate: str, edate: str, notificationType: NotificationType):
        try:
            c = self.conn.cursor()
            c.execute(self.dateQueryBuilder(elderly_id=elderly_id, sdate=sdate, edate=edate, notificationType=notificationType))
            if notificationType == NotificationType.REPEAT:
                
                pass
            return c.fetchall()
        except Exception as e:
            print(e.with_traceback())
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
                    
                    pass
                else :
                    raise StoreException("Invalid Date Format for QueryBuilder!")
        except Exception as e:
            print(e.with_traceback())
            raise StoreException("Error in reading {} user's calandar data".format(elderly_id))