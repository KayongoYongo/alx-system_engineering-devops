#The puppet script executes a command that kills a process named killmenow

exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}

