---
layout: post
title: オフライン強化学習
tags: [Seminars]
permalink: seminars/2021-02-28-offline-rl
---

## 概要
機械学習の一分野である強化学習では，環境が未知の場合でも用いることのできる最適化手法として，エージェントと呼ばれる学習主体が環境と相互作用し学習しながら目的関数の最適化を行います．近年では強化学習はゲームAIへの応用において人間のパフォーマンスを凌駕し注目を集めていますが，実はその学習過程には多くの"探索"と呼ばれる試行錯誤が必要としています．一方，実世界では，例えば医療や自動運転，広告配信などの意思決定システムにおいて，安全面のリスクや経済損失といったコストが発生する場面ではオンラインでの環境と相互作用しながら探索を行うことは望ましくなく，あまり導入が進んでいません．そこで今回は，オンラインでの環境との相互作用なしに過去に集めたデータ上で強化学習を行う，オフライン強化学習という新しい学習フレームワークについて紹介し，基礎的な知識を身につけます．

## 目的
- オフライン強化学習の重要性を理解する．
- オフライン強化学習の技術課題と基礎的な手法について学ぶ．

## 発表日時
場所:  オンライン (Zoom) \
日時: 2020年2月28日 14時 - 15時

## 参考資料
[1] S. Levine et al. Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems. 2020. [[arXiv]](https://arxiv.org/abs/2005.01643) \
[2] A. Kumar et al. Stabilizing Off-Policy Q-Learning via Bootstrapping Error Reduction. NeurIPS, 2019. [[arXiv]](https://arxiv.org/abs/1906.00949) \
[3] S. Ross et al. A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. AISTATS, 2011. [[arXiv]](https://arxiv.org/abs/1011.0686) \
[4] D. Precup et al. Eligibility Traces for Off-Policy Policy Evaluation. ICML, 2000. [[pdf]](https://scholarworks.umass.edu/cgi/viewcontent.cgi?article=1079&context=cs_faculty_pubs) \
[5] N. Jiang and L. Li. Doubly Robust Off-policy Value Evaluation for Reinforcement Learning. ICML, 2016. [[arXiv]](https://arxiv.org/abs/1511.03722) \
[6] R. Sutton et al. An Emphatic Approach to the Problem of Off-Policy Temporal-Difference Learning. JMLR, 2016. [[arXiv]](https://arxiv.org/abs/1503.04269) \
[7] R. Zhang et al. GenDICE: Generalized Offline Estimation of Stationary Values. ICLR, 2020. [[arXiv]](https://arxiv.org/abs/2002.09072) \
[8] S. Levine and K. Vladlen. Guided Policy Search. ICML, 2013. [[pdf]](http://proceedings.mlr.press/v28/levine13.pdf) \
[9] N. Jaques et al. Way Off-Policy Batch Deep Reinforcement Learning of Implicit Human Preferences in Dialog. 2019. [[arXiv]](https://arxiv.org/abs/1907.00456) \
[10] Y. Wu et al. Behavior Regularized Offline Reinforcement Learning. 2019. [[arXiv]](https://arxiv.org/abs/1911.11361) \
[11] I. Osband et al. Deep Exploration via Bootstrapped DQN. NeurIPS, 2016. [[arXiv]](https://arxiv.org/abs/1602.04621) \
[12] A. Kumar et al. Conservative Q-Learning for Offline Reinforcement Learning. NeurIPS, 2020. [[arXiv]](https://arxiv.org/abs/2006.04779) \
[13] M. Janner et al. When to Trust Your Model: Model-Based Policy Optimization. NeurIPS, 2019. [[arXiv]](https://arxiv.org/abs/1906.08253) \
[14] J. Fu et al. D4RL: Datasets for Deep Data-Driven Reinforcement Learning. 2020. [[arXiv]](https://arxiv.org/abs/2004.07219) \
[15] C. Gulcehre et al. RL Unplugged: Benchmarks for Offline Reinforcement Learning. 2020 [[arXiv]](https://arxiv.org/abs/2006.13888) \
[16] R. Qin et al. NeoRL: A Near Real-World Benchmark for Offline Reinforcement Learning. 2021. [[arXiv]](https://arxiv.org/abs/2102.00714) \
[17] A. Kendall et al. Learning to Drive in a Day. ICRA, 2019. [[arXiv]](https://arxiv.org/abs/1807.00412) \
[18] H. Zhu et al. Optimized Cost per Click in Taobao Display Advertising. KDD, 2017. [[arXiv]](https://arxiv.org/abs/1703.02091)
