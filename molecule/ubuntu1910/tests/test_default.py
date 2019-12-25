import pytest

testinfra_hosts = ["xenial"]


@pytest.mark.parametrize('pkg', [
  'software-properties-common'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
