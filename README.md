# geop-collectd-installer

## Требования к хостам для установки сборщика метрик

 * ОС Ubuntu 20 LTS / Ubuntu 18 LTS / Debian 9 / Debian 10 / CentOS 7 / CentOS 8 / RHEL 7 / RHEL 8
 * Наличие python2 или 3

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
    - добавить все необходимые хосты для последующей установки агента на них
    - выставить нужные значения vm_id, tenant_id и др. для каждого хоста
1. Запустить установку
```
ansible-playbook playbooks/install-telegraf.yaml -i hosts.yaml
```

