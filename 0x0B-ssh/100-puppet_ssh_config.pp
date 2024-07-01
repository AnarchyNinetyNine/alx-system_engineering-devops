file { 'ssh_config':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('ssh/ssh_config.erb'),
}

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#?IdentityFile',
}
