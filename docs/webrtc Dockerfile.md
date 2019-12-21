FROM ubuntu:18.04  
  
WORKDIR /app  
COPY . /app/  
  
RUN dpkg -i /app/requirements/archives/*.deb && ./webrtc-streamer -V  
  
EXPOSE 8000  
  
ENTRYPOINT [ "./webrtc-streamer" ]  
CMD [ "-a", "-C", "config.json" ]
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM3ODY2MzQxNV19
-->