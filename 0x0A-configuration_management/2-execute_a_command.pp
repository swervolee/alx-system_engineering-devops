# kills a process
exec {'killing':
  command  => 'pkill killmenow',
  provider => 'shell'
  }
