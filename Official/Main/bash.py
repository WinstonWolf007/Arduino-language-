import os


# execute 'os' function to add interaction with linux
class Command:

    # give information for command syntax
    def cmd_help(self, command=None) -> None:
        print()

    # display all case or file in directory
    def lnx_ls(self, command=None) -> None:
        all_dir = os.listdir()
        print("\n".join(all_dir))

    # change directory
    def lxn_cd(self, command: str) -> None:
        os.chdir(os.getcwd() + '/' + command)

    # create ADN project
    def dft_adn(self, command: str) -> None:
        os.mkdir(command)
        self.lxn_cd(command)
        for x in ['doc', 'default', 'package']:
            os.mkdir(x)
        self.lxn_cd("")

    # run adn file
    def dft_run(self, command: str) -> list:
        file_type = command.split('.')[1]
        if file_type == 'adn':
            with open(command, 'r+') as file:
                all_code_line = [line for line in file]
        return all_code_line


def check_command(array_code: list) -> None:
    all_command = {}
    if array_code[0] == "run":
        print("running !")


def inputs() -> list:
    listCode = input(">>> ").split()
    return listCode


if __name__ == '__main__':
    value = inputs()
    check_command(value)
