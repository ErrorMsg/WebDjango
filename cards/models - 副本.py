# -*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


char_dict = {
    'badcard': '灾祸牌',
    'basiccard': '基本牌',
    'cardname': '卡牌名称',
    'club': '梅花',
    'country': '国籍',
    'delay': '延时',
    'diamond': '方块',
    'effect': '效果',
    'equipcard': '装备牌',
    'heroname': '武将名称',
    'herocard': '武将牌',
    'heart': '红桃',
    'horse': '坐骑',
    'hide': '伏击',
    'hp': '体力上限',
    'immed': '非延时',
    'jun': '君',
    'kind': '卡牌种类',
    'length': '距离',
    'measure': '宝物',
    'nickname': '武将称号',
    'pattern': '花色',
    'point': '点数',
    'power': '势力',
    'qun': '群',
    'ruse': '诡计',
    'shield': '防具',
    'shu': '蜀',
    'skill': '技能',
    'spade': '黑桃',
    'special': '特殊',
    'united': '珠联璧合',
    'weapon': '武器',
    'wei' : '魏',
    'wisdomcard': '锦囊牌',
    'wu': '吴',
}

short_dict = {
    'c': 'club',
    'd': 'diamond',
    'h': 'heart',
    's': 'spade',
}

pattern_choices = (
        ('heart', char_dict['heart']),
        ('spade', char_dict['spade']),
        ('diamond', char_dict['diamond']),
        ('club', char_dict['club']),
    )

country_choices = (
    ('wei', char_dict['wei']),
    ('shu', char_dict['shu']),
    ('wu', char_dict['wu']),
    ('qun', char_dict['qun']),
    ('jun', char_dict['jun']),
)

hp_choices = (
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

equip_choices = (
    ('weapon', char_dict['weapon']),
    ('horse', char_dict['horse']),
    ('shield', char_dict['shield']),
    ('measure', char_dict['measure']),
)

wisdom_choices = (
    ('immed', char_dict['immed']),
    ('delay', char_dict['delay']),
    ('ruse', char_dict['ruse']),
    ('power', char_dict['power']),
)


# Card
class Card(models.Model):
    name = models.CharField(max_length=30)
    pic = models.ImageField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.short_description = 'new ?'
    was_published_recently.boolean = True


# HeroCard
class HeroCard(Card):
    country = models.CharField(max_length=10, choices=country_choices)
    nickname = models.CharField(max_length=50)
    hp = models.IntegerField(choices=hp_choices)
    skill = models.TextField()
    united = models.CharField(max_length=30, blank=True)
    kind = 'herocard'

    def __str__(self):
        return self.name

    def short_description(self):
        return "%s:%s\n%s:%s\n%s:%s\n%s:%s\n" % (
            char_dict['heroname'], Card, char_dict['nickname'], self.nickname, char_dict['country'], self.country, char_dict['hp'], self.hp,
        )

    def get_kind(self):
        return self.kind

    def set_united(self, card):
        pass


# BasicCard
class BasicCard(Card):
    point = models.CharField(max_length=5)
    pattern = models.CharField(max_length=10, choices=pattern_choices)
    color = 'red' if pattern == 'heart' or pattern == 'diamond' else 'black'
    special = models.CharField(max_length=10, blank=True)
    effect = models.TextField(max_length=300, blank=True)
    kind = 'basiccard'

    def __str__(self):
        return self.special + self.name

    def short_description(self):
        return "%s:%s\n%s:%s\n%s:%s\n" % (
            char_dict['pattern'], char_dict[self.pattern], char_dict['point'], self.point, char_dict['kind'], char_dict[self.kind],
        )

    def get_kind(self):
        return self.kind


# EquipCard
class EquipCard(Card):
    special = models.CharField(max_length=20, choices=wisdom_choices, default='immed')
    point = models.CharField(max_length=5)
    pattern = models.CharField(max_length=10, choices=pattern_choices)
    color = 'red' if pattern == 'heart' or pattern == 'diamond' else 'black'
    effect = models.TextField()
    kind = 'equipcard'


# WeaponCard
class WeaponCard(Card):
    point = models.CharField(max_length=5)
    pattern = models.CharField(max_length=10, choices=pattern_choices)
    color = 'red' if pattern == 'heart' or pattern == 'diamond' else 'black'
    length = models.IntegerField()
    effect = models.TextField()
    kind = 'equipcard'

    def __str__(self):
        return self.name

    def short_description(self):
        return "%s:%s\n%s:%s\n%s:%s\n" % (
            char_dict['pattern'], char_dict[self.pattern], char_dict['point'], self.point, char_dict['kind'], char_dict[self.kind], char_dict['length'], self.length,
        )

    def get_kind(self):
        return self.kind


# HorseCard
class HorseCard(Card):
    point = models.CharField(max_length=5)
    pattern = models.CharField(max_length=10, choices=pattern_choices)
    color = 'red' if pattern == 'heart' or pattern == 'diamond' else 'black'
    length = models.IntegerField()
    effect = models.TextField()
    kind = 'equipcard'

    def __str__(self):
        return self.name

    def short_description(self):
        return "%s:%s\n%s:%s\n%s:%s\n" % (
            char_dict['pattern'], char_dict[self.pattern], char_dict['point'], self.point, char_dict['kind'], char_dict[self.kind], char_dict['length'], self.length,
        )

    def get_kind(self):
        return self.kind


# ShieldCard
class ShieldCard(Card):
    point = models.CharField(max_length=5)
    pattern = models.CharField(max_length=10, choices=pattern_choices)
    color = 'red' if pattern == 'heart' or pattern == 'diamond' else 'black'
    effect = models.TextField()
    kind = 'equipcard'

    def __str__(self):
        return self.name

    def short_description(self):
        return "%s:%s\n%s:%s\n%s:%s\n" % (
            char_dict['pattern'], char_dict[self.pattern], char_dict['point'], self.point, char_dict['kind'], char_dict[self.kind],
        )

    def get_kind(self):
        return self.kind


# MeasureCard
class MeasureCard(Card):
    point = models.CharField(max_length=5)
    pattern = models.CharField(max_length=10, choices=pattern_choices)
    color = 'red' if pattern == 'heart' or pattern == 'diamond' else 'black'
    effect = models.TextField()
    kind = 'equipcard'

    def __str__(self):
        return self.name

    def short_description(self):
        return "%s:%s\n%s:%s\n%s:%s\n" % (
            char_dict['pattern'], char_dict[self.pattern], char_dict['point'], self.point, char_dict['kind'], char_dict[self.kind],
        )

    def get_kind(self):
        return self.kind


# WisdomCard
class WisdomCard(Card):
    special = models.CharField(max_length=20, choices=wisdom_choices, default='immed')
    point = models.CharField(max_length=5)
    pattern = models.CharField(max_length=10, choices=pattern_choices)
    color = 'red' if pattern == 'heart' or pattern == 'diamond' else 'black'
    effect = models.TextField()
    kind = 'wisdomcard'

    def __str__(self):
        return self.name

    def short_description(self):
        return "%s:%s\n%s:%s\n%s:%s\n" % (
            char_dict['pattern'], char_dict[self.pattern], char_dict['point'], self.point, char_dict['kind'], char_dict[self.kind],
        )

    def get_kind(self):
        return self.kind


# ImmedWisdom
class ImmedWisdomCard(Card):
    wisdom = models.ForeignKey(WisdomCard, on_delete=models.CASCADE)
    kind = 'wisdomcard'
    special = 'immed'

    def short_description(self):
        return "%s:%s/%s\n" % (
            char_dict['kind'], char_dict[self.kind], char_dict[self.special],
        )


# DelayWisdom
class DelayWisdomCard(Card):
    wisdom = models.ForeignKey(WisdomCard, on_delete=models.CASCADE)
    kind = 'wisdomcard'
    special = 'delay'

    def short_description(self):
        return "%s:%s/%s\n" % (
            char_dict['kind'], char_dict[self.kind], char_dict[self.special],
        )


# RuseWisdom
class RuseWisdomCard(Card):
    wisdom = models.ForeignKey(WisdomCard, on_delete=models.CASCADE)
    kind = 'wisdomcard'
    special = 'ruse'
    hide = models.TextField()

    def short_description(self):
        return "%s:%s/%s\n" % (
            char_dict['kind'], char_dict[self.kind], char_dict[self.special],
        )


# PowerWisdom
class PowerWisdomCard(Card):
    wisdom = models.ForeignKey(WisdomCard, on_delete=models.CASCADE)
    kind = 'wisdomcard'
    special = 'power'
    country = models.CharField(max_length=10, choices=country_choices)

    def short_description(self):
        return "%s:%s/%s\n" % (
            char_dict['kind'], char_dict[self.kind], char_dict[self.special],
        )


# BadCard
class BadCard(Card):
    special = models.CharField(max_length=10)
    effect = models.TextField()
    kind = 'badcard'

    def __str__(self):
        return self.name + ' ' + self.speical

    def short_description(self):
        return "%s:%s\n" % (
            char_dict['kind'], char_dict[self.kind],
        )

    def get_kind(self):
        return self.kind
