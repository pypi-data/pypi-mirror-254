# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_badrawcard']

package_data = \
{'': ['*'], 'nonebot_plugin_badrawcard': ['Data/*', 'Data/student_icons/*']}

install_requires = \
['aiofiles>=23.2.1,<24.0.0',
 'nonebot-plugin-apscheduler>=0.3.0,<0.4.0',
 'nonebot-plugin-send-anything-anywhere>=0.5.0,<0.6.0',
 'nonebot2[httpx]>=2.1.3,<3.0.0',
 'pillow>=10.0.1,<11.0.0',
 'pydantic[dotenv]>=1.10.0,<2.0.0',
 'redis>=5.0.0,<6.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-badrawcard',
    'version': '0.2.3',
    'description': '模拟BA抽卡',
    'long_description': '<div align="center">\n\n<img src="./images/icon.jpg" width="200" height="200" alt="Icon">\n\n# Nonebot-Plugin-BAdrawcard  \n### 《碧蓝档案》抽卡模拟插件\n\n</div>\n\n<p align="center">\n  <img src="https://img.shields.io/github/license/lengmianzz/nonebot-plugin-BAdrawcard" alt="license">\n  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python">\n  <img src="https://img.shields.io/badge/nonebot-2.0.0+-red.svg" alt="NoneBot">\n  <a href="https://pypi.python.org/pypi/nonebot-plugin-badrawcard">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-badrawcard.svg" alt="pypi">\n  </a>\n</p>\n\n\n## **Warning**: 使用本插件需要安装Redis!!!  \n## 本插件只在Matcha通过onebotV11适配器测试, 不保证其他适配器可用  \n\n\n\n<div align="center">\n\n### 效果展示:\n<img src="./images/info.jpg" width="450" height="400">\n\n<img src="./images/drawcard1.jpg" width="450" height="300" >\n<img src="./images/drawcard2.jpg" width="450" height="350" >\n<img src="./images/drawcard3.jpg" width="450" height="350" >\n\n</div>\n\n\n### 功能:\n - 自动更新抽卡概率\n - 自动更新up卡池, 检测更新卡池和图标库\n - 展示当前UP学生\n - 展示当前概率\n\n\n### 安装:\n - 使用 nb-cli 安装  \n```\nnb plugin install nonebot-plugin-BAdrawcard\n```\n\n - 使用 pip\n```\npip install nonebot-plugin-badrawcard\n```\n\n### 配置:\n - proxy: 本插件需要使用代理(`http://ip:host`格式)\n - redis_host: Redis的host(默认为localhost)\n - redis_port: Redis的开放端口(默认为6379)  \n\n\n### 触发:\n - `/ba单抽`\n - `/ba十连`\n - `/ba来一井`\n - `/当前概率`\n - `/当前up`\n - `/订阅更新`(当自动更新up池时提醒用户)\n',
    'author': 'LMZZ',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
