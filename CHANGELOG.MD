# [](https://github.com/zhiyuChen-aqumon/arkid-core/compare/v1.0.2-magnum...v) (2020-09-03)



## [1.0.2-magnum](https://github.com/zhiyuChen-aqumon/arkid-core/compare/v1.0.1-magnum...v1.0.2-magnum) (2020-09-02)


### Bug Fixes

* **samlsso:** 修复钉钉扫码登录后 saml 应用登录报错 ([7ecd925](https://github.com/zhiyuChen-aqumon/arkid-core/commit/7ecd9253b8d6d8e06678e355fffb238c4c0f7a4e))
* **uwsgi:** 生产中需要开启 threading 不然 sentry 无法工作 ([bdbca65](https://github.com/zhiyuChen-aqumon/arkid-core/commit/bdbca651bb5993576445e22107f4c1e3cc45f40d))



## [1.0.1-magnum](https://github.com/zhiyuChen-aqumon/arkid-core/compare/v1.0.0-magnum...v1.0.1-magnum) (2020-09-01)


### Features

* **djangosaml:** 接入 sentry ([4354f4f](https://github.com/zhiyuChen-aqumon/arkid-core/commit/4354f4f8ddcad9081db29e64312bbf2ff3f3eda5))



# [1.0.0-magnum](https://github.com/zhiyuChen-aqumon/arkid-core/compare/v1.3.8...v1.0.0-magnum) (2020-08-31)


### Bug Fixes

* **0078_auto_20200803_2109.py:** handle conflict because of mergeing ([986257f](https://github.com/zhiyuChen-aqumon/arkid-core/commit/986257fbf5aaa0c60ef22122efbd3b52ee20fe04))
* **aliyun sso:** 修复 SP_config key 重复问题 ([c18d918](https://github.com/zhiyuChen-aqumon/arkid-core/commit/c18d918b60a22c7983c1a320abcb636137fb2331))
* **djangosaml:** 修复因 RoleSessionName 是中文导致阿里云 SSO 失败的问题 ([cfad5d2](https://github.com/zhiyuChen-aqumon/arkid-core/commit/cfad5d294ad7e4a6e5386abf775c43238b690688))





### Features

* **aliyun sso:** 添加国际阿里云支持 ([7e3fe51](https://github.com/zhiyuChen-aqumon/arkid-core/commit/7e3fe51924b048f3d81c531524c45fc84bf63bc1))
