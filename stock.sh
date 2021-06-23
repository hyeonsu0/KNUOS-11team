#!/bin/bash

file_path='elasticsearch-7.6.2-linux-x86_64.tar.gz'

if [ -e "$file_path" ]; then
	echo "file exist"
else
	echo "file not exist"
	wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.6.2-linux-x86_64.tar.gz
	tar xvzf elasticsearch-7.6.2-linux-x86_64.tar.gz
fi

cd elasticsearch-7.6.2
./bin/elasticsearch -d
cd ..

pip3 install flask
pip3 install requests
pip3 install beautifulsoup4
pip3 install elasticsearch

cd app
python3 app.py;
