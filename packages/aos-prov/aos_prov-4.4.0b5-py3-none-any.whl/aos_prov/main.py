#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#

import argparse
import logging
import sys
from pathlib import Path

from aos_prov.actions import (
    create_new_unit,
    download_image,
    provision_unit,
    remove_vm_unit,
    start_vm_unit,
)
from aos_prov.communication.cloud.cloud_api import DEFAULT_REGISTER_PORT, CloudAPI
from aos_prov.utils import DEFAULT_USER_CERT_PATH, DEFAULT_USER_KEY_PATH
from aos_prov.utils.common import AOS_DISKS_PATH, DISK_IMAGE_DOWNLOAD_URL, print_error
from aos_prov.utils.errors import (
    CloudAccessError,
    DeviceRegisterError,
    OnUnitError,
    UnitError,
)
from aos_prov.utils.user_credentials import UserCredentials

try:
    from importlib.metadata import version  # noqa: WPS433
except ImportError:
    import importlib_metadata as version  # noqa: WPS433,WPS432,WPS440

_ARGUMENT_USER_CERTIFICATE = '--cert'
_ARGUMENT_USER_KEY = '--key'
_ARGUMENT_USER_PKCS12 = '--pkcs12'

_COMMAND_NEW_VM = 'vm-new'
_COMMAND_REMOVE_VM = 'vm-remove'
_COMMAND_START_VM = 'vm-start'
_COMMAND_UNIT_CREATE = 'unit-new'
_COMMAND_DOWNLOAD = 'download'

_DEFAULT_USER_CERTIFICATE = str(Path.home() / '.aos' / 'security' / 'aos-user-oem.p12')

logger = logging.getLogger(__name__)


def _parse_args():  # noqa: WPS213
    parser = argparse.ArgumentParser(
        prog='aos-prov',
        description='The unit provisioning tool using gRPC protocol',
        epilog="Run 'aos-prov [COMMAND] --help' for more information about commands",
    )

    parser.add_argument(
        '-u',
        '--unit',
        required=False,
        help='Unit address in format IP_ADDRESS or IP_ADDRESS:PORT',
    )

    parser.add_argument(
        _ARGUMENT_USER_CERTIFICATE,
        default=DEFAULT_USER_CERT_PATH,
        help=f'User certificate file. Default: {DEFAULT_USER_CERT_PATH}',
    )

    parser.add_argument(
        _ARGUMENT_USER_KEY,
        default=DEFAULT_USER_KEY_PATH,
        help=f'User key file. Default: {DEFAULT_USER_KEY_PATH}',
    )

    parser.add_argument(
        '-p',
        _ARGUMENT_USER_PKCS12,
        required=False,
        help='Path to user certificate in pkcs12 format.',
        dest='pkcs',
        default=_DEFAULT_USER_CERTIFICATE,
    )

    parser.add_argument(
        '--register-port',
        default=DEFAULT_REGISTER_PORT,
        help=f'Cloud port. Default: {DEFAULT_REGISTER_PORT}',
    )

    parser.add_argument(
        '-w',
        '--wait-unit',
        action='store',
        metavar='N',
        help='Wait for unit to respond for the first time in seconds. Default value 0 means wait for 5 seconds',
        dest='wait_unit',
        default=0,
        type=int,
    )

    parser.set_defaults(which=None)

    sub_parser = parser.add_subparsers(title='Commands')

    new_vm_command = sub_parser.add_parser(
        _COMMAND_NEW_VM,
        help='Create new Oracle VM',
    )
    new_vm_command.set_defaults(which=_COMMAND_NEW_VM)

    new_vm_command.add_argument(
        '-N',
        '--name',
        required=True,
        help='Name of the VM',
    )

    new_vm_command.add_argument(
        '-D',
        '--disk',
        required=False,
        help='Full path to the AosCore-powered disk.',
        default=AOS_DISKS_PATH,
    )

    remove_vm_command = sub_parser.add_parser(
        _COMMAND_REMOVE_VM,
        help='Remove Oracle VM',
    )
    remove_vm_command.set_defaults(which=_COMMAND_REMOVE_VM)

    remove_vm_command.add_argument(
        '-N',
        '--name',
        required=True,
        help='Name of the VM',
    )

    start_vm_command = sub_parser.add_parser(
        _COMMAND_START_VM,
        help='Start the VM',
    )
    start_vm_command.add_argument(
        '-N',
        '--name',
        required=True,
        help='Name of the VirtualBox group where VMs are located.',
    )

    start_vm_command.add_argument(
        '-H',
        '--headless',
        action='store_true',
        help='Start VMs in headless mode.',
    )
    start_vm_command.set_defaults(which=_COMMAND_START_VM)

    create_unit_command = sub_parser.add_parser(
        _COMMAND_UNIT_CREATE,
        help='Create and provision new VirtualBox-based unit',
    )
    create_unit_command.set_defaults(which=_COMMAND_UNIT_CREATE)

    create_unit_command.add_argument(
        '--name',
        required=True,
        help='Name of the VM',
    )

    create_unit_command.add_argument(
        '--disk',
        required=False,
        help='Full path to the AosCore-powered disk.',
        default=AOS_DISKS_PATH,
    )

    create_unit_command.add_argument(
        '-H',
        '--headless',
        action='store_true',
        help='Start created VMs in headless mode.',
    )

    create_unit_command.add_argument(
        '-p',
        _ARGUMENT_USER_PKCS12,
        required=False,
        help='Path to user certificate in pkcs12 format',
        dest='pkcs',
        default=_DEFAULT_USER_CERTIFICATE,
    )

    parser.add_argument(
        '-V',
        '--version',
        action='version',
        version=f'%(prog)s {version("aos-prov")}',  # noqa: WPS323,WPS237
    )

    download_command = sub_parser.add_parser(_COMMAND_DOWNLOAD, help='Download image')
    download_command.set_defaults(which=_COMMAND_DOWNLOAD)
    download_command.add_argument(
        '-a',
        '--address',
        dest='download_address',
        help='Address to download image',
    )

    download_command.add_argument(
        '-f',
        '--force',
        action='store_true',
        help='Force overwrite existing file',
    )

    return parser.parse_args()


def _parse_user_creds(args) -> UserCredentials:
    is_default_pkcs = args.pkcs == _DEFAULT_USER_CERTIFICATE
    if is_default_pkcs and (args.cert != DEFAULT_USER_CERT_PATH or args.key != DEFAULT_USER_KEY_PATH):
        args.pkcs = None
    return UserCredentials(cert_file_path=args.cert, key_file_path=args.key, pkcs12=args.pkcs)


def main():
    status = 0
    args = _parse_args()

    try:  # noqa: WPS225
        if args.which is None:
            user_creds = _parse_user_creds(args)
            cloud_api = CloudAPI(user_creds, args.register_port)
            cloud_api.check_cloud_access()
            wait = args.wait_unit // 5 or 1
            provision_unit(args.unit, cloud_api, wait)

        if args.which == _COMMAND_DOWNLOAD:
            url = DISK_IMAGE_DOWNLOAD_URL
            if args.download_address:
                url = args.download_address
            download_image(url, args.force)

        if args.which == _COMMAND_NEW_VM:
            user_creds = _parse_user_creds(args)
            create_new_unit(args.name, user_creds, args.disk)

        if args.which == _COMMAND_REMOVE_VM:
            remove_vm_unit(args.name)

        if args.which == _COMMAND_START_VM:
            start_vm_unit(args.name, args.headless)

        if args.which == _COMMAND_UNIT_CREATE:
            user_creds = _parse_user_creds(args)
            create_new_unit(args.name, user_creds, args.disk, do_provision=True, headless=args.headless)

    except CloudAccessError as exc:
        print_error(f'Failed during communication with the AosCloud with error: {exc}')
        status = 1
    except DeviceRegisterError as exc:
        print_error(f'FAILED with error: {exc}')
        status = 1
    except UnitError as exc:
        print_error(f'Failed during communication with device with error: \n {exc}')
        status = 1
    except OnUnitError as exc:
        print_error('Failed to execute the command!')
        print_error(f'Error: {exc} ')
        status = 1
    except (AssertionError, KeyboardInterrupt):
        print_error('Stopped by keyboard...')
        status = 1

    sys.exit(status)


if __name__ == '__main__':
    main()
