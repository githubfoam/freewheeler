# freewheeler
dummy TOX




Travis (.com) branch:
[![Build Status](https://travis-ci.com/githubfoam/freewheeler.svg?branch=master)](https://travis-ci.com/githubfoam/freewheeler)  

Travis (.com) dev branch:
[![Build Status](https://travis-ci.com/githubfoam/freewheeler.svg?branch=dev)](https://travis-ci.com/githubfoam/freewheeler)  
Travis (.com) tox-branch branch:
[![Build Status](https://travis-ci.com/githubfoam/freewheeler.svg?branch=tox-branch)](https://travis-ci.com/githubfoam/freewheeler)  

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
    - MOLECULE_SCENARIO=centos76
    - MOLECULE_SCENARIO=centos74
    - MOLECULE_SCENARIO=fedora29
    - MOLECULE_SCENARIO=alpine38
    - MOLECULE_SCENARIO=amazonlinux
    - MOLECULE_SCENARIO=oraclelinux
    - MOLECULE_SCENARIO=opensuseleap
    - MOLECULE_SCENARIO=opensusetumbleweed
    - MOLECULE_SCENARIO=debianjessie



License
-------

GNU General Public License v3.0

Author Information
------------------

An optional section for the role authors


~~~~
