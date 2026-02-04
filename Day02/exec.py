lunch_start = 12
lnch_end = 13

tea_start = 16
tea_end = 17

ct = input("Enter currnt timeee? ")
cur_time = int(ct)

if cur_time >= 12 and cur_time <= 13:
	print("It's a lunch time")
elif cur_time >= 16 and cur_time <= 17:
	print("It's a tea time")
else:
	print("Go practice python")