FROM python:2.7

#Docker Build Command $docker build -t dirs3arch .
#Docker Command to run dirs3arch container $docker run -it --entrypoint

RUN apt update && apt install -y git
RUN git clone https://github.com/puniaze/dirs3arch.git
RUN mkdir /dirs3arch_results
ENTRYPOINT ["/dirs3arch/dirs3arch.py"]