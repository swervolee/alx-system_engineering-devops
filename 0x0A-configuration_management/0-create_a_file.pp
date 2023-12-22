#creates a file in /tmp called school with content 'i love puppet'
file { 'school':
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744'
  }
