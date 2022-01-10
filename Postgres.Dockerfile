FROM postgres:11
RUN localedef -i es_PE -c -f UTF-8 -A /usr/share/locale/locale.alias es_PE.UTF-8
ENV LANG es_PE.UTF-8