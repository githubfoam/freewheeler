#!/bin/bash -eux

bundle exec thor packer:build \
  --vagrant_cloud_version=1.0 \
  --os=centos \
  --os_version=centos-7.7-x86_64 \
  --providers=virtualbox
