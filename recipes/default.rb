#
# Cookbook Name:: mycookbook
# Recipe:: default
#
# Copyright (C) 2016 YOUR_NAME
#
# All rights reserved - Do Not Redistribute
#

# downloading jdk7u80
remote_file '/opt/jdk-7u80-linux-x64.tar.gz' do
	source 'https://box.cognifide.com/java/jdk7/jdk-7u80-linux-x64.tar.gz'
	action :create_if_missing
end

#downloading jdk7u55
remote_file '/opt/jdk-7u55-linux-x64.tar.gz' do
    source 'https://box.cognifide.com/java/jdk7/jdk-7u55-linux-x64.tar.gz'
    action :create_if_missing
end

#downloading jdk8
remote_file '/opt/jdk-8u66-linux-x64.tar.gz' do
    source 'https://box.cognifide.com/java/jdk8/jdk-8u66-linux-x64.tar.gz'
    action :create_if_missing
end

# including libarchive recipe to be able to use libarchive_file resource
include_recipe "libarchive"

# include_recipe "jenkins::java"

# extracting jdk7 and jdk8 in the /tmp directory
for file in ["jdk-7u80-linux-x64.tar.gz", "jdk-8u66-linux-x64.tar.gz", "jdk-7u55-linux-x64.tar.gz"] do
	libarchive_file "#{file}" do
		path "/opt/#{file}"
		extract_to "/opt/"
    	action :extract 
    	extract_options :no_overwrite
    end
end

# installation of jenkins master
include_recipe "jenkins::master"
