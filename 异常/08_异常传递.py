import time
try:
    f = open('2.md', 'r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(1)
            print(content)
    except:
        print('Unexpected termination of program.')
except:
    print('no such file or dir.')
