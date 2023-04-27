### Discovery

* We are given `Spooky.mp4` video file and a description: `booOoooOoooOoooO`

### Exploitation

* By running the video we can see that during some frames, there are flashing letters.
* Slowing down the video we can check that they really are there.
* Either by using suggestion in the description or by experimenting we find out that letters are flashing every 4 seconds.
* We extract each frame of the video and calculate which frames to use, with framerate in mind.
* Using resulting images we compose the flag.
