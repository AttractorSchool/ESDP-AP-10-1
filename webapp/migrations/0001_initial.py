# Generated by Django 4.2.2 on 2023-07-01 12:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citi_name', models.CharField(max_length=30, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('events_at', models.DateTimeField(verbose_name='Дата мероприятия')),
                ('number_of_seats', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(100)], verbose_name='Количество мест')),
                ('start_register_at', models.DateTimeField(default=None, null=True, verbose_name='Дата начала регистрации')),
                ('end_register_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата конца регистрации')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('place', models.CharField(max_length=200, null=True, verbose_name='Место')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')),
                ('cities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='сities', to='webapp.cities', verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user_pic', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_image', to=settings.AUTH_USER_MODEL, verbose_name='Организатор')),
            ],
        ),
        migrations.CreateModel(
            name='NameVotingTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_voting_type', models.CharField(max_length=100, verbose_name='Наименование типа голосования')),
            ],
        ),
        migrations.CreateModel(
            name='TypeEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events_name', models.CharField(max_length=30, verbose_name='Мероприятие')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_to_vote', models.TextField(max_length=100, verbose_name='Вопрос на голосование')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обнавления голосования')),
            ],
        ),
        migrations.CreateModel(
            name='VotingTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean_value', models.BooleanField(default=True, verbose_name='Булева значение')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_type', to='webapp.vote', verbose_name='Голосование типы')),
                ('voting_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name_voting_types', to='webapp.namevotingtypes', verbose_name='Тип голосования')),
            ],
        ),
        migrations.CreateModel(
            name='VotingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(max_length=100, verbose_name='Вариант')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления варианта')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удаление варианта')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_options', to='webapp.vote', verbose_name='Голосование опции')),
            ],
        ),
        migrations.CreateModel(
            name='UsersWhoVoted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_at', models.DateTimeField(auto_now=True, verbose_name='Дата ответа')),
                ('possible_answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='possible_answer', to='webapp.votingoptions', verbose_name='Вариант ответа')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
        ),
        migrations.CreateModel(
            name='UserBooked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField()),
                ('date_of_payment', models.DateTimeField(blank=True, null=True)),
                ('cancellation_date', models.DateTimeField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.events', verbose_name='Мероприятие')),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Забронировал')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='удалено')),
                ('cities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='сities_for_news', to='webapp.cities', verbose_name='Город')),
                ('photo', models.ManyToManyField(related_name='photo_for_news', to='webapp.image', verbose_name='Фото')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_for_news', to=settings.AUTH_USER_MODEL, verbose_name='Организатор')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ListVotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_vote', models.CharField(max_length=200, verbose_name='Наименование голосования')),
                ('date_group_was_added_from_polls', models.DateTimeField(auto_now=True, verbose_name='Дата добавления группу из голосований')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления списка')),
                ('voting_opening_at', models.DateTimeField(auto_now=True, verbose_name='Дата открытия голосования')),
                ('expiration_at', models.DateTimeField(auto_now=True, verbose_name='Дата окончания')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено голосования')),
                ('user_who_created_list_votes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь создавший список из голосований')),
                ('vote', models.ManyToManyField(related_name='vote_list', to='webapp.vote', verbose_name='Голосование список')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_image', to='webapp.image', verbose_name='Фото мероприятия'),
        ),
        migrations.AddField(
            model_name='events',
            name='resident_booked',
            field=models.ManyToManyField(blank=True, related_name='user_booked', through='webapp.UserBooked', to=settings.AUTH_USER_MODEL, verbose_name='Бранированные резиденты'),
        ),
        migrations.AddField(
            model_name='events',
            name='sponsor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to=settings.AUTH_USER_MODEL, verbose_name='Организатор'),
        ),
        migrations.AddField(
            model_name='events',
            name='type_events',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_events', to='webapp.typeevents', verbose_name='Тип мероприятия'),
        ),
        migrations.CreateModel(
            name='AttachingToBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата добавления голосования')),
                ('events', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='webapp.events', verbose_name='Мероприятия')),
                ('list_of_votes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_of_votes', to='webapp.listvotes', verbose_name='Список голосования')),
                ('news', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='webapp.news', verbose_name='Новости')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь которому дали список из голосований')),
            ],
        ),
    ]
