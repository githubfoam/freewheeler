import pytest


testinfra_hosts = ["tumbleweed"]


@pytest.mark.parametrize('pkg', [
  'nmap'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
