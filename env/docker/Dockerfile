FROM nvidia/cuda:11.2.0-cudnn8-devel-ubuntu20.04

SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND=noninteractive



ARG PYVER=3.9
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  software-properties-common \
  && apt-add-repository -y \
  ppa:deadsnakes/ppa \
  && apt update -q=2 \
  && apt install -yq=2 \
  python$PYVER \
  python$PYVER-dev \
  python$PYVER-distutils \
  python3-pip \
  && ln -fns \
  /usr/bin/python$PYVER \
  /usr/bin/python3 \
  && apt update -q=2

  


COPY py/requirements.txt .
RUN \
  pip install -Uqr requirements.txt \
  && rm requirements.txt
