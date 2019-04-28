from django.db import models
from pytz import timezone  # 현지 시각 출력을 위하여
from django.conf import settings
from django.urls import reverse

def local_time(input_time):
    fmt = '%Y-%m-%d %H:%M'
    my_zone = timezone(settings.TIME_ZONE)
    my_local_time = input_time.astimezone(my_zone)
    return my_local_time.strftime(fmt)

class Item(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # 'auth.User'라고 쓰는 것보다 강추
        on_delete=models.CASCADE,
        # related_name='post_set',  # 기본 설정과 동일하므로 주석 처리
        related_name='items',
        verbose_name='글쓴이',
    )
    name = models.CharField(max_length=20)
    desc = models.TextField(blank=True)
    photo = models.ImageField()  # blank=True 지정하지 않은 경우
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags')

    def __str__(self):
        return self.name

    def updated(self):
        return local_time(self.updated_at)
    updated.short_description='수정 일시'

    def get_absolute_url(self):
        # return reverse('blog:post_detail', args=[self.pk])
        return reverse('shop:item_detail', kwargs={'pk': self.pk})

    def tagged(self):
        ts = self.tags.all()
        # return ', '.join(ts)      # 에러!!
        return '{' + ', '.join(map(str, ts)) + '}'

        # if ts:
        #     tag_string = '{'
        #     for t in ts:  # M2M 속성은 관리자이지, 쿼리셋이 아님
        #         tag_string += t.name + ', '  # t가 아니라 t.name
        #     tag_string = tag_string[:len(tag_string)-2] + '}'
        #     # tag_string 후미 ', '를 '}'으로 치환
        # else:
        #     tag_string = '{ }'
        # return tag_string
    tagged.short_description = '태그 집합'
    # 클래스 메소드로 속성을 대신할 때, verbose_name 대신에 short_description



class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='reviews', verbose_name='아이템')
    review = models.TextField('후기')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['item__id', '-id']  # '-post__id', '-id'

    def __str__(self):
        return self.review

    def updated(self):
        return local_time(self.updated_at)
    updated.short_description = '수정 일시'


class Tag(models.Model):
    name = models.CharField('태그', max_length=100, unique=True)

    class Meta:
        ordering = ['-id']  # Tag 객체의 기본 정렬 순서 지정

    def __str__(self):
        return self.name

