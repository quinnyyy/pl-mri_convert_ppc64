#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build -t local/pl-mri_convert_ppc64 .
#
# In the case of a proxy (located at 192.168.13.14:3128), do:
#
#    docker build --build-arg http_proxy=http://192.168.13.14:3128 --build-arg UID=$UID -t local/pl-mri_convert_ppc64 .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pl-mri_convert_ppc64
#
# To pass an env var HOST_IP to container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/pl-mri_convert_ppc64
#

#FROM docker.io/quinnyyy/test123:test2
FROM docker.io/quinnyyy/centos_python_ppc_base:firsttry
MAINTAINER fnndsc "dev@babymri.org"

ENV FREESURFER_HOME="/freesurferhome"
ENV SUBJECTS_DIR="/usr/src/mri_convert_ppc64"
ENV APPROOT="/usr/src/mri_convert_ppc64"
COPY ["mri_convert_ppc64", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]
COPY ["FreeSurferColorLUT.txt", "/freesurferhome"]

WORKDIR $APPROOT

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["mri_convert_ppc64.py", "--help"]

