import time

# 获取高考日期输入
gk_date_input = input("请输入高考日期（格式为YYYY-MM-DD，默认为2025-06-07）：").strip()
gk_date_str = gk_date_input.replace(" ", "") if gk_date_input else "2025-06-07"

try:
    gk_struct = time.strptime(gk_date_str, "%Y-%m-%d")
except ValueError:
    print("日期格式错误，请按格式输入。")
    exit()


# 计算当前日期0点时间戳
current_time = time.localtime()
current_day_ts = time.mktime((
    current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
    0, 0, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst
))

# 计算高考日期时间戳和天数差
gk_ts = time.mktime(gk_struct)
days = int((gk_ts - current_day_ts) // 86400)

# 输出结果
current_date = time.strftime("%Y-%m-%d", current_time)
print("="*30)
print(f"{gk_struct.tm_year} 年高考日期是 {gk_date_str}")
print(f"今天是 {current_date}")
print(f"距离 {gk_struct.tm_year} 年高考还有 {days} 天")
print("="*30)
