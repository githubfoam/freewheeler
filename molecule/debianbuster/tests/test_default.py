import pytest


testinfra_hosts = ["jessie"]


@pytest.mark.parametrize('pkg', [
  'curl',
  'findutils',
  'tar',
  'unzip',
  'zip',
  'debianutils'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
