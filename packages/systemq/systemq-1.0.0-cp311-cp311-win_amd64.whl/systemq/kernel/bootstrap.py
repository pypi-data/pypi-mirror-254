import json
import pathlib
import pickle
import sys
from pathlib import Path

import requests

from .sched.executor import FakeExecutor, QuarkExecutor
from .sched.sched import bootstrap as _bootstrap

etc = Path(__file__).parent.parent / 'etc'
systemq_base = pathlib.Path.home() / '.systemq'
systemq_base.mkdir(exist_ok=True, parents=True)

cfg = {}


def load_registry(config_path):
    with open(config_path, 'rb') as f:
        try:
            config = json.load(f)
        except:
            try:
                f.seek(0)
                config = pickle.load(f)
            except:
                import dill
                f.seek(0)
                config = dill.load(f)
    return config


def bootstrap(config_path: str = etc / 'bootstrap.json'):
    if not config_path.exists():
        config_path = etc / 'bootstrap.json.sample'

    with open(config_path) as f:
        config = json.load(f)

    if config['executor']['type'] == 'debug':
        executor = FakeExecutor(load_registry(config['executor']['path']))
    else:
        executor = QuarkExecutor(config['executor']['host'])
    if config['data']['path'] == '':
        datapath = Path.home() / 'data'
        datapath.mkdir(parents=True, exist_ok=True)
        config['data']['path'] = str(datapath)
    else:
        datapath = Path(config['data']['path'])
    if config['data']['url'] == '':
        url = 'sqlite:///{}'.format(datapath / 'waveforms.db')
        config['data']['url'] = url
    else:
        url = config['data']['url']
    repo = config.get('repo', None)

    cfg.update(config)

    _bootstrap(executor, url, datapath, repo)

    base_url = config['extentions']['server']
    for module, file in config['extentions']['modules'].items():
        module_path = systemq_base / file

        if not module_path.exists():
            resp = requests.get(f"{base_url}/packages/{file}")

            with open(module_path, 'wb') as f:
                f.write(resp.content)

        if str(module_path) not in sys.path:
            sys.path.append(str(module_path))
