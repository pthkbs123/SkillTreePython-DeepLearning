# Style Transfer

* paper: [Image Style Transfer Using Convolutional Neural Networks](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)


Style transfer란, 두 영상(content image & style image)이 주어졌을 때 그 이미지의 주된 형태는 content image와 유사하게 유지하면서 스타일만 우리가 원하는 style image와 유사하게 바꾸는 것을 말한다. 위 그림에서는 주택사진을 content image로 주고 다른 화가의 작품들을 style image로 주었는데, 주택의 형태와 배치는 유지되면서 화풍만 각 작품과 유사하게 바뀐 것을 확인할 수 있다.



Style transfer의 연구는 아래와 같이 두 분류로 나눠짐.

1. mage-net 등의 데이터로 미리 학습된(pre-trained) 네트워크를 이용한 방법. 
  * Content image와 style image를 네트워크에 통과시킬 때 나온 각각의 feature map을 저장하고, 새롭게 합성될 영상의 feature map이 content image와 style image로부터 나온 feature map과 비슷한 특성을 가지도록 영상을 최적화.
  장점 : 이미지 2장(content image & style image)으로 style transfer가 가능.
  단점 : 매번 이미지를 새롭게 최적화 해야 하므로 시간이 오래걸림.

2. Style transfer network를 학습시키는 방법.
  * 서로 다른 두 도메인의 영상들이 주어졌을 때, 한 도메인에서 다른 도메인으로 바꿔주도록 학습 시킴.
  장점 : 네트워크를 한 번 학습시킨 후에 새로운 이미지에 적용할 때는 feed forward만 해주면 됨.
  단점 : 새로운 네트워크를 학습해야 하므로 각 도메인 별로 다수의 영상이 필요하며, 학습에 시간이 소요됨.

이번 정리에서는, 이전에 공부했던 GAN을 이용한 Style transfer network 학습 방법을 정리.

## Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks

<img src ='https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-9-39-16.png?w=740'>
이 연구에서는 GAN 구조를 응용하여 두 도메인 X, Y의 영상이 주여졌을 때, X에 속하는 영상을 Y에 속하는 영상으로 바꿔주는 네트워크 G: X\mapsto Y, 그리고 그 반대로 바꿔주는 네트워크 F: Y\mapsto X를 동시에 학습하는 방법을 제시.

<img src ='https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-17-e1848be185a9e18492e185ae-5-40-33.png?w=740'>

 domain transfer 후에도 같은 content를 유지하도록 cycle-consistency loss를 추가.  Cycle consistency loss란, x\in X에 대해, x\approx F(G(x))가 되도록 하는 loss를 뜻 함.
 
 <img src ='https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-17-e1848be185a9e18492e185ae-7-32-20.png?w=403&h=457'>
 
 이렇게 양쪽의 generator와 discriminator를 동시에 학습시키며 F와 G가 서로의 역함수가 되도록 유도하였고, 아래와 같이 성공적으로 style transfer 및 domain transfer 네트워크를 학습한 결과 확인 가능.
 
 
