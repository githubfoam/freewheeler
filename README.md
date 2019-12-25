# freewheeler
dummy TOX




Travis (.com) branch:
[![Build Status](https://travis-ci.com/githubfoam/freewheeler.svg?branch=master)](https://travis-ci.com/githubfoam/freewheeler)  

Travis (.com) dev branch:
[![Build Status](https://travis-ci.com/githubfoam/freewheeler.svg?branch=dev)](https://travis-ci.com/githubfoam/freewheeler)  

Travis (.com) tox-branch branch:
[![Build Status](https://travis-ci.com/githubfoam/freewheeler.svg?branch=tox-branch)](https://travis-ci.com/githubfoam/freewheeler)  




~~~~

----------------

Playbook
----------------

molecule testinfra :

    - MOLECULE_SCENARIO=ubuntu1604
    - MOLECULE_SCENARIO=ubuntu1804
    - MOLECULE_SCENARIO=ubuntu1810
    - MOLECULE_SCENARIO=ubuntu1904
    - MOLECULE_SCENARIO=centos77    
    - MOLECULE_SCENARIO=centos76
    - MOLECULE_SCENARIO=centos74
    - MOLECULE_SCENARIO=fedora29
    - MOLECULE_SCENARIO=alpine38
    - MOLECULE_SCENARIO=amazonlinux
    - MOLECULE_SCENARIO=oraclelinux
    - MOLECULE_SCENARIO=opensuseleap
    - MOLECULE_SCENARIO=opensusetumbleweed
    - MOLECULE_SCENARIO=debianjessie
    - MOLECULE_SCENARIO=debianstretch


License
-------

GNU General Public License v3.0

Author Information
------------------

An optional section for the role authors


~~~~

upgrade
~~~~

#add

.travis.yml
     - TOX_ENV=py27 MOLECULE_SCENARIO=centos77

# Install package (task)
tasks\CentOS-install.yml

# extend task for specific CentOS versions, 7.7 etc.. (optional)
tasks\CentOS-install.yml
when: ansible_distribution == 'CentOS'



# configure package (task),extend task for specific CentOS versions, 7.7 etc.. (optional)

tasks\configure\configure-CentOS.yml



# create a directort (copy && rename existing previous distro)
# testinfra tasks (verify package and configurations)

molecule\centos77


# image name and versions from docker hub

molecule\centos77\molecule.yml

platforms:
  - name: centos77
    image: centos:7.7.1908


# new scenario name same as MOLECULE_SCENARIO name "centos77"

- TOX_ENV=py27 MOLECULE_SCENARIO=centos77

molecule\centos77\molecule.yml

    scenario:
      name: centos77    


~~~~

release watch
~~~~
debian
https://hub.docker.com/_/debian
https://wiki.debian.org/DebianReleases

~~~~
