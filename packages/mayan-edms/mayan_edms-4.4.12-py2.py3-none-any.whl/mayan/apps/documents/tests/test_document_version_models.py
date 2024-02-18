from ..document_file_actions import (
    DocumentFileActionAppendNewPages, DocumentFileActionNothing,
    DocumentFileActionUseNewPages
)
from ..events import event_document_version_edited

from .base import GenericDocumentTestCase
from .mixins.document_file_mixins import DocumentFileTestMixin
from .mixins.document_version_mixins import DocumentVersionTestMixin


class DocumentVersionTestCase(
    DocumentFileTestMixin, GenericDocumentTestCase
):
    def test_version_new_file_new_pages(self):
        test_document_version_page_content_objects = self._test_document_version.page_content_objects

        self.assertEqual(self._test_document.versions.count(), 1)

        self._upload_test_document_file(
            action=DocumentFileActionUseNewPages.backend_id
        )

        self.assertEqual(self._test_document.versions.count(), 2)

        self.assertNotEqual(
            self._test_document_version.page_content_objects,
            test_document_version_page_content_objects
        )
        self.assertEqual(
            self._test_document_version.page_content_objects,
            list(self._test_document.file_latest.pages.all())
        )

    def test_version_new_version_keep_pages(self):
        test_document_version_page_content_objects = self._test_document_version.page_content_objects

        self.assertEqual(self._test_document.versions.count(), 1)

        self._upload_test_document_file(
            action=DocumentFileActionNothing.backend_id
        )

        self.assertEqual(self._test_document.versions.count(), 1)

        self.assertEqual(
            self._test_document_version.page_content_objects,
            test_document_version_page_content_objects
        )
        self.assertNotEqual(
            self._test_document_version.page_content_objects,
            list(self._test_document.file_latest.pages.all())
        )

    def test_version_new_file_append_pages(self):
        test_document_version_page_content_objects = self._test_document_version.page_content_objects

        self.assertEqual(self._test_document.versions.count(), 1)
        self.assertEqual(self._test_document.files.count(), 1)

        self._upload_test_document_file(
            action=DocumentFileActionAppendNewPages.backend_id
        )

        self.assertEqual(self._test_document.files.count(), 2)
        self.assertEqual(self._test_document.versions.count(), 2)

        test_document_version_expected_page_content_objects = list(
            self._test_document.files.first().pages.all()
        )
        test_document_version_expected_page_content_objects.extend(
            list(
                self._test_document.files.last().pages.all()
            )
        )

        self.assertNotEqual(
            self._test_document_version.page_content_objects,
            test_document_version_page_content_objects
        )
        self.assertEqual(
            self._test_document_version.page_content_objects,
            test_document_version_expected_page_content_objects
        )

    def test_method_get_absolute_url(self):
        self._clear_events()

        self.assertTrue(
            self._test_document.version_active.get_absolute_url()
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)


class DocumentVersionBusinessLogicTestCase(
    DocumentVersionTestMixin, GenericDocumentTestCase
):
    def test_multiple_active(self):
        self._create_test_document_version()

        self._test_document_versions[0].refresh_from_db()
        self._test_document_versions[1].refresh_from_db()

        self.assertEqual(self._test_document_versions[0].active, False)
        self.assertEqual(self._test_document_versions[1].active, True)

        self._clear_events()

        self._test_document_versions[0].active = True
        self._test_document_versions[0]._event_actor = self._test_case_user
        self._test_document_versions[0].save()

        self._test_document_versions[0].refresh_from_db()
        self._test_document_versions[1].refresh_from_db()

        self.assertEqual(self._test_document_versions[0].active, True)
        self.assertEqual(self._test_document_versions[1].active, False)

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, self._test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(
            events[0].target, self._test_document_versions[0]
        )
        self.assertEqual(events[0].verb, event_document_version_edited.id)
