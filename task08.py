def convert_number_to_time(number):
    minute = int( number % 60)
    hour = int( number // 60)
    hours = "hour" if( hour == 1) else "hours"
    minutes = "minute" if(minute == 1) else "minutes"
    return f"{int(number//60)} {hours}, {int(number%60)} {minutes}"
