from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from validated.models import TestResult


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('test_method', 'object_link', 'details', 'passed', 'xfail', 'justification')
    list_filter = ('passed', 'xfail', 'test_method', ('content_type', admin.RelatedOnlyFieldListFilter))
    list_editable = ('xfail', 'justification')
    list_per_page = 20
    readonly_fields = ['test_method', 'details', 'object_link', 'passed']
    fields = readonly_fields + ['xfail', 'justification']

    def details(self, obj):
        return obj.message

    details.allow_tags = True

    def object_link(self, obj):
        return obj.object_admin_hyperlink(str(obj.object))

    object_link.allow_tags = True


class ValidatedAdminMixin():
    def run_tests(self, request, obj):
        TestResult.rerun_tests_for_object(obj)
        obj.refresh_from_db()
        test_results = TestResult.test_results_for_object(obj)
        failing = test_results.filter(passed=False, xfail=False)
        if failing.exists():
            report = '<br>'.join([f.test_result_admin_hyperlink(text=f.message) for f in failing])
            self.message_user(request,
                              mark_safe("Object saved successfully the following tests are failing: <br>%s" % report),
                              messages.WARNING)

    def response_add(self, request, obj, post_url_continue=None):
        self.run_tests(request, obj)
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        self.run_tests(request, obj)
        return super().response_change(request, obj)
