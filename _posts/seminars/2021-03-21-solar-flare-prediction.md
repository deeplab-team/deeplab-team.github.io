---
layout: post
title: 太陽フレア予測におけるCNNの有効性の検証
tags: [Seminars]
permalink: seminars/2021-03-21-solar-flare-prediction
---

## 概要
太陽フレアは太陽大気中で起こる爆発現象であり，それにより生じる高エネルギー粒子の放出は，衛星を故障させたり，電波システムに障害を発生させます．そのため，太陽フレアの発生を正確に予測し，想定する障害に事前に対策する必要があります．近年，機械学習の発展から，それを用いたフレア予測モデルの構築が活発に研究され，専門家による予測を超えるまでに至ってます．磁場画像データを入力とした太陽フレア予測研究に関して，近年の機会学習界隈の動向と反し，統計的学習手法やMultilayer Perceptron (MLP) が，Convolution Neural Network (CNN) より高い予測精度を出しています．本セミナーでは，この傾向の原因を探るために，統計的学習手法，MLP，CNNを用いて，24時間以内のフレア発生を予測するモデルを構築し，太陽フレア予測におけるCNNの有効性を調査しました．

## 目的
- 機械学習を用いた太陽フレア発生の予測手法を理解する．
- 今後，太陽フレア発生の予測精度向上のためにどのような手法がとれそうかを議論する．

## 発表日時
場所:  オンライン (Zoom) \
日時: 2021年3月21日11時 - 12時

## 参考資料
[1] N. Nishizuka et al. Deep Flare Net (DeFN) Model for Solar Flare Prediction. 2018. [[IOPscience]](https://iopscience.iop.org/article/10.3847/1538-4357/aab9a7/pdf) \
[2] X. Huang et al. Deep Learning Based Solar Flare Forecasting Model. I. Results for Line-of-sight Magnetograms. 2018. [[IOPscience]](https://iopscience.iop.org/article/10.3847/1538-4357/aaae00/pdf) \
[3] X. Li et al. Predicting Solar Flares Using a Novel Deep Convolutional Neural Network. 2020. [[IOPscience]](https://iopscience.iop.org/article/10.3847/1538-4357/ab6d04/pdf) \
[4] M. G. Bobra et al. The Helioseismic and Magnetic Imager (HMI) Vector Magnetic Field Pipeline: SHARPs - Space-Weather HMI Active Region Patches. 2014. [[Springer]](https://link.springer.com/content/pdf/10.1007/s11207-014-0529-3.pdf) \
[5] R. A. Angryk et al. Multivariate time series dataset for space weather data analytics. 2020. [[Data Mining Lab]](https://dmlab.cs.gsu.edu/wp-content/uploads/mvts4swa.pdf) \
[6] E. Jonas et al. Flare Prediction Using Photospheric and Coronal Image Data. 2018. [[Springer]](https://link.springer.com/content/pdf/10.1007/s11207-018-1258-9.pdf) \
[7] K. Florios et al. Forecasting Solar Flares Using Magnetogram-based Predictors and Machine Learning. 2018. [[Springer]](https://link.springer.com/content/pdf/10.1007/s11207-018-1250-4.pdf) \
[8] H Liu et al. Predicting solar flares using a long short-term memory network. 2019. [[IOPscience]](https://iopscience.iop.org/article/10.3847/1538-4357/ab1b3c/pdf)
