import pytest


testinfra_hosts = ["amazonlinux"]


@pytest.mark.parametrize('pkg', [
  'httpd'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
