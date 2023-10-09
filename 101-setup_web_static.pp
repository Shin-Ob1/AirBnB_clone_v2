# Puppet for setup

-> package { 'nginx':
  ensure  => 'installed',
}

-> file { '/data/web_static/releases/tests/':
  ensure  => directory,
}

-> file { '/data/web_static/shared/':
  ensure  => directory,
}

$cont = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

-> file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "$cont",
}

-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => true,
}

-> file { '/data/':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

$ngconfig = 'location /hbnb_static {
                alias /data/web_static/current/;
        }'
-> file_line { 'find and replace':
  path  => '/etc/nginx/sites-available/default',
  line  => "$ngconfig",
  after => 'server_name index2.com www.index2.com;',
}

-> service { 'nginx':
  ensure => running,
}
