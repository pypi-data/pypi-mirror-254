import json,pathlib,pickle,sys

from systemq.lib.arch.baqis_config import QuarkConfig, QuarkLocalConfig
import qlisp
from qlispc.config import CompileConfigMixin

from .sched.executor import FakeExecutor, QuarkExecutor
from .sched.sched import bootstrap as kss_bootstrap

# TODO : DISCUS
# should the etc path  be defaulted to hom directory ? 

# will check from the first of the config dirs to the last until
# the wanted directory is found, this works good in NT as well
config_dirs =  [
    pathlib.Path.cwd(), 
    pathlib.Path.home() / ".systemq"  ,   # hidden directory
    pathlib.Path.home() / ".config" / "systemq"  , # conifgs together systemq 
    pathlib.Path.home() , # just under home , not often used
    pathlib.Path(__file__).parent.parent / 'etc' # defalut path for etc file in the site package
]

cfg = {} ; # global configure dictionary


def add_config_dir(pth_) :
    global config_dirs ; 
    pth = pathlib.Path(pth_);
    if pth in config_dirs :  config_dirs.remove(pth); # load for order sake
    config_dirs.insert(0, pth) ; # first see first get


# This function is used to load configuration table 
# to the system
def load_registry(config_path):
    with open(config_path, 'rb') as f:
        try:
            config = json.load(f)
            # TODO : check if it is json syntax error
        except:
            try:
                f.seek(0)
                config = pickle.load(f)
            except:
                import dill
                f.seek(0)
                config = dill.load(f)
    return config


# bootstrap : 
# call this function when initalizing the kernel system
def bootstrap( boot_file_path = None ):  
    print("############  BOOT ##################") 
    # chosing the most close file to bootstraping 
    config = {} ; 
    candidate_boot_paths = [] ; 
    if(None != boot_file_path) : candidate_boot_paths.append(pathlib.Path(boot_file_path) ); 
    candidate_boot_paths+=[pth / "bootstrap.json" for pth in config_dirs ];
   
    has_config = False ;
    for bfp  in candidate_boot_paths :
        if(bfp.exists()) :
            print(f"USING : {str(bfp)} as boot file");
            config = json.load(open(bfp , "r")); 
            has_config = True ; 
            break ;

    assert(has_config), "No available 'bootstrap.json' found, check kernel.config.config_dirs for the scanned paths";

    if config['executor']['type'] == 'debug':
        executor = FakeExecutor(load_registry(config['executor']['path']))
    else:
        executor = QuarkExecutor(config['executor']['host'])
    if config['data']['path'] == '':
        datapath = pathlib.Path.home() / 'data'
        datapath.mkdir(parents=True, exist_ok=True)
        config['data']['path'] = str(datapath)
    else:
        datapath = pathlib.Path(config['data']['path'])
    if config['data']['url'] == '':
        url = 'sqlite:///{}'.format(datapath / 'waveforms.db')
        config['data']['url'] = url
    else:
        url = config['data']['url']
    repo = config.get('repo', None)
    print(f"USING : {str(repo)} as git repo") 
    cfg.update(config)  
    kss_bootstrap(executor, url, datapath, repo)
    print("#####################################") 
