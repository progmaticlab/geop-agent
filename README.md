# geop-agent

* collectd installation and configuration

## run collectd playbook


```
ansible-playbook --connection=local --inventory 127.0.0.1,  playbooks/install-collectd.yaml
```


## run telegraf playbook

```
ansible-playbook --connection=local --inventory 127.0.0.1, playbooks/install-telegraf.yaml
```
