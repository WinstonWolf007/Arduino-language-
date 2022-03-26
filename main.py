import os
import time
import sys
import random


class AdnLang:
    def __init__(self):
        self.code = []

    def execute(self):
        print('language started...')
        time.sleep(2)
        for i in self.code:
            print(i)


class AdnBash:
    def __init__(self):
        self.code = []
        self.package = [
            'random', 'os', 'stat', 'machine', 'arduino'
        ]

    def update_code(self, directory: str) -> int:
        try:
            with open(directory, 'r+') as file:
                for line in file:
                    self.code.append(line)
            return 200

        except Exception as e:
            print(e)
            return 400

    def display_code(self):
        print("\n".join(self.code))


if __name__ == '__main__':
    adnBash = AdnBash()
    adnLang = AdnLang()

    while True:
        directoryNow = os.getcwd()

        try:
            content = input(f"\033[90m{directoryNow}\033[0m\033[93m/~$\033[0m ").split()
        except KeyboardInterrupt:
            exit()

        if content[0] == 'run' and len(content) == 2:
            if adnBash.update_code(content[1]) == 200:
                adnLang.code = adnBash.code
                break
        elif content[0] == 'ls':
            allFile = os.listdir()
            print("\n".join(allFile))

        elif content[0] == 'cd' and len(content) == 2:
            os.chdir(content[1])

        elif content[0] == 'exit':
            break

        elif content[0] == 'adn' and len(content) == 2:
            a = 0
            num = 0

            def update():
                global a, num
                num += 1
                if num == 5:
                    a = 100
                else:
                    a += random.randint(10, 20)
                c = ('\033[90mcreating project: \033[93m'+str(a)+'%\033[0m')
                sys.stdout.write('\r'+c)
                time.sleep(0.3)


            os.chdir(directoryNow)
            try:
                os.mkdir(content[1])
            except FileExistsError:
                pass

            update()

            os.chdir(directoryNow+f'/{content[1]}')
            try:
                os.mkdir("file")
                os.mkdir("package")
                os.mkdir("doc")
            except FileExistsError:
                pass

            update()

            for directoryName in ['file', 'package', 'doc']:
                update()
                os.chdir(directoryNow + f'/{content[1]}/{directoryName}')

                if directoryName == 'file':
                    open(os.getcwd()+"/main.adn", 'a').close()
                elif directoryName == 'package':
                    for packageName in adnBash.package:
                        open(os.getcwd()+'/'+packageName, 'a').close()
                elif directoryName == 'doc':
                    open(os.getcwd()+'/'+'document.txt', 'a').close()

            print("\n")

            os.chdir(directoryNow)

        elif content[0] == 'help':
            print('command:\n\trun <fileName>\n\tls\n\tcd <directory>\n\tadn <projectName>\n\texit')

    adnLang.execute()