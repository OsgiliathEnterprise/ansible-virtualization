Virtualization
=========

Configure virtualization on the host.
It's a simple wrapper over the community-provided [libvirt role](https://github.com/stackhpc/ansible-role-libvirt-host)

Requirements
------------

executing `.configure` will download requirements for the role

Role Variables
--------------

Same as the one of the [original role](https://github.com/stackhpc/ansible-role-libvirt-host)

Dependencies
------------

The [original role](https://github.com/stackhpc/ansible-role-libvirt-host) Thanks stack HPC as well as the [LVM one](https://github.com/OsgiliathEnterprise/ansible-volumes)  

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
