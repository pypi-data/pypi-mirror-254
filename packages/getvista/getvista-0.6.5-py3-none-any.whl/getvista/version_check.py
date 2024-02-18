import importlib.metadata
import requests
from packaging import version

def get_latest_version_from_pypi(package_name):
    try:
        response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
        data = response.json()
        latest_version = data['info']['version']
        return latest_version
    except requests.RequestException:
        return None  # Failed to fetch latest version


# Check for package updates
def check_for_updates():
    try:
        current_version = importlib.metadata.version('getvista')
        latest_version = get_latest_version_from_pypi('getvista')
        if version.parse(latest_version) > version.parse(current_version):
            print(f"Update available: {latest_version}. You are using {current_version}. Run 'pip install getvista --upgrade' to get the latest version.")
    except importlib.metadata.PackageNotFoundError:
        pass  # Package is not installed, so version check is not possible

if __name__ == '__main__':
    check_for_updates()