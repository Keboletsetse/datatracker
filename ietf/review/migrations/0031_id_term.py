# Generated by Django 2.2.28 on 2023-02-10 19:58

from django.db import migrations, models
import ietf.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0030_use_date_today_helper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreviewersettings',
            name='filter_re',
            field=models.CharField(blank=True, help_text='Internet-Draft names matching this regular expression should not be assigned', max_length=255, validators=[ietf.utils.validators.RegexStringValidator()], verbose_name='Filter regexp'),
        ),
        migrations.AlterField(
            model_name='reviewersettings',
            name='filter_re',
            field=models.CharField(blank=True, help_text='Internet-Draft names matching this regular expression should not be assigned', max_length=255, validators=[ietf.utils.validators.RegexStringValidator()], verbose_name='Filter regexp'),
        ),
    ]