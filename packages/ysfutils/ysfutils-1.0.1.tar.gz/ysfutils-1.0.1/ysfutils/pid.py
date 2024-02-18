from pathlib import Path


class Pid:
    @staticmethod
    def pid_allowed(pid_file_path: str):
        """ 判断磁盘上是否存在pid文件

        Args:
            pid_file_path: pid文件路径
        """
        find_pid_file = Path(pid_file_path)
        # 存在返回True
        if find_pid_file.exists():
            return True
        else:
            return False

    @staticmethod
    def deal_pid(pid_file_path: str, action: str):
        """ 处理磁盘上的pid文件

        Notes:
            1. 创建或删除pid文件

        Args:
            pid_file_path: pid文件名
            action: CREATE或者DEL
        """
        if action == "CREATE":
            Path(pid_file_path).touch(exist_ok=True)
        elif action == "DEL":
            Path(pid_file_path).unlink(missing_ok=True)
