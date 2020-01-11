#!/bin/bash -eux

# codename of distro
LSB_RELEASE=$(lsb_release -sc)

# Prepare puppetlabs repo
wget http://apt.puppetlabs.com/puppetlabs-release-${LSB_RELEASE}.deb
dpkg -i puppetlabs-release-${LSB_RELEASE}.deb
apt-get -qy update

# Install puppet/facter
apt-get -qy install puppet facter
rm -f puppetlabs-release-${LSB_RELEASE}.deb
