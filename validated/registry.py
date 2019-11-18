import inspect
from collections import defaultdict

from django.apps import apps

model_tests = defaultdict(list)


class Test(object):
    def __init__(self, method, test_method, cls):
        self.test_method = test_method
        self.method = method
        self.cls = cls


for cls in apps.get_models():
    for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
        if hasattr(method, 'is_model_test') and method.is_model_test:
            model_tests[cls].append(
                Test(method, method.test_method, cls))


# Used as a decorator
def test_method(title=None, queryset=None, is_class_method=False):
    def test_method_inner(method):
        method.is_model_test = True
        method.is_class_method = is_class_method
        method.queryset = queryset
        method.model_test_title = title
        return method

    return test_method_inner


def test_class_method(title=None):
    return test_method(title, is_class_method=True)
