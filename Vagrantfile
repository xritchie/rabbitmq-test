Vagrant.configure(2) do |config|
  config.vm.box = "bento/centos-6.7"
  config.vm.hostname = "rabbitmq-dev"
  config.vm.provision "shell", path: "provision.sh"
  config.vm.synced_folder ".", "/home/vagrant/vagrant"
end
