# Generated by Django 2.1.11 on 2019-10-09 10:45

from django.db import migrations


def create_initial_mark_rule_set(apps, schema_editor):
    MarkRuleSet = apps.get_model('marks', 'MarkRuleSet')
    RuleAcceptance = apps.get_model('marks', 'RuleAcceptance')
    User = apps.get_model('authentication', 'OnlineUser')

    current_rules = MarkRuleSet.objects.create(
        content='Initial Mark Rules (--replace-this--)',
        version='0.0-alpha',
    )

    for user in User.objects.all():
        if user.mark_rules:
            RuleAcceptance.objects.create(
                user=user,
                rule_set=current_rules,
            )


def reverse_mark_rule_acceptance(apps, schema_editor):
    RuleAcceptance = apps.get_model('marks', 'RuleAcceptance')
    User = apps.get_model('authentication', 'OnlineUser')

    for user in User.objects.all():
        if RuleAcceptance.objects.filter(user=user):
            user.mark_rules = True


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0007_auto_20191009_1244'),
    ]

    operations = [
        migrations.RunPython(create_initial_mark_rule_set, reverse_mark_rule_acceptance)
    ]