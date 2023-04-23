import time

now = time.time()

print(now)

print(time.gmtime(now))

now_tm = time.gmtime(now)

print(now_tm.tm_year)

print(f"Evenimentul s-a intamplat in anul {now_tm.tm_year}, luna {now_tm.tm_mon}, ora {now_tm.tm_hour}, minutul {now_tm.tm_min}, secunda {now_tm.tm_sec}")

B_YEAR = 1993

print(time.strftime("%Y ___", now_tm))

event_time = "12 April 2023 16:48:53"

ev_tm = time.strptime(event_time, "%d %B %Y %H:%M:%S")

print(ev_tm)

ev1 = "20-02-2023 10:11"
ev2 = "22-02-2023 12:45"

event_one = time.strptime(ev1, "%d %B %S")
event_two = time.strptime(ev2, "%d %B %S")

print(f"Au trecut {event_one.tm_mday - event_two.tm_mday * 60} secunde ")