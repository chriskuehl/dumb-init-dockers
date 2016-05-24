# Template for Debian-based OSes
FROM ubuntu:xenial

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
        ca-certificates \
        curl \
    && curl -sLo /tmp/dumb-init.deb \
		https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-init_1.0.1_amd64.deb \
	&& dpkg -i /tmp/dumb-init.deb \
	&& rm /tmp/dumb-init.deb \
	&& apt-get clean

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

# vim: ft=dockerfile
