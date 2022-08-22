# WaveNet

* paper: [WAVENET: A GENERATIVE MODEL FOR RAW AUDIO](https://arxiv.org/pdf/1609.03499.pdf)

## Introduce

WaveNet 이란, 2016년 구글 딥마인드에서 발표한 Audio waveform을 generate 하는 모델. 확률기반의 autoregressive model(AR)이다. wavefrom을 결합확률분포로 표현하고, 이를 conv layer를 쌓아서 모델링하겠다는 아이디어로 시작된 모델.

t 시점의 오디오 샘플을 t-1 시점까지의 샘플들의 조건부 분포로 모델링하는 것으로, 다음과 같은 수식으로 나타낸다.

<img src ='https://velog.velcdn.com/images%2Fcrosstar1228%2Fpost%2Ffc4dd640-eeec-4bef-ba3a-8c98bc34e0e6%2Fimage.png'>

특정 시점의 아웃풋을 계산할때 이전 시점의 인풋 데이터값을 보겠다는 의미이다. WaveNet은 위와 같은 조건부 분포를 Conv layer를 쌓아서 모델링한다. 네트워크에 pooling layer는 없고 input, output 차원이 동일하다. output에는 softmax를 취해 multinomial classification 문제로 다룬다. 최적화는 MLE를 사용하는 것.

## Dilated Causal Convolutions

Dilated causal convolution은 dilation과 causal 두 개념이 같이 사용된 Conv 네트워크 구조. Conv의 receptive field는 넓히면서 연산량은 크게 증가시키지 않는 방법으로 사용된 것이 dilation이고, Causal Conv는 특정 시점을 연산하기 위해 이전 시점 데이터만을 이용하는 것을 의미한다. 이 둘을 같이 사용하면 다음과 같은 네트워크가 된다.

<img src ='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcrLAYO%2FbtrCWL62lGG%2FTVK6LhkU5IKwnMqo9DdJuK%2Fimg.png'>

## SoftMax

PixelCNN에서 제안한것으로, 오디오 샘플의 conditional distribution을 모델링하기위해서 softmax distribution을 이용한다는 아이디어. 기존에 Gausian Mixture등보다 더 좋은 결과를 보였고 16비트 오디오 (65536)의 값이 너무 크기때문에 이를 $\mu$-law companding transformation을 이용하여 256으로 줄였음. 이는 단순한 linear quantization보다 훨씬 더 좋은 결과를 보임. 수식은 다음과 같음.

<img src ='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FtWeWa%2FbtrC1ia3ksm%2FQ8ffL6ptZPm4yoHd99o8x0%2Fimg.png'>
