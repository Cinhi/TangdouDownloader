# 糖豆广场舞下载器

在网页内抓取[糖豆广场舞](https://www.tangdou.com/)视频链接，并下载到本地。
~~（其实是母上经常要求下载所以无聊写了这个）~~

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="76" height="20"><linearGradient id="b" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="a"><rect width="76" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#a)"><path fill="#555" d="M0 0h49v20H0z"/><path fill="#4c1" d="M49 0h27v20H49z"/><path fill="url(#b)" d="M0 0h76v20H0z"/></g><g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="110"> <text x="255" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="390">Python</text><text x="255" y="140" transform="scale(.1)" textLength="390">Python</text><text x="615" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="170">2.7</text><text x="615" y="140" transform="scale(.1)" textLength="170">2.7</text></g> </svg>

## 功能

- 自动重命名为视频标题
- 支持批量下载
- 支持从文件中读取链接
- 好像再没有了（

## 缺点

- 写得太弱智（废话
- 单线程下载
- 对 Windows 支持可能不友好

## 用法

```shell
tddown.py links | -l list_file [-t dest_path]
```
| 参数 | 用法 |
|---|---|
| `links` | 一个或多个视频页面链接，可以是```www.tangdou.com m.tangdou.com share.tangdou.com``` 。|
| `-t dest_path` | 可选，将下载的文件存储至自定义的位置 `dest_path` 。如果牡蛎不存在，则将创建。 |
| `-l list_file` | 若没有 `links` 则必须提供。读取文件 `list_file` 里的视频页面链接，批量下载。 |

## Donate

因为太弱了，所以无法接受捐赠。
