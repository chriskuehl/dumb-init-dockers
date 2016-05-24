# Template for Debian-based OSes
FROM debian:stretch

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
        ca-certificates \
        curl \
    && curl -sLo /tmp/dumb-init.deb \
		https://github.com/Yelp/dumb-init/releases/download/v0.1.0/dumb-init_0.1.0_amd64.deb \
	&& dpkg -i /tmp/dumb-init.deb \
	&& rm /tmp/dumb-init.deb \
	&& apt-get clean

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

# vim: ft=dockerfile
