import shutil
import unittest
import zipfile
from SenyashaSystem import System

class TestSystem(unittest.TestCase):

    def setUp(self):

        self.zipfilePathOriginal = 'testData/test_archive.zip'
        self.zipfilePathTmp = 'testData/test_archive.zip.tmp'

        self.makeCopy()

    def makeCopy(self):
        shutil.copy(self.zipfilePathOriginal, self.zipfilePathTmp)

        self.zip_file = zipfile.ZipFile(self.zipfilePathTmp, 'a')
        self.system = System(path="", zipfile=self.zip_file, zipfilePath=self.zipfilePathTmp)

    def test_ls_root(self):
        self.makeCopy()
        result = self.system.ls()
        expected = ['dir2/', 'dir1/', 'file4.txt']
        self.assertEqual(result, expected)

    def test_cd_into_directory(self):
        self.makeCopy()
        self.system.cd("dir1")
        result = self.system.ls()
        expected = ['file2.txt', 'file1.txt']
        self.assertEqual(result, expected)

    def test_cd_unknown_directory(self):
        self.makeCopy()
        error = self.system.cd("unknown")
        self.assertEqual(error, "Error: Unknown dir")

    def test_isExist_file(self):
        self.makeCopy()
        self.system.cd("dir1")
        self.assertTrue(self.system.isExist("file1.txt"))

    def test_isExist_directory(self):
        self.makeCopy()
        self.assertTrue(self.system.isExist("dir1/"))

    def test_rm_non_existing_file(self):
        self.makeCopy()
        error = self.system.rm("non_existent.txt")
        self.assertEqual(error, "Error: No such file")

    def test_rm_directory(self):
        self.makeCopy()
        error = self.system.rm("dir1/")
        self.assertEqual(error, "Error: Can't remove directory")

    def test_cp_file(self):
        self.makeCopy()
        self.system.cp("file4.txt", "dir1/")
        self.system.cd("dir1")
        result = self.system.ls()
        self.assertIn("Copyfile4.txt", result)

    def test_rm_file(self):
        self.makeCopy()
        self.system.rm("file4.txt")
        result = self.system.ls()
        self.assertNotIn("file4.txt", result)

    def test_cp_non_existing_file(self):
        self.makeCopy()
        error = self.system.cp("non_existent.txt", "dir1/")
        self.assertEqual(error, "Error: File doesn't exist")

    def test_cp_directory(self):
        self.makeCopy()
        error = self.system.cp("dir1/", "dir2/")
        self.assertEqual(error, "Error: Cannot copy dir")

    def test_cp_directory_target_not_exist(self):
        self.makeCopy()
        error = self.system.cp("file4.txt", "non_existing_dir/")
        self.assertEqual(error, "Error: Dir doesn't exist")


if __name__ == '__main__':
    unittest.main()
