def convert_number_to_time(number):
    mins = int( number % 60)
    hour = int( number // 60)
    hours = "hours" if( hour == 1) else "hours"
    minutes = "minute" if(mins == 1) else "minutes"
    return f"{int(number//60)} {hours}, {int(number%60)} {minutes}"
