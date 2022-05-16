from .auxiliary_functions import percentage_diff, bmi_calc


def data_extractor(context, User_Data, Weight_Update):
    "Gets and sorts Dates and Weighs from Weight_Update."
    user_id_list = []
    weight_progress = []
    for q in context.get('weight_update'):
        if q.user.id not in user_id_list:
            user_id_list.append(q.user.id)

    weight_update_values = Weight_Update.objects.all().order_by('user').values()

    for id in user_id_list:
        weight_id_data = weight_update_values.filter(user=id)
        weight_progress.append(weight_id_data)

    "Data proccess for plots and other"
    group_weight = 0
    group_goal_weight = 0
    counter = 0
    user_initial_weight = 0
    weight_context = {}
    for user in User_Data.objects.all().order_by('user').values():
        # print(user)
        user_id = user.get('id')
        user_name = user.get('name')
        user_weight = user.get('weight')
        user_goal_weight = user.get('goal_weight')
        user_height = user.get('height')

        weight_context[user_name] = {}
        recorded_weights = weight_progress[counter]
        user_initial_weight += user_weight
        percentage_change_list = []
        bmi_list = []
        record_date_list = []
        record_list = []


        for q in recorded_weights:
            record_date = q.get('created')
            record = q.get('weight_update')
            per_change = percentage_diff(record, user_weight)

            user_weight = record
            bmi = bmi_calc(user_weight, user_height)

            record_date_list.append(record_date)
            record_list.append(record)
            percentage_change_list.append(per_change)
            bmi_list.append(bmi)

            weight_context[user_name]['Date'] = record_date_list
            weight_context[user_name]['Weight'] = record_list
            weight_context[user_name]['Change %'] = percentage_change_list
            weight_context[user_name]['BMI'] = bmi_list

        counter += 1
        group_weight += user_weight
        group_goal_weight += user_goal_weight

    group_to_lose = group_weight - group_goal_weight
    print("HHHHHHHHHHHHHHHHHHHHHHHHH", user_initial_weight)
    return (weight_context, group_weight,
                        user_initial_weight, group_goal_weight)
