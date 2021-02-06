import uuid
from django.utils import timezone
from datetime import datetime
from django.db import models


class Meeting(models.Model):
    """会議モデル"""
    class Meta:
        # テーブル名を定義
        db_table = 'meeting'
        ordering = ['created_at']
        verbose_name = verbose_name_plural = "会議"

    # テーブルのカラムに対応するフィールドを定義
    meeting_id = models.AutoField(verbose_name='会議ID', primary_key=True)
    num_men = models.IntegerField(verbose_name='男性の人数', null=True)
    num_women = models.IntegerField(verbose_name='女性の人数', null=True)
    duration_men = models.IntegerField(verbose_name='男性の継続時間', null=True, blank=True)
    duration_women = models.IntegerField(verbose_name='女性の継続時間', null=True, blank=True)
    meeting_status = models.CharField(verbose_name='会議ステータス', max_length=25, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
