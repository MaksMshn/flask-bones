Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  # Skip checking for box updates. Speed up vagrant up.
  config.vm.box_check_update = false

  # Set hostname.
  config.vm.hostname = "guest"

  # Port forwarding.
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"

  # VirtualBox configuration.
  config.vm.provider "virtualbox" do |vb|
      # Set the name for the VM
      vb.name = "MyProject2"

      # Use VBoxManage to customize the VM. For example to change memory:
      vb.customize ["modifyvm", :id, "--memory", "2048"]
      #vb.customize ["modifyvm", :id, "--cpus", 2]
      #vb.customize ["modifyvm", :id, "--cpuexecutioncap", "95"]
   end

  config.ssh.username = "ubuntu"

  config.vm.provision "shell", inline: <<-SHELL
    # yarn
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
    # install packages
    user=ubuntu
    apt-get -qqy update
    apt-get -qqy install build-essential zip unzip postgresql nginx yarn redis-server
    # https://coderwall.com/p/ztskha
    sed -i "s/sendfile on;/sendfile off;/" /etc/nginx/nginx.conf
    # By default stop and disable Nginx.
    service nginx stop
    update-rc.d nginx disable
    rm /etc/nginx/sites-enabled/default
    # postgres
    su postgres -c "createuser -dRS $user"
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
    
    echo "Done installing your virtual machine!"
  SHELL
end
