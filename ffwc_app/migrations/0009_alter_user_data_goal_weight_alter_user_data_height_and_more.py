# Generated by Django 4.0.4 on 2022-05-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffwc_app', '0008_alter_user_data_goal_weight_alter_user_data_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='goal_weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='weight_update',
            field=models.FloatField(default=0),
        ),
    ]
