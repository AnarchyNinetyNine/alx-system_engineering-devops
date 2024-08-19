class nginx_config {
  # Ensure the 'sed' command is run to replace the placeholder in /etc/default/nginx
  exec { 'update_ulimit_in_default_nginx':
    command => 'sed -i "/ULIMIT/#ULIMIT/g" /etc/default/nginx',
    unless  => 'grep -q "#ULIMIT" /etc/default/nginx',
  }

  # Ensure the worker_rlimit_nofile directive is added to /etc/nginx/nginx.conf
  exec { 'insert_worker_rlimit_nofile':
    command => 'sed -i "/^worker_processes/a worker_rlimit_nofile 65535;" /etc/nginx/nginx.conf',
    unless  => 'grep -q "worker_rlimit_nofile 65535;" /etc/nginx/nginx.conf',
  }

  # Restart Nginx to apply the changes
  exec { 'restart_nginx':
    command     => '/etc/init.d/nginx restart',
    refreshonly => true,
    subscribe   => Exec['insert_worker_rlimit_nofile'],
  }
}

include nginx_config

