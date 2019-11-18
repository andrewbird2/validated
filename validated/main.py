from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

from validated.models import TestResult
from validated.registry import model_tests


def get_test_results(obj):
    return obj.test_results()


def run_test(obj, test):
    method = test.method

    try:
        result = obj.test_results().get(method_name=method.__name__)
    except ObjectDoesNotExist:
        result = TestResult(testing=obj, method_name=method.__name__)
    result.title = test.title

    try:
        if test.method.is_class_method:
            qs_failing, message = test.method(test.cls)
            if obj in qs_failing:
                method_result = False, message
            else:
                method_result = True
        else:
            method_result = method(obj)
    except Exception as e:
        method_result = False, "Test failed to run correctly!!! " + str(e)
    try:
        passed, message = method_result
        result.passed = passed
        result.message = message[0:500]
    except TypeError:
        if method_result:
            result.passed = True
            result.message = test.success
        else:
            result.passed = False
            result.message = test.failure
    result.method_name = method.__name__
    result.save()
