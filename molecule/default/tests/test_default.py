"""Role testing files using testinfra."""


def test_vagrant_machine_is_running(host):
    command = r"""vagrant status | grep -Ec 'myvm\s*running\s\(libvirt\)'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_ip_forwarding_is_enabled(host):
    command = r"""
    sysctl net.ipv4.conf.eth0.forwarding | \
    cut -d " " -f 3"""
    with host.sudo():
        cmd = host.run(command)
        assert '1' in cmd.stdout
