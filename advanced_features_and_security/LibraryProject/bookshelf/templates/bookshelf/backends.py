from django.contrib.auth.backends import BaseBackend
from django.db.models import Q
from django.contrib.auth import get_user_model


class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()   # <— moved inside function
        try:
            user = UserModel.objects.get(
                Q(email__iexact=username) | Q(username__iexact=username)
            )
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()   # safe call here too
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None