# CrashRestarter 1.0
# Official GitHub repo: https://github.com/watermelon46/crashrestarter

print('CrashRestarter 1.0 ||| Release')

# Edit this variables!!!
fileforlaunch = 'C:\\Users\\User\\Desktop\\coding\\main.py' # File what you need restart from crash. Example: C:\\Users\\User\\PythonProjects\\cookieclicker.py
reportcrash = True # Report crash or start without notify
askforrestart = False # Ask user for restart


counter = 0
def anticrash():
    global counter
    if reportcrash:
        print('\n[CRASHRESTARTER] File has been started. №' + str(counter) + '\n')
    try:
        exec(open(fileforlaunch).read())
    except:
        if reportcrash:
            print('\nCRASHRESTARTER] File has been crashed or you entered wrong path.')
    if reportcrash:
        print('\n[CRASHRESTARTER] File has been stopped (not crashed).')
    if askforrestart:
        input('Press enter for restart')
    counter += 1
    anticrash()
anticrash()


