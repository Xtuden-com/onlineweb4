# Generated by Django 3.0.5 on 2020-05-21 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0004_remove_notification_icon"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subscription",
            options={
                "ordering": ("user", "endpoint"),
                "verbose_name": "Varselsabonnement",
                "verbose_name_plural": "Varselsabonnementer",
            },
        ),
        migrations.AlterField(
            model_name="permission",
            name="default_value_push",
            field=models.BooleanField(
                default=False, verbose_name="Standardverdi for pushvarsel"
            ),
        ),
        migrations.AlterField(
            model_name="userpermission",
            name="permission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_permissions",
                to="notifications.Permission",
            ),
        ),
    ]