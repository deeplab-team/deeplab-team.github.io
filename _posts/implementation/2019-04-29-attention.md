---
layout: post
title: Attentionチュートリアル
tags: [Implementation]
permalink: implementation/2019-04-29-attention
---

## 概要
2017年 “Attention Is All You Need” という論文が Googleから発表され，機械翻訳の分野で既存のRNN，LSTM，GRU等のモデルを大きく上回る結果となりました．提案されたTransformerモデルは，従来のRNNやCNNを使用せず，Attention機構のみを用いるSeq2Seqモデルです．今回は，このAttention機構を実装ベースで理解します．RNNと異なり並列計算が可能で計算が高速な上，Self-Attentionと呼ばれる機構を用いることにより，局所的な情報しか参照できないCNNと異なり，系列内の任意の位置情報を参照することができます．現在，自然言語処理のデファクトスタンダードとなっているBERTはこのTransformerに端を発しています．さらに，類似手法が，画像認識，生成モデル，音声認識などの分野で幅広く利用されています．このようにAttentionの動作原理を理解することは，深層学習分野において極めて重要です．

## 目的
- 様々な場面で登場するようになったAttention機構を実装ベースで理解する．
- 実際に機械翻訳のタスクを実行し，従来のSeq2Seqモデルと比較してTransformerの精度の高さを確認する．

## 実施期間・日時
場所: 友人宅 \
日時: 2019年4月29日 10時 - 12時

## 参考資料
A. Vaswani et al. Attention is All You Need NeurIPS, 2017. [[arXiv]](https://arxiv.org/abs/1706.03762)