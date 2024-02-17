import unittest
from tfana.main import list_rc_files


class TestListRCFiles(unittest.TestCase):
    def test_list_rc_files(self):
        # 测试 list_rc_files 函数是否能够正确列出 rc 文件
        rc_files = list_rc_files()

        # 假设用户主目录下有一个示例 .rc 文件
        expected_rc_file = ".pypirc"

        self.assertIn(expected_rc_file, rc_files, f"{expected_rc_file} 应该在 rc 文件列表中")

    def test_list_rc_files_no_rc_files(self):
        # 测试当没有 rc 文件时，list_rc_files 函数是否返回空列表
        # 假设用户主目录下没有 rc 文件
        rc_files = list_rc_files()

        self.assertEqual(len(rc_files), 0, "没有 rc 文件时，应该返回空列表")


if __name__ == "__main__":
    unittest.main()
