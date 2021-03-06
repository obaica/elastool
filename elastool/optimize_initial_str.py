"""
  Elastool -- Elastic toolkit for finite-temperature elastic constants calculations

  Copyright (C) 2019-2020 by Zhong-Li Liu

  This program is free software; you can redistribute it and/or modify it under the
  terms of the GNU General Public License as published by the Free Software Foundation
  version 3 of the License.

  This program is distributed in the hope that it will be useful, but WITHOUT ANY
  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
  PARTICULAR PURPOSE.  See the GNU General Public License for more details.

  E-mail: zl.liu@163.com
"""
from os import mkdir, chdir
from os.path import isdir
from ase.io import vasp
from vasp_run import vasp_run
from read_input import indict


def optimize_initial_str(pos_conv, cwd, tag):
    if not isdir('OPT'):
        mkdir('OPT')
    chdir('OPT')

    vasp.write_vasp('POSCAR', pos_conv, vasp5=True, direct=True)
    kpoints_file_name = 'KPOINTS-static'
    pos_optimized = vasp_run(tag, kpoints_file_name, cwd)

    chdir('..')

    return pos_optimized
    