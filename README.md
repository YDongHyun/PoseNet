# PoseNet

# PoseNet 실습을 위한 환경 구축

리눅스 환경에서 CUDA설치 오류가 발생하여 Windows상에서 실습을 진행하였다.

PoseNet의 경우 하위버전으로 작성되었기 때문에 상위버전에서 실행시 오류가 발생한다.

(Pytorch 1.1.0 이하 버전에서 실행이 가능하다.)

따라서 아래와 같은 환경에서 실습을 진행하였다.

Anaconda3를 이용한 가상환경에서 구축하였다.

```jsx
Python 3.5.6
Pytorch 1.0.1
# GPU 사용
CUDA 10.0\
```

## Pytorch & CUDA 설치

Pytorch 는 1.1.0 이하 버전이어야 하므로 1.0.1 버전을 설치하였다.

```jsx
conda install pytorch==1.0.1 torchvision==0.2.2 -c pytorch
```

또한 Pytorch 버전에 맞게 CUDA는 10.0 버전을 설치하였다.

[CUDA Toolkit 10.0 Archive](https://developer.nvidia.com/cuda-10.0-download-archive)

 CUDA가 잘 설치되었는지 확인하기 위해 아래 명령어를 터미널상에 입력한다.

```jsx
# CUDA 버전 확인
nvcc —version
```

Pytorch상에서 GPU 사용할 수 있는지 아래와 같이 확인할 수 있다

```jsx
python
>>> import torch
>>> torch.cuda.is_available()
True
```

True가 출력되면 정상적으로 GPU를 사용할 수 있다.

## 라이브러리 설치

필요한 라이브러리들을 아래 명령어를 통해 설치해준다.

```jsx
# numpy는 1.10.x 버전 이하 사용
pip install numpy==1.10.4

# pandas 설치
pip install pandas

# matplotlib 설치
pip install matplotlib

# tensorboardX 설치
pip install tensorboardX
```

위 과정을 완료하면 실습을 위한 환경 구축은 끝났다.
