from django.db import models
# from django.conf import settings
from movie import settings


def get_pwd(usr, pwd):
    import hashlib
    sha = hashlib.sha384()
    # for i in settings:
    #     print(i)
    salt = settings.__dict__["SALT"]
    sha.update(bytes(salt, encoding="utf-8"))
    sha.update(bytes(usr, encoding="utf-8"))
    sha.update(bytes(pwd, encoding="utf-8"))
    return sha.hexdigest()



# 创建用户
class User(models.Model):
    username = models.CharField(max_length=32, unique=True, verbose_name="用户名")
    nickname = models.CharField(max_length=100, verbose_name="昵称")
    password = models.CharField(max_length=100, verbose_name="密码")
    email = models.CharField(max_length=100, unique=True, verbose_name="邮箱")
    phone = models.CharField(max_length=20, unique=True, verbose_name="电话")
    info = models.TextField(verbose_name="描述", null=True, blank=True)
    face = models.CharField(max_length=100, unique=True, verbose_name="头像")
    addtime = models.DateField(auto_now_add=True, verbose_name="添加时间")
    uuid = models.CharField(max_length=100, unique=True, verbose_name="唯一标识符")


    def __str__(self):
        return self.nickname

    @classmethod
    def get_pwd(cls, usr, pwd):
        import hashlib
        sha = hashlib.sha384()
        # for i in settings:
        #     print(i)
        salt = settings.__dict__["SALT"]
        sha.update(bytes(salt, encoding="utf-8"))
        sha.update(bytes(usr, encoding="utf-8"))
        sha.update(bytes(pwd, encoding="utf-8"))
        return sha.hexdigest()

    def check_pwd(self, pwd):
        return self.password == get_pwd(self.username, pwd)

# 会员登录日志
class Userlog(models.Model):
    user = models.ForeignKey(verbose_name="所属会员", to="User")
    ip = models.CharField(max_length=20, verbose_name="登录IP")
    addtime = models.DateField(auto_now_add=True, verbose_name="登录时间")

    def __str__(self):
        return self.user.username

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="标签名")
    addtime = models.DateField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.name

# 电影
class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="电影名")
    url = models.CharField(max_length=255, unique=True, verbose_name="地址")
    info = models.TextField(verbose_name="简介")
    logo = models.CharField(max_length=255, unique=True, verbose_name="封面")
    star = models.IntegerField(verbose_name="星级")
    playnum = models.IntegerField(verbose_name="播放量")
    commentnum = models.IntegerField(verbose_name="评论量")
    tag = models.ForeignKey(verbose_name="所属标签", to="Tag")
    area = models.CharField(max_length=100, verbose_name="上映地区")
    release_time = models.DateField(verbose_name="上映时间", blank=True, null=True)
    lenght = models.CharField(max_length=15, verbose_name="播放时长")
    addtime = models.DateField(verbose_name="添加时间", auto_now_add=True)

    def __str__(self):
        return self.title


# 上映预告
class Preview(models.Model):
    title = models.CharField(max_length=100, verbose_name="电影名", unique=True)
    logo = models.CharField(max_length=100, verbose_name="封面", unique=True)
    addtime = models.DateField(verbose_name="添加时间", auto_now_add=True)

    def __str__(self):
        return self.title


# 评论
class Comment(models.Model):
    content = models.TextField(verbose_name="评论内容")
    movie = models.ForeignKey(verbose_name="电影名", to="Movie", null=True, blank=True)
    preview = models.ForeignKey(verbose_name="预告", to="Preview", null=True, blank=True)
    user = models.ForeignKey(verbose_name="用户", to="User")
    addtime = models.DateField(verbose_name="添加时间", auto_now_add=True)

    def __str__(self):
        return "%s%s" % (self.content[:20], "...")


# 电影收藏
class Moviecol(models.Model):
    movie = models.ForeignKey(verbose_name="电影名", to="Movie")
    user = models.ForeignKey(verbose_name="用户", to="User")
    addtime = models.DateField(verbose_name="添加时间", auto_now_add=True)

    def __str__(self):
        return self.movie.name


# 权限
class Auth(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="权限名")
    url = models.CharField(max_length=255, unique=True, verbose_name="地址")
    addtime = models.DateField(verbose_name="添加时间", auto_now_add=True)

    def __str__(self):
        return self.name


# 角色
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="名称")
    auths = models.CharField(max_length=600, verbose_name="权限列表")
    addtime = models.DateField(verbose_name="添加时间", auto_now_add=True)

    def __str__(self):
        return self.name


# 管理员
class Admin(models.Model):
    username = models.CharField(max_length=32, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    is_supper = models.BooleanField(verbose_name="超级管理员", default=False)
    role = models.ForeignKey(verbose_name="角色", to="Role", blank=True, null=True)
    addtime = models.DateField(verbose_name="添加时间", auto_now_add=True)

    def __str__(self):
        return self.username


# 登录日志
class Adminlog(models.Model):
    admin = models.ForeignKey(verbose_name="管理员", to="Admin")
    ip = models.CharField(max_length=20, verbose_name="登录IP")
    addtime = models.DateField(auto_now_add=True, verbose_name="登录时间")


# 操作日志
class Oplog(models.Model):
    admin = models.ForeignKey(verbose_name="管理员", to="Admin")
    ip = models.CharField(max_length=20, verbose_name="登录IP")
    reason = models.CharField(max_length=600, verbose_name="操作原因")
    addtime = models.DateField(auto_now_add=True, verbose_name="登录时间")


