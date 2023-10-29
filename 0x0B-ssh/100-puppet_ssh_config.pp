# /usr/bin/pup
# using Puppet to make changes to configuration file
file { 'Turn off passwd auth':
  path    => '/etc/ssh/sshd_config',
  ensure  => present,
  content => "PasswordAuthentication no\n",
}

file { 'Declare identity file':
  path    => '/home/wonder/.ssh/config',
  ensure  => present,
  content => "IdentityFile ~/.ssh/school\n",
}
#file { '/home/wonder/.ssh/config':
  #ensure  => present,
  #content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
#}
