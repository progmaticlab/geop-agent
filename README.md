# geop-collectd-installer
### нужно иметь хост,  на котором будут запускаться ansible playbooks.

## Требования к хосту

 * ОС Ubuntu 20 LTS / Ubuntu 18 LTS / Debian 9 / Debian 10 / CentOS 7 / CentOS 8 / RHEL 7 / RHEL 8
 * Наличие python2 или 3

## Установка
1. установить git
1. установить ansible (https://docs.ansible.com/ansible/latest/installation_guide/index.html)
1. скачать репозиторий geop-agent
```
git clone https://github.com/progmaticlab/geop-agent.git
cd geop-agent
```
1. Отредактировать hosts.yaml
    - добавить все необходимые хосты для последующей установки агента на них
    - выставить нужные значения vm_id, tenant_id и др. для каждого хоста
1. запустить установку
```
ansible-playbook playbooks/install-telegraf.yaml -i hosts.yaml
```

