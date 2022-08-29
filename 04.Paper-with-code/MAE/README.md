# Masked Autoencoders Are Scalable Vision Learners (MAE)

AutoEncoder는 Encoder-Decoder 형태의 아키텍쳐이며, '좋은 인코더' 얻으려고 학습한다. 디코더를 통해 input을 복원하도록 loss를 학습시키면, 
핵심적인 시맨틱을 가지는 좋은 feature를 뽑는 구조를 이용하여 네트워크를 훈련한다. 

## Abstract
MAE의 접근 방법은 간단한데, 입력 이미지의 Patch를 임의로 골라서 마스킹 작업하고, 손실된 픽셀을 재구축하는 방식으로 학습을 진행한다.  
  
본 구조의 첫 번째 핵심 설계는, 비대칭 형태의 Encoder-Decoder 구조로, Encoder는 Masking된 patch를 제외하고 Visible Patches만을 사용한다.  
  
두 번째 핵심 설계는, 높은 masking 비율이다. 본 논문에서는 효과적인 Self Supervisory Task를 수행하기 위해서 75%의 Mask Ratio를 가지고 있다. 너무 작은 Masking 비율을 둘 경우, Image의 각 픽셀은 
그다지 Semantic하지 않기 때문에 단순히 주변 영역을 보고 쉽게 추론할 수 있기 때문에 높은 Masking을 통해 학습을 진행한다.  

이러한 두가지 설계를 합쳐서 구현한 MAE는 3배 이상의 속도 향상을 이뤄냈고, 인코더의 입력 차원이 줄었으므로 정확도 또한 ImageNet 1K 데이터만으로 ViT-Huge에서 87.8%의 정확도를 얻어냈으며, 이는 기존 Supervised Learning 방식의 정확도보다 높다.  

## Introduction

### introduction: ViT (Vision Transformer)
이전에 CNN 구조(ResNet)을 배운 적이 있으나, 최근에는 조금 다른 방법을 사용한다. ViT는 CNN과 다르게 self-attention 모듈을 여러 block으로 쌓아서 표현력을 높이는 구조이다.

<img src ='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbbDpDH%2FbtroSsGRwqn%2FV9oXahTZpdQfbCOU3eWzF0%2Fimg.png'>

CNN 기반 model과는 입력을 사용하는 방법에서 조금 차이가 있는데, Language에서 sequence의 sample 단위는 word token인데 이것을 일정 크기의 patch(16x16)으로 나눠서 입력에 사용한다.  

<img src ='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FShnk1%2FbtroWn6fWof%2FDkYBO7QK8iSlnwUDJ3qeok%2Fimg.png'>

왼 쪽이 ViT 논문에 있는 구조고, 오른 쪽은 Transformer로 encoder에서 decoder로 들어가는 layer입력을 MLP head로 빼서 classification을 수행한 것.

### introduction: MAE
Masked autoencoder 구조 및 학습 방법을 알아보자.  
* 전체적인 구조는 ViT의 형태를 따른다.

<img src ='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcnqyFN%2FbtrqmOBfrYb%2FzDFEdyC5Kv15MsLEl8M8k1%2Fimg.png'>

Masking의 경우 75%정도로, 매우 높은 비율의 Masking을 진행함으로써 주변 Pixel을 통해 단순히 Masked Patches를 찾아낼 수 없도록 유도한다. 이 때, MAE Encoder 부분은 ViT를 그대로 사용하였으며, 차이점은 Visible(Unmasked Patches)만을 사용했다는 점이다.  
이러한 특성으로 인해 메모리 사용량 및 계산량에서 큰 이점을 가지며, 전체 입력 데이터의 25%만을 사용하는 효과가 있다.

Decoder는 Visible과 Masked Patches를 모두 사용하는 방식으로 구성되며, 비어있는 patches들을 채워 넣는 방식으로 reconstruction을 진행한다. decoder는 사전 학습시에만 사용되기 때문에 Encoder와 별개로 사용자들이 원하는 디자인으로 유동적으로 변경할 수 있는 구조이다.  

Decoder 자체는 Encoder에서 Latent Vector만 잘 뽑아낸다면 상대적으로 그다지 복잡한 작업을 요하지 않기 때문에 저자들은 Encoder보다 좁고 짧은 lightweight decoder 구조를 사용하였으며 성능 차이가 그렇게 크지 않았다고 한다.

## Experiments

<img src ='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlIinY%2FbtrqnjushPK%2FQXCAIRqplP7lA9TFeaaTGk%2Fimg.png'>
*왼 쪽은 Classification 성능이고, 오른 쪽은 Fine-tuning을 통한 Segmentation 성능이다.

기존 방식들에 비해서 더 높은 Generalization 성능을 바탕으로 정확도가 향상되었을 뿐 만 아니라, Random Sampling과 Masking 자체가 이미 꽤나 강력한 Augmentation과 같은 기능을 하기 때문에, 최소한의 Augmentation만으로도 높은 정확도를 달성할 수 있었다고 한다.  
기존 방식 대비 Encoder에서 사용하는 입력 사이즈가 1/4 정도 수준이기 때문에, Parameter가 보다 적고 가벼우며, Scalable 한 특성을 지닌다.

## Conclusion

본 논문은 NLP에서 자주 쓰이는 방식인 Self-Supervised Learning을 Vision Task에도 적용시키기 위한 MAE를 제안하였고 매우 높은 Masking Ratio를 통해 단순히 주변 Pixel을 활용하여 추론이 불가능하도록 하게 함으로써, 모델로 하여금 Visual Understanding을 학습하도록 강제하고, 실제로 유망한 결과를 얻어낼 수 있었다.  
