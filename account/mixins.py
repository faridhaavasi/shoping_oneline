from django.contrib.auth.mixins import UserPassesTestMixin



#mixin
class IsAdminRequiredMixin(UserPassesTestMixin):
    '''
    user is admin and is_authenticated
    '''
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin


