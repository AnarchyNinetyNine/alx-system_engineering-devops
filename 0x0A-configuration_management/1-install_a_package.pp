# Ensure Python 3.8 is installed
package { 'python3.8.10':
  ensure => 'installed',
}

# Ensure pip for Python 3 is installed
package { 'python3-pip':
  ensure => 'installed',
  require => Package['python3.8.10'],
}

# Install Flask version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Install Werkzeug version 2.1.1 using pip3
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['flask'],
}

