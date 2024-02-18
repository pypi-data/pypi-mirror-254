# SMA Manager ![Release](https://img.shields.io/github/v/release/DEADSEC-SECURITY/sma-manager?label=Release&style=flat-square) ![Python_Version](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square) ![License](https://img.shields.io/github/license/DEADSEC-SECURITY/sma-manager?label=License&style=flat-square) 

[![CodeQL](https://github.com/DEADSEC-SECURITY/sma-manager/actions/workflows/codeql.yml/badge.svg)](https://github.com/DEADSEC-SECURITY/sma-manager/actions/workflows/codeql.yml) 

![PyPI - Downloads](https://img.shields.io/pypi/dd/sma-manager?label=Daily%20Downloads&style=flat-square) ![PyPI - Downloads](https://img.shields.io/pypi/dw/sma-manager?label=Weekly%20Downloads&style=flat-square) ![PyPI - Downloads](https://img.shields.io/pypi/dm/sma-manager?label=Monthly%20Downloads&style=flat-square)

## 📝 CONTRIBUTIONS

Before doing any contribution read <a href="https://github.com/DEADSEC-SECURITY/sma-manager/blob/main/CONTRIBUTING.md">CONTRIBUTING</a>.

## 📧 CONTACT

Email: amng835@gmail.com

General Discord: https://discord.gg/dFD5HHa

Developer Discord: https://discord.gg/rxNNHYN9EQ

## 📥 INSTALLING
<a href="https://pypi.org/project/sma-manager">Latest PyPI stable release</a>
```bash
pip install sma-manager
```

## ⚙ HOW TO USE
```python
import sma_manager_api
sma_manager_api.SMA(<PARAMS>)
```
OR
```python
from sma_manager_api import SMA
SMA(<PARAMS>)
```

## 🤝 PARAMETERS
- name : str, required
  - Sensor name. 
  - Used only for Home Assistant Integration, a random value can be used if not implementing as a Home Assistant Component
- ip : str, required
  - IP of SMA Manager
- port : str, required 
  - Port of SMA Manager
- refresh_time : int, optional
  - Option to disable/enable the default progress bar (Default: 1)
