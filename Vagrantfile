# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = '2'

Vagrant.require_version '>= 1.5.0'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "bento/centos-6.7"
  config.vm.hostname = 'bento-server'

  config.vm.network :private_network, ip: '192.168.123.107'
  config.vm.network 'forwarded_port', guest: 8080, host: 8080

  config.omnibus.chef_version = '12.6.0'
  config.berkshelf.enabled = true
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.ignore_private_ip = false
  config.hostmanager.include_offline = true

  config.hostmanager.aliases = %w(
    jenkins-server.local
  )
  
  config.vm.provision :chef_solo do |chef|
    chef.run_list = [ "recipe[mycookbook::default]"
                    ]
  end
end
