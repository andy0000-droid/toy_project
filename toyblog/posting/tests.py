'''from django.test import TestCase, Client
from django.urls import reverse
from .models import MyModel
from .forms import MyForm
from django.urls import resolve
from .views import my_view


class MyModelTestCase(TestCase):
    def SetUp(self):
        MyModel.obgect.creat(name="Test")
        
    def test_model_can_create_an_instance(self):
        instance=MyModel.obgect.get(name="Test")
        self.assertEqual(instance.name,"Test")
        
        
class MyModelViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.instance = MyModel.objects.create(name="Test")

    def test_view_can_retrieve_an_instance(self):
        """뷰는 인스턴스를 검색할 수 있습니다."""
        response = self.client.get(reverse('my_model_detail', args=[self.instance.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'].name, "Test")
        
class MyFormTestCase(TestCase):
    def test_form_validation(self):
        """폼은 데이터를 올바르게 유효성 검사합니다."""
        form = MyForm(data={'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

class URLsTestCase(TestCase):
    def test_url_resolves_to_correct_view(self):
        """URL은 올바른 뷰 함수로 해석됩니다."""
        resolver = resolve('/my-url/')
        self.assertEqual(resolver.func, my_view)
        
        
class TemplateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.instance = MyModel.objects.create(name="Test")

    def test_template_renders_correct_context_data(self):
        """템플릿은 올바른 컨텍스트 데이터를 렌더링합니다."""
        response = self.client.get(reverse('my_model_detail', args=[self.instance.id]))
        self.assertContains(response, "Test")
      '''  
        

# Create your tests here.
