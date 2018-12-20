from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import CourseOrg, CityDict
from .forms import UserAskForm
from courses.models import Course
from operation.models import UserFavorite

# Create your views here.


class OrgView(View):
    def get(self, request):
        """
        课程机构列表功能
        :param request:
        :return:
        """

        # 课程机构
        all_orgs = CourseOrg.objects.all()

        # 课程机构按照点击量排名
        hot_orgs = all_orgs.order_by("-click_nums")[:3]  # -倒序排列  # 取前三

        # 城市
        all_citys = CityDict.objects.all()

        # 取出筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 排序
        sort = request.GET.get("sort", "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")

        # 统计
        org_nums = all_orgs.count()

        # 取出页码 page
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 分页
        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(all_orgs, 5, request=request)

        orgs = p.page(page)

        #



        return render(request, 'org-list.html', {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            "city_id": city_id,
            "category": category,
            "hot_orgs":hot_orgs,
            "sort": sort,
        })


class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)  # ModelForm 可以选择直接保存到数据库
            return HttpResponse('{"status": "success"}', content_type='application/json')  # 返回json
        else:
            # return HttpResponse('{"status": "fail", "msg": {0}}'.format(userask_form.errors), content_type='application/json')  # 返回json
            return HttpResponse('{"status": "fail", "msg": "添加出错"}', content_type='application/json')  # 返回json  # json数据里面的引号要用双引号！！！


class OrgHomeView(View):
    """
    课程机构首页
    """

    def get(self, request, org_id):
        current_page = "home"
        course_org = CourseOrg.objects.get(id=int(org_id))

        # 用户是否收藏了该课程机构
        has_fav = False
        if request.user.is_authenticated():  # 如果用户登录了
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        # MxOnline\templates\org_base.html
        #                  {% if has_fav %}已收藏{% else %}收藏{% endif %}

        # all_courses = course_org.course_set.all()[:3]  # 取出所有以 course_org 为外键的 Course  # [models下的class名]_set  # 取3个
        all_courses = course_org.course_set.all()  # 取出所有以 course_org 为外键的 Course  # [models下的class名]_set
        all_teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-homepage.html', {
            "all_courses": all_courses,
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,

        })


class OrgCourseView(View):
    """
    课程机构课程列表页
    """

    def get(self, request, org_id):
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))

        # 用户是否收藏了该课程机构
        has_fav = False
        if request.user.is_authenticated():  # 如果用户登录了
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()  # 取出所有以 course_org 为外键的 Course  # [models下的class名]_set
        return render(request, 'org-detail-course.html', {
            "all_courses": all_courses,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,

        })


class OrgDescView(View):
    """
    课程机构机构介绍页
    """

    def get(self, request, org_id):
        current_page = "desc"
        course_org = CourseOrg.objects.get(id=int(org_id))

        # 用户是否收藏了该课程机构
        has_fav = False
        if request.user.is_authenticated():  # 如果用户登录了
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        return render(request, 'org-detail-desc.html', {
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,

        })


class OrgTeacherView(View):
    """
    课程机构教师列表页
    """

    def get(self, request, org_id):
        current_page = "teacher"
        course_org = CourseOrg.objects.get(id=int(org_id))

        # 用户是否收藏了该课程机构
        has_fav = False
        if request.user.is_authenticated():  # 如果用户登录了
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,

        })


class AddFavView(View):
    """
    用户收藏，用户取消收藏
    """
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():  # 如果用户未登录
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type='application/json')  # 返回json  # json数据里面的引号要用双引号！！！
            # 这里只回传json数据，跳转到登录页面由ajax完成

        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:  # 如果记录已经存在，说明用户是要取消收藏
            exist_records.delete()
            return HttpResponse('{"status": "success", "msg": "收藏"}', content_type='application/json')  # 返回json  # json数据里面的引号要用双引号！！！
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status": "success", "msg": "已收藏"}', content_type='application/json')  # 返回json  # json数据里面的引号要用双引号！！！
            else:
                return HttpResponse('{"status": "fail", "msg": "收藏失败"}', content_type='application/json')  # 返回json  # json数据里面的引号要用双引号！！！

