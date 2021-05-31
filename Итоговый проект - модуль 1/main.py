"""Скрипт запуска демонстрации работы системы из двух сервисов и клиента
"""

import subprocess

with open('train.log', 'wt') as tf:
  with open('apply.log', 'wt') as af:
    train_proc = subprocess.Popen(
      ['python', 'train.py'],
      stdout = tf
    )
    apply_proc = subprocess.Popen(
      ['python', 'apply.py'],
      stdout = af
    )
    subprocess.run(['sleep', '10'])
    subprocess.run(['python', 'client.py'])
    for proc in [train_proc, apply_proc]:
      proc.terminate()
      proc.wait()
