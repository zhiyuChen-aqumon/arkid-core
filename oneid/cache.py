from django.core.cache import cache as django_cache


class Cache():
    def get(self, name):
        res = django_cache.get(name)

        if name == "oneid:constant:node:g_extern:id" and res is None:
            from oneid_meta.models import Group
            extern = Group.valid_objects.filter(uid='extern').first()
            if extern:
                django_cache.set('oneid:constant:node:g_extern:id', extern.id)
                return extern.id
        return res

    def __getattr__(self, name):
        return getattr(django_cache, name)

    def __setattr__(self, name, value):
        return setattr(django_cache, name, value)

    def __delattr__(self, name):
        return delattr(django_cache, name)

    def __contains__(self, key):
        return key in django_cache

    def __eq__(self, other):
        return django_cache == other


cache = Cache()
