from django.contrib.admin.sites import AdminSite
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase
from django.test import RequestFactory


class MockSuperUser:
    def has_perm(self, perm):
        return True
    
class TestAdminPage:
    def test_admin_page(self):
        request = RequestFactory().get('/admin/')
        request.user = MockSuperUser()
        request.session = 'session'
        request._messages = FallbackStorage(request)
        admin_site = AdminSite()
        response = admin_site.index(request)
        assert response.status_code == 200
        assert response.template_name == 'admin/index.html'
        assert response.context_data['site_title'] == 'Django administration'
        assert response.context_data['site_header'] == 'Django administration'
        assert response.context_data['title'] == 'Site administration'
        assert response.context_data['site_url'] == '/admin/'
        assert response.context_data['has_permission'] == True
        assert response.context_data['available_apps'] == []
        assert response.context_data['recent_actions'] == []
        assert response.context_data['is_popup'] == False
        assert response.context_data['to_field'] == None
        assert response.context_data['media'] == {
            'js': [
                '/static/admin/js/core.js',
                '/static/admin/js/vendor/jquery/jquery.min.js',
                '/static/admin/js/jquery.init.js',
                '/static/admin/js/vendor/xregexp/xregexp.min.js',
                '/static/admin/js/vendor/SelectFilter2.js',
            ],
            'css': {
                'all': [
                    '/static/admin/css/base.css',
                    '/static/admin/css/base.css',
                    '/static/admin/css/dashboard.css',
                    '/static/admin/css/responsive.css',
                    '/static/admin/css/fonts.css',
                    '/static/admin/css/vendor/font-awesome/css/font-awesome.min.css',
                ]
            }
        }
        assert response.context_data['app_list'] == []
        assert response.context_data['site'] == admin_site
        assert response.context_data['cl'] == None
        assert response.context_data['media'] == {
            'js': [
                '/static/admin/js/core.js',
                '/static/admin/js/vendor/jquery/jquery.min.js',
                '/static/admin/js/jquery.init.js',
                '/static/admin/js/vendor/xregexp/xregexp.min.js',
                '/static/admin/js/vendor/SelectFilter2.js',
            ],
            'css': {
                'all': [
                    '/static/admin/css/base.css',
                    '/static/admin/css/base.css',
                    '/static/admin/css/dashboard.css',
                    '/static/admin/css/responsive.css',
                    '/static/admin/css/fonts.css',
                    '/static/admin/css/vendor/font-awesome/css/font-awesome.min',
                ]
            }
        }