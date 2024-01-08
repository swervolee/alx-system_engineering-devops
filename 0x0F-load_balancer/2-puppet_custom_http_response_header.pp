#installs and configures nginx

package { 'nginx':
  ensure => 'installed'
}

file { 'var/www/html/index.html':
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

exec { 'ufw':
  command  => "sudo ufw allow 'Nginx HTTP'",
  provider => 'shell',
}

exec { 'header':
  command  => "sudo sed -i '/listen 80 default_server/a \\        add_header X-Served-By \"\$HOSTNAME\";' /etc/nginx/sites-available/default",
  provider => 'shell',
}

exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
