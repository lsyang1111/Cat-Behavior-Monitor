# Cat-Behavior-Monitor
## Brief Summary
Cat's health condition will be reflected on daily behavior, such as drinking, eating, and toileting timing. 

This project is able to record these activities and send detected pictures to AWS S3. After analyzing picture time stamps, we will know behavior is normal or not.

1. Set up Jetson Nano Environment
2. Save camera image naming in timestamp and upload to AWS S3 using AWS CLI.
3. Download All Image from AWS S3 and parse filename into a csv file

## Demo Steps
### 1. Set up Jetson Nano Environment
Follow this YouTube Tutorial by [NVIDIA Developer](https://www.youtube.com/watch?v=bcM5AQSAzUY&feature=youtu.be), which shows the process for seting up objection detection environment on jetson nano.

### 2. Save camera image naming in timestamp and upload to AWS S3 using AWS CLI.
Firstly, we need to configure AWS CLI configuration. Follow this [AWS tutorial](https://aws.amazon.com/tw/getting-started/tutorials/backup-to-s3-cli/), which shows how to make a unique AWS access key for each device, and other batch controll command(download/upload).

Revise demo code(detectnet-camera). If detections Class-ID is 17(cat) and it is the first detection within this sec, then save image with timestamp and upload it to AWS S3.

```python
python detectnet-camera_cat.py
```

### 3. Download All Image from AWS S3 and parse filename into a csv file
Use this command to batch download all files in AWS S3.
```python
aws s3 sync s3://hellocat .
```
Use this command to parse filename into a csv file.

```python
python extract_filename_202004291000.py
```

