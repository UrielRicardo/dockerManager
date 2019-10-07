FROM debian:latest
RUN apt-get update && apt-get install -y openssh-server
EXPOSE 22
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD [ "sh", "-c", "sleep infinity" ]
