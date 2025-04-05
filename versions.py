#!/usr/bin/env python3
"""Display versions of key Python scientific computing packages."""

import sys
from typing import Dict
import importlib

def get_package_versions() -> Dict[str, str]:
    """Get versions of installed scientific computing packages.
    
    Returns:
        Dictionary mapping package names to their version strings.
    """
    packages = {
        'sys': None,  # Special case for Python version
        'scipy': None,
        'numpy': None,
        'matplotlib': None,
        'pandas': None,
        'statsmodels': None,
        'sklearn': None
    }
    
    versions = {}
    for pkg in packages:
        if pkg == 'sys':
            versions[pkg] = sys.version.split()[0]
        else:
            try:
                module = importlib.import_module(pkg)
                versions[pkg] = getattr(module, '__version__', 'unknown')
            except ImportError:
                versions[pkg] = 'not installed'
    
    return versions

def print_versions(versions: Dict[str, str]) -> None:
    """Print package versions in a consistent format.
    
    Args:
        versions: Dictionary of package names and versions
    """
    max_len = max(len(pkg) for pkg in versions)
    for pkg, ver in versions.items():
        print(f"{pkg.ljust(max_len)}: {ver}")

if __name__ == '__main__':
    versions = get_package_versions()
    print_versions(versions)
