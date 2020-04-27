# Cat-Behavior-Monitor
## Brief Summary
Cat's health condition will be reflected on daily behavior, such as drinking, eating, and toileting timing. 

This project is able to record these activities and send detected pictures to AWS S3. After analyzing picture time stamps, we will know behavior is normal or not.

1. Set up Jetson Nano Environment
2. Using AWS CLI to upload file to AWS S3
3. Save camera image with timestamp in filename

## Steps
1. Set up Jetson Nano Environment
Follow this YouTube Tutorial by [NVIDIA Developer](https://www.youtube.com/watch?v=bcM5AQSAzUY&feature=youtu.be), which shows the process for seting up objection detection environment on jetson nano.

2. Using AWS CLI to upload file to AWS S3
Follow this [AWS tutorial](https://aws.amazon.com/tw/getting-started/tutorials/backup-to-s3-cli/), which shows how to make a unigque AWS access key to each device, and other controll command(download/upload).

3. Save camera image with timestamp in filename.
Revise demo code(detectnet-camera). If detections Class-ID is 17(cat) and it is the first detection within this sec, then dave image with timestamp and upload it.
