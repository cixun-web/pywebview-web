# pywebview + Next.js/Vue

> 该项目pnpm管理pywebview + Next.js/Vue的两个项目模板，以供大家参考使用。

## 环境说明
1. node 本人是使用nvm管理node版本，当前node版本为v18.1.0
2. pnpm 因为该项目是使用pnpm管理依赖，所以需要安装pnpm，安装方式：`npm install -g pnpm`，你也可以使用npm或者yarn管理依赖，但是需要自行修改package.json文件
3. python 本人使用的是python3.11的版本，并且需要自己下载virtualenv，安装方式：`pip install virtualenv`

## 项目说明

对于Next.js和vue的两个项目，本人都将所有的操作封装在了指令当中，直接执行指令即可，不需要自己手动操作，并且本人将指令还封装在了最外层的package.json文件中，所以你可以直接在最外层的package.json文件中执行指令，也可以进入到对应的项目中执行指令，效果是一样的。

### init

项目依赖的初始化

### start

开发的时候调试，但是存在一个问题没有热更新，如果有人知道如何解决，欢迎提issue

### build

打包成可执行文件

## 额外说明

1. 在nextJs中是将代码生成静态可执行文件，这就导致对于next export不支持的都不能在此项目中使用，详情请自己查看nextJs的文档
.....

