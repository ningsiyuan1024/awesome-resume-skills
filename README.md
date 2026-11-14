# Awesome Resume Skills

面向中文求职者的简历 Agent Skills 清单：中文排版、Word/PDF 渲染、成果表达、JD 适配与交付检查。

A Chinese-first, evidence-linked directory of resume agent skills, with practical notes on typography, editable formats and runtime requirements.

**最近核查：2026-11-14。** 收录 6 个排版与交付项目、3 个内容优化项目，另列 4 个待评估项目。这里的“收录”表示已经读取上游文档与 Skill 入口，不代表安装、运行测试、招聘效果认证或安全审计。

## 快速选择

- **中文技术简历，想比较模板**：先看 [cosen1024/resume-builder-skill](https://github.com/cosen1024/resume-builder-skill) 的 compact / classic。
- **稳定排版、主题和间距配置**：先看 [RenderCV](https://github.com/rendercv/rendercv-skill)；内容与设计配置分开维护。
- **必须交付可编辑 Word**：先看 [JSON-Resume](https://github.com/Eric-Zhou-0302/JSON-Resume) 与 [resume-layout-skill](https://github.com/Denis-Tang/resume-layout-skill)。
- **现有正文只换排版**：看 [ResumeMD](https://github.com/beholder91/resume-md-skill)；原生 Windows 当前不在它的支持范围。
- **希望自己微调字号和间距**：看 [Chasen-Liao 的 resume-canvas](https://github.com/Chasen-Liao/resume-skills/tree/main/skills/resume-canvas)，仅适配其内置视觉模板。
- **内容像流水账**：先看内容优化类，再交给排版工具。没有收益数字时保留可观察产物，不补造百分比。

## 目录

- [排版与文件交付](#排版与文件交付)
- [内容、成果与岗位适配](#内容成果与岗位适配)
- [待评估与适用限制](#待评估与适用限制)
- [相邻工具](#相邻工具)
- [中文社区发现记录](docs/community-sources.md)
- [收录和核查标准](#收录和核查标准)
- [贡献条目](CONTRIBUTING.md)

## 排版与文件交付

| 项目 | 适合做什么 | 输出 | 环境与使用限制 |
| --- | --- | --- | --- |
| **[rendercv](https://github.com/rendercv/rendercv-skill)**<br>[Skill](https://github.com/rendercv/rendercv-skill/blob/main/skills/rendercv/SKILL.md) | 官方维护的 Typst 简历排版入口，提供工程、Harvard 等六套主题及字体、边距、间距配置。<br>语言：含中文语言配置 | PDF / PNG / HTML / Markdown / YAML | 需要 RenderCV 运行时；未列出 DOCX 输出。中文字体与实际分页需渲染确认。 |
| **[cosen-resume-builder](https://github.com/cosen1024/resume-builder-skill)**<br>[Skill](https://github.com/cosen1024/resume-builder-skill/blob/main/resume_skill/SKILL.md) | 中文优先，提供 compact、classic、modern、timeline、minimal 五套模板，使用 WeasyPrint 本地渲染。<br>语言：中文、英文、中英双语 | PDF / HTML / Markdown | 需要 Python 与 WeasyPrint 系统依赖。包含内容润色流程，只排版时应明确保留原文；原规则中的强动词不能扩大本人职责。 |
| **[json-resume-docx](https://github.com/Eric-Zhou-0302/JSON-Resume)**<br>[Skill](https://github.com/Eric-Zhou-0302/JSON-Resume/blob/main/SKILL.md) | 从结构化 JSON 生成 Word 简历，区分忠实渲染与内容创作模式，要求实际导出和逐页检查。<br>语言：中文及英文混排 | DOCX / PDF / JSON | PDF 导出依赖 Windows/macOS 的 Microsoft Word；在线编辑器与本地 CLI 的数据路径不同。项目名不代表兼容 jsonresume.org 标准。 |
| **[resume-docx](https://github.com/Denis-Tang/resume-layout-skill)**<br>[Skill](https://github.com/Denis-Tang/resume-layout-skill/blob/main/SKILL.md) | Markdown 源文件与 Word 双向维护，含模板自举、Word 页数检查及预览流程。<br>语言：中文 | DOCX / PNG / Markdown | 精确页数依赖 Word；Python 页数检查是估算。源规则有严格的一页及固定版式约束，具体任务以用户要求为准。 |
| **[resumemd](https://github.com/beholder91/resume-md-skill)**<br>[Skill](https://github.com/beholder91/resume-md-skill/blob/main/plugins/resume-md/skills/resume-md/SKILL.md) | 保真转换与确定性本地排版，关注字体嵌入、可提取文本和自然分页，不为排版主动改写内容。<br>语言：中文优先，也支持英文 | PDF / Markdown | 上游 README 声明支持 macOS、Linux、WSL，暂不支持原生 Windows、多栏或头像；不强制一页。 |
| **[chasen-resume-skills](https://github.com/Chasen-Liao/resume-skills)**<br>[Skill](https://github.com/Chasen-Liao/resume-skills/blob/main/skills/resume-builder/SKILL.md) · [Canvas](https://github.com/Chasen-Liao/resume-skills/blob/main/skills/resume-canvas/SKILL.md) | 母版构建与岗位定制工作流，提供视觉版、单栏版，以及本地 Canvas 字号和间距微调。<br>语言：中文工作流 | HTML / PDF / YAML | Canvas 只适配内置视觉模板，不适用于 ATS-safe 或任意外部 HTML；需完整渲染环境，不生成 DOCX。 |

## 内容、成果与岗位适配

| 项目 | 适合做什么 | 输出 | 环境与使用限制 |
| --- | --- | --- | --- |
| **[resume-optimizer](https://github.com/wyh0626/resume-optimizer)**<br>[Skill](https://github.com/wyh0626/resume-optimizer/blob/main/SKILL.md) | 审计职责型表述，围绕成果、交付物和业务价值改写，并结合 JD 调整重点。<br>语言：中文 | 诊断 / 改写草稿 / 行动清单 | 主要是内容工作流，不能当作确定性排版器或面试率保证；缺失指标仍需用户事实。 |
| **[resume-coach](https://github.com/leemysw/skills)**<br>[Skill](https://github.com/leemysw/skills/blob/main/resume-coach/SKILL.md) | 从招聘阅读视角分析定位、成果叙事和 JD 匹配，配套解析 PDF/DOCX 等文件。<br>语言：中文 | 评分卡 / 诊断 / 改写草稿 | 评分是提示词定义的主观检查，未经招聘结果校准；不属于模板排版工具。 |
| **[repo-to-resume-tailor](https://github.com/Ssabby1/repo-to-resume-tailor)**<br>[Skill](https://github.com/Ssabby1/repo-to-resume-tailor/blob/main/repo-to-resume-tailor/SKILL.md) | 从代码、配置和架构材料提炼项目描述，按岗位方向或具体 JD 选择高信号证据。<br>语言：中文及英文说明 | 证据分析 / 项目经历正文 | 仓库功能不等于个人贡献，代码存在不证明业务收益；内部项目应留在授权的本地环境。 |

## 待评估与适用限制

下面项目有明确能力线索，但存在适配或使用规则问题；列出用于比较，不作为开箱即用推荐。

| 项目 | 适合做什么 | 输出 | 环境与使用限制 |
| --- | --- | --- | --- |
| **[resume-builder-cn](https://github.com/LittleDrunkWang/resume-builder-cn)**<br>[Skill](https://github.com/LittleDrunkWang/resume-builder-cn/blob/main/SKILL.md) | 提供单栏、研发成果型、侧栏和学术版式规则，含短词断行与可编辑 HTML 参数。<br>语言：中文、英文、双语 | HTML / Markdown / PDF | 流程较长，含内容与岗位研究；入口描述字段的格式需在安装时检查。当前只核对文档，未确认可直接加载。 |
| **[init-resume-builder](https://github.com/INIT1996/resume-builder)**<br>[Skill](https://github.com/INIT1996/resume-builder/blob/main/SKILL.md) | 中文优先的 HTML 简历生成与分页规则，强调保留事实与可编辑交付。<br>语言：中文优先 | HTML | 默认只生成 HTML，PDF 需单独请求；入口描述字段的格式需检查，当前未确认可直接加载。 |
| **[resume-md2pdf](https://github.com/HduSy/resume-md2pdf)**<br>[Skill](https://github.com/HduSy/resume-md2pdf/blob/main/SKILL.md) | 忠于 Markdown 原文设计视觉主题，用 Chromium 导出 A4 PDF。<br>语言：中文或纯英文 | HTML / PDF | 上游明确不做中英混排，包含浏览器预览和确认环节；技术词密集的中文简历需先验证。 |
| **[resume-factory](https://github.com/hyf020908/resume-factory)**<br>[Skill](https://github.com/hyf020908/resume-factory/blob/main/SKILL.md) | 十套 LaTeX 风格，强调内容保真、编译与版面检查。<br>语言：可指定目标语言 | PDF / LaTeX | 当前规则要求照片，并允许为强制一页把正文压到 5.5pt 甚至更小；不宜不加判断地用于正式求职简历。 |

## 相邻工具

以下是渲染器或模板库，不计入已收录 Skill 数量：

- [YAMLResume](https://github.com/yamlresume/yamlresume)：结构化内容与简历渲染生态，中文社区有作者分享。是否有可用 Skill、输出格式和版本以实际项目文档为准。
- [中文简历模板库](https://github.com/ql-link/drawoffer-chinese-resume-templates)：可用于比较中文简历的信息层级与视觉版式。模板数量和授权以仓库当前说明为准，本清单未运行模板。

## 中文社区发现记录

从 V2EX、LINUX DO 及中文项目文档反查作者仓库，详细来源见 [社区记录](docs/community-sources.md)。社区发帖、作者宣传、第三方使用反馈分别记录；点赞、收藏、评分和“ATS-friendly”标签均不作为获得面试的证据。

## 收录和核查标准

1. 核心条目必须有公开、可定位的 `SKILL.md`；普通简历网站、提示词列表和模板库另列。
2. 读取原始 Skill 入口和与能力相关的 README / 排版参考，记录输入、输出、语言与运行依赖。
3. 明确区分**文档已读、实际安装、示例渲染、中文一页验证、真实求职反馈**。本仓库首批条目均仅到文档已读，未执行上游脚本或安装依赖。
4. 不凭仓库名称推断功能；不凭一个测试成功宣称全平台、所有字体或 ATS 均可用。
5. 不把 Skill 内“必须一页”、使用照片或强动词等个人规则当作所有求职者的固定要求。事实与个人归因应优先于模板。
6. 排版核查应包含实际页数、文本可提取、字体、裁切/重叠和阅读顺序。Word 成功保存不等于 PDF 正确渲染。
7. 本仓库只发布公共资源链接与原创概述，不收集真实简历、联系方式、客户资料或内部代码。

### 安装和使用

先进入项目链接查看当前安装说明。安装 Skill 与安装渲染器是两件事；包含公共脚本、字体和模板的项目应按上游目录完整安装。某些项目的 Skill 名称相同，安装前注意目标目录冲突。

安装不自动授权改写事实、上传简历、投递或联系招聘方。推荐为“忠实排版”明确指定输入稿；为“成果改写”保留原始事实与作者确认记录。不要为了凑一页把字号压到难以阅读，也不要隐藏溢出内容。

## 数据与维护

- [catalog.json](catalog.json)：条目、Skill 路径、输出格式、来源和限制。
- `python tools/build_readme.py`：从清单重建本页。
- `python tools/validate_catalog.py`：检查重复条目、必填字段、源链接和 README 一致性；不执行上游代码，也不构成在线链接可用性测试。
- 核查时间是本项目阅读日期；上游默认分支可能变化。新增实跑结果须记录版本、操作系统、样本和产物检查，不覆盖失败记录。

## License

本仓库原创目录、说明与维护脚本使用 [MIT License](LICENSE)。链接项目、字体和模板各自保留原授权；收录不授予其代码或素材的再分发权。
