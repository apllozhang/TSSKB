# -*- coding: utf-8 -*-
"""部署 site/ 到 10.20.30.103（覆盖旧版）"""
import os, paramiko

HOST = os.environ.get('TSSKB_HOST', '10.20.30.103')
USER = os.environ.get('TSSKB_USER', 'tina')
PWD = os.environ.get('TSSKB_DEPLOY_PWD', '')  # 从环境变量读取，勿写入代码
SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
REMOTE = '/home/tina/ov-learn-site'

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(HOST, username=USER, password=PWD, timeout=10)
_, out, err = c.exec_command(f"rm -rf {REMOTE} && mkdir -p {REMOTE}", timeout=60)
out.read(); err.read()

sftp = c.open_sftp()
def updir(local, remote):
    try: sftp.mkdir(remote)
    except IOError: pass
    for name in os.listdir(local):
        lp, rp = os.path.join(local, name), remote + '/' + name
        if os.path.isdir(lp):
            updir(lp, rp)
        else:
            sftp.put(lp, rp)
updir(SITE, REMOTE)

def run(cmd):
    _, out, err = c.exec_command(cmd, timeout=30)
    print(f'$ {cmd}\n{out.read().decode("utf-8","replace")}{err.read().decode("utf-8","replace")}')
run(f"find {REMOTE} -name '*.html' | wc -l")
run("curl -s -o /dev/null -w 'cover:%{http_code} ' http://127.0.0.1:8899/; curl -s -o /dev/null -w 'sub:%{http_code} ' http://127.0.0.1:8899/postsales/ov-terra/; curl -s -o /dev/null -w 'skill:%{http_code}\\n' http://127.0.0.1:8899/postsales/ov-terra/skills/ov-rf-tuning.html")
c.close()
print('DONE')
