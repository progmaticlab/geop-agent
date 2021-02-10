# geop-collectd-installer
## нужно иметь джампхост, с которого будут запускаться ansible playbooks.
.. возможные ОС для хостов, на которые будут установлены collectd и telegraf:
    Ubuntu 20 LTS / Ubuntu 18 LTS / Debian 9 / Debian 10 / CentOS 7 / CentOS 8

## установить git

## установить ansible

### клонировать geop-agent
    git clone https://github.com/progmaticlab/geop-agent.git

### запустить установку telegraf
    cd geop-agent
    # выставить переменную listen_at [IP] в hosts.yaml
    # и указать хост, на который надо установить telegraf
    ansible-playbook playbooks/install-telegraf.yaml -i hosts.yaml

