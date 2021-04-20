#BETA IMAGE
FROM centos:latest

#We can also comment this step, once the repo is public
RUN mkdir stegE

# We will change the step when we make the repo public,
# for now, build this docker file inside the Minor2_Work folder only
COPY . /stegE

RUN yum update -y && yum install -y \
    git \
    python3 \
    python3-pip \
    vim

# We can clone the repo here and then change the workdir to respective folder name
# git clone https://github.com/cptn3m0grv/<repo_name>
WORKDIR /stegE

RUN python3  -m pip install --upgrade pip

RUN pip3 install --user -r requirements.txt