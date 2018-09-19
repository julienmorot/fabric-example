# Simple demo fabfile.py for Fabric 1
# http://www.fabfile.org/
from fabric.api import abort, cd, env, get, hide, hosts, local, prompt, \
    put, require, roles, run, runs_once, settings, show, sudo, warn, open_shell


# Hostgroup definitions
env.roledefs = {
    'dns': [	'dns1.domain.tld',
                'dns2.domain.tld'],
    'ldap': ['master.domain.tld', 'slave.domain.tld',],
}

# Login/pass for SSH Authentication
env.user = "master"
env.password = ""

# Simple command :
def host_distribution():
    run('lsb_release -a')

# Admin command :
def RebooT():
    sudo('reboot')

# Multiple command as another user
def get_ldap_localconfig():
    sudo('/opt/zimbra/bin/zmlocalconfig ldap_host',user="zimbra")
    sudo('/opt/zimbra/bin/zmlocalconfig ldap_url',user="zimbra")
    sudo('/opt/zimbra/bin/zmlocalconfig ldap_master_url',user="zimbra")

# Get file
def get_userlist():
    run('getent passwd > /tmp/userlist.txt')
    get('/tmp/userlist.txt','/tmp/'+env.host+env.host++'userlist.txt')
    run('rm -f /tmp/userlist.txt')

# Send file with sudo with same permission from origin
def send_resolvconf():
    put('/etc/resolv.conf','/etc/resolv.conf',use_sudo=True,mirror_local_mode=True)

# Interactive fabric 
def send_file_to_tmp():
    file_path = prompt('Which file ?')
    put(file_path, '/tmp')

# Do not quit on error
def remove_most():
    with settings(warn_only=True):
        sudo('dpkg -P most')

# Using shell variables inside a function
def echo_path():
    run("echo $PATH")

