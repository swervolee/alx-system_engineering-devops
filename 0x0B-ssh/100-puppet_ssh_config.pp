#configuring the sshd_config file

file_line { 'Identity file':
  ensure    => present,
  path      => '/etc/ssh/ssh_config',
  line      => '    IdentityFile ~/.ssh/school',
  replace   => true
}

file_line { 'Password auth off':
  ensure    => present,
  path      => '/etc/ssh/ssh_config',
  line      => '    PasswordAuthentication no',
  replace   => true
}
