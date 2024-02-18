import json

from django.db.models import Q

from ...models.workflow_state_action_models import WorkflowStateAction

from ..literals import (
    DOCUMENT_WORKFLOW_LAUNCH_ACTION_CLASS_PATH,
    TEST_WORKFLOW_TEMPLATE_STATE_ACTION_GENERIC_DOTTED_PATH,
    TEST_WORKFLOW_TEMPLATE_STATE_ACTION_LABEL,
    TEST_WORKFLOW_TEMPLATE_STATE_ACTION_LABEL_EDITED,
    TEST_WORKFLOW_TEMPLATE_STATE_ACTION_DOTTED_PATH,
    TEST_WORKFLOW_TEMPLATE_STATE_ACTION_WHEN
)
from ..workflow_actions import TestWorkflowAction

from .workflow_template_state_mixins import WorkflowTemplateStateTestMixin


class WorkflowTemplateStateActionTestMixin(WorkflowTemplateStateTestMixin):
    TestWorkflowAction = TestWorkflowAction
    _test_workflow_template_state_action_path = TEST_WORKFLOW_TEMPLATE_STATE_ACTION_GENERIC_DOTTED_PATH

    def setUp(self):
        super().setUp()
        self._test_workflow_template_state_actions = []

    def _create_test_workflow_template_state_action(
        self, extra_backend_data=None, extra_data=None,
        workflow_state_index=0
    ):
        total_test_workflow_template_state_actions = len(
            self._test_workflow_template_state_actions
        )
        label = '{}_{}'.format(
            TEST_WORKFLOW_TEMPLATE_STATE_ACTION_LABEL,
            total_test_workflow_template_state_actions
        )

        backend_data = {}

        if extra_backend_data:
            backend_data.update(**extra_backend_data)

        data = {
            'action_data': json.dumps(obj=backend_data),
            'action_path': self._test_workflow_template_state_action_path,
            'label': label
        }

        if extra_data:
            data.update(extra_data)

        self._test_workflow_template_state_action = self._test_workflow_template_states[
            workflow_state_index
        ].actions.create(**data)

        self._test_workflow_template_state_actions.append(
            self._test_workflow_template_state_action
        )


class WorkflowTemplateStateActionAPIViewTestMixin(
    WorkflowTemplateStateActionTestMixin
):
    def _request_test_workflow_template_state_action_create_api_view(self):
        pk_list = list(
            WorkflowStateAction.objects.values_list('pk', flat=True)
        )

        total_test_workflow_template_state_actions = len(
            self._test_workflow_template_state_actions
        )
        label = '{}_{}'.format(
            TEST_WORKFLOW_TEMPLATE_STATE_ACTION_LABEL,
            total_test_workflow_template_state_actions
        )

        data = {
            'label': label,
            'action_path': self._test_workflow_template_state_action_path
        }

        response = self.post(
            viewname='rest_api:workflow-template-state-action-list',
            kwargs={
                'workflow_template_id': self._test_workflow_template.pk,
                'workflow_template_state_id': self._test_workflow_template_state.pk
            }, data=data
        )

        try:
            self._test_workflow_template_state_action = WorkflowStateAction.objects.get(
                ~Q(pk__in=pk_list)
            )
        except WorkflowStateAction.DoesNotExist:
            self._test_workflow_template_state_action = None

        return response

    def _request_test_workflow_template_state_action_delete_api_view(self):
        return self.delete(
            viewname='rest_api:workflow-template-state-action-detail',
            kwargs={
                'workflow_template_id': self._test_workflow_template.pk,
                'workflow_template_state_id': self._test_workflow_template_state.pk,
                'workflow_template_state_action_id': self._test_workflow_template_state_action.pk
            }
        )

    def _request_test_workflow_template_state_action_detail_api_view(self):
        return self.get(
            viewname='rest_api:workflow-template-state-action-detail',
            kwargs={
                'workflow_template_id': self._test_workflow_template.pk,
                'workflow_template_state_id': self._test_workflow_template_state.pk,
                'workflow_template_state_action_id': self._test_workflow_template_state_action.pk
            }
        )

    def _request_test_workflow_template_state_action_list_api_view(self):
        return self.get(
            viewname='rest_api:workflow-template-state-action-list', kwargs={
                'workflow_template_id': self._test_workflow_template.pk,
                'workflow_template_state_id': self._test_workflow_template_state.pk
            }
        )

    def _request_test_workflow_template_state_action_edit_patch_api_view(self):
        return self.patch(
            viewname='rest_api:workflow-template-state-action-detail',
            kwargs={
                'workflow_template_id': self._test_workflow_template.pk,
                'workflow_template_state_id': self._test_workflow_template_state.pk,
                'workflow_template_state_action_id': self._test_workflow_template_state_action.pk
            }, data={
                'label': TEST_WORKFLOW_TEMPLATE_STATE_ACTION_LABEL_EDITED
            }
        )

    def _request_test_workflow_template_state_action_edit_put_api_view(self):
        return self.put(
            viewname='rest_api:workflow-template-state-action-detail',
            kwargs={
                'workflow_template_id': self._test_workflow_template.pk,
                'workflow_template_state_id': self._test_workflow_template_state.pk,
                'workflow_template_state_action_id': self._test_workflow_template_state_action.pk
            }, data={
                'label': TEST_WORKFLOW_TEMPLATE_STATE_ACTION_LABEL_EDITED,
                'action_path': self._test_workflow_template_state_action_path
            }
        )


class WorkflowTemplateStateActionLaunchViewTestMixin(
    WorkflowTemplateStateActionTestMixin
):
    def _request_document_workflow_template_launch_action_create_view(self):
        return self.post(
            viewname='document_states:workflow_template_state_action_create',
            kwargs={
                'workflow_template_state_id': self._test_workflow_template_state.pk,
                'class_path': DOCUMENT_WORKFLOW_LAUNCH_ACTION_CLASS_PATH
            }, data={
                'enabled': True,
                'label': TEST_WORKFLOW_TEMPLATE_STATE_ACTION_LABEL,
                'when': TEST_WORKFLOW_TEMPLATE_STATE_ACTION_WHEN,
                'workflows': self._test_workflow_templates[0].pk
            }
        )


class WorkflowTemplateStateActionViewTestMixin(
    WorkflowTemplateStateActionTestMixin
):
    def _request_test_workflow_template_state_action_create_get_view(self, class_path):
        return self.get(
            viewname='document_states:workflow_template_state_action_create',
            kwargs={
                'workflow_template_state_id': self._test_workflow_template_state.pk,
                'class_path': class_path
            }
        )

    def _request_test_workflow_template_state_action_create_post_view(
        self, class_path, extra_data=None
    ):
        data = {
            'label': TEST_WORKFLOW_TEMPLATE_STATE_ACTION_LABEL,
            'when': TEST_WORKFLOW_TEMPLATE_STATE_ACTION_WHEN
        }
        if extra_data:
            data.update(extra_data)

        pk_list = list(
            WorkflowStateAction.objects.values_list('pk', flat=True)
        )

        response = self.post(
            viewname='document_states:workflow_template_state_action_create',
            kwargs={
                'workflow_template_state_id': self._test_workflow_template_state.pk,
                'class_path': class_path
            }, data=data
        )

        try:
            self._test_workflow_template_state_action = WorkflowStateAction.objects.get(
                ~Q(pk__in=pk_list)
            )
        except WorkflowStateAction.DoesNotExist:
            self._test_workflow_template_state_action = None

        return response

    def _request_test_workflow_template_state_action_delete_view(self):
        return self.post(
            viewname='document_states:workflow_template_state_action_delete',
            kwargs={
                'workflow_template_state_action_id': self._test_workflow_template_state_action.pk
            }
        )

    def _request_test_workflow_template_state_action_edit_get_view(self):
        return self.get(
            viewname='document_states:workflow_template_state_action_edit',
            kwargs={
                'workflow_template_state_action_id': self._test_workflow_template_state_action.pk
            }
        )

    def _request_test_workflow_template_state_action_edit_post_view(
        self, extra_data=None
    ):
        data = {
            'label': TEST_WORKFLOW_TEMPLATE_STATE_ACTION_LABEL_EDITED,
            'when': self._test_workflow_template_state_action.when
        }

        if extra_data:
            data.update(**extra_data)

        return self.post(
            viewname='document_states:workflow_template_state_action_edit',
            kwargs={
                'workflow_template_state_action_id': self._test_workflow_template_state_action.pk
            }, data=data
        )

    def _request_test_workflow_template_state_action_list_view(self):
        return self.get(
            viewname='document_states:workflow_template_state_action_list',
            kwargs={
                'workflow_template_state_id': self._test_workflow_template_state.pk
            }
        )

    def _request_test_workflow_template_state_action_selection_view(self):
        return self.post(
            viewname='document_states:workflow_template_state_action_selection',
            kwargs={
                'workflow_template_state_id': self._test_workflow_template_state.pk
            }, data={
                'klass': TEST_WORKFLOW_TEMPLATE_STATE_ACTION_DOTTED_PATH
            }
        )
