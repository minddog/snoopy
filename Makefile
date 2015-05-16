run-kafka:
	export ZOOKEEPER=`boot2docker ip`:2181
	export KAFKA=`boot2docker ip`:9092
	cd ~/Projects/kafka-tools
	docker run -d -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=`boot2docker ip` --env ADVERTISED_PORT=9092 spotify/kafka
	cd -

dev-server:
	python snoopy/server.py
