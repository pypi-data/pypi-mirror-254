from mayan.apps.common.tests.mixins import ObjectCopyTestMixin
from mayan.apps.testing.tests.base import BaseTestCase

from .mixins.workflow_template_state_action_mixins import WorkflowTemplateStateActionTestMixin
from .mixins.workflow_template_transition_mixins import WorkflowTemplateTransitionTestMixin


class WorkflowTemplateCopyTestCase(
    ObjectCopyTestMixin, WorkflowTemplateStateActionTestMixin,
    WorkflowTemplateTransitionTestMixin, BaseTestCase
):
    auto_upload_test_document = False

    def setUp(self):
        super().setUp()
        self._create_test_workflow_template(add_test_document_type=True)
        self._create_test_workflow_template_state()
        self._create_test_workflow_template_state()
        self._create_test_workflow_template_transition()
        self._create_test_workflow_template_state_action()
        self._test_object = self._test_workflow_template
