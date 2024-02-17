####### MP spawning method ########## 

import multiprocessing as mp ;

try : mp.set_start_method("spawn") ;
except : pass ;


from .config import bootstrap, add_config_dir
from .sched import sched as scheduler
from .sched.compose import Compose, Coupler, Qubit, Spectrum
from .sched.sched import (after_task_finished, before_task_start,
                          before_task_step, cancel, create_task, exec, get,
                          get_config, get_executor, get_system_info,
                          register_hook, session, set, submit,
                          unregister_all_hooks, unregister_hook,
                          update_parameters)
from .sched.task import set_default_lib, update_tags
cfg =  None ; executor = None ; 



def init(boot_file = None ) :
    global cfg, executor; 
    bootstrap(boot_file) ; 
    executor = get_executor() ;
    cfg = get_config()
    
def debug_on():
    executor.debug_on()
    scheduler.debug_on()


def debug_off():
    executor.debug_off()
    scheduler.debug_off()
