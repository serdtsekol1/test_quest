import os


class Cleaner:
    path = None
    delete_empty_dir = False

    def __init__(self, _path, _delete_empty_dir=False):
        self.delete_empty_dir = _delete_empty_dir
        self.path = _path

    @staticmethod
    def __del_file__(_path: str):
        try:
            os.remove(_path)
            print("file deleted", _path)
        except Exception as ex:
            print(f'error delete file {_path}', ex)

    def __del_emp_dir__(self, _path: str) -> bool:
        list_dirs = os.listdir(_path)
        if not list_dirs:
            if not self.delete_empty_dir:
                return True
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
    path = input(r"Путь до папки (Приклад 'C:\test\test2'): ")
    cleaner = Cleaner(_path=path)

    user_answer = input("Видаляти папки пусті папки? true/false: ").lower().strip()
    if user_answer in ['true', '1']:
        cleaner.delete_empty_dir = True
    elif user_answer in ['false', '0']:
        cleaner.delete_empty_dir = False
    else:
        print("Error: напишіть true або false")
    cleaner.del_empty_dirs_and_bak_files()
    print("finish")
