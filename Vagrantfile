# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define :servidorParcial do |servidorParcial|
    servidorParcial.vm.box = "bento/ubuntu-22.04"
    servidorParcial.vm.network :private_network, ip: "192.168.80.3"
    servidorParcial.vm.provision "file", source: "frontend", destination: "/home/vagrant/frontend"
    servidorParcial.vm.provision "file", source: "microUsers", destination: "/home/vagrant/microUsers"
    servidorParcial.vm.provision "file", source: "microProducts", destination: "/home/vagrant/microProducts"
    servidorParcial.vm.provision "file", source: "microOrders", destination: "/home/vagrant/microOrders"
    servidorParcial.vm.provision "file", source: "db", destination: "/home/vagrant/db"
    servidorParcial.vm.provision "file", source: "docker-compose.yml", destination: "/home/vagrant/docker-compose.yml"
    servidorParcial.vm.provision "shell", path: "script.sh"
    servidorParcial.vm.hostname = "servidorParcial"
    config.vm.synced_folder "./recursos", "/vagrant_data"
  end
end
