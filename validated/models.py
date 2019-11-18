# -*- coding: utf-8 -*-

from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType
from django.db import models

from model_utils.models import TimeStampedModel


class TestMethod(models.Model):
    title = models.CharField(max_length=256)
    method_name = models.CharField(max_length=256)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)


class TestResult(TimeStampedModel):
    test_method = models.ForeignKey(TestMethod, on_delete=models.CASCADE)
    message = models.CharField(max_length=1024)
    passed = models.BooleanField(default=False)
    xfail = models.BooleanField(default=False, verbose_name="Supposed to fail")
    justification = models.CharField(blank=True, max_length=500)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    object = fields.GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ['test_method', 'object_id', 'content_type']

    @classmethod
    def get_test_results(cls, obj=None, qs=None):
        assert obj is not None or qs is not None  # Note "assert obj or qs" does not work
        ids = [obj.id] if obj else qs.values_list('id', flat=True)
        class_type = type(obj) if obj else qs.model
        ct = ContentType.objects.get(app_label=class_type._meta.app_label, model=class_type._meta.model_name)
        return cls.objects.filter(content_type=ct, object_id__in=ids)
