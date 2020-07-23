from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('api/students', views.StudentView, 'students')
router.register('api/studentsGet', views.StudentGetView, 'studentsGet')
router.register('api/courses', views.CourseView, 'course')
router.register('api/coursesGet', views.CourseGetView, 'coursesGet')
router.register('api/staffs', views.StaffView, 'staff')
router.register('api/staffsGet', views.StaffGetView, 'staffsGet')
router.register('api/periods', views.PeriodView, 'period')

urlpatterns = router.urls
