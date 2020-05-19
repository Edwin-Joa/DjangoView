from django.db import models

# Create your models here.
class BookInfo(models.Model):
	btitle = models.CharField(max_length=64,verbose_name='书名')
	bup_data = models.DateField(verbose_name='发布时间')
	bread = models.IntegerField(default=0,verbose_name='阅览量')
	bcomment = models.IntegerField(default=0,verbose_name='评论量')
	is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

	class Meta():
		db_table = 'tb_bookinfo'


class HeroInfo(models.Model):
	gender = (
		(0,'男'),
		(1,'女'),
	)

	hbook_id = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='书籍编号')
	hname = models.CharField(max_length=64,verbose_name='英雄名字')
	hgender = models.SmallIntegerField(choices=gender,default=0,verbose_name='性别')
	hcomment = models.CharField(max_length=200,null=True,verbose_name='描述信息')
	is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

	class Meta():
		db_table = 'tb_heroinfo'




