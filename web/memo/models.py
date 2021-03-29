from django.db import models
from django.utils import timezone
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Memo(models.Model):
    class Meta:
        verbose_name = 'メモ'
        verbose_name_plural = 'メモ'

    user = models.ForeignKey(
        User,
        verbose_name='ユーザー',
        on_delete=models.CASCADE,
        default=1
    )

    users = models.CharField(
        verbose_name='作成したユーザー名',
        max_length=50,
        default=user
    )

    # 問題
    question = models.CharField(
        verbose_name='メモ問題',
        max_length=150,
        help_text='問題タイトル',
    )

    # 画像
    image = models.ImageField(
        verbose_name='アイコン',
        upload_to='image/',
        default='image/memo.jpg'
    )

    # 問題内容
    text = models.TextField(
        verbose_name='問題内容',
        help_text='問題内容',
    )

    # 作成日
    creat_time = models.DateField(
        verbose_name='作成日',
        default=timezone.datetime.today,
    )

    # 復習日
    update_time = models.DateField(
        verbose_name='復習日',
        default=timezone.now,
    )

    # タグ
    tag = models.CharField(
        verbose_name='タグ',
        max_length=50,
        help_text='タグ',
        blank=True,
    )

    # 復習カウンター
    counter = models.IntegerField(
        verbose_name='復習カウンター',
        default=1,
    )

    def __str__(self):
        return str(self.question) + str(self.update_time) + str(self.tag) + str(
            self.counter)