import app_requests, config
import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

currentlyScheduledShutdown = None

def main():
    checkSchedule()
    scheduler = BlockingScheduler()
    scheduler.add_job(checkSchedule, 'interval', minutes = config.schedule_interval)
    scheduler.start()
    
def checkSchedule():
    events = app_requests.areaInfo(config.area_code)["events"]
    global currentlyScheduledShutdown
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))

    #no loadshed scheduled :) (unlikely to occur...)
    if events[0] is None:
        if currentlyScheduledShutdown is not None:
            os.system("shutdown -c")
        return

    #wont run if no events
    for event in events:
        time = datetime.datetime.fromisoformat(event["start"])


        if now > datetime.datetime.fromisoformat(event["end"]) or now > time:
            continue

        if time.day != now.day and time.hour != 0 :
            continue

        if time.hour == 0:
            hour = str(23)
        else:
            hour = str(time.hour-1)
        newScheduledShutdown = hour + ":" + str(60-config.shutdown_delta)
        if newScheduledShutdown == currentlyScheduledShutdown:
            return
        currentlyScheduledShutdown = newScheduledShutdown
        print("Scheduling a shutdown for " + currentlyScheduledShutdown)
        #print("shutdown -P " + currentlyScheduledShutdown + " \"Shutting down due to scheduled loadshedding!\"")
        os.system("shutdown -P " + currentlyScheduledShutdown + " \"Shutting down due to scheduled loadshedding!\"")
        break

    

if __name__ == '__main__':
    main()