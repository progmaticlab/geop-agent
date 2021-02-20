# geop-agent

## Требования к хостам для установки агента

 * ОС Ubuntu 20 LTS / Ubuntu 18 LTS / Debian 9 / Debian 10 / CentOS 7 / CentOS 8 / RHEL 7 / RHEL 8
 * Наличие python 2 или 3

## Установка

**Все действия в документе производятся на управлящей машине**

1. Установить git
1. Установить ansible (https://docs.ansible.com/ansible/latest/installation_guide/index.html)
1. Скачать репозиторий geop-agent
   ```
   git clone https://github.com/progmaticlab/geop-agent.git
   cd geop-agent
   ```
1. Отредактировать hosts.yaml
    - добавить целевой хост для последующей установки агента
    - выставить нужные значения окружения
    ```
      hosts:
        172.16.112.51:
          ansible_user: centos
          namespace: 0c2b8049-976a-4de7-8e76-74d300dcdac9
          project: '0000000000000000000'
          supplier_id: 'f16b0120-6d13-11eb-8572-0800200c9a66'
          endpoint: http://213.219.214.155:9999/v1
    ```
1. Пользователь debian из hosts.yaml (может быть любое имя пользователя) должен иметь возможность запуска команд с привилегиями суперпользователя (sudo) без ввода пароля.
1. Доступ к целевому хосту для этого пользователя должен быть по ключу без пароля.
1. Запустить установку
   ```
   ansible-playbook playbooks/install-agent.yaml -i hosts.yaml
   ```

