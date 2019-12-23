FROM ubuntu:18.04  
  
WORKDIR /app  
COPY . /app/  
  
ENV http_proxy="proxy" \
https_proxy="proxy"

RUN apt-get update && apt-get install -y --no-install-recommends libasound2 libgtk-3-0 libssl1.0 \ 
   && apt-get clean && rm -rf /var/lib/apt/lists/ \  
   && ./webrtc-streamer -V  
  
EXPOSE 8000  

ENV http_proxy="" \
https_proxy=""

ENTRYPOINT [ "./webrtc-streamer" ]  
CMD [ "-a", "-C", "config.json" ]
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMTkyNDA0MTJdfQ==
-->