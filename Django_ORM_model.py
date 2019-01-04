# 转自  https://blog.csdn.net/qq_23934063/article/details/73293355 

# http://www.cnblogs.com/vamei/p/6602025.html

from django.db.models import Q,F
from user.models import Users
# 数据基础操作包括增删查改，常用的过滤属性，Q,F库的使用，外键的反向查询 _set()
class Users(models.Model):
    nickname = models.CharField('昵称', max_length=256, null=True)
    head_portrait = models.CharField('头像', max_length=256, null=True)
    appkey = models.CharField('appkey', max_length=256, null=True)
    status = models.CharField('状态', max_length=1, choices=STATUS_CHOICES, default='e')
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    update_date = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey('auth.user', verbose_name='用户',
                             null=True,
                             on_delete=models.SET_NULL)
class Branch(models.Model):
    name = models.CharField('公司名称', max_length=128, null=True)
    code = models.CharField('公司编码', max_length=64, null=True)
    logo = models.CharField('公司logo', max_length=256, null=True)
    invitation_code = models.CharField('邀请码', max_length=128, null=True)
    website = models.CharField('公司网站', max_length=128, null=True)
    address = models.CharField('地址', max_length=128, null=True)
    telephone = models.CharField('公司联系电话', max_length=32, null=True)
    introduction = models.TextField('公司简介', null=True)
    status = models.CharField('状态', max_length=1, choices=STATUS_CHOICES, default='e')
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    update_date = models.DateTimeField('更新时间', auto_now=True)
    users = models.ManyToManyField('Users',
                                    verbose_name='昵称',
                                    null=True,
                                    blank=True)
# 增加 save
users = Users(
user_account=user_account,
org_id=org
)
users.save()
# 删除 delete
Users.objects.filter(id=user_id).delete()
 
# 修改 update
Users.objects.filter(id=user_id).update(
user_account=user_account,
org_id=org
)

# 查询
# filter在没取到数据时返回空数组list，不会抛异常
# get在没取到数据 或 取到的数据有多条时，抛出异常

# 检索记录 get
# get获取单个符合条件的记录,没找到或者超过一个都会抛出异常
user = Users.objects.get(id=10)
 
# 检索所有的记录 all
user = Users.objects.all()
#取前5个
Users.objects.all()[:5]
#取第五个到第十个
Users.objects.all()[5:10]
 
# 检索第一条记录 first
user = Users.objects.first()
 
# 检索记录条数 count
user = Users.objects.count()
 
# 检索记录排序 order_by
user = Users.objects.order_by(‘id’)
user = Users.objects.order_by(‘id’)[0:1]
# 如果需要逆序 在字段前加负号 例 （‘-id’）
 
# 检索记录特定字段 values
user = Users.objects.values('id', 'nickname').all()
# 返回 指定字段的数据列表
# 这里也可以指定外键字段 使用双下划线指定，返回的键值与values中的参数一致
 
# 检索记录特定字段 values
user = Users.objects.values_list('id', flat=True).all()
# 返回 id 列表
# 这里也可以指定外键字段 使用双下划线指定，返回的键值与values中的参数一致
 
# 条件查询exclude
# 和filter相反,查找不符合条件的那些记录
 
# 条件查询 filter
 
# 或条件查询
user = Users.objects.filter(Q(nickname='qxt_common') | Q(nickname=u'系统管理员')).all()
 
# 非条件查询
user = Users.objects.filter(~Q(nickname='administrator')).all()
user = Users.objects.exclude(nickname='administrator').all()
# 字段名加关键字 例：filter(id__gt='10') # id 大于10
'''
常用的过滤属性
__exact        精确等于 like 'aaa'
__iexact    精确等于 忽略大小写 ilike 'aaa'
__contains    包含 like '%aaa%'
__icontains    包含 忽略大小写 ilike '%aaa%'，但是对于sqlite来说，contains的作用效果等同于icontains。
__gt    大于
__gte    大于等于
__lt    小于
__lte    小于等于
__in     存在于一个list范围内
__startswith   以...开头
__istartswith   以...开头 忽略大小写
__endswith     以...结尾
__iendswith    以...结尾，忽略大小写
__range    在...范围内
__year       日期字段的年份
__month    日期字段的月份
__day        日期字段的日
__isnull=True/False
__isnull=True 与 __exact=None的区别
'''

# Q
# 或 条件查询
user = Users.objects.filter(Q(nickname='qxt_common') | Q(nickname=u'系统管理员')).all()
# 非条件查询
user = Users.objects.filter(~Q(nickname='administrator')).all()
 
# F
# 例如我们有个统计点击量的字段，每次更新的操作其实就是把字段的值加1.
# 一般我们的做法是把这条记录取出来，把相应字段加+1，然后在save:
articles = Article.objects.filter(id=self.product_id).first()
articles.likes += 1
articles.save()
# 使用 F 改写：
Article.objects.filter(id=self.product_id).update(likes=F('likes') + 1)
 
# 外键反向查询
# 一对多外键，多对多外键反向查询方法一致
users = Users.objects.all()
users.branch_set.all()   # 反查
 
branchs = Branch.objects.all()
branchs.users.all()		# 正查
# 一对多外键绑定
# 可使用 外键对象，也可以使用外键id直接绑定
# 多对多外键绑定
branchs.users.add(users_obj)
branchs.users.add(users_id)
# 多对多外键删除
branchs.users.remove(users_obj)
branchs.users.remove(users_id)
# 多对多删除所有外键
branchs.users.clear()
# 批量插入
users_list = []
users_list.append(Users(nickname='11'))
users_list.append(Users(nickname='22'))
users_list.append(Users(nickname='33'))
Users.objects.bulk_create(users_list)
distinct 去重
