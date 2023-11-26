import paramiko


def ssh_checkout(host, user, passwd, cmd, text, port=22):
    out, exit_code = ssh_getout(host, user, passwd, cmd, port)
    if text in out and exit_code == 0:
        return True
    else:
        return False


def ssh_checkout_negative(host, user, passwd, cmd, text, port=22):
    out, exit_code = ssh_getout(host, user, passwd, cmd, port)
    if (text in out) and exit_code != 0:
        return True
    else:
        return False


def ssh_getout(host, user, passwd, cmd, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode("utf-8")
    client.close()
    return out, exit_code
