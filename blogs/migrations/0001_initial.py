
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=30,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Username must consist of @ followed by at least three alphanumericals",
                                regex="^@\\w{3,}$",
                            )
                        ],
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("bio", models.CharField(blank=True, max_length=520)),
                (
                    "favourite_genre",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("NO", "None"),
                            ("E", "Ebooks"),
                            ("A", "Arts"),
                            ("BM", "Biographies & Memoirs"),
                            ("BI", "Business & Investing"),
                            ("C", "Comics"),
                            ("CT", "Computers & Technology"),
                            ("CF", "Cookery, Food & Wine"),
                            ("F", "Fantasy"),
                            ("FL", "Fiction & Literature"),
                            ("G", "Gardening"),
                            ("HF", "Health & Fitness"),
                            ("HM", "Health, Mind & Body"),
                            ("H", "History"),
                            ("M", "Mystery & Thrillers"),
                            ("N", "Nature"),
                            ("P", "Poetry"),
                            ("PC", "Politics & Current Affairs"),
                            ("R", "Reference"),
                            ("RO", "Romance"),
                            ("RS", "Religion & Spirituality"),
                            ("S", "Science"),
                            ("SF", "Science Fiction"),
                            ("SP", "Sports"),
                            ("T", "Travel"),
                            ("Y", "Young Adult"),
                        ],
                        default="NO",
                        max_length=2,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="AttendEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isbn", models.CharField(max_length=255, verbose_name="ISBN")),
                (
                    "book_title",
                    models.CharField(max_length=255, verbose_name="Book-Title"),
                ),
                (
                    "book_author",
                    models.CharField(max_length=255, verbose_name="Book-Author"),
                ),
                (
                    "year_of_publication",
                    models.CharField(max_length=4, verbose_name="Year-Of-Publication"),
                ),
                (
                    "publisher",
                    models.CharField(max_length=255, verbose_name="Publisher"),
                ),
                (
                    "image_url_s",
                    models.CharField(max_length=255, verbose_name="Image-URL-S"),
                ),
                (
                    "image_url_m",
                    models.CharField(max_length=255, verbose_name="Image-URL-M"),
                ),
                (
                    "image_url_l",
                    models.CharField(max_length=255, verbose_name="Image-URL-L"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Club",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Club name cannot contain numbers and special characters in their name.",
                                regex="^[a-zA-Z]*$",
                            )
                        ],
                    ),
                ),
                ("bio", models.CharField(blank=True, max_length=500)),
                ("rules", models.CharField(blank=True, max_length=1000)),
                (
                    "theme",
                    models.CharField(
                        choices=[
                            ("E", "Ebooks"),
                            ("A", "Arts"),
                            ("BM", "Biographies & Memoirs"),
                            ("BI", "Business & Investing"),
                            ("C", "Comics"),
                            ("CT", "Computers & Technology"),
                            ("CF", "Cookery, Food & Wine"),
                            ("F", "Fantasy"),
                            ("FL", "Fiction & Literature"),
                            ("G", "Gardening"),
                            ("HF", "Health & Fitness"),
                            ("HM", "Health, Mind & Body"),
                            ("H", "History"),
                            ("M", "Mystery & Thrillers"),
                            ("N", "Nature"),
                            ("P", "Poetry"),
                            ("PC", "Politics & Current Affairs"),
                            ("R", "Reference"),
                            ("RO", "Romance"),
                            ("RS", "Religion & Spirituality"),
                            ("S", "Science"),
                            ("SF", "Science Fiction"),
                            ("SP", "Sports"),
                            ("T", "Travel"),
                            ("Y", "Young Adult"),
                        ],
                        default="",
                        max_length=2,
                    ),
                ),
                (
                    "admins",
                    models.ManyToManyField(
                        related_name="admin_of", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=280)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "in_club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="club_posts",
                        to="blogs.club",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="FeaturedBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_title", models.CharField(max_length=255)),
                ("book_author", models.CharField(max_length=255)),
                (
                    "curator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),

        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(max_length=1024)),
                ("location", models.CharField(blank=True, max_length=50)),
                ("address", models.CharField(blank=True, max_length=50)),
                ("date", models.DateField()),
                ("startTime", models.TimeField()),
                ("endTime", models.TimeField()),
                ("eventLink", models.CharField(blank=True, max_length=200)),
                (
                    "attendees",
                    models.ManyToManyField(
                        related_name="upcoming_events",
                        through="blogs.AttendEvent",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="upcoming_events",
                        to="blogs.club",
                    ),
                ),
                (
                    "selectedBook",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="club_events",
                        to="blogs.book",
                    ),
                ),
            ],
        ),

        migrations.AddField(
            model_name="club",
            name="book",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="blogs.featuredbook",
            ),
        ),
        migrations.AddField(
            model_name="club",
            name="members",
            field=models.ManyToManyField(
                related_name="member_of", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="club",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owned_clubs",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="club",
            name="pending_members",
            field=models.ManyToManyField(
                blank=True,
                related_name="pending_member_of",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="attendevent",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attend_event",
                to="blogs.event",
            ),
        ),
        migrations.AddField(
            model_name="attendevent",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attend_event",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=280)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="published_comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_comments",
                        to="blogs.club",
                    ),
                ),
                (
                    "commented_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blogs.post",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "unique_together": {("author", "created_at")},
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='published_comments', to=settings.AUTH_USER_MODEL)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='blogs.club')),
                ('commented_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.post')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('author', 'created_at')},
            },
        ),
        migrations.AlterUniqueTogether(
            name="attendevent",
            unique_together={("event", "user")},
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("email"),
                name="unique_lower_user_email",
            ),
        ),
    ]
