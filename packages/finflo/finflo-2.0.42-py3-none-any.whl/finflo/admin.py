from django.contrib import admin

# Register your models here.
from .base_enum import Values
from .models import (Action, Flowmodel, Party, SignList, States,
                     TransitionManager, workevents, workflowitems)


@admin.action(description="Reset selected items")
def make_in_progress_to_false(modeladmin, request, queryset):
    workflowitems.objects.filter(
        transitionmanager=queryset.get().id, model_type=queryset.get().type
    ).update(
        action=Values.DRAFT,
        subaction=Values.DRAFT,
        initial_state=Values.DRAFT,
        interim_state=Values.DRAFT,
        final_state=Values.DRAFT,
        next_available_transitions=None,
    )
    queryset.update(in_progress=False, sub_sign=0)


class TransitionModeladmin(admin.ModelAdmin):
    search_fields = ["t_id", "type"]
    list_display = ("t_id", "type", "in_progress")
    actions = [make_in_progress_to_false]


class WorkflowItemModeladmin(admin.ModelAdmin):
    search_fields = ["transitionmanager__t_id", "interim_state", "model_type", "action"]
    list_display = ("id", "model_type", "action", "interim_state")


class WorkflowEventModeladmin(admin.ModelAdmin):
    search_fields = [
        "workflowitems__transitionmanager__t_id",
        "interim_state",
        "model_type",
        "action",
    ]
    list_display = ("id", "model_type", "action", "interim_state")


class CustomActionAdminModel(admin.ModelAdmin):
    list_display = ["description", "model", "stage_required"]

    def has_delete_permission(self, request, obj=None):
        return obj is None or obj.pk != 1


class customadminforsign(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Flowmodel)
admin.site.register(TransitionManager, TransitionModeladmin)
admin.site.register(Action, CustomActionAdminModel)
admin.site.register(States)
admin.site.register(Party)
admin.site.register(SignList, customadminforsign)
admin.site.register(workflowitems, WorkflowItemModeladmin)
admin.site.register(workevents, WorkflowEventModeladmin)
