from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

#lists是单元测 functional_test是功能测
# # 冒烟测试
# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)

class HomePageTest(TestCase):

    # def test_root_utl_resolve_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func,home_page)
    #
    # def test_home_page_returns_correct_html(self):
    #     response = self.client.get('/')
    #
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title',html)
    #     self.assertTrue(html.strip().endswith('</html>'))
    #     self.assertTemplateUsed(response,'home.html')
    #
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/',data={'item_text':'A new list item'})
        self.assertIn('A new list item',response.content.decode())
        self.assertTemplateUsed(response,'home.html')
# Create your tests here.
