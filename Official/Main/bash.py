import os


# execute 'os' function to add interaction with linux
class Command:

    # give information for command syntax
    def cmd_help(self, command=None) -> None:
        print("\thelp\n"
              "\tls\n"
              "\tcd <directory>\n"
              "\tadn <project name>\n"
              "\texit\n"
              "\trun <file name>")

    # display all case or file in directory
    def lnx_ls(self, command=None) -> None:
        all_dir = os.listdir()
        print("\t"+"\n\t".join(all_dir))

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
        print(all_code_line)
        return all_code_line

    # exit bash
    def dft_exit(self, command=None) -> None:
        exit()


# execute command whit dict
def check_command(array_code: list) -> None:
    command = Command()
    array_code.append(None)

    all_command = {
        "help": command.cmd_help,
        "ls": command.lnx_ls,
        "cd": command.lxn_cd,
        "adn": command.dft_adn,
        "exit": command.dft_exit,
        "run": command.dft_run
    }

    if all_command.get(array_code[0]):
        all_command.get(array_code[0])(array_code[1])
    else:
        print(f'\tcommand no find "{array_code[0]}"')


# get input and return a list
def inputs() -> list:
    listCode = input('\033[90m'+os.getcwd() + "/~$ \033[0m").split()
    return listCode


# main loop prog
if __name__ == '__main__':
    while True:
        value = inputs()
        check_command(value)
