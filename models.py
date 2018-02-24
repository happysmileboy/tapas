# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Drama2(models.Model):
    place = models.TextField(blank=True, null=True)
    perf_kind = models.TextField(blank=True, null=True)
    perf_id = models.TextField(blank=True, null=True)
    openrun = models.TextField(blank=True, null=True)
    poster = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    end_date = models.TextField(blank=True, null=True)
    perf_state = models.TextField(blank=True, null=True)
    detail_url = models.TextField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)
    casts = models.TextField(blank=True, null=True)
    crews = models.TextField(blank=True, null=True)
    theater_company = models.TextField(blank=True, null=True)
    id = models.TextField(unique=True, blank=True, null=True)
    tag_places = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Drama2'
# Unable to inspect table 'Drama2_liker_set'
# The error was: list index out of range
# Unable to inspect table 'Drama2_tag2'
# The error was: list index out of range


class AccountEmailaddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AccountsUser', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AccountsEmailconfirm(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key = models.CharField(max_length=60)
    is_confirmed = models.BooleanField()
    created_at = models.DateTimeField()
    user = models.ForeignKey('AccountsUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_emailconfirm'


class AccountsProfile(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nickname = models.CharField(max_length=20)
    image = models.CharField(max_length=100, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    description = models.TextField()
    phone_number = models.IntegerField()
    user = models.ForeignKey('AccountsUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'accounts_profile'


class AccountsUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=254)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    avatar = models.CharField(max_length=100, blank=True, null=True)
    is_superuser = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'accounts_user'


class AccountsUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_groups'
        unique_together = (('user', 'group'),)


class AccountsUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class EtcNotice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=200)
    write_by = models.CharField(max_length=20)
    content = models.TextField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'etc_notice'


class PlaceList(models.Model):
    field1 = models.TextField(blank=True, null=True)
    field2 = models.TextField(blank=True, null=True)
    field3 = models.TextField(blank=True, null=True)
    field4 = models.TextField(blank=True, null=True)
    field5 = models.TextField(blank=True, null=True)
    field6 = models.TextField(blank=True, null=True)
    field7 = models.TextField(blank=True, null=True)
    field8 = models.TextField(blank=True, null=True)
    field9 = models.TextField(blank=True, null=True)
    field11 = models.TextField(blank=True, null=True)
    field12 = models.TextField(blank=True, null=True)
    field13 = models.TextField(blank=True, null=True)
    field14 = models.TextField(blank=True, null=True)
    field15 = models.TextField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place_list'


class SocialaccountSocialaccount(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class TagsTagPlaces(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tags_tag_places'
# Unable to inspect table 'yeonsonam_comment'
# The error was: list index out of range


class YeonsonamTag(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'yeonsonam_tag'


class YeonsonamTag2(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'yeonsonam_tag2'
