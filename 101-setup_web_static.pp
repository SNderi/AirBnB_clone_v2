# puppet manifest preparing a server for static content deployment
exec { 'update':
  command => '/usr/bin/env apt-get -y update',
}
-> exec {'install':
  command => '/usr/bin/env apt-get -y install nginx',
}
-> exec {'test':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec {'shared':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
-> exec {'index':
  command => '/usr/bin/env echo "Puppet x Holberton School" > /data/web_static/releases/test/index.html',
}
-> exec {'symbolic':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}
-> exec {'alias':
  command => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}
-> exec {'restart':
  command => '/usr/bin/env service nginx restart',
}
-> exec {'chown':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
