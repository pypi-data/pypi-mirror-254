from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View


User = get_user_model()


class RedirectMixin:
    redirect = None

    def get_redirect(self, *args, permanent=False, **kwargs):
        if self.redirect is None:
            raise ImproperlyConfigured(
                'RedirectMixin must define `.redirect` or implement `.get_redirect()`'
            )
        return redirect(self.redirect, *args, permanent, **kwargs)


class FormResponseMixin(TemplateResponseMixin, ContextMixin):
    error = None

    fields = None

    def get_error(self):
        if self.error is None:
            raise ImproperlyConfigured(
                'FormResponseMixin must define `.error` or implement `.get_error()`'
            )
        return self.error

    def get_fields(self):
        if self.fields is None:
            raise ImproperlyConfigured(
                'FormResponseMixin must define `.fields` or implement `.get_fields()`'
            )
        return {
            field: self.request.POST[field]
            for field in self.fields
            if field in self.request.POST
        }
    
    def get_error_response(self, **kwargs):
        context = self.get_context_data(**kwargs)
        context['error'] = self.get_error()
        return self.render_to_response(context)
    

class TemplateView(TemplateResponseMixin, ContextMixin, View):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    

class FormTemplateView(FormResponseMixin, RedirectMixin, View):
    redirect = '/'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class LoginView(FormTemplateView):
    error = f'Incorrect {User.USERNAME_FIELD} or password.'

    fields = [
        User.USERNAME_FIELD,
        'password',
    ]

    redirect = '/'
    
    def post(self, request, *args, **kwargs):
        fields = self.get_fields()
        user = authenticate(**fields)
        if user is not None:
            login(request, user)
            return self.get_redirect()
        return self.get_error_response(**kwargs)


class LogoutView(RedirectMixin, View):
    redirect = '/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return self.get_redirect()


class RegisterView(FormTemplateView):
    error = f'User with {User.USERNAME_FIELD} already exists.'

    fields = [
        User.USERNAME_FIELD,
        'password',
    ]

    redirect = '/'

    def post(self, request, *args, **kwargs):
        fields = self.get_fields()
        try:
            User.objects.get(**{User.USERNAME_FIELD: fields[User.USERNAME_FIELD]})
            return self.get_error_response()
        except User.DoesNotExist:
            User.objects.create_user(**fields)
            user = authenticate(**{User.USERNAME_FIELD: fields[User.USERNAME_FIELD], 'password': fields['password']})
            login(request, user)
            return self.get_redirect()
