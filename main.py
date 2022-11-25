import app_requests, config
import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

next_loadshed = None
def main():
    checkSchedule()
    checkShutdown()
    scheduler = BlockingScheduler()
    scheduler.add_job(checkSchedule, 'interval', minutes = config.schedule_interval)
    scheduler.add_job(checkShutdown, 'interval', minutes = config.shutdown_interval)
    scheduler.start()
    
def checkSchedule():
    global next_loadshed
    event = app_requests.areaInfo(config.area_code)["events"][0]
    if event is None:
        next_loadshed = None
        return
    time = datetime.datetime.fromisoformat(event["start"])
    #timediff = time-datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))
    
    next_loadshed = time

def checkShutdown():
    if next_loadshed is None:
        print('none')
        return


    if next_loadshed-datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))  <= datetime.timedelta(minutes=config.shutdown_delta):
        print("shutting down")
        #print(next_loadshed-datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2))))
        os.system("shutdown now \" Shutting down for Loadshedding  :( \" ")

    else:
        print("not shutting down")
       # print(next_loadshed-datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2))))



if __name__ == '__main__':
    main()