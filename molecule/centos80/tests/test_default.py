import pytest


testinfra_hosts = ["centos74"]


@pytest.mark.parametrize('pkg', [
  'httpd',
  'httpd-tools'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
