###############################################################################
# (c) Copyright 2021 CERN for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################
"""
Contains functions used to run the checks implemented in LbAPCommon.
These are used in conjunction with `lb-ap test`, and require an ntuple created during a test.
Handles the storage of any figures produced when running the checks.
"""

import os
from os.path import join

import click
import matplotlib.pyplot as plt
import mplhep
from LbAPCommon import parse_yaml, render_yaml, validate_yaml
from LbAPCommon.checks import run_job_checks
from LbAPCommon.checks.utils import checks_to_JSON, hist_to_root

from .utils import check_production


# TODO this is no longer needed as we will always have some default checks now for general validation
def checks_exist(checks_data):
    """
    Return true if any checks have been defined in the config file for this production
    Otherwise returns false
    """
    return len(checks_data) > 0


def perform_checks(
    production_name, jobs_data, job_name, test_ntuple_path_list, checks_output_dir
):
    """
    Run all stages of checks
    """
    job_data, checks_data = prepare_checks(
        production_name, job_name, test_ntuple_path_list, checks_output_dir
    )

    click.secho("Running checks", fg="green")
    check_results = run_job_checks(
        jobs_data, job_name, job_data["checks"], checks_data, test_ntuple_path_list
    )
    output_check_results(job_name, checks_data, check_results, checks_output_dir)

    if all([cr.passed for cr in check_results.values()]):
        click.secho(
            f"All checks passed! Any output can be found in {checks_output_dir}",
            fg="green",
        )


def prepare_checks(production_name, job_name, test_ntuple_path_list, checks_output_dir):
    """
    For a specific job's checks, run anything required before the checks themselves are executed.
    This includes:
    * Parsing & validating the config file
    * (If necessary) creating the output directory where any figures will be stored

    Returns info needed for later stages:
    * Dictionary containing info on all jobs
    * Dictionary containing checks configuration
    * Path to output directory where figures from checks should be stored
    """
    # Check if production exists
    check_production(production_name)

    # Check if job actually exists in production
    with open(os.path.join(production_name, "info.yaml"), "rt") as fp:
        raw_yaml = fp.read()
    prod_data, checks_data = parse_yaml(render_yaml(raw_yaml))
    validate_yaml(prod_data, checks_data, ".", production_name)
    try:
        job_data = prod_data[job_name]
    except KeyError:
        raise click.ClickException(
            f"Job {job_name} is not found for production {production_name}!"
        )

    # Check that test ntuple exists at path provided
    for test_ntuple_path in test_ntuple_path_list:
        if not os.path.isfile(test_ntuple_path):
            raise click.ClickException(f"No file found at {test_ntuple_path}")

    # Create directory for checks
    if not os.path.exists(checks_output_dir):
        os.makedirs(checks_output_dir)

    return job_data, checks_data


def output_check_results(job_name, checks_data, check_results, checks_out_dir):
    """
    Handle all output from checks
    This includes both terminal output, and saving figures
    """
    # Save histograms in a root file
    hist_file_name = f"{job_name}_histograms.root"
    hist_out_path = join(checks_out_dir, hist_file_name)
    hist_to_root(job_name, check_results, hist_out_path)

    # Save check results to JSON file
    check_results_with_job = {job_name: check_results}
    json_out_path = join(checks_out_dir, "checks.json")
    checks_to_JSON(
        checks_data,
        check_results_with_job,
        json_output_path=json_out_path,
    )

    for name, cr in check_results.items():
        if cr.passed:
            for key, data in cr.tree_data.items():
                # Output histograms for 1D range
                hist_counter = 0
                for _histo in data.get("histograms", []):
                    hist_counter += 1
                    fig, ax = plt.subplots(figsize=(10, 6))
                    if cr.check_type == "range":
                        mplhep.histplot(_histo)
                        ax.set_xlabel(_histo.axes[0].name)
                        ax.set_ylabel("Frequency density")
                    elif cr.check_type == "range_bkg_subtracted":
                        mplhep.histplot(_histo)
                        ax.set_xlabel(_histo.axes[0].name)
                        ax.set_ylabel("Frequency density")
                    elif cr.check_type == "range_nd":
                        if len(_histo.axes) == 2:
                            mplhep.hist2dplot(_histo)
                            ax.set_xlabel(_histo.axes[0].name)
                            ax.set_ylabel(_histo.axes[1].name)
                    tree_name = "_".join(key.split("/"))
                    fig_name = f"{job_name}_{tree_name}_{name}_{hist_counter-1}.pdf"
                    plt.savefig(join(checks_out_dir, fig_name))
        else:
            click.secho(f"Check '{name}' failed!", fg="red")
        for level, msg in cr.messages:
            click.secho(f"{name}: ({level!r}) {msg}", fg="yellow")
