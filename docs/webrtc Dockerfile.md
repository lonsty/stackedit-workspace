FROM ubuntu:18.04  
  
WORKDIR /app  
COPY . /app/  
  
RUN dpkg -i /app/requirements/libasound2_1.1.3-5ubuntu0.2_amd64.deb /app/requirements/libasound2-data_1.1.3-5ubuntu0.2_all.deb /app/requirements/libgtk-3-0_3.22.30-1ubuntu4_amd64.deb /app/requirements/libssl1.0.0_1.0.2n-1ubuntu5.3_amd64.deb /app/requirements/libssl1.0-dev_1.0.2n-1ubuntu5.3_amd64.deb && ./webrtc-streamer -V  

EXPOSE 8000  
  
ENTRYPOINT [ "./webrtc-streamer" ]  
CMD [ "-a", "-C", "config.json" ]
<!--stackedit_data:
eyJoaXN0b3J5IjpbODE2NjYzMzI4XX0=
-->