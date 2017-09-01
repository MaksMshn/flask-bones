Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"

  config.ssh.username = "ubuntu"

  config.vm.provision "shell", inline: <<-SHELL
    user=ubuntu
    apt-get -qqy update
    apt-get -qqy install build-essential zip unzip postgresql
    su postgres -c "createuser -dRS $user"
    su $user
    createdb
    createdb test
    # anaconda
    anaconda=Anaconda3-4.4.0-Linux-x86_64.sh
    mkdir /vagrant/tmp
    cd /vagrant/tmp
    echo -e "\n\nDownloading Anaconda installer. This may take more than a few minutes."
    curl -sSLO https://repo.continuum.io/archive/$anaconda
    if [ -s $anaconda ]; then
      chmod +x $anaconda
      ./$anaconda -b -p /home/${user}/opt/anaconda
      cat >> /home/${user}/.bashrc << EOF
      # Conda path
      PATH=/home/${user}/opt/anaconda/bin:$PATH
EOF
    else
      echo "ERROR: no anaconda installer found"
    fi
    # redis
    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    make
    make install
    # user
    source ~/.bashrc
    # flask
    pip install flask packaging oauth2client redis passlib flask-httpauth flask-migrate  flask_login flask-mail
    pip install sqlalchemy flask-sqlalchemy psycopg2 bleach requests
    
    echo "Done installing your virtual machine!"
  SHELL
end
