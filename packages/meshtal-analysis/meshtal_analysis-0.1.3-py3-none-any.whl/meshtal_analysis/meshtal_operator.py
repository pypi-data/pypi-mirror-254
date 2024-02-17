#!/usr/bin/python3
##############################################################################
# Author: Xiaokang Zhang, Zhiqi Shi
# Function: Adding two meshtallies with the same shape.
# Aim: adding nuclear responses from neutron and photon
#   - nuclear heat from n and p
#   - operation dose from n and p
# Usage:
#   - fill out the 'config.ini'
#   - run 'python3 meshtal_operate.py -h' for detailed information
# Changelog:
#   - 20240126: read assigned meshtally from meshtal
#   - 20221007: init the script
##############################################################################
import os
import numpy as np
import argparse
from pyne import mcnp
from pyne.mesh import MeshTally
import matplotlib.pyplot as plt
import seaborn as sns
from natf.utils import format_single_output
from meshtal_analysis.meshtal_analysis import MeshtalWithNumber
from pymoab import core as mb_core
from configparser import ConfigParser

def get_ptype(particle='neutron'):
    ptype = 'n'
    if particle.lower() in ['n', 'neutron']:
        ptype = 'n'
    elif particle.lower() in ['p', 'photon']:
        ptype = 'p'
    return ptype


def create_tag_content(particle='neutron'):
    """
    Create tags according to the tally_nums and particle.

    Parameters:
    -----------
    particle: string
        particle type, allowed particle: 'neutron', 'n', 'photon', 'p'
    """
    ptype = get_ptype(particle)
    tag_content = [f'{ptype}_result', f'{ptype}_rel_error',
                   f'{ptype}_total_result', f'{ptype}_total_rel_error']
    return tag_content


def create_tags(tally_nums, particle='n'):
    if isinstance(tally_nums, int):
        tally_nums = [tally_nums]
    tags = {}
    tag_content = create_tag_content(particle=particle)
    for tid in tally_nums:
        tags[tid] = tag_content
    return tags


def meshtally2h5m(meshtally, ofname=None):
    """
    Convert meshtally data to h5m.

    Parameters:
    -----------
    meshtally: pyne.mesh MeshTally object
        The meshtally to be converted.
    ofname: str
        output file name
    """

    tally_num = meshtally.tally_number
    if ofname is None:
        ofname = f"meshtally{tally_num}.h5m"
    meshtally.write_hdf5(ofname, write_mats=False)
    return


def meshtally_evaluation(meshtally, ctm=None, tag_name='n_total_rel_error'):
    """
    Some typical analyses value are evaluated.
    - score percentage, eta: ratio of non_zero mesh elements / total mesh elements
    - effective score percentage:
        - eta_eff_10: ratio of mesh elements with rel_err < 0.1 / non_zero mesh elements
        - eta_eff_5: ratio of mesh elements with rel_err < 0.05 / non_zero mesh elements
    - Global Figure-of-Merit, FOG_g: fom_g = 1/(ctm * SIG(rel_err**2) / num_ves)
        - Note: for those elements with zero rel_err (not tallied), rel_err should be
                replaced with 1.0

    Parameters:
    -----------
    meshtally: PyNE MeshTally object
        meshtally to analysis
    ctm: float
        Compute time in minutes
    tag_name: str
        Total relative error tag name.

    Returns:
    --------
    eta, eta_eff_10, eta_eff_5, fom_g, sig_re
    """

    num_ves = meshtally.num_ves
    # calculate eta and eta_eff_10, eta_eff_5
    num_nonzero = 0
    num_eff_10 = 0
    num_eff_5 = 0
    total_rel_error = getattr(meshtally, tag_name)[:]
    for i, rel_err in enumerate(total_rel_error):
        if rel_err > 0:
            num_nonzero += 1
        if rel_err > 0 and rel_err < 0.1:
            num_eff_10 += 1
        if rel_err > 0 and rel_err < 0.05:
            num_eff_5 += 1
    eta = num_nonzero/float(num_ves)
    eta_eff_10 = num_eff_10/float(num_nonzero)
    eta_eff_5 = num_eff_5/float(num_nonzero)

    if ctm is None:
        print(f"ctm is not given, FOM_g will not be calculated")
        return eta, eta_eff_10, eta_eff_5, 0.0
    # reset 0.0 rel_err to 1
    sum_rel_err_squre = 0.0
    for i, rel_err in enumerate(total_rel_error):
        if rel_err == 0.0:
            total_rel_error[i] = 1.0
        sum_rel_err_squre += rel_err * rel_err
    # calculate fom_g
    # FOG_m = 1/(ctm * SIG(rel_err**2) / num_ves)
    fog_m = 1.0 / (ctm * sum_rel_err_squre / num_ves)

    return eta, eta_eff_10, eta_eff_5, fog_m


def remove_tally_fc(filename):
    """
    Remove the comment line of tally results.
    """
    tmpout = 'tmpout'
    fo = open(tmpout, 'w')
    with open(filename, 'r') as fin:
        tally_start = False
        while True:
            line = fin.readline()
            if line == '':
                break
            if 'Mesh Tally Number' in line:
                fo.write(line)
                line = fin.readline()
                if ('neutron' not in line) and ('photon' not in line):  # comment line
                    pass
                else:
                    fo.write(line)
            else:
                fo.write(line)
    # close w file
    fo.close()
    # remove the old file and name to new file
    os.remove(filename)
    os.system(f"mv {tmpout} {filename}")

    return


def get_tally_nums(filename):
    """
    Read meshtal file to get tally numbers.

    Parameters:
    -----------
    filename: str
        The filename of the meshtal.

    Returns:
    --------
    tally_nums: list
        List of tally numbers
    """
    tally_nums = []
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                break
            if 'Mesh Tally Number' in line:
                tokens = line.strip().split()
                tid = int(tokens[-1])
                tally_nums.append(tid)
    return tally_nums


def plot_pdf_vs_rel_err(meshtally, tag_name='n_total_rel_error', ofname='pdf_err.png', bins=20):
    """
    Plot the probability distribution function vs. relative error.
    """
    # make the plot
    total_rel_error = getattr(meshtally, tag_name)
    sns.set_style('darkgrid')
    ax = sns.histplot(total_rel_error[:], bins=bins)
    # tidy up the figure
    # ax.legend(loc='best')
    ax.set_xlabel('Relative error')
    ax.set_ylabel('Frequency')
    fig = ax.get_figure()
    fig.savefig(ofname, dpi=600, bbox_inches='tight')
    plt.close()
    return


def plot_cdf_vs_rel_err(meshtally, tag_name='n_total_rel_error', ofname='cdf_err.png', bins=None):
    """
    Plot the cumulative probabitity distribution function vs. relative error.
    """
    total_rel_error = getattr(meshtally, tag_name)
    # set up bins
    if bins is None:
        num_ves = meshtally.num_ves
        if num_ves < 5:
            bins = num_ves
        elif num_ves < 20:
            bins = 5
        elif num_ves < 100:
            bins = 20
        elif num_ves < 1e4:
            bins = 50
        else:
            bins = 100
    values, base = np.histogram(total_rel_error[:], bins=bins)
    # evaluate the culmulative
    normed_values = values / sum(values)
    cumulative = np.cumsum(normed_values)
    sns.set_style("darkgrid")
    ax = sns.lineplot(x=base[:-1], y=cumulative)
    # ax.set(title='Cumulative probability distribution of relative error')
    ax.set(xlabel='Relative error')
    ax.set_ylabel('Cumulative density')
    # ax.legend(loc='best')
    fig = ax.get_figure()
    fig.savefig(ofname, dpi=600, bbox_inches='tight')
    plt.close()
    return


def get_ctm(filename):
    """
    Read log file to get ctm.
    """
    ctm = -1.0
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                break
            if 'ctm =' in line:
                ctm = float(line.strip().split()[2])
    if ctm < 0:
        raise ValueError(f"ctm not found in {filename}")
    return ctm


def scale_with_multiplier(meshtally, multiplier, particle):
    """
    Multiply the result with multiplier
    """
    meshtally1 = meshtally
    ptype = get_ptype(particle)
    # result
    result_tag_name = f"{ptype}_result"
    result = getattr(meshtally1, result_tag_name)[:]
    result = np.multiply(result, multiplier)
    if ptype == 'n':
        meshtally1.n_result[:] = result[:]
    elif ptype == 'p':
        meshtally1.p_result[:] = result[:]
    # total result
    total_result_tag_name = f"{ptype}_total_result"
    total_result = getattr(meshtally1, total_result_tag_name)[:]
    total_result = np.multiply(total_result, multiplier)
    if ptype == 'n':
        meshtally1.n_total_result[:] = total_result[:]
    elif ptype == 'p':
        meshtally1.p_total_result[:] = total_result[:]
    return meshtally1


def add_meshtally_results(meshtally1, meshtally2):
    """Add two meshtallies"""
    meshtally = meshtally1
    particle = 'n'
    # add total result
    ptype = get_ptype(particle)
    result_tag_name = f"n_total_result"
    result1 = getattr(meshtally1, result_tag_name)
    result2 = getattr(meshtally2, result_tag_name)
    result = np.add(result1, result2)
    # print(result)
    meshtally.n_total_result[:] = result[:]
    return meshtally


def calc_midx(r, x_bounds, y_bounds, z_bounds):
    """
    Calculate the index of the mesh element.
    """
    xidx = np.searchsorted(x_bounds, r[0]) - 1
    yidx = np.searchsorted(y_bounds, r[1]) - 1
    zidx = np.searchsorted(z_bounds, r[2]) - 1
    midx = zidx + yidx*(len(z_bounds)-1) + xidx * \
        (len(y_bounds)-1)*(len(z_bounds)-1)
    return midx


def get_result_by_pos(meshtally, r, particle='n', ofname='result.txt', style='fispact'):
    """
    Get the result of specific position.
    """
    midx = calc_midx(r, meshtally.x_bounds,
                     meshtally.y_bounds, meshtally.z_bounds)
    ptype = get_ptype(particle)
    result_tag_name = f"{ptype}_result"
    results = getattr(meshtally, result_tag_name)[:]
    result = results[midx]
    result_total_tag_name = f"{ptype}_total_result"
    results_total = getattr(meshtally, result_total_tag_name)[:]
    result_total = results_total[midx]
    if isinstance(result, float):
        result = [result]
    with open(ofname, 'w') as fo:
        if style == 'fispact':
            for i in range(len(result)):  # reverse the neutron flux
                fo.write(
                    ''.join([format_single_output(result[len(result) - 1 - i]), '\n']))
            fo.write('1.0\n')
            fo.write(' '.join(['Neutron energy group', str(
                len(result)), 'G, TOT = ', format_single_output(result_total)]))
        else:
            raise ValueError(f"style {style} not supported")
    fo.close()


def get_meshtally(filename, particle, tally_ana):
    if filename.split('.')[-1] == 'h5m':
        meshtally = MeshTally()
        meshtally.mesh = mb_core.Core()
        meshtally.mesh.load_file(filename)
        super(MeshTally, meshtally).__init__(mesh=meshtally.mesh, structured=True)
        return meshtally
    else:
        remove_tally_fc(filename)
        tags = create_tags(tally_ana, particle=particle)
        meshtal = MeshtalWithNumber(filename, tags=tags, tally_number=tally_ana)
        meshtally = meshtal.tally[tally_ana]
        return meshtally


def main():
    """
    Operate the meshtally in meshtals.
    """
    meshtal_analysis = (
        'This script read meshtal files and operates the meshtally results.\n')
    parser = argparse.ArgumentParser()
    parser.add_argument("-f1", "--filename1", required=False,
                        help="meshtal file 1, default: meshtal")
    parser.add_argument("-f2", "--filename2", required=False,
                        help="meshtal file 2, default: meshtal")
    parser.add_argument("-t1", "--tally1", required=False,
                        help="tally number in meshtal1 to analysis, default: 4")
    parser.add_argument("-t2", "--tally2", required=False,
                        help="tally number in meshtal2 to analysis, default: 14")
    parser.add_argument("-m1", "--multiplier1", required=False,
                        help="multiplier for meshtal1, default: 1.0")
    parser.add_argument("-m2", "--multiplier2", required=False,
                        help="multiplier for meshtal2, default: the same as multiplier1")
    parser.add_argument("--operator", required=False,
                        help="operator of two meshtallies, support: 'add' (default), 'sub' or 'subtract'")
    parser.add_argument("-o", "--output", required=False,
                        help="output h5m filename")
    parser.add_argument("-c", "--config", required=False,
                        help="using config to specify tally")
    args = vars(parser.parse_args())

    # old method preserved
    if args['filename1'] is not None:
        # file1 info
        filename1 = 'meshtally4.h5m'
        if args['filename1'] is not None:
            filename1 = args['filename1']
        particle = 'n'
        tally_ana1 = 14
        if args['tally1'] is not None:
            tally_ana1 = int(args['tally1'])
        multiplier1 = 1.0
        if args['multiplier1'] is not None:
            multiplier1 = float(args['multiplier1'])
        print(
            f"tally: {tally_ana1} in file {filename1} will be used with multiplier: {multiplier1}")

        # file2 info
        filename2 = 'meshtal'
        if args['filename2'] is not None:
            filename2 = args['filename2']
        particle = 'n'
        tally_ana2 = 14
        if args['tally2'] is not None:
            tally_ana2 = int(args['tally2'])
        multiplier2 = multiplier1
        if args['multiplier2'] is not None:
            multiplier2 = float(args['multiplier2'])
        print(
            f"tally: {tally_ana2} in file {filename2} will be used with multiplier: {multiplier2}")

        operator = 'sub'
        if args['operator'] is not None:
            operator = args['operator']
        if operator not in ('add', 'sub', 'subtract'):
            raise ValueError(
                f"Wrong operator provided. Support: 'add'(default), 'sub', 'subtract'")

        ofname = f"{filename1}_fmesh{tally_ana1}_times_{multiplier1}_{operator}_{filename2}_fmesh{tally_ana2}_times_{multiplier2}.h5m"

        if filename1 == filename2:
            print(f"  warning: two tallies are in the same file: {filename1}")
            # meshtal = mcnp.Meshtal(filename1, tags=tags)
            # meshtally1 = meshtal.tally[tally_ana1]
            # meshtally2 = meshtal.tally[tally_ana2]
        print(f"getting meshtally1 ...")
        meshtally1 = get_meshtally(filename1, particle, tally_ana1)
        print(f"getting meshtally2 ...")
        meshtally2 = get_meshtally(filename2, particle, tally_ana2)

        # multiply the multiplier
        if multiplier1 != 1.0:
            meshtally1 = scale_with_multiplier(meshtally1, multiplier1, particle)

        print(f"operating meshtally1 and meshtally2 ...")
        if operator.lower() == 'add':
            print(f"  adding meshtally1 and meshtally2 ...")
            meshtally2 = scale_with_multiplier(
                meshtally2, multiplier2, particle)
        elif operator.lower() in ('sub', 'subtract'):
            print(f"  subtracting meshtally1 by meshtally2 ...")
            meshtally2 = scale_with_multiplier(
                meshtally2, -multiplier2, particle)

        meshtally1 = add_meshtally_results(meshtally1, meshtally2)
    else:
        conf = ConfigParser()
        if args['config'] is None:
            conf.read('config.ini')
        else:
            conf.read(args['config'])
        meshtallys = conf.sections()
        print(f'getting {meshtallys[0]} ...')
        meshtally1 = get_meshtally(conf[meshtallys[0]]['filename'], 'n', conf[meshtallys[0]].getint('tallyid'))
        meshtally1 = scale_with_multiplier(meshtally1, conf[meshtallys[0]].getint('multiplier'), 'n')
        ofname = f"{conf[meshtallys[0]]['filename']}_{conf[meshtallys[0]]['tallyid']}_times_{conf[meshtallys[0]]['multiplier']}"
        for tally in meshtallys[1:]:
            print(f'getting {tally} ...')
            meshtally2 = get_meshtally(conf[tally]['filename'], 'n', conf[tally].getint('tallyid'))
            print(f'operating {meshtallys[0]} and {tally} ...')
            meshtally2 = scale_with_multiplier(meshtally2, conf[tally].getint('multiplier'), 'n')
            meshtally1 = add_meshtally_results(meshtally1, meshtally2)
            ofname = ofname + f"_add_{conf[tally]['filename']}_{conf[tally]['tallyid']}_times_{conf[tally]['multiplier']}"
        ofname = ofname + '.h5m'
    # convert to h5m
    if args['output'] is not None:
        ofname = args['output']
    print(f"writing results...")
    meshtally2h5m(meshtally1, ofname=ofname)
    print(f"Done")


if __name__ == '__main__':
    main()
