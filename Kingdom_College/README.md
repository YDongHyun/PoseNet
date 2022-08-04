# Kings_College 예제 실행

예제 시작에 앞서 먼저 데이터셋을 다운받아  PoseNet-Pytorch 폴더에 넣는다.

```jsx
wget https://www.repository.cam.ac.uk/bitstream/handle/1810/251342/KingsCollege.zip?sequence=4&isAllowed=y****
```

다음 명령어를 통해 데이터셋을 받을 수 있다.

## Training

먼저 아나콘다로 만든 가상환경을 Activate한 후,   PoseNet-Pytorch 디렉토리로 이동한다.

다음과 같은 명령어로 예제를 실행할 수 있다.

```jsx
python train.py --image_path ./posenet/KingsCollege --metadata_path ./posenet/KingsCollege/dataset_train.txt
```

그러면 다음과 같이 트레이닝이 시작된다.

![캡처](https://user-images.githubusercontent.com/80799025/182822344-dc958fde-4b45-430d-a3fb-8d7a0beebe13.JPG)

트레이닝이 끝난 후  Tensorboard를 통해 시각화된 자료를 확인할 수 있다.

```jsx
tensorboard --logdir=./summary_KingsCollege
```

실행 한 후, 로컬주소로 이동하면 다음과 같은 결과를 확인할 수 있다.

![King_College](https://user-images.githubusercontent.com/80799025/182822325-2dbfff2f-04bb-47df-98d4-216874d56117.JPG)

## Test

다음 명령어를 입력하여 Test를 할 수 있다.

```jsx
python test.py --image_path ./posenet/KingsCollege --metadata_path ./posenet/KingsCollege/dataset_test.txt
```

실행하여 다음과 같은 결과를 얻을 수 있었다.

![Untitled](https://user-images.githubusercontent.com/80799025/182822375-627cbdd5-2fe2-485c-bd94-faaa646df121.png)
