# CrashRestarter 1.0
# Official GitHub repo: https://github.com/watermelon46/crashrestarter

print('CrashRestarter 1.0 ||| Release')

# Edit this variables!!!
fileforlaunch = 'C:\\PleaseChangeMe\\YourScript.py' # File what you need restart from crash. Example: C:\\Users\\User\\PythonProjects\\cookieclicker.py
askforrestart = False # Рестартить только с подтверждения пользователя




if fileforlaunch == 'C:\\PleaseChangeMe\\YourScript.py':
    input('Путь до программы установлен по умолчанию. Пожалуйста, измените переменную fileforlaunch. Если ваш файл как раз и хранится по такому пути (что странно) - нажмите Enter. Если послe нажатия Enter вы увидите бесконечную волну крашей - вероятно, вам все же надо изменить путь.')
counter = 0
def anticrash():
    crash = False
    global counter
    print('\n[CRASHRESTARTER] Файл был запущен. Попытка №' + str(counter) + '\n')
    try:
        exec(open(fileforlaunch).read())
    except:
        print('\nCRASHRESTARTER] Файл был крашнут (или вы ввели неправильный путь)')
        crash = True
    if crash == False:
        print('\n[CRASHRESTARTER] Файл был остановлен (не крашнут)')
    if askforrestart:
        input('Нажмите Enter для рестарта')
    counter += 1
    anticrash()
anticrash()
