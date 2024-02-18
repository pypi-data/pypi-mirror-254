"""stratis.py: Module with test specific method for Stratis."""

#  Copyright: Contributors to the sts project
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

import json
import logging

from sts import linux
from sts.utils.cli_tools import Wrapper
from sts.utils.cmdline import run


def get_stratis_service() -> str:
    """Return name of the stratis service.

    Returns:
      str: Name of the stratis service.
    """
    return 'stratisd'


class Stratis(Wrapper):
    """Wrapper class for stratis command line interface."""

    def __init__(self, disable_check=True) -> None:  # noqa: ANN001
        self.stratis_version = ''
        self.disable_check = disable_check

        for pkg in ['stratisd', 'stratis-cli']:
            if not linux.is_installed(pkg) and not linux.install_package(pkg):
                logging.critical(f'Could not install {pkg} package')

        self.commands: dict[str, list[str]] = {}
        self.commands['all'] = list(self.commands.keys())
        self.arguments = {
            'force': [self.commands['all'], ' --force'],
            'redundancy': [self.commands['all'], ' --redundancy'],
            'propagate': [self.commands['all'], '--propagate '],
        }

        if not linux.is_service_running(get_stratis_service()):
            if not linux.service_restart(get_stratis_service()):
                logging.error(f'Could not start {get_stratis_service()} service')
            else:
                logging.info(f'Service {get_stratis_service()} restarted.')

        Wrapper.__init__(self, self.commands, self.arguments, self.disable_check)

    @staticmethod
    def _remove_nones(kwargs):  # noqa: ANN001, ANN205
        return {k: v for k, v in kwargs.items() if v is not None}

    def _run(self, cmd, **kwargs):  # noqa: ANN001, ANN003, ANN202
        # Constructs the command to run and runs it

        # add '--propagate' flag by default to show whole trace when getting errors
        # This is a suggestion from devs
        if not ('propagate' in kwargs and not kwargs['propagate']):
            cmd = self.arguments['propagate'][1] + cmd

        cmd = 'stratis ' + cmd
        cmd = self._add_arguments(cmd, **kwargs)

        ret = run(cmd).rc
        if isinstance(ret, tuple) and ret[0] != 0:
            logging.warning(f"Running command: '{cmd}' failed. Return with output.")
        elif isinstance(ret, int) and ret != 0:
            logging.warning(f"Running command: '{cmd}' failed.")
        return ret

    def set_stratis_version(self, version):  # noqa: ANN001, ANN201
        self.stratis_version = version

    def get_stratis_version(self):  # noqa: ANN201
        if not self.stratis_version:
            ret, data = self._run(cmd='--version', return_output=True)
            if ret == 0:
                self.set_stratis_version(data)
                return data
            logging.error('Could not get stratis version!')
            return '0.0.0'
        return self.stratis_version

    def get_stratis_major_version(self):  # noqa: ANN201
        return int(self.get_stratis_version().split('.')[0])

    def get_stratis_minor_version(self):  # noqa: ANN201
        return int(self.get_stratis_version().split('.')[1])

    def get_pool_uuid(self, pool_name):  # noqa: ANN001, ANN201
        ret, data = self._run(cmd='report', return_output=True)
        if ret == 0 and data:
            try:
                report = json.loads(data)
            except json.JSONDecodeError:
                logging.exception("Could not deserialize data returned from 'stratis report' command!")
                return None
            for pool in report['pools']:
                if pool_name == pool['name']:
                    logging.info(f"Found UUID: {pool['uuid']} for pool_name: {pool_name}.")
                    return pool['uuid']
            logging.error(f'Could not find pool UUID for provided pool_name: {pool_name}!')
            return None
        return None

    def pool_create(  # noqa: ANN201
        self,
        pool_name=None,  # noqa: ANN001
        blockdevs=None,  # noqa: ANN001
        force=False,  # noqa: ANN001
        redundancy=None,  # noqa: ANN001
        key_desc=None,  # noqa: ANN001
        tang_url=None,  # noqa: ANN001
        thumbprint=None,  # noqa: ANN001
        clevis=None,  # noqa: ANN001
        trust_url=None,  # noqa: ANN001
        no_overprovision=None,  # noqa: ANN001
        **kwargs,  # noqa: ANN003
    ):
        cmd = 'pool create '
        if key_desc:
            cmd += f'--key-desc {key_desc} '
        if clevis:
            cmd += f'--clevis {clevis} '
        if tang_url:
            cmd += f'--tang-url {tang_url} '
        if thumbprint:
            cmd += f'--thumbprint {thumbprint} '
        if trust_url:
            cmd += '--trust-url '
        if no_overprovision:
            cmd += '--no-overprovision '
        if pool_name:
            cmd += f'{pool_name} '
        if blockdevs:
            if not isinstance(blockdevs, list):
                blockdevs = [blockdevs]
            cmd += ' '.join(blockdevs)
        kwargs.update(
            {
                'force': force,
                'redundancy': redundancy,
            },
        )
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_list(self, pool_uuid=None, stopped_pools=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool list '
        if pool_uuid:
            cmd += f'--uuid {pool_uuid} '
        if stopped_pools:
            cmd += '--stopped '
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_destroy(self, pool_name=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool destroy '
        if pool_name:
            cmd += f'{pool_name} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_rename(self, current=None, new=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool rename '
        if current:
            cmd += f'{current} '
        if new:
            cmd += f'{new} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_add_data(self, pool_name=None, blockdevs=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool add-data '
        if pool_name:
            cmd += f'{pool_name} '
        if blockdevs:
            if not isinstance(blockdevs, list):
                blockdevs = [blockdevs]
            cmd += ' '.join(blockdevs)
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_add_cache(self, pool_name=None, blockdevs=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool add-cache '
        if pool_name:
            cmd += f'{pool_name} '
        if blockdevs:
            if not isinstance(blockdevs, list):
                blockdevs = [blockdevs]
            cmd += ' '.join(blockdevs)
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_init_cache(self, pool_name=None, blockdevs=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool init-cache '
        if pool_name:
            cmd += f'{pool_name} '
        if blockdevs:
            if not isinstance(blockdevs, list):
                blockdevs = [blockdevs]
            cmd += ' '.join(blockdevs)
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_bind(  # noqa: ANN201
        self,
        binding_method=None,  # noqa: ANN001
        pool_name=None,  # noqa: ANN001
        key_desc=None,  # noqa: ANN001
        trust_url=None,  # noqa: ANN001
        thumbprint=None,  # noqa: ANN001
        tang_url=None,  # noqa: ANN001
        force=None,  # noqa: ANN001
        redundancy=None,  # noqa: ANN001
        **kwargs,  # noqa: ANN003
    ):
        cmd = 'pool bind '
        if binding_method:
            cmd += f'{binding_method} '
        if trust_url:
            cmd += '--trust-url '
        if thumbprint:
            cmd += f'--thumbprint {thumbprint} '
        if pool_name:
            cmd += f'{pool_name} '
        if key_desc:
            cmd += f'{key_desc} '
        if tang_url:
            cmd += f'{tang_url} '
        kwargs.update(
            {
                'force': force,
                'redundancy': redundancy,
            },
        )
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_rebind(  # noqa: ANN201
        self,
        binding_method=None,  # noqa: ANN001
        pool_name=None,  # noqa: ANN001
        key_desc=None,  # noqa: ANN001
        force=None,  # noqa: ANN001
        redundancy=None,  # noqa: ANN001
        **kwargs,  # noqa: ANN003
    ):
        cmd = 'pool rebind '
        if binding_method:
            cmd += f'{binding_method} '
        if pool_name:
            cmd += f'{pool_name} '
        if key_desc:
            cmd += f'{key_desc} '
        kwargs.update(
            {
                'force': force,
                'redundancy': redundancy,
            },
        )
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_unbind(  # noqa: ANN201
        self,
        binding_method=None,  # noqa: ANN001
        pool_name=None,  # noqa: ANN001
        force=None,  # noqa: ANN001
        redundancy=None,  # noqa: ANN001
        **kwargs,  # noqa: ANN003
    ):
        cmd = 'pool unbind '
        if binding_method:
            cmd += f'{binding_method} '
        if pool_name:
            cmd += f'{pool_name} '
        kwargs.update(
            {
                'force': force,
                'redundancy': redundancy,
            },
        )
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_set_fs_limit(  # noqa: ANN201
        self,
        pool_name=None,  # noqa: ANN001
        fs_amount=None,  # noqa: ANN001
        force=None,  # noqa: ANN001
        redundancy=None,  # noqa: ANN001
        **kwargs,  # noqa: ANN003
    ):
        cmd = 'pool set-fs-limit '
        if pool_name:
            cmd += f'{pool_name} '
        if fs_amount:
            cmd += f'{fs_amount} '
        kwargs.update(
            {
                'force': force,
                'redundancy': redundancy,
            },
        )
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_overprovision(self, pool_name=None, pool_overprovision=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool overprovision '
        if pool_name:
            cmd += f'{pool_name} '
        if pool_overprovision:
            cmd += f'{pool_overprovision}'
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_explain(self, pool_error_code=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool explain '
        if pool_error_code:
            cmd += f'{pool_error_code} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_debug(  # noqa: ANN201
        self,
        debug_subcommand=None,  # noqa: ANN001
        pool_name=None,  # noqa: ANN001
        pool_uuid=None,  # noqa: ANN001
        **kwargs,  # noqa: ANN003
    ):
        cmd = 'pool debug '
        if debug_subcommand:
            cmd += f'{debug_subcommand} '
        if pool_name:
            cmd += f'--name {pool_name} '
        if pool_uuid:
            cmd += f'--uuid {pool_uuid} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_start(self, pool_name=None, pool_uuid=None, unlock_method=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool start '
        if unlock_method:
            cmd += f'--unlock-method {unlock_method} '
        if self.get_stratis_major_version() <= 3 and self.get_stratis_minor_version() < 4:
            if pool_uuid:
                cmd += f'{pool_uuid} '
            return self._run(cmd, **self._remove_nones(kwargs))
        if pool_name:
            cmd += f'--name {pool_name} '
        if pool_uuid:
            cmd += f'--uuid {pool_uuid} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_stop(self, pool_name=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool stop '
        if pool_name:
            cmd += f'{pool_name} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def pool_extend_data(self, pool_name=None, device_uuid=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'pool extend-data '
        if pool_name:
            cmd += f'{pool_name} '
        if device_uuid:
            cmd += f'--device-uuid {device_uuid}'
        return self._run(cmd, **self._remove_nones(kwargs))

    def blockdev_list(self, pool_name=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'blockdev list '
        if pool_name:
            cmd += f'{pool_name} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def blockdev_debug(self, debug_subcommand=None, dev_uuid=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'blockdev debug '
        if debug_subcommand:
            cmd += f'{debug_subcommand} '
        if dev_uuid:
            cmd += f'--uuid {dev_uuid} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def fs_create(self, pool_name=None, fs_name=None, fs_size=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'fs create '
        if fs_size:
            cmd += f'--size {fs_size} '
        if pool_name:
            cmd += f'{pool_name} '
        if fs_name:
            cmd += f'{fs_name} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def fs_debug(self, debug_subcommand=None, fs_name=None, fs_uuid=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'fs debug '
        if debug_subcommand:
            cmd += f'{debug_subcommand} '
        if fs_name:
            cmd += f'--name {fs_name} '
        if fs_uuid:
            cmd += f'--uuid {fs_uuid} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def fs_snapshot(  # noqa: ANN201
        self,
        pool_name=None,  # noqa: ANN001
        origin_name=None,  # noqa: ANN001
        snapshot_name=None,  # noqa: ANN001
        **kwargs,  # noqa: ANN003
    ):
        cmd = 'fs snapshot '
        if pool_name:
            cmd += f'{pool_name} '
        if origin_name:
            cmd += f'{origin_name} '
        if snapshot_name:
            cmd += f'{snapshot_name} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def fs_list(self, pool_name=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'fs list '
        if pool_name:
            cmd += f'{pool_name} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def fs_destroy(self, pool_name=None, fs_name=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'fs destroy '
        if pool_name:
            cmd += f'{pool_name} '
        if fs_name:
            cmd += f'{fs_name} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def fs_rename(self, pool_name=None, fs_name=None, new_name=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'fs rename '
        if pool_name:
            cmd += f'{pool_name} '
        if fs_name:
            cmd += f'{fs_name} '
        if new_name:
            cmd += f'{new_name} '
        return self._run(cmd, **kwargs)

    def key_set(self, keyfile_path=None, key_desc=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'key set '
        if keyfile_path:
            cmd += f'--keyfile-path {keyfile_path} '
        if key_desc:
            cmd += f'{key_desc} '
        ret = self._run('key list', return_output=True)
        # ret is a tuple in format -> (return_code, return_output)
        if key_desc in ret[1]:
            return self._run('key list')
        return self._run(cmd, **kwargs)

    def key_reset(self, keyfile_path=None, key_desc=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'key reset '
        if keyfile_path:
            cmd += f'--keyfile-path {keyfile_path} '
        if key_desc:
            cmd += f'{key_desc} '
        return self._run(cmd, **kwargs)

    def key_list(self, **kwargs):  # noqa: ANN003, ANN201
        return self._run('key list', **kwargs)

    def key_unset(self, key_desc=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'key unset '
        if key_desc:
            cmd += f'{key_desc} '
        return self._run(cmd, **kwargs)

    # Pool unlock has been removed in favor of pool_start in Stratisd 3.2.0
    def pool_unlock(self, **kwargs):  # noqa: ANN003, ANN201
        return self._run('pool unlock', **kwargs)

    def daemon_redundancy(self, **kwargs):  # noqa: ANN003, ANN201
        return self._run('daemon redundancy', **kwargs)

    def daemon_version(self, **kwargs):  # noqa: ANN003, ANN201
        return self._run('daemon version', **kwargs)

    def debug_refresh(self, **kwargs):  # noqa: ANN003, ANN201
        return self._run('debug refresh', **kwargs)

    def version(self, **kwargs):  # noqa: ANN003, ANN201
        return self._run('--version', **kwargs)
