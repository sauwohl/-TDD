from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
#一个是单元测 一个是功能测
# # 冒烟测试
# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)

class HomePageTest(TestCase):

    def test_root_utl_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

# Create your tests here.
