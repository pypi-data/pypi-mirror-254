import math

def from_seconds(seconds, force_minimal_two_digits=False):
    seconds = seconds % 60
    minutes = math.floor((seconds % 3600) / 60)
    hours = math.floor((seconds % 21600) / 3600)
    
    strsec = str(seconds)
    strmin = str(minutes)
    strhor = str(hours)

    if(force_minimal_two_digits):
        if(len(strhor) == 1):
            strhor = "0" + strhor
        if(len(strmin) == 1):
            strmin = "0" + strmin
        if(len(strsec) == 1):
            strsec = "0" + strsec
    
    return strhor + ":" + strmin + ":" + strsec

def from_minutes(minutes, force_minimal_two_digits=False):
    seconds = minutes * 60
    minutes = math.floor((seconds % 3600) / 60)
    hours = math.floor((seconds % 21600) / 3600)
    
    strsec = str(seconds)
    strmin = str(minutes)
    strhor = str(hours)

    if(force_minimal_two_digits):
        if(len(strhor) == 1):
            strhor = "0" + strhor
        if(len(strmin) == 1):
            strmin = "0" + strmin
        if(len(strsec) == 1):
            strsec = "0" + strsec
    
    return strhor + ":" + strmin + ":" + strsec

def from_hours(hours, force_minimal_two_digits=False):
    seconds = minutes * 3600
    minutes = math.floor((seconds % 3600) / 60)
    hours = math.floor((seconds % 21600) / 3600)
    
    strsec = str(seconds)
    strmin = str(minutes)
    strhor = str(hours)

    if(force_minimal_two_digits):
        if(len(strhor) == 1):
            strhor = "0" + strhor
        if(len(strmin) == 1):
            strmin = "0" + strmin
        if(len(strsec) == 1):
            strsec = "0" + strsec
    
    return strhor + ":" + strmin + ":" + strsec

def to_seconds(hour_minute_seconds):
    return int(hour_minute_seconds.split(":")[0]) * 3600 + int(hour_minute_seconds.split(":")[1]) * 60 + int(hour_minute_seconds.split(":")[2])