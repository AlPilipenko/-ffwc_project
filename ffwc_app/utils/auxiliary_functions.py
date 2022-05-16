




def percentage_diff(new_value, old_value):
    try:
        diff = round(((new_value - old_value) / old_value) * 100, 2)
        return diff
    except:
        return 0



def bmi_calc(weight, height):
    return round(weight / (height/100)**2, 1)






"Tests"

user_weight = 101
weights = [100, 98, 96]
for record in weights:
    per_change = percentage_diff(record, user_weight)
    user_weight = record
    print(per_change)
