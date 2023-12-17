import os, time


def show_time_of_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time of execution {func.__name__}: {end - start:.5f} secods")
        return result

    return wrapper


class CommandPrompt:
    def __init__(self):
        pass

    @show_time_of_execution
    def dir(self):
        '''
        show all existing directories in the current folder
        :return:
        '''
        try:
            return os.listdir()

        except Exception as e:
            print(f"Error: {e}")

    @show_time_of_execution
    def cd(self, path):
        '''
        moving between directories using the command “cd folder name“
         and “cd ..“ to go back,
         otherwise, print Exception that the directory was not found
        :return:
        '''
        try:
            os.chdir(path)
            return
        except Exception as e:
            print(f"Error: directory was not found \n{e} ")

    @show_time_of_execution
    def create_dir(self, dir_name):
        '''
        create directory
        :return:
        '''
        try:
            os.makedirs(dir_name)
            return
        except Exception as e:
            print(f"Error: {e}")

    @show_time_of_execution
    def rename_dir(self, old_name, new_name):
        '''
        renaming of the directory
        :return:
        '''
        try:
            os.rename(old_name, new_name)
            return
        except Exception as e:
            print(f"Error: {e}")

    @show_time_of_execution
    def del_dir(self, path):
        '''
        delete dir
        :return:
        '''
        try:
            os.rmdir(path)
            return
        except Exception as e:
            print(f"Error: {e}")

    @show_time_of_execution
    def type(self, file_name):
        '''
        Просмотр текстового файла
        :return:
        '''
        try:
            with open(file_name, "r") as file:
                return file.read()
        except Exception as e:
            return f"Error {e} "

    @show_time_of_execution
    def pwd(self):
        """
        current directory
        :return:  name of current dir
        """
        try:
            return os.getcwd()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    while True:
        command = input().lower().strip()
        cmd = CommandPrompt()
        match command:
            case "ls":
                print(cmd.dir())
            case "pwd":
                print(cmd.pwd())
            case "cd":
                name = input("Input path to the new dir: ")
                cmd.cd(name)
            case "cd":
                name = input("Input path to the new dir: ")
                cmd.cd(name)
            case "cd ..":
                name = cmd.pwd().split("\\")[:-1]
                # print(cmd.pwd().split("\\")[:-1])
                cmd.cd("/".join(name))
            case "mkdir":
                name = input("Input name of the new dir: ")
                cmd.create_dir(name)
            case "mv":
                old_name = input("Input old name of the dir: ")
                new_name = input("Input new name of the dir: ")
                cmd.rename_dir(old_name, new_name)
            case "rmdir":
                path = input("Input path to the dir: ")
                cmd.del_dir(path)
            case "type":
                name = input("Input path to the file: ")
                print(cmd.type(name))
            case _:
                print("No such command in list")
