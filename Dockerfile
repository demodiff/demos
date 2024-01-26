FROM ghcr.io/riotbib/investigraph:main

USER root
RUN pip uninstall -y followthemoney
RUN pip install "followthemoney @ git+https://github.com/investigativedata/followthemoney.git@schema/science-identifiers"

USER 1000

COPY ./datasets/ /datasets/
