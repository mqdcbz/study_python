### 事故

firefox设置下的硬件加速并不是视频加速，当然我把他错认为了视频加速……


然后终于有一天(今天)我实在受不了卡顿……于是开始了折腾之旅

这玩意的别名还挺多


视频加速 AKA 视频硬件解码 或者 硬件视频加速 或者 视频硬解

我首先看了


[在 Linux 平台的 Firefox 上启用 VA-API 的视频硬件解码](https://zhuanlan.zhihu.com/p/268401890 "firefox")

但是并没有用，所以我又看了
[archwiki](https://wiki.archlinuxcn.org/wiki/%E7%81%AB%E7%8B%90#%E8%A7%86%E9%A2%91%E7%A1%AC%E8%A7%A3 "火狐")

我按照上面的配置了，仍然没有什么卵用……

所以我又按照
[硬件视频加速](https://wiki.archlinuxcn.org/wiki/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F "硬件")检查了一遍

一直不起作用

直到我按照

> 您可以通过检查 Firefox 的 VA-API 日志来验证 VA-API 的使用情况：使用环境变量 MOZ_LOG="PlatformDecoderModule:5" 启动 Firefox，用浏览器播放一段视频，并检查日志输出(搜索字符串"VA-API")。请注意这些日志，因为它们可以表明前面描述的两个可能的合成器（OpenGL或WebRender）中究竟哪一个被使用了。 

检查了一遍 然后发现了

FFMPEG: VA-API works in RDD process only

将

media.rdd-vpx.enabled 与 media.rdd-process.enabled 设置成默认就可以硬解了……


但是为什么呢……我也不知道

PS 我是将firefox的日志重定向到一个文件然后查询的 firefox 的日志好像不是标准输出 可以使用 &> 来全部重定向
