import argparse
import fileinput
import json
import requests
from datetime import datetime
import logging
import traceback

def metrics_by_ts(metrics):
    out = {}
    tset = set()
    for metric in metrics:
        if metric['name'] == 'ballast_value':
            continue
        ts = metric.pop('timestamp')
        secs = ts % 60
        ts = ts - secs
        if ts not in tset:
            out[ts] = [metric,]
            tset.add(ts)
        else:
            out[ts].append(metric)
    print(tset)
    return out

def metrics_by_tags(metrics):
    out = []
    taglist = []
    for metric in metrics:
        if metric['tags'] in taglist:
            idx  = taglist.index(metric['tags'])
            out[idx].append(metric)
        else:
            taglist.append(metric['tags'])
            out.append([metric,])
    return out

def prepare_metrics(metriclist):
    out = []
    tags = []
    for metric in metriclist:
        host_tag = []
        if 'host' in metric['tags']:
            host_tag = metric['tags']['host'].split(" ")
        m = {
            'metricName': metric['tags']['type'],
            'value': metric['fields']['value'],
            'tags': [{
                'name': 'resource_name',
                'value': host_tag[0]
            }]
        }
        if len(host_tag)>1:
            m['tags'].append({
                'name': 'resource_id',
                'value': host_tag[1]
            })
        if len(host_tag)>2:
            m['tags'].append({
                'name': 'tenant_id',
                'value': host_tag[2]
            })
        if 'type_instance' in metric['tags']:
            resource = metric['tags']['type_instance'].split("_")
            m['tags'].append({
                'name': 'subsystem_compute_resource_name',
                'value': resource[0]
            })
            if len(resource)>1:
                m['tags'].append({
                    'name': 'object_monitoring_id',
                    'value': resource[1]
                })
        if m['tags'] not in tags:
            tags.append(m['tags'])
            out.append([m,])
        else:
            idx = tags.index(m['tags'])
            out[idx].append(m)
    return out

def run(j, config):
    jts = metrics_by_ts(j['metrics'])
    for ts in jts:
        tosend = {
            'date': datetime.fromtimestamp(ts).isoformat(),
            'namespace': config.namespace,
            'metrics': [],
        }
        taggedlist = prepare_metrics(jts[ts])
        for tagged in taggedlist:
            labels = tagged[0]['tags']
            labels.append({
                'name': 'supplier_id',
                'value': config.supplier
            })
            ml = []
            for m in tagged:
                m.pop('tags', None)
                print(m)
                ml.append(m)
            tosend['metrics'].append({
                'labels': labels,
                'metricsSet': ml
            })
        try:
            r = requests.post(config.endpoint+'/'+config.project+'/metrics_set', json=tosend)
        except Exception as e:
            with open(config.logfile, 'a') as f:
                f.write(str(e))
                f.write(traceback.format_exc())
            exit(3)
        if (r.status_code >= 400):
            with open(config.logfile, 'a') as f:
                f.write(json.dumps(tosend))
                f.write(str(r.status_code))
                f.write(r.text)
            exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('--namespace', action='store', type=str, required=True)
parser.add_argument('--endpoint', action='store', type=str, required=True)
parser.add_argument('--project', action='store', type=str, required=True)
parser.add_argument('--supplier', action='store', type=str, required=True)
parser.add_argument('--logfile', action='store', type=str, default='/var/log/mcs.log')
args = parser.parse_args()

try:
    a=input()
    j=json.loads(a)
    run(j, args)
except Exception  as e:
    with open(args.logfile, 'a') as f:
        f.write(str(e))
        f.write(traceback.format_exc())
    exit(-1)

