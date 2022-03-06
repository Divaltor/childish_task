from django.db.models import Q, QuerySet
from django_filters import filters, FilterSet
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from base.models import User
from base.serializers.user import UserSerializer


class UserFilterSet(FilterSet):
    phone = filters.CharFilter(field_name='phone_number', lookup_expr='contains')
    search = filters.CharFilter(method='multi_search')

    class Meta:
        model = User
        fields = ['phone']

    # noinspection PyMethodMayBeStatic
    def multi_search(self, queryset: QuerySet[User], name: str, value: str) -> QuerySet[User]:
        """Search in queryset by `email` and `username` fields."""
        return queryset.filter(
            Q(email__icontains=value) | Q(username__icontains=value)
        )


class UserCRUDPermission(DjangoModelPermissions):

    def has_permission(self, request, view) -> bool:
        if request.method == 'POST':
            return True

        return super().has_permission(request, view)


class UserCRUDView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filterset_class = UserFilterSet
    permission_classes = [UserCRUDPermission]

    def get_queryset(self) -> QuerySet[User]:
        queryset = super().get_queryset()

        return queryset.only(
            'phone_number',
            'deactivated_date',
            'email',
            'username',
            'first_name',
            'last_name',
            'is_active'
        )
