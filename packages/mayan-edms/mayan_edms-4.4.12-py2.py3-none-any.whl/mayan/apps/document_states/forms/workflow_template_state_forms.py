import json

from django import forms
from django.db.models import Model
from django.db.models.query import QuerySet
from django.utils.module_loading import import_string
from django.utils.translation import ugettext_lazy as _

from mayan.apps.templating.fields import ModelTemplateField
from mayan.apps.views.forms import DynamicModelForm

from ..classes import WorkflowAction
from ..models import (
    WorkflowStateEscalation, WorkflowInstance, WorkflowState,
    WorkflowStateAction
)


class WorkflowTemplateStateActionDynamicForm(DynamicModelForm):
    class Meta:
        fields = ('label', 'when', 'enabled', 'condition', 'action_data')
        model = WorkflowStateAction
        widgets = {'action_data': forms.widgets.HiddenInput}

    def __init__(self, request, *args, **kwargs):
        self.action_path = kwargs.pop('action_path')
        self.request = request
        super().__init__(*args, **kwargs)
        if self.instance.action_data:
            for key, value in json.loads(s=self.instance.action_data).items():
                self.fields[key].initial = value

        self.fields['condition'] = ModelTemplateField(
            initial_help_text=self.fields['condition'].help_text,
            label=self.fields['condition'].label, model=WorkflowInstance,
            model_variable='workflow_instance', required=False
        )

    def clean(self):
        data = super().clean()

        # Consolidate the dynamic fields into a single JSON field called
        # 'action_data'.
        action_data = {}

        for field_name, field_data in self.schema['fields'].items():
            action_data[field_name] = data.pop(
                field_name, field_data.get('default', None)
            )
            if isinstance(action_data[field_name], QuerySet):
                # Flatten the queryset to a list of ids
                action_data[field_name] = list(
                    action_data[field_name].values_list('id', flat=True)
                )
            elif isinstance(action_data[field_name], Model):
                # Store only the ID of a model instance
                action_data[field_name] = action_data[field_name].pk

        data['action_data'] = action_data
        data = import_string(dotted_path=self.action_path).clean(
            form_data=data, request=self.request
        )
        data['action_data'] = json.dumps(obj=action_data)

        return data


class WorkflowTemplateStateActionSelectionForm(forms.Form):
    klass = forms.ChoiceField(
        choices=(), help_text=_('The action type for this action entry.'),
        label=_('Action'), widget=forms.Select(
            attrs={'class': 'select2'}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['klass'].choices = WorkflowAction.get_choices()


class WorkflowTemplateStateEscalationForm(forms.ModelForm):
    def __init__(self, workflow_template_state, *args, **kwargs):
        self.workflow_template_state = workflow_template_state
        super().__init__(*args, **kwargs)

        self.fields[
            'transition'
        ].queryset = self.workflow_template_state.workflow.transitions.filter(
            origin_state=self.workflow_template_state
        )

        self.fields['condition'] = ModelTemplateField(
            initial_help_text=self.fields['condition'].help_text,
            label=self.fields['condition'].label, model=WorkflowInstance,
            model_variable='workflow_instance', required=False
        )

    class Meta:
        fields = (
            'enabled', 'transition', 'priority', 'unit', 'amount',
            'condition'
        )
        model = WorkflowStateEscalation


class WorkflowTemplateStateForm(forms.ModelForm):
    class Meta:
        fields = ('initial', 'label', 'completion')
        model = WorkflowState
