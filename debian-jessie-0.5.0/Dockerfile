# Template for Debian-based OSes
FROM debian:jessie

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
        ca-certificates \
        curl \
    && curl -sLo /tmp/dumb-init.deb \
		https://github.com/Yelp/dumb-init/releases/download/v0.5.0/dumb-init_0.5.0_amd64.deb \
	&& dpkg -i /tmp/dumb-init.deb \
	&& rm /tmp/dumb-init.deb \
	&& apt-get clean

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

# vim: ft=dockerfile
