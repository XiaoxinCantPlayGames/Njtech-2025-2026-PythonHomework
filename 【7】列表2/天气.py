# 【遍历】假设列表lst_weather中存放了一周内每天的天气情况（包括最低气温、最高气温、天气状况、风力和空气质量等级）,数据如下：
# Ist_weather=[['周一’,'16℃C',’26℃,‘多云','1级',优”],
# [周二,’17°℃,27℃’,晴,2级’,优],
# [周三’,’16℃,28℃’,晴’,3级’,优],
# [‘周四,16℃’,’25℃’,阴’,’2级’,良”,
# ['周五’,’15℃’,’24℃C’,阴,2级’,良”,
# ['周六’,′15℃’,’25℃,晴3级’,优],
# ['周日,14℃',23°℃’,小雨,3级’,良1]
# 试编写程序,统计以下数据：
# (1)空气质量为优的天数。
# (2)风力低于3级且最高气温不超过25℃的天数。
# (3)平均气温低于20°℃的天数。
# [要求]
# 输出结果格式如下：
# 空气质量为优的天数：4,它们分别是：周一,周二,周三,周六
# 风力低于3级且最高气温不超过25℃的天数：2,它们分别是：周四,周五
# 平均气温低于20℃的天数：2,它们分别是：周五,周日



lst_weather = [['周一','16℃','26℃','多云','1级','优'],
               ['周二','17℃','27℃','晴','2级','优'],
               ['周三','16℃','28℃','晴','3级','优'],
               ['周四','16℃','25℃','阴','2级','良'],
               ['周五','15℃','24℃','阴','2级','良'],
               ['周六','15℃','25℃','晴','3级','优'],
               ['周日','14℃','23℃','小雨','3级','良']]
# (1)空气质量为优的天数
count_quality = 0
days_quality = []
for weather in lst_weather:
    if weather[5] == '优':
        count_quality += 1
        days_quality.append(weather[0])
print(f"空气质量为优的天数：{count_quality}, 它们分别是：{','.join(days_quality)}")
# (2)风力低于3级且最高气温不超过25℃的天数
count_wind_temp = 0
days_wind_temp = []
for weather in lst_weather:
    wind_level = int(weather[4][0]) # 获取风力等级
    max_temp = int(weather[2][:-1]) # 获取最高气温
    if wind_level < 3 and max_temp <= 25:
        count_wind_temp += 1
        days_wind_temp.append(weather[0])
print(f"风力低于3级且最高气温不超过25℃的天数：{count_wind_temp}, 它们分别是：{','.join(days_wind_temp)}")
# (3)平均气温低于20℃的天数
count_avg_temp = 0
days_avg_temp = []
for weather in lst_weather:
    min_temp = int(weather[1][:-1]) # 获取最低气温
    max_temp = int(weather[2][:-1]) # 获取最高气温
    avg_temp = (min_temp + max_temp) / 2 # 计算平均气温
    if avg_temp < 20:
        count_avg_temp += 1
        days_avg_temp.append(weather[0])
print(f"平均气温低于20℃的天数：{count_avg_temp}, 它们分别是：{','.join(days_avg_temp)}")