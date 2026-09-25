"""Harmless export regressions; temporary source/output trees only."""
import unittest
from export_probes import probe


class ExportBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.results=probe(archived=False)

    def test_untracked_destination_file_not_published(self):
        self.assertEqual(self.results['preexisting_untracked']['build'],'rejected')

    def test_source_symlink_not_dereferenced(self):
        self.assertEqual(self.results['source_symlink']['build'],'rejected')

    def test_extra_traversal_zip_member_is_rejected(self):
        self.assertFalse(self.results['extra_traversal_zip_member']['verifier_passed'])

    def test_symlink_zip_metadata_is_rejected(self):
        self.assertFalse(self.results['symlink_zip_metadata']['verifier_passed'])

    def test_unmanifested_destination_file_is_rejected(self):
        self.assertFalse(self.results['unmanifested_output']['verifier_passed'])

if __name__=='__main__':unittest.main()
