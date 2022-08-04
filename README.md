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
CUDA 10.0
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
pip install tensorboard
pip install tensorboardX
```

위 과정을 완료하면 실습을 위한 환경 구축은 끝났다.

## PoseNet 다운

적절한 디렉토리에 다음과 같은 명령어를 입력하여 PoseNet을 다운받는다.

`git clone https://github.com/youngguncho/PoseNet-Pytorch.git`

PoseNet이 다운된 디렉토리에 실습할 데이터셋을 집어넣은 후 실습을 진행한다.

</br>

# PoseNet Training&Test

## Training

먼저 트레이닝을 위해  PoseNet이 설치된 디렉토리로 이동한다.

그 후 아래의 명령어를 통해 Training을 진행 할 수 있다.

```jsx
python train.py --image_path <이미지 경로> --metadata_path <metadata 경로>
```

기본적으로 image_path와 metadata_path는 필수적으로 입력해야 한다.

추가적으로 train.py파일을 살펴본 결과 다음과 같은 parameter들을 확인 할 수 있었다.

![Untitled (1)](https://user-images.githubusercontent.com/80799025/182063253-ae1a6d34-0a49-4e55-9727-924cfa02ef2c.png)

만약 기존 파라미터를 수정하고싶다면, 명령어에 추가적으로 입력하여 실행하면 된다.

EX)

```jsx
python train.py --image_path ./posenet/KingsCollege --metadata_path ./posenet/KingsCollege/dataset_train.txt **--num_epochs 100**
```

만약 중단된 트레이닝을 이어서 하고싶다면 다음 명령어를 통해 재개할 수 있다.

```jsx
python train.py --image_path <이미지 경로> --metadata_path <metadata 경로> --pretrained_model <원하는 epoch>
```

</br>

또한 tensorboard를 이용하여 결과를 시각적으로 확인 할 수 있다.

```jsx
tensorboard --logdir=./로그디렉토리/
```
log 디렉토리는 학습 후 결과로 나오는 `summary_<dataset 이름>` 폴더를 경로로 지정해주면 된다.
그러면 다음과 같이 터미널에 로컬 주소가 나타난다.

![image](https://user-images.githubusercontent.com/80799025/182791642-66392fee-7240-4626-b460-fad6f44cc13b.png)

다음 링크를 복사하여 접속하면 다음과 같은 결과를 확인할 수 있다.
</br>
EX)

![King_College](https://user-images.githubusercontent.com/80799025/182791718-e29f788b-5186-4a8e-a766-017dfe620fe9.JPG)

## Test

test를 위해 먼저 트레이닝된 파일이 `models_<dataset 이름>` 폴더 안에 **pth**파일이 존재해야 한다.

아래 명령어를 통해 test를 진행할 수 있다.

```jsx
python test.py --image_path <이미지 경로> --metadata_path <metadata 경로>
```

위 명령어는 기본 epoch이 400이므로, 399.pth파일을 찾을것이다.

만약 epoch을 다르게 설정하였다면 아래 명령어를 통해 test할 수 있다.

```jsx
python test.py --image_path <이미지 경로> --metadata_path <metadata 경로> --test_model <원하는 epoch>
```

test를 통해 최종적으로 결과를 얻을 수 있다.

## 결과

![Untitled (2)](https://user-images.githubusercontent.com/80799025/182063269-803b847a-97b2-4a82-ab57-61f5715d870d.png)

다음과 같은 결과를 얻을 수 있다.  `거리오차/각도 오차`

거리의 오차와, 각도의 오차를 확인 할 수 있다.
