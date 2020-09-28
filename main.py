import os


class Cleaner:
    path = None

    def __init__(self, _path):
        self.path = _path

    @staticmethod
    def __del_file__(_path: str):
        try:
            os.remove(_path)
            print("file deleted", _path)
        except Exception as ex:
            print(f'error delete file {_path}', ex)

    @staticmethod
    def __del_emp_dir__(_path: str) -> bool:
        list_dirs = os.listdir(_path)
        if not list_dirs:
            try:
                os.rmdir(_path)
                print('dir deleted', _path)
            except Exception as ex:
                print(f'error delete dir {_path}', ex)
            return True
        return False

    def del_empty_dirs_and_bak_files(self, _path: str = None):
        if not _path:
            _path = self.path
            if not os.path.isdir(_path):
                raise NotADirectoryError("Is not a directory")
        for d in os.listdir(_path):
            a = os.path.join(_path, d)
            if os.path.isdir(a):
                self.del_empty_dirs_and_bak_files(a)
                if self.__del_emp_dir__(a) is False:
                    list_dirs = os.listdir(a)
                    for df in list_dirs:
                        if df.__contains__('.bak') and not (df.replace('.bak', '.doc') in list_dirs or df.replace('.bak', '.docx') in list_dirs):
                            p_file_del = os.path.join(a, df)
                            self.__del_file__(p_file_del)
                            # final check empty dir after delete files
                            self.__del_emp_dir__(a)


if __name__ == '__main__':
    path = r"D:\xampp\htdocs\python_projects\GroupBWT\catalog"
    cleaner = Cleaner(_path=path)
    cleaner.del_empty_dirs_and_bak_files()
    print("finish")
