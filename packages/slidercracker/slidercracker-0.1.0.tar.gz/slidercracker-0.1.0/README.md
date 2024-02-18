# slidercracker

#### 介绍
滑块验证码识别

#### 软件架构
软件架构说明


#### 安装教程

1.  pip安装
```shell script
pip install slidercracker
```
2.  pip安装（使用阿里镜像加速）
```shell script
pip install slidercracker -i https://mirrors.aliyun.com/pypi/simple
```

#### 使用说明

1.  demo
```python
import slidercracker
test_res = slidercracker.identify_gap_locations(
            background_img_url='background_img_url',
            slider_img_url='slider_img_url',
            retain=False
        )
```

2. point_n说明
- 这个表中每个格子的数字代表n，0代表point_0

| 1   | 2   | 3   |
|-----|-----|-----|
| 8   | 0   | 4   |
| 7   | 6   | 5   |


2.  注意：如果不设置图片保存位置参数，图片将保存在依赖所在位置
