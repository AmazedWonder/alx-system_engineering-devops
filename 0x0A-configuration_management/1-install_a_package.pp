#!/usr/bin/pup
# Using Puppet, install flask Version 2.1.0 from pip3.
#package { 'flask':
  #ensure   => '2.1.0',
  #provider => 'pip3',
#}
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => '/usr/local/bin:/usr/bin',
  refreshonly => true,
}

# Optional: Notify a service restart or other resource that depends on Flask
# service { 'my_app':
#   ensure  => running,
#   require => Exec['install_flask'],
# }
