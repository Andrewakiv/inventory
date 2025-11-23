import django_filters


class MaterialFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='by_name_filter')

    def by_name_filter(self, queryset, name, value):
        if value:
            value = value.strip()
            return queryset.filter(name__icontains=value)
        else:
            return queryset.none()
