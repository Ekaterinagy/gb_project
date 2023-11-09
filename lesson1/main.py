import subprocess

# python lesson1/main.py
if __name__ == '__main__':
    print('PyCharm')
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if '20.04.6' in out and 'focal' in out and result.returncode == 0:
        print('SUCCESS')
    else:
        print('FAIL')
