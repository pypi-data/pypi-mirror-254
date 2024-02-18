"""Install Freesurfer license.txt file where algorithm expects it.
"""

import logging
import os
import re
import subprocess
from pathlib import Path

log = logging.getLogger(__name__)


def install_freesurfer_license(context, fs_license_path: os.PathLike = None):
    """Install the Freesurfer license file.

    The text for the license is found in one of 3 ways and in this order:

    1) license.txt is provided as an input file (manifest value = freesurfer_license_file),
    2) the text from license.txt is pasted into the "freesurfer_license_key"
       config, or
    3) the text from license.txt is pasted into a Flywheel project's "info"
       metadata (using the key FREESURFER_LICENSE).

    Once the text is located, the license file will be written to the FreeSurfer
    top-level directory. This will enable FreeSurfer to be used by the gear.

    See `How to include a Freesurfer license file...
    <https://docs.flywheel.io/User_Guides/user_freesurfer_license_file_to_run_a_freesurfer_or_fmriprep_gear/>`_

    Args:
        context (flywheel.gear_context.GearContext): The gear context with core
            functionality.
        fs_license_path (str): Path to where the license should be installed,
            $FREESURFER_HOME, usually "/opt/freesurfer/license.txt".

    Examples:
        >>> from flywheel_gear_toolkit.licenses.freesurfer import install_freesurfer_license
        >>> install_freesurfer_license(context, '/opt/freesurfer/license.txt')
    """
    log.debug("Locating Freesurfer installation")
    fs_license_path = get_fs_license_path(fs_license_path)

    log.debug("Looking for Freesurfer license")
    license_info = find_license_info(context)

    if license_info:
        write_license_info(fs_license_path, license_info)
    else:
        msg = "Could not find FreeSurfer license anywhere"
        raise FileNotFoundError(f"{msg} ({fs_license_path}).")


def get_fs_license_path(fs_license_path=None):
    if fs_license_path:
        if Path(fs_license_path).suffix != ".txt":
            fs_license_path = Path(fs_license_path) / "license.txt"
    else:
        if os.getenv("FREESURFER_HOME"):
            fs_license_path = Path(os.getenv("FREESURFER_HOME"), "license.txt")
        else:
            try:
                log.debug(
                    "FREESURFER_HOME is either not defined in the manifest"
                    "or does not exist as defined. (${FREESURFER_HOME})\n"
                    "Trying to locate freesurfer."
                )
                which_output = subprocess.check_output(
                    ["which", "recon-all"], text=True
                )
                pattern = ".*freesurfer.*?"
                match = re.search(pattern, which_output)
                if match:
                    fs_license_path = Path(match.group(), "license.txt")
                else:
                    log.error(f"Could not isolate FreeSurfer path from {which_output}")
                    raise
            except subprocess.CalledProcessError as e:
                log.error(e.output)
                raise
    return fs_license_path


def find_license_info(context):
    license_info = ""
    config_key = isolate_key_name(context)
    if context.get_input_path("freesurfer_license_file"):
        license_info = read_input_license(context)
        log.info("Using input file for FreeSurfer license information.")
    elif config_key:
        fs_arg = context.config[config_key]
        license_info = "\n".join(fs_arg.split())
        log.info("Using FreeSurfer license in gear configuration argument.")
    else:
        license_info = check_project_for_license(context)
    return license_info

def isolate_key_name(context):
    keys = ["freesurfer_license_key", "FREESURFER_LICENSE", "FREESURFER-LICENSE",
            "gear-FREESURFER_LICENSE"]
    for k in keys:
        if context.config.get(k):
            return k
        elif context.config.get(k.lower()):
            return k.lower()
    log.info(f"{k} keyword not found in config.")
    return None



def read_input_license(context):
    input_license = context.get_input_path("freesurfer_license_file")
    if input_license:
        with open(input_license) as lic:
            license_info = lic.read()
            license_info = "\n".join(license_info.split())
        return license_info


def check_project_for_license(context):
    fly = context.client
    destination_id = context.destination.get("id")
    project_id = fly.get_analysis(destination_id)["parents"]["project"]
    project = fly.get_project(project_id)
    if any(
        lic in ("FREESURFER-LICENSE", "FREESURFER_LICENSE") for lic in project["info"]
    ):
        try:
            space_separated_text = project["info"]["FREESURFER-LICENSE"]
        except KeyError:
            space_separated_text = project["info"]["FREESURFER_LICENSE"]
        license_info = "\n".join(space_separated_text.split())
        log.info("Using FreeSurfer license in project info.")
        return license_info


def write_license_info(fs_license_path, license_info):
    head = Path(fs_license_path).parents[0]
    if not Path(head).exists():
        Path(head).mkdir(parents=True)
        log.debug("Created directory %s", head)
    with open(fs_license_path, "w") as flp:
        flp.write(license_info)
        log.debug("Wrote license %s", license_info)
        log.debug(" to license file %s", fs_license_path)
