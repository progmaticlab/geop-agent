# geop-agent

## Требования к хостам для установки агента

 * ОС Ubuntu 20 LTS / Ubuntu 18 LTS / Debian 9 / Debian 10
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
    - выставить нужные значения окружения (namespace, project, endpoint, supplier_id)
1. Запустить установку
```
ansible-playbook playbooks/install-agent.yaml -i hosts.yaml
```

