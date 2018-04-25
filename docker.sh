docker run -d --hostname q.life2film.com \
  --name q.life2film.com \
  -p 127.0.0.1:15672:15672 \
  -p 127.0.0.1:15671:15671 \
  -p 5671:5671 \
  -p 5672:5672 \
  -p 127.0.0.1:4369:4369 \
  -p 127.0.0.1:25672:25672 \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=LetMe \
  rabbitmq:3-management

#docker exec [CONTAINER_NAME] rabbitmq-plugins enable rabbitmq_management
