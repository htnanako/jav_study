from mbot.core.plugins import plugin, PluginCommandContext, PluginCommandResponse
from mbot.core.params import ArgSchema, ArgType
from mbot.openapi import mbot_api
import logging

from .update import update


@plugin.command(name='install', title='安装jav_study', desc='点击安装jav_study。会自动重启主程序。',
                icon='AutoAwesome', run_in_background=True)
def install_jav_study(ctx: PluginCommandContext):
    try:
        update()
        return PluginCommandResponse(True, '安装成功，正在重启主程序')
    except Exception as e:
        logging.error(f'安装失败，错误信息：{e}', exc_info=True)
        return PluginCommandResponse(False, f'安装失败，错误信息：{e}')
