import sys
import os
import numpy as np
from custodian.vasp.handlers import VaspErrorHandler

# Replace the path below with your own path to workflows.py
sys.path.append('/storage/home/lam7027/work/bin/vasp-job-automation')
import dfttk.workflows as workflows

# Specify custodian handlers
subset = list(VaspErrorHandler.error_msgs.keys())
subset.remove("algo_tet")
subset.remove("brmix")
subset.remove("zbrent")
handlers = [VaspErrorHandler(errors_subset_to_catch=subset)]

vasp_cmd = ["mpirun", "/opt/packages/VASP/VASP6/6.4.1/INTEL/vasp_std"]

workflows.run_phonons(vasp_cmd, handlers)

