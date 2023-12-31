# Generated by Django 4.2.7 on 2023-12-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eventapp", "0009_eventsignup"),
    ]

    operations = [
        migrations.AddField(
            model_name="toon",
            name="tclass",
            field=models.CharField(
                choices=[
                    ("death_knight", "Death Knight"),
                    ("demon_hunter", "Demon Hunter"),
                    ("druid", "Druid"),
                    ("evoker", "Evoker"),
                    ("hunter", "Hunter"),
                    ("mage", "Mage"),
                    ("monk", "Monk"),
                    ("paladin", "Paladin"),
                    ("priest", "Priest"),
                    ("rogue", "Rogue"),
                    ("shaman", "Shaman"),
                    ("warlock", "Warlock"),
                    ("warrior", "Warrior"),
                ],
                default="death_knight",
                max_length=30,
            ),
        ),
    ]
